"""make-slides 的關卡腳本（見 SKILL.md、docs/slides-plan.md）。

用法：python .claude/skills/make-slides/gates.py <g1|g2|g4|render>

  g1      覆蓋率：主題頁與 sources.md 的相關來源都 >=3 篇且存在
  g2      出處：每張證據卡的每個主張都有有效連結、頁碼，Wiki 原文逐字存在
  render  把 drafts/*.md 機械地轉成 deck.html（不改任何字），並複製 deck.css
  g4      渲染：頁數 8-15、站內連結都存在、含數字的項目都有出處、比喻不含數字
          （文字溢出另由瀏覽器執行 g4_overflow.js 量測）

關卡只讀檔與回報，不修改成品；全部通過時結束碼為 0。所有路徑由本檔位置推算。
"""
import html
import re
import shutil
import sys
from pathlib import Path

import markdown
import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DECK = ROOT / "decks" / "world-models"
WIKI_ZH = ROOT / "wiki" / "zh"
TOPIC = "world-models"

LINK = re.compile(r"\[([^\]]+)\]\(\.\./\.\./zh/(sources|concepts|topics)/([a-z0-9-]+)\.html\)")
REF = re.compile(r"\((?:p\.(\d+)|pp\.(\d+)-(\d+))(?:, (?:Fig\.|Table|Eq\.|Alg\.) ?(?:[A-Z]\.?)?\d+[a-z]?)?\)")
REF_LOOSE = re.compile(r"\(pp?\.[^)]*\)")
# 不算數字：年份、名稱中的數字（DreamerV3、VQGAN-2、3D）、Dreamer 4
NAME_WITH_DIGIT = re.compile(r"[A-Za-z]+[-]?\d+[A-Za-z\d-]*|\d+[A-Za-z]+[A-Za-z\d-]*|Dreamer 4")
NUMBER = re.compile(r"\d[\d,]*(?:\.\d+)?")
YEAR = re.compile(r"(19|20)\d\d")


def split_fm(text):
    text = text.lstrip("﻿").replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def wiki_page(kind, slug):
    return WIKI_ZH / kind / f"{slug}.md"


