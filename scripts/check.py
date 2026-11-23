"""check.py — Wiki 檢查（AGENTS.md 第 8 節；項目來自 docs/decisions.md 6.1 與 docs/requirements.md）。

用法：
  python scripts/check.py                  執行全部檢查；全部通過時結束碼為 0
  python scripts/check.py --hash <英文檔>   輸出中文版 translated_from 要填的雜湊
  python scripts/check.py --accept-notes   擁有者修改 My notes 後更新快照（AI 不可執行）

檢查項目：
  [語言與翻譯] wiki/en/ 沒有中文字元（My notes 除外）；中英頁一一對應；translated_from 相符；
      frontmatter 值一致；標題層級與順序、出處集合、連結集合、內容標記數量一致
  [格式] frontmatter 必填欄位與合法值；區塊與範本一致且不空；沒有殘留 {{；出處格式與頁碼不超過 pages；
      含數字的句子有出處；解釋區塊與 Explainer 不含數字；Background 每項有外部連結；
      引用長度與數量；概念頁 Explanation 長度
  [連結與結構] Markdown 站內連結存在且指向同語言；frontmatter 與內文的雙向連結；
      index.md 列出所有頁面；沒有孤兒頁；HTML 存在、未過期、沒有 {{、連結存在
  [紀錄與保護] log.md 標題格式；raw/README.md 列出每個 PDF；.gitignore 排除 raw/*.pdf；
      My notes 快照；AGENTS.md 長度；沒有本機絕對路徑
本檔只讀不寫（--accept-notes 除外），不使用 git。
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from common import (
    KINDS,
    LANGS,
    NOTES_HEADING,
    ROOT,
    SINGULAR,
    TEMPLATES,
    WIKI,
    Page,
    as_list,
    file_hash,
    lang_hash,
    load_areas,
    load_pages,
    notes_hash,
    read_text,
    rel,
    sections,
    translation_hash,
)

# 名稱中帶獨立數字、不算「含數字」的專有名詞。新增時記一筆 rules（AGENTS.md 第 5 節）。
NUMBERED_NAMES = ["Dreamer 4"]

AGENTS_MAX_CHARS = 12000
QUOTE_MAX_WORDS = 25
QUOTES_PER_PAGE = 2
EXPLANATION_MAX = {"en": 200, "zh": 300}
STATUSES = {"read", "skimmed", "to-read"}
LOG_TYPES = ("setup", "ingest", "query", "lint", "rules")
SNAPSHOT = WIKI / ".notes-snapshot.json"

REQUIRED = {
    "sources": ["title", "authors", "year", "venue", "url", "raw", "pages", "added", "updated",
                "areas", "status", "concepts", "topics"],
    "concepts": ["title", "aliases", "updated", "areas", "sources"],
    "topics": ["title", "area", "updated", "sources", "concepts"],
}
LIST_FIELDS = {"areas", "concepts", "topics", "sources", "aliases"}
LANG_FREE_FIELDS = {"title", "aliases", "translated_from"}

# 區塊分類（N4①：只寫通用知識、不可含數字的區塊；不檢查數字的區塊）
EXPLAIN_SECTIONS = {
    "en": {"One-line definition", "Explanation", "Overview", "Key terms"},
    "zh": {"一句話定義", "說明", "概述", "術語表"},
}
BACKGROUND = {"en": "Background", "zh": "背景資料"}
EXPLANATION = {"en": "Explanation", "zh": "說明"}
MARKERS = {
    "explainer": {"en": "**Explainer:**", "zh": "**解說（Explainer）：**"},
    "superseded": {"en": "**Superseded:**", "zh": "**後續變更：**"},
    "conflict": {"en": "**Conflict:**", "zh": "**衝突：**"},
}
PLACEHOLDERS = {
    "(Not covered in this paper)", "(None yet)", "No directly related sources yet.",
    "（本文未提及）", "（尚無）", "目前沒有直接相關的來源。",
}

CJK = re.compile(r"[　-〿㐀-䶿一-鿿豈-﫿＀-￯]")
REF_ANY = re.compile(r"\(pp?\.[^)]*\)")
REF_OK = re.compile(r"\((?:p\.\d+|pp\.\d+-\d+)(?:, (?:Fig\.|Table|Eq\.) ?[A-Z]?\d+[a-z]?)?\)")
MD_LINK = re.compile(r"!?\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
AUTO_LINK = re.compile(r"<(https?://[^>\s]+)>")
QUOTE = re.compile(r"\"([^\"\n]+)\"|“([^”\n]+)”")
HTML_LINK = re.compile(r"(?:href|src)=\"([^\"]+)\"")
EXTERNAL = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
LOG_HEADING = re.compile(r"^## \[\d{4}-\d{2}-\d{2}\] (" + "|".join(LOG_TYPES) + r") \| \S.*$")
# 本機絕對路徑：磁碟代號開頭，或常見的使用者目錄（字串拆開寫，避免本檔自己被掃到）
ABS_PATH = re.compile(r"(?<![A-Za-z])[A-Za-z]:[\\/]|/" + "Users/|/" + "home/")
ABBREVIATIONS = ["e.g.", "i.e.", "et al.", "vs.", "Figs.", "Fig.", "Eqs.", "Eq.", "Sec.",
                 "approx.", "cf.", "No.", "pp.", "p.", "etc."]
EXEMPT_NUMBERS = [
    re.compile(r"`[^`]*`"),
    REF_ANY,
    MD_LINK,
    AUTO_LINK,
    re.compile(r"\((?:to be verified)\)|（待確認）"),
    re.compile(r"\b(?:Fig|Figs|Figure|Figures|Table|Tables|Tab|Eq|Eqs|Equation|Section|Sec|"
               r"Appendix|App|Alg|Algorithm|Chapter|Step)\.?\s*[A-Z]?\d+(?:\.\d+)*[a-z]?"),
    re.compile(r"§\s?\d+(?:\.\d+)*|[圖表式]\s?[A-Z]?\d+|第\s?\d+\s?[節章步]|附錄\s?[A-Z]\d*"),
    re.compile(r"(?<!\d)(?:19|20)\d{2}s?(?!\d)"),  # 年份
    re.compile(r"\b(?=[\w-]*[A-Za-z])(?=[\w-]*\d)[\w-]+\b"),  # 字母與數字混合的名稱
]

errors: dict[str, list[str]] = defaultdict(list)


def err(category: str, where, message: str) -> None:
    where = rel(where) if isinstance(where, Path) else where
    errors[category].append(f"{where}: {message}")


# ---------------------------------------------------------------- 文字工具

def strip_code(text: str) -> str:
    """去掉程式碼區塊與行內程式碼（裡面的文字不算連結、出處或引用）。"""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def links_in(text: str) -> list[str]:
    text = strip_code(text)
    return [m.group(2) for m in MD_LINK.finditer(text)] + AUTO_LINK.findall(text)


def mask_numbers(text: str) -> str:
    for name in NUMBERED_NAMES:
        text = text.replace(name, "")
    for pattern in EXEMPT_NUMBERS:
        text = pattern.sub(" ", text)
    return text


def split_sentences(text: str) -> list[str]:
    for abbr in ABBREVIATIONS:
        text = text.replace(abbr, abbr.replace(".", "\x00"))
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"“(\[*])|(?<=[。！？])", text)
    return [p.replace("\x00", ".").strip() for p in parts if p.strip()]


def units(content: str):
    """把區塊內容切成 ('quote', 文字) 或 ('text', 文字)：引用區塊整段、清單項目與表格列各一個。"""
    content = strip_code(content)
    quote: list[str] = []
    items: list[str] = []
    for line in content.split("\n") + [""]:
        s = line.strip()
        if s.startswith(">"):
            quote.append(s.lstrip(">").strip())
            continue
        if quote:
            yield "quote", " ".join(quote)
            quote = []
        if not s:
            yield from (("text", i) for i in items)
            items = []
        elif s.startswith("#"):
            continue
        elif s.startswith("|"):
            if not re.fullmatch(r"\|[\s:|-]+\|?", s):
                items.append(s)
        elif re.match(r"([-*+]|\d+\.)\s+", s):
            items.append(re.sub(r"^([-*+]|\d+\.)\s+", "", s))
        elif items and not items[-1].startswith("|"):
            items[-1] += " " + s
        else:
            items.append(s)


def marker_of(text: str, lang: str) -> str | None:
    for name, by_lang in MARKERS.items():
        if text.startswith(by_lang[lang]):
            return name
    return None


def heading_levels(body: str) -> list[int]:
    return [len(m.group(1)) for m in re.finditer(r"^(#{1,6}) ", strip_code(body), flags=re.M)]


def template_headings(kind: str, lang: str) -> list[str]:
    path = TEMPLATES / f"{SINGULAR[kind]}.{lang}.md"
    return [h for h, _ in sections(read_text(path))] if path.exists() else []


# ---------------------------------------------------------------- 格式

def check_format(page: Page, areas: dict) -> None:
    fm, lang, kind = page.fm, page.lang, page.kind
    cat = "格式"
    if kind == "index":
        if lang == "zh" and "translated_from" not in fm:
            err(cat, page.path, "缺少 frontmatter 欄位 translated_from")
        return
    for key in REQUIRED[kind] + (["translated_from"] if lang == "zh" else []):
        if key not in fm:
            err(cat, page.path, f"缺少 frontmatter 欄位 {key}")
    for key in LIST_FIELDS & fm.keys():
        if not isinstance(fm[key], list):
            err(cat, page.path, f"frontmatter {key} 必須是清單 [..]")
    for area in as_list(fm.get("areas")) + ([fm["area"]] if "area" in fm else []):
        if area not in areas:
            err(cat, page.path, f"領域 {area} 不在 wiki/areas.yml")
    if kind == "sources" and fm.get("status") not in STATUSES:
        err(cat, page.path, f"status 必須是 read / skimmed / to-read，目前是 {fm.get('status')}")
    if kind == "sources" and "pages" in fm and not (isinstance(fm["pages"], int) and fm["pages"] > 0):
        err(cat, page.path, f"pages 必須是正整數（PDF 總頁數），目前是 {fm['pages']}")
    if kind == "sources" and fm.get("raw") and not (ROOT / str(fm["raw"])).exists():
        err(cat, page.path, f"raw 指向的 PDF 不存在：{fm['raw']}")
    if "{{" in page.text:
        err(cat, page.path, "殘留範本佔位符 {{")

    secs = sections(page.body)
    headings = [h for h, _ in secs]
    expected = template_headings(kind, lang)
    if headings != expected:
        err(cat, page.path, f"區塊標題或順序與範本不同：應為 {expected}，實際為 {headings}")

    notes_heading = NOTES_HEADING[lang]
    quotes = 0
    for heading, content in secs:
        if heading == notes_heading:
            continue
        if not content.strip():
            err(cat, page.path, f"區塊「{heading}」是空的，請寫佔位文字")
            continue
        plain = strip_code(content)
        for m in REF_ANY.finditer(plain):
            if not REF_OK.fullmatch(m.group(0)):
                err(cat, page.path, f"出處格式錯誤：{m.group(0)}（應為 (p.7)、(pp.7-8)、(p.7, Fig. 3)）")
        for m in QUOTE.finditer(plain):
            quotes += 1
            words = len((m.group(1) or m.group(2)).split())
            if words > QUOTE_MAX_WORDS:
                err(cat, page.path, f"引用超過 {QUOTE_MAX_WORDS} 個字（{words}）：{m.group(0)[:40]}...")
            if not re.match(r"\s*\(pp?\.", plain[m.end(): m.end() + 12]):
                err(cat, page.path, f"引用後面沒有出處：{m.group(0)[:40]}")
        if heading == BACKGROUND[lang]:
            check_background(page, content)
            continue
        if kind == "concepts" and heading == EXPLANATION[lang]:
            check_length(page, content)
        explain = heading in EXPLAIN_SECTIONS[lang]
        for unit_kind, text in units(content):
            if text in PLACEHOLDERS:
                continue
            marker = marker_of(text, lang) if unit_kind == "quote" else None
            if marker == "explainer":
                if re.search(r"\d", mask_numbers(text)):
                    err(cat, page.path, f"Explainer 不可含數字：{text[:60]}")
                continue
            for sentence in split_sentences(text):
                if not re.search(r"\d", mask_numbers(sentence)):
                    continue
                if explain:
                    err(cat, page.path, f"「{heading}」只寫通用知識，不可含數字：{sentence[:60]}")
                elif not REF_ANY.search(sentence):
                    err(cat, page.path, f"含數字的句子沒有出處：{sentence[:60]}")
    if quotes > QUOTES_PER_PAGE:
        err(cat, page.path, f"原文引用 {quotes} 句，超過每頁 {QUOTES_PER_PAGE} 句")


def check_background(page: Page, content: str) -> None:
    text = content.strip()
    if text in PLACEHOLDERS:
        return
    for line in text.split("\n"):
        s = line.strip()
        if not s:
            continue
        if not re.match(r"[-*+]\s+", s):
            err("格式", page.path, f"Background 只能是清單項目：{s[:50]}")
        elif not re.search(r"\]\(https?://|<https?://", s):
            err("格式", page.path, f"Background 項目沒有外部連結：{s[:50]}")


def check_length(page: Page, content: str) -> None:
    text = MD_LINK.sub(lambda m: m.group(1), strip_code(content))
    if page.lang == "en":
        size = len(re.findall(r"[A-Za-z0-9'’-]+", text))
        unit = "words"
    else:
        size = len(CJK.findall(text)) + len(re.findall(r"[A-Za-z0-9'’-]+", text))
        unit = "字"
    if size > EXPLANATION_MAX[page.lang]:
        err("格式", page.path, f"Explanation 長度 {size} {unit}，上限 {EXPLANATION_MAX[page.lang]}")


# ---------------------------------------------------------------- 語言與翻譯

def check_translation(en: dict[str, Page], zh: dict[str, Page]) -> None:
    cat = "語言與翻譯"
    for page in en.values():
        before = page.text.split(f"\n## {NOTES_HEADING['en']}")[0]
        for no, line in enumerate(before.split("\n"), 1):
            if CJK.search(line):
                err(cat, page.path, f"第 {no} 行有中文字元：{line.strip()[:50]}")
                break
    for key in sorted(en.keys() - zh.keys()):
        err(cat, en[key].path, "缺少對應的中文頁")
    for key in sorted(zh.keys() - en.keys()):
        err(cat, zh[key].path, "缺少對應的英文頁")
    for key in sorted(en.keys() & zh.keys()):
        e, z = en[key], zh[key]
        if e.error or z.error:
            continue
        expected = translation_hash(e.path)
        if str(z.fm.get("translated_from", "")) != expected:
            err(cat, z.path, f"中文版過期：translated_from 應為 {expected}（英文版已修改，請重譯變動處）")
        for k in sorted((e.fm.keys() | z.fm.keys()) - LANG_FREE_FIELDS):
            if str(e.fm.get(k)) != str(z.fm.get(k)):
                err(cat, z.path, f"frontmatter {k} 與英文版不同")
        eb, zb = e.body_without_notes, z.body_without_notes
        if heading_levels(eb) != heading_levels(zb):
            err(cat, z.path, "標題數量或層級與英文版不同")
        e_refs = set(REF_ANY.findall(strip_code(eb)))
        z_refs = set(REF_ANY.findall(strip_code(zb)))
        if e_refs != z_refs:
            err(cat, z.path, f"出處集合與英文版不同：只在英文 {sorted(e_refs - z_refs)}，只在中文 {sorted(z_refs - e_refs)}")
        e_links, z_links = set(links_in(eb)), set(links_in(zb))
        if e_links != z_links:
            err(cat, z.path, f"連結集合與英文版不同：只在英文 {sorted(e_links - z_links)}，只在中文 {sorted(z_links - e_links)}")
        for name, by_lang in MARKERS.items():
            if eb.count(by_lang["en"]) != zb.count(by_lang["zh"]):
                err(cat, z.path, f"{name} 標記數量與英文版不同")


# ---------------------------------------------------------------- 連結與結構

def resolve(page: Page, href: str) -> Path | None:
    target = href.split("#")[0]
    if not target:
        return None
    return (page.path.parent / target).resolve()


def check_structure(lang: str, pages: dict[str, Page]) -> None:
    cat = "連結與結構"
    base = (WIKI / lang).resolve()
    by_path = {p.path.resolve(): p for p in pages.values()}
    out: dict[str, set[str]] = defaultdict(set)
    inbound: dict[str, set[str]] = defaultdict(set)
    for page in pages.values():
        for href in links_in(page.body_without_notes):
            if EXTERNAL.match(href) or href.startswith("#"):
                continue
            target = resolve(page, href)
            if target is None:
                continue
            if not target.exists():
                err(cat, page.path, f"連結指向不存在的檔案：{href}")
            elif base not in target.parents:
                err(cat, page.path, f"站內連結必須指向 wiki/{lang}/ 內的頁面：{href}")
            elif target in by_path:
                key = by_path[target].key
                out[page.key].add(key)
                if page.kind != "index" and key != page.key:
                    inbound[key].add(page.key)

    def need(kind: str, slug, page: Page, field_name: str) -> Page | None:
        other = pages.get(f"{kind}/{slug}")
        if other is None:
            err(cat, page.path, f"{field_name} 列出的 {kind}/{slug} 不存在")
        return other

    for page in pages.values():
        if page.error or page.kind == "index":
            continue
        fm = page.fm
        if page.kind == "sources":
            for slug in as_list(fm.get("concepts")):
                c = need("concepts", slug, page, "concepts")
                if c:
                    if page.slug not in as_list(c.fm.get("sources")):
                        err(cat, c.path, f"frontmatter sources 缺少 {page.slug}（來源頁有列這個概念）")
                    if c.key not in out[page.key]:
                        err(cat, page.path, f"內文沒有連到概念頁 {slug}")
                    if page.key not in out[c.key]:
                        err(cat, c.path, f"內文沒有連到來源頁 {page.slug}")
            for slug in as_list(fm.get("topics")):
                t = need("topics", slug, page, "topics")
                if t and page.slug not in as_list(t.fm.get("sources")):
                    err(cat, t.path, f"frontmatter sources 缺少 {page.slug}（來源頁有列這個主題）")
        elif page.kind == "concepts":
            for slug in as_list(fm.get("sources")):
                s = need("sources", slug, page, "sources")
                if s and page.slug not in as_list(s.fm.get("concepts")):
                    err(cat, s.path, f"frontmatter concepts 缺少 {page.slug}（概念頁有列這個來源）")
        elif page.kind == "topics":
            for slug in as_list(fm.get("sources")):
                s = need("sources", slug, page, "sources")
                if s:
                    if page.slug not in as_list(s.fm.get("topics")):
                        err(cat, s.path, f"frontmatter topics 缺少 {page.slug}（主題頁有列這個來源）")
                    if fm.get("area") not in as_list(s.fm.get("areas")):
                        err(cat, s.path, f"areas 缺少主題頁 {page.slug} 的領域 {fm.get('area')}")
                    if s.key not in out[page.key]:
                        err(cat, page.path, f"內文沒有連到來源頁 {slug}")
            for slug in as_list(fm.get("concepts")):
                c = need("concepts", slug, page, "concepts")
                if c and c.key not in out[page.key]:
                    err(cat, page.path, f"內文沒有連到概念頁 {slug}")

    index = pages.get("index")
    for page in pages.values():
        if page.kind == "index":
            continue
        if index is not None and page.key not in out["index"]:
            err(cat, WIKI / lang / "index.md", f"沒有列出 {page.key}")
        if page.kind in ("sources", "concepts") and not inbound[page.key]:
            err(cat, page.path, "孤兒頁：沒有任何其他頁面連到這裡")
    if index is None:
        err(cat, WIKI / lang / "index.md", "檔案不存在")


def ref_pages(ref: str) -> list[int]:
    """(p.7) → [7]；(pp.7-8) → [7, 8]。"""
    return [int(n) for n in re.findall(r"\d+", ref.split(",")[0])]


def check_page_bounds(lang: str, pages: dict[str, Page]) -> None:
    """出處頁碼不可超過來源頁的 pages。
    來源頁：所有出處都屬於本篇。概念頁與主題頁：出處屬於同一行（或同一個 ### 小節中）最近連到的來源頁。"""
    cat = "格式"
    limits = {p.slug: p.fm.get("pages") for p in pages.values()
              if p.kind == "sources" and isinstance(p.fm.get("pages"), int)}

    def check_ref(page: Page, ref: str, slug: str) -> None:
        nums = ref_pages(ref)
        limit = limits.get(slug)
        if len(nums) == 2 and nums[0] >= nums[1]:
            err(cat, page.path, f"頁碼範圍錯誤：{ref}")
        if limit and any(n < 1 or n > limit for n in nums):
            err(cat, page.path, f"出處 {ref} 超過 {slug} 的 PDF 總頁數 {limit}")

    for page in pages.values():
        if page.error or page.kind == "index":
            continue
        text = strip_code(page.body_without_notes)
        if page.kind == "sources":
            for ref in REF_ANY.findall(text):
                check_ref(page, ref, page.slug)
            continue
        current = None
        for line in text.split("\n"):
            if line.startswith("#"):
                current = None
            linked = re.findall(r"\]\([^)]*?sources/([a-z0-9-]+)\.md", line)
            if linked:
                current = linked[-1]
            for ref in REF_ANY.findall(line):
                if current:
                    check_ref(page, ref, current)


