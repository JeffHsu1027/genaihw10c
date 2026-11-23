"""build.py — 由 wiki/ 的 Markdown 產生全站 HTML（AGENTS.md 第 8 節）。

用法：python scripts/build.py

產生：
  index.html                         根入口（簡介＋選語言）
  <lang>/index.html                  首頁：依領域分區的卡片（主題、來源、概念）
  <lang>/<kind>/<slug>.html          每個 Markdown 頁面
並刪除 <lang>/<kind>/ 下沒有對應 Markdown 的舊 HTML。
每個 HTML 都寫入 source-hash，check.py 用它判斷 HTML 是否過期。
"""
from __future__ import annotations

import html
import re
import sys

import markdown

from common import (
    KINDS,
    LANGS,
    ROOT,
    TEMPLATES,
    Page,
    as_list,
    file_hash,
    lang_hash,
    load_areas,
    load_pages,
    read_text,
    rel,
    sections,
    split_notes,
)

OTHER = {"en": "zh", "zh": "en"}
HTML_LANG = {"en": "en", "zh": "zh-Hant"}
SITE_NAME = {"en": "Paper Wiki", "zh": "論文 Wiki"}
SWITCH_LABEL = {"en": "中文", "zh": "English"}
HOME_LABEL = {"en": "Back to home", "zh": "回首頁"}
ROOT_LABEL = {"en": "Choose language", "zh": "選擇語言"}
KIND_LABEL = {
    "en": {"sources": "Source", "concepts": "Concept", "topics": "Topic"},
    "zh": {"sources": "來源", "concepts": "概念", "topics": "主題"},
}
GROUP_LABEL = {
    "en": {"topics": "Topics", "sources": "Sources", "concepts": "Concepts"},
    "zh": {"topics": "主題", "sources": "來源", "concepts": "概念"},
}
STATUS_LABEL = {
    "en": {"read": "Read", "skimmed": "Skimmed", "to-read": "To read"},
    "zh": {"read": "已讀", "skimmed": "略讀", "to-read": "未讀"},
}
TO_READ_NOTE = {
    "en": "The owner has not read this paper yet. This page was written by the AI from the full PDF.",
    "zh": "擁有者尚未閱讀這篇論文。本頁由 AI 讀完 PDF 全文後撰寫。",
}
INTRO = {
    "en": "A personal paper knowledge base maintained as an LLM Wiki. "
    "Pages are grouped by area; each paper links to the concepts and topics it relates to.",
    "zh": "依 LLM Wiki 方式維護的個人論文知識庫。頁面依領域分區，每篇論文都連到相關的概念與主題。",
}
EMPTY = {"en": "No pages yet.", "zh": "目前還沒有頁面。"}
PAPER_LINK = {"en": "Paper", "zh": "論文連結"}
COUNT = {
    "en": lambda n: f"{n} source" + ("" if n == 1 else "s"),
    "zh": lambda n: f"{n} 個來源",
}
NOTE_MARKERS = {
    "explainer": ("Explainer:", "解說（Explainer）："),
    "superseded": ("Superseded:", "後續變更："),
    "conflict": ("Conflict:", "衝突："),
}


def esc(value) -> str:
    return html.escape(str(value if value is not None else ""))


def md_to_html(text: str) -> str:
    out = markdown.markdown(text, extensions=["extra", "sane_lists"])
    # 站內 .md 連結改成 .html
    out = re.sub(
        r'href="(?![a-zA-Z][a-zA-Z0-9+.-]*:|#)([^"#]*?)\.md(#[^"]*)?"',
        lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"',
        out,
    )
    # 內容標記加上 class
    for cls, markers in NOTE_MARKERS.items():
        for marker in markers:
            out = out.replace(
                f"<blockquote>\n<p><strong>{marker}</strong>",
                f'<blockquote class="note note-{cls}">\n<p><strong>{marker}</strong>',
            )
    return out


def render_body(page: Page) -> str:
    """正文轉 HTML；空白的 My notes 區塊不顯示。"""
    before, notes = split_notes(page.body, page.lang)
    text = before if not notes.strip() else page.body
    return md_to_html(text)


def first_sentence(text: str) -> str:
    """取第一句（到 。！？ 或後面接空白與大寫字母的 . ! ?）；找不到就回傳全文。"""
    candidates = [m.group(0) for m in (
        re.match(r".+?[。！？]", text),
        re.match(r".+?[.!?](?=\s+[A-Z\"“(\[]|\s*$)", text),
    ) if m]
    return min(candidates, key=len) if candidates else text