def plain(text):
    """去掉 Markdown 連結語法、強調、行內程式碼與「」，壓縮空白。"""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*`]", "", text)
    text = text.replace("「", "").replace("」", "")
    text = re.sub(r"^\s*(?:[-+>]|\d+\.)\s+", "", text)
    return re.sub(r"\s+", " ", text).strip()


def numbers(text):
    text = REF_LOOSE.sub("", text)
    text = LINK.sub(lambda m: "", text)
    text = NAME_WITH_DIGIT.sub("", text)
    return [n for n in NUMBER.findall(text) if not YEAR.fullmatch(n)]


class Report:
    def __init__(self, gate):
        self.gate, self.errors, self.notes = gate, [], []

    def err(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def finish(self):
        for n in self.notes:
            print(f"  {n}")
        if self.errors:
            print(f"[FAIL] {self.gate}：{len(self.errors)} 個問題")
            for e in self.errors:
                print(f"    - {e}")
            sys.exit(1)
        print(f"[OK] {self.gate}：通過")
        sys.exit(0)


def g1():
    r = Report("G1 覆蓋率")
    tp = wiki_page("topics", TOPIC)
    if not tp.exists():
        r.err(tp.relative_to(ROOT).as_posix(), "主題頁不存在")
        r.finish()
    fm, _ = split_fm(tp.read_text(encoding="utf-8"))
    topic_sources = [s for s in (fm.get("sources") or []) if wiki_page("sources", s).exists()]
    r.notes.append(f"主題頁 {TOPIC} 的來源：{len(topic_sources)} 篇")
    if len(topic_sources) < 3:
        r.err("主題頁", f"來源只有 {len(topic_sources)} 篇（需要 >=3）")
    sp = DECK / "sources.md"
    if not sp.exists():
        r.err("sources.md", "不存在（節點 1 尚未完成）")
        r.finish()
    picked = []
    for _, kind, slug in LINK.findall(sp.read_text(encoding="utf-8")):
        if kind == "sources" and slug not in picked:
            picked.append(slug)
    r.notes.append(f"sources.md 選出的相關來源：{len(picked)} 篇（{', '.join(picked)}）")
    for slug in picked:
        if not wiki_page("sources", slug).exists():
            r.err("sources.md", f"來源頁 {slug} 不存在")
        elif slug not in topic_sources:
            r.err("sources.md", f"{slug} 不在主題頁 {TOPIC} 的來源中")
    if len(picked) < 3:
        r.err("sources.md", f"相關來源只有 {len(picked)} 篇（需要 >=3），請回報缺什麼")
    r.finish()


def page_lines(path):
    _, body = split_fm(path.read_text(encoding="utf-8"))
    body = re.split(r"\n## 我的筆記", body)[0]
    return [plain(l) for l in body.split("\n") if l.strip()]


def g2():
    r = Report("G2 出處")
    cards = sorted((DECK / "cards").glob("*.md"))
    if not cards:
        r.err("cards/", "沒有任何證據卡")
        r.finish()
    total = 0
    for card in cards:
        name = f"cards/{card.name}"
        slug = card.stem
        sp = wiki_page("sources", slug)
        if not sp.exists():
            r.err(name, f"卡片檔名 {slug} 不是存在的來源頁")
            continue
        sfm, sbody = split_fm(sp.read_text(encoding="utf-8"))
        allowed_concepts = set(re.findall(r"\(\.\./concepts/([a-z0-9-]+)\.md\)", sbody))
        max_page = int(sfm.get("pages") or 0)
        text = card.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
        heads = list(re.finditer(r"(?m)^## C\d+[ \t]*$", text))
        claims = [text[h.start():(heads[k + 1].start() if k + 1 < len(heads) else len(text))]
                  for k, h in enumerate(heads)]
        stray = re.findall(r"(?m)^## (?!C\d+[ \t]*$).*$", text)
        for s in stray:
            r.err(name, f"無法辨識的小節標題（主張要寫成 ## C<n>）：{s}")
        if not claims:
            r.err(name, "沒有任何 ## C<n> 主張")
        for b in claims:
            cid = b.split("\n", 1)[0][3:].strip()
            where = f"{name}#{cid}"
            total += 1
            claim = re.search(r"^- 主張：(.+)$", b, re.M)
            src = re.search(r"^- 出處：(.+)$", b, re.M)
            quote = re.search(r"^- Wiki 原文：「(.+)」\s*$", b, re.M)
            if not (claim and src and quote):
                r.err(where, "缺少「主張／出處／Wiki 原文」其中一行，或原文沒有用「」包住")
                continue
            links = LINK.findall(src.group(1))
            if len(links) != 1:
                r.err(where, f"出處要恰好一個中文 Wiki 連結（../../zh/<kind>/<slug>.html），找到 {len(links)} 個")
                continue
            _, kind, target = links[0]
            tp = wiki_page(kind, target)
            if not tp.exists():
                r.err(where, f"連結的 Wiki 頁 {kind}/{target} 不存在")
                continue
            if kind == "sources" and target != slug:
                r.err(where, f"混入其他來源 {target}（這張卡只能用 {slug}）")
            if kind == "concepts" and target not in allowed_concepts:
                r.err(where, f"概念頁 {target} 沒有被 {slug} 連到，不在這張卡可讀的範圍")
            if kind == "topics":
                r.err(where, "證據卡不可引用主題頁")
            refs = REF.findall(src.group(1))
            loose = REF_LOOSE.findall(src.group(1))
            if len(refs) != len(loose):
                r.err(where, f"頁碼格式不正確：{loose}")
            if kind == "sources" and not loose:
                r.err(where, "來源頁的主張必須有頁碼 (p.X)")
            for p1, p2, p3 in refs:
                hi = int(p1 or p3)
                if max_page and hi > max_page:
                    r.err(where, f"頁碼 {hi} 超過 {slug} 的 pages: {max_page}")
            q = plain(quote.group(1))
            if len(q) < 12:
                r.err(where, f"Wiki 原文太短（{len(q)} 字），至少要 12 個字才能確認出處")
                continue
            hit = [l for l in page_lines(tp) if q in l]
            if not hit:
                r.err(where, f"Wiki 原文沒有逐字出現在 {kind}/{target}.md：「{q[:40]}…」")
                continue
            for ref in loose:
                if not any(ref in l for l in hit):
                    r.err(where, f"頁碼 {ref} 不在原文所在的段落中")
            for n in numbers(claim.group(1)):
                if n not in q and n.replace(",", "") not in q.replace(",", ""):
                    r.err(where, f"主張中的數字 {n} 沒有出現在 Wiki 原文")
    r.notes.append(f"檢查 {len(cards)} 張卡、{total} 個主張")
    r.finish()


TEMPLATE = """<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="deck.css">
</head>
<body>
<main class="deck">
{slides}
</main>
</body>
</html>
"""


def render():
    drafts = sorted((DECK / "drafts").glob("*.md"))
    if not drafts:
        print("[FAIL] render：drafts/ 沒有逐頁稿")
        sys.exit(1)
    out, n = [], len(drafts)
    deck_title = ""
    for i, d in enumerate(drafts, 1):
        fm, body = split_fm(d.read_text(encoding="utf-8"))
        title = str(fm.get("title", ""))
        deck_title = deck_title or title
        layout = fm.get("layout", "content")
        inner = markdown.markdown(body.strip(), extensions=["tables"])
        inner = re.sub(r"<blockquote>\s*<p>(比喻|過場)：",
                       lambda m: f'<blockquote class="{ {"比喻": "analogy", "過場": "transition"}[m.group(1)] }"><p><span class="tag">{m.group(1)}</span>',
                       inner)
        out.append(
            f'<section class="slide slide-{layout}" id="s{i:02d}">\n'
            f'<p class="num">{i} / {n}</p>\n'
            f'<h2>{html.escape(title)}</h2>\n'
            f'<div class="body">\n{inner}\n</div>\n'
            f'</section>')
    (DECK / "deck.html").write_text(TEMPLATE.format(title=html.escape(deck_title), slides="\n".join(out)),
                                    encoding="utf-8", newline="\n")
    shutil.copyfile(HERE / "deck.css", DECK / "deck.css")
    print(f"[OK] render：{n} 頁 → decks/world-models/deck.html")


def g4():
    r = Report("G4 渲染（腳本部分）")
    dp = DECK / "deck.html"
    if not dp.exists():
        r.err("deck.html", "不存在，請先執行 render")
        r.finish()
    text = dp.read_text(encoding="utf-8")
    slides = re.findall(r'<section class="slide[^"]*" id="(s\d+)">(.*?)</section>', text, re.S)
    r.notes.append(f"頁數：{len(slides)}")
    if not 8 <= len(slides) <= 15:
        r.err("deck.html", f"頁數 {len(slides)} 不在 8-15")
    checked = 0
    for href in re.findall(r'(?:href|src)="([^"#]+)(?:#[^"]*)?"', text):
        if re.match(r"[a-z]+:", href):
            continue
        checked += 1
        if not (DECK / href).resolve().exists():
            r.err("deck.html", f"連結目標不存在：{href}")
    r.notes.append(f"站內連結：{checked} 個")
    for sid, body in slides:
        for bq in re.findall(r"<blockquote.*?</blockquote>", body, re.S):
            t = html.unescape(re.sub(r"<[^>]+>", "", bq))
            if numbers(t):
                r.err(sid, f"比喻或過場不可含數字：{t.strip()[:40]}")
        body_wo_bq = re.sub(r"<blockquote.*?</blockquote>", "", body, flags=re.S)
        for item in re.findall(r"<(?:li|p|td)>(.*?)</(?:li|p|td)>", body_wo_bq, re.S):
            t = html.unescape(re.sub(r"<[^>]+>", "", item))
            if numbers(t) and "../../zh/" not in item:
                r.err(sid, f"含數字但沒有 Wiki 出處連結：{t.strip()[:40]}")
            if '../../zh/sources/' in item and not REF_LOOSE.search(t):
                r.err(sid, f"引用來源頁但沒有頁碼：{t.strip()[:40]}")
    r.finish()


if __name__ == "__main__":
    cmds = {"g1": g1, "g2": g2, "g4": g4, "render": render}
    if len(sys.argv) != 2 or sys.argv[1] not in cmds:
        print(__doc__)
        sys.exit(2)
    cmds[sys.argv[1]]()