def check_html(lang: str, pages: dict[str, Page]) -> None:
    cat = "連結與結構"
    expected = set()
    for page in pages.values():
        if page.kind == "index" or page.error:
            continue
        out = ROOT / lang / page.kind / f"{page.slug}.html"
        expected.add(out.resolve())
        if not out.exists():
            err(cat, out, "HTML 不存在，請執行 python scripts/build.py")
        elif f'name="source-hash" content="{file_hash(page.path)}"' not in read_text(out):
            err(cat, out, "HTML 已過期，請執行 python scripts/build.py")
    home = ROOT / lang / "index.html"
    if not home.exists():
        err(cat, home, "首頁不存在，請執行 python scripts/build.py")
    elif f'name="source-hash" content="{lang_hash(lang)}"' not in read_text(home):
        err(cat, home, "首頁已過期，請執行 python scripts/build.py")
    for kind in KINDS:
        folder = ROOT / lang / kind
        for path in folder.glob("*.html") if folder.exists() else []:
            if path.resolve() not in expected:
                err(cat, path, "沒有對應的 Markdown，請執行 python scripts/build.py 清除")


def check_html_links() -> None:
    cat = "連結與結構"
    files = [ROOT / "index.html"] + [p for lang in LANGS for p in (ROOT / lang).rglob("*.html")]
    for path in files:
        if not path.exists():
            err(cat, path, "不存在，請執行 python scripts/build.py")
            continue
        text = read_text(path)
        if "{{" in text:
            err(cat, path, "HTML 殘留 {{")
        for href in HTML_LINK.findall(text):
            if EXTERNAL.match(href) or href.startswith("#"):
                continue
            target = href.split("#")[0].split("?")[0]
            if target and not (path.parent / target).resolve().exists():
                err(cat, path, f"連結指向不存在的檔案：{href}")