def shorten(text: str, limit: int) -> str:
    """超過 limit 時截斷；英文在字的邊界截斷，避免切在字中間。"""
    if len(text) <= limit:
        return text
    cut = text[: limit - 1]
    if " " in cut and not re.search(r"[一-鿿]", cut):
        cut = cut.rsplit(" ", 1)[0]
    return cut.rstrip(" ,;:，；：") + "…"


def plain_summary(page: Page, limit: int = 200) -> str:
    """首頁卡片用：第一個區塊第一段文字的第一句，去掉 Markdown 與出處。"""
    secs = sections(page.body)
    if not secs:
        return ""
    for line in secs[0][1].split("\n"):
        line = line.strip()
        if not line or line.startswith((">", "|", "#")):
            continue
        line = re.sub(r"^([-*+]|\d+\.)\s+", "", line)
        line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)
        line = re.sub(r"\s*\(pp?\.[^)]*\)", "", line)
        line = line.replace("**", "").replace("`", "").replace("*", "")
        return shorten(first_sentence(line), limit)
    return ""


def fill(template: str, values: dict[str, str], content_key: str | None = None) -> str:
    """替換 {{key}}；內容最後才放，避免內容裡的文字被當成佔位符。"""
    for key, value in values.items():
        if key != content_key:
            template = template.replace("{{" + key + "}}", value)
    if content_key:
        template = template.replace("{{" + content_key + "}}", values[content_key])
    return template


def status_badge(lang: str, status) -> str:
    status = str(status or "")
    label = STATUS_LABEL[lang].get(status, status)
    return f'<span class="status status-{esc(status)}">{esc(label)}</span>'


def page_meta(page: Page, pages: dict[str, Page], areas: dict) -> str:
    lang, fm = page.lang, page.fm
    lines: list[str] = []
    if page.kind == "sources":
        parts = [esc(fm.get("authors")), esc(fm.get("year")), esc(fm.get("venue"))]
        url = fm.get("url")
        if url and str(url).startswith("http"):
            parts.append(f'<a href="{esc(url)}">{PAPER_LINK[lang]}</a>')
        lines.append(" · ".join(p for p in parts if p))
        second = [status_badge(lang, fm.get("status"))]
        for slug in as_list(fm.get("topics")):
            topic = pages.get(f"topics/{slug}")
            title = topic.fm.get("title", slug) if topic else slug
            second.append(f'<a href="../topics/{esc(slug)}.html">{esc(title)}</a>')
        lines.append(" · ".join(second))
        if fm.get("status") == "to-read":
            lines.append(f'<span class="status-note">{esc(TO_READ_NOTE[lang])}</span>')
    elif page.kind == "concepts":
        parts = []
        aliases = as_list(fm.get("aliases"))
        if aliases:
            parts.append(esc(", ".join(str(a) for a in aliases)))
        parts.append(COUNT[lang](len(as_list(fm.get("sources")))))
        lines.append(" · ".join(parts))
    elif page.kind == "topics":
        area = areas.get(fm.get("area"), {}) or {}
        parts = [esc(area.get(lang, fm.get("area", ""))), COUNT[lang](len(as_list(fm.get("sources"))))]
        lines.append(" · ".join(parts))
    return "\n".join(f'  <p class="meta">{line}</p>' for line in lines)


def build_page(page: Page, pages: dict[str, Page], areas: dict, template: str) -> str:
    lang = page.lang
    values = {
        "lang": HTML_LANG[lang],
        "source_hash": file_hash(page.path),
        "title": esc(page.fm.get("title", page.slug)),
        "site_name": SITE_NAME[lang],
        "root": "../../",
        "home": "../index.html",
        "home_label": HOME_LABEL[lang],
        "switch_href": f"../../{OTHER[lang]}/{page.kind}/{page.slug}.html",
        "switch_lang": HTML_LANG[OTHER[lang]],
        "switch_label": SWITCH_LABEL[lang],
        "kind": page.kind[:-1],
        "kind_label": KIND_LABEL[lang][page.kind],
        "meta": page_meta(page, pages, areas),
        "content": render_body(page),
    }
    return fill(template, values, content_key="content")