# ---------------------------------------------------------------- 紀錄與保護

def check_records(all_pages: list[Page]) -> None:
    cat = "紀錄與保護"
    log = WIKI / "log.md"
    if not log.exists():
        err(cat, log, "檔案不存在")
    else:
        entries = [line for line in read_text(log).split("\n") if line.startswith("## ")]
        if not entries:
            err(cat, log, "沒有任何紀錄")
        for i, line in enumerate(entries):
            m = LOG_HEADING.match(line)
            if not m:
                err(cat, log, f"標題格式應為 ## [YYYY-MM-DD] 類型 | 標題：{line[:60]}")
            elif m.group(1) == "setup" and i != 0:
                err(cat, log, f"setup 只能用於第一筆紀錄：{line[:60]}")

    readme = ROOT / "raw" / "README.md"
    listing = read_text(readme) if readme.exists() else ""
    if not readme.exists():
        err(cat, readme, "檔案不存在")
    for pdf in sorted((ROOT / "raw").glob("*.pdf")):
        if pdf.name not in listing:
            err(cat, readme, f"沒有列出 {pdf.name}")
    gitignore = ROOT / ".gitignore"
    if not gitignore.exists() or "raw/*.pdf" not in [l.strip() for l in read_text(gitignore).split("\n")]:
        err(cat, gitignore, "必須包含 raw/*.pdf（PDF 不可進入 git）")

    snapshot = json.loads(read_text(SNAPSHOT)) if SNAPSHOT.exists() else {}
    for page in all_pages:
        if page.kind == "index":
            continue
        key, notes = rel(page.path), page.notes
        if key in snapshot:
            if notes_hash(notes) != snapshot[key]:
                err(cat, page.path, "My notes 與快照不同：AI 不可修改 My notes"
                    "（若是擁有者自己改的，請擁有者執行 --accept-notes）")
        elif notes.strip():
            err(cat, page.path, "My notes 不是空的，但不在快照中：AI 建立頁面時必須留空"
                "（若是擁有者寫的，請擁有者執行 --accept-notes）")

    agents = ROOT / "AGENTS.md"
    if agents.exists():
        size = len(read_text(agents))
        if size > AGENTS_MAX_CHARS:
            err(cat, agents, f"{size} 字元，超過上限 {AGENTS_MAX_CHARS}")
    else:
        err(cat, agents, "檔案不存在")

    scan = [ROOT / n for n in ("AGENTS.md", "CLAUDE.md", "README.md", "requirements.txt", "index.html")]
    scan += list((ROOT / "scripts").glob("*.py")) + list(TEMPLATES.glob("*"))
    scan += list((ROOT / "assets").glob("*")) + list(WIKI.rglob("*.md")) + list(WIKI.glob("*.yml"))
    scan += [readme] + [p for lang in LANGS for p in (ROOT / lang).rglob("*.html")]
    for path in scan:
        if path.is_file():
            for no, line in enumerate(read_text(path).split("\n"), 1):
                if ABS_PATH.search(line):
                    err(cat, path, f"第 {no} 行疑似本機絕對路徑：{line.strip()[:60]}")


# ---------------------------------------------------------------- 主程式

def accept_notes() -> int:
    snapshot = {}
    for lang in LANGS:
        for page in load_pages(lang).values():
            if page.kind != "index" and page.notes.strip():
                snapshot[rel(page.path)] = notes_hash(page.notes)
    SNAPSHOT.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8", newline="\n")
    print(f"已更新 My notes 快照：{len(snapshot)} 個頁面有筆記。")
    return 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["--hash"]:
        if len(argv) != 2:
            print("用法：python scripts/check.py --hash wiki/en/<kind>/<slug>.md")
            return 2
        path = (ROOT / argv[1]).resolve()
        if (WIKI / "en").resolve() not in path.parents or not path.exists():
            print(f"找不到英文檔：{argv[1]}")
            return 2
        print(translation_hash(path))
        return 0
    if argv[:1] == ["--accept-notes"]:
        return accept_notes()
    if argv:
        print(__doc__)
        return 2

    areas = load_areas()
    if not areas:
        err("格式", WIKI / "areas.yml", "檔案不存在或是空的")
    pages = {lang: load_pages(lang) for lang in LANGS}
    all_pages = [p for lang in LANGS for p in pages[lang].values()]
    for page in all_pages:
        if page.error:
            err("格式", page.path, page.error)
        else:
            check_format(page, areas)
    check_translation(pages["en"], pages["zh"])
    for lang in LANGS:
        check_structure(lang, pages[lang])
        check_page_bounds(lang, pages[lang])
        check_html(lang, pages[lang])
    check_html_links()
    check_records(all_pages)

    counts = {lang: sum(1 for p in pages[lang].values() if p.kind != "index") for lang in LANGS}
    print(f"check: 英文 {counts['en']} 頁、中文 {counts['zh']} 頁")
    for category in ("語言與翻譯", "格式", "連結與結構", "紀錄與保護"):
        problems = errors.get(category, [])
        print(f"[{'OK' if not problems else 'FAIL'}] {category}" + (f"：{len(problems)} 個問題" if problems else ""))
        for problem in problems:
            print(f"    - {problem}")
    total = sum(len(v) for v in errors.values())
    print("check: 全部通過" if total == 0 else f"check: 共 {total} 個問題")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(errors="replace")
    except AttributeError:
        pass
    sys.exit(main(sys.argv[1:]))