def card(page: Page) -> str:
    lang, fm, kind = page.lang, page.fm, page.kind
    singular = kind[:-1]
    head = f'<span class="tag tag-{singular}">{KIND_LABEL[lang][kind]}</span>'
    if kind == "sources":
        head += " " + status_badge(lang, fm.get("status"))
        meta = " · ".join(esc(x) for x in (fm.get("authors"), fm.get("year")) if x)
    else:
        meta = COUNT[lang](len(as_list(fm.get("sources"))))
    return (
        f'<a class="card card-{singular}" href="{kind}/{esc(page.slug)}.html">{head}'
        f'<h4>{esc(fm.get("title", page.slug))}</h4>'
        f'<p class="card-meta">{meta}</p>'
        f"<p>{esc(plain_summary(page))}</p></a>"
    )


def build_home(lang: str, pages: dict[str, Page], areas: dict, template: str) -> str:
    blocks: list[str] = []
    content = [p for p in pages.values() if p.kind in KINDS and not p.error]
    for slug, names in areas.items():
        names = names or {}
        groups = {
            "topics": sorted(
                (p for p in content if p.kind == "topics" and p.fm.get("area") == slug),
                key=lambda p: str(p.fm.get("title", "")),
            ),
            "sources": sorted(
                (p for p in content if p.kind == "sources" and slug in as_list(p.fm.get("areas"))),
                key=lambda p: (str(p.fm.get("year", "")), str(p.fm.get("title", ""))),
            ),
            "concepts": sorted(
                (p for p in content if p.kind == "concepts" and slug in as_list(p.fm.get("areas"))),
                key=lambda p: str(p.fm.get("title", "")).lower(),
            ),
        }
        if not any(groups.values()):
            continue
        parts = [f'<section class="area" id="{esc(slug)}">', f"<h2>{esc(names.get(lang, slug))}</h2>"]
        for kind in ("topics", "sources", "concepts"):
            if groups[kind]:
                parts.append(f"<h3>{GROUP_LABEL[lang][kind]}</h3>")
                parts.append('<div class="cards">' + "\n".join(card(p) for p in groups[kind]) + "</div>")
        parts.append("</section>")
        blocks.append("\n".join(parts))
    if not blocks:
        blocks.append(f'<p class="empty">{EMPTY[lang]}</p>')
    values = {
        "lang": HTML_LANG[lang],
        "source_hash": lang_hash(lang),
        "site_name": SITE_NAME[lang],
        "switch_href": f"../{OTHER[lang]}/index.html",
        "switch_lang": HTML_LANG[OTHER[lang]],
        "switch_label": SWITCH_LABEL[lang],
        "intro": esc(INTRO[lang]),
        "root_label": ROOT_LABEL[lang],
        "sections": "\n".join(blocks),
    }
    return fill(template, values, content_key="sections")


def write(path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    page_tpl = read_text(TEMPLATES / "page.html")
    home_tpl = read_text(TEMPLATES / "home.html")
    landing_tpl = read_text(TEMPLATES / "landing.html")
    areas = load_areas()
    counts: dict[str, int] = {}
    problems: list[str] = []
    written = 0
    removed: list[str] = []

    for lang in LANGS:
        pages = load_pages(lang)
        expected = set()
        for page in pages.values():
            if page.kind == "index":
                continue
            if page.error:
                problems.append(f"{rel(page.path)}: {page.error}")
                continue
            out = ROOT / lang / page.kind / f"{page.slug}.html"
            write(out, build_page(page, pages, areas, page_tpl))
            expected.add(out.resolve())
            written += 1
        for kind in KINDS:
            folder = ROOT / lang / kind
            if folder.exists():
                for old in folder.glob("*.html"):
                    if old.resolve() not in expected:
                        removed.append(rel(old))
                        old.unlink()
        write(ROOT / lang / "index.html", build_home(lang, pages, areas, home_tpl))
        counts[lang] = sum(1 for p in pages.values() if p.kind in KINDS)

    write(ROOT / "index.html", fill(landing_tpl, {"zh_count": str(counts["zh"]), "en_count": str(counts["en"])}))

    print(f"build: 產生 {written} 個頁面、2 個首頁、1 個根入口。")
    for item in removed:
        print(f"build: 刪除沒有對應 Markdown 的舊檔 {item}")
    for item in problems:
        print(f"build: 無法建置 {item}")
    return 1 if problems else 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(errors="replace")
    except AttributeError:
        pass
    sys.exit(main())
