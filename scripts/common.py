"""build.py 與 check.py 共用的解析與雜湊函式。

雜湊與區塊切分只能有一種算法，所以集中在這裡。修改前依 AGENTS.md 7.4 先提議。
所有路徑都由本檔位置推算，不使用本機絕對路徑。
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
TEMPLATES = ROOT / "templates"
LANGS = ("en", "zh")
KINDS = ("sources", "concepts", "topics")
SINGULAR = {"sources": "source", "concepts": "concept", "topics": "topic"}
NOTES_HEADING = {"en": "My notes", "zh": "我的筆記"}


def rel(path: Path) -> str:
    """相對於專案根目錄的路徑（正斜線）。"""
    return path.resolve().relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    """讀 UTF-8 文字檔；去掉部分編輯器會加的 BOM，並統一換行字元。"""
    return path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")


def split_frontmatter(text: str) -> tuple[dict, str]:
    """回傳 (frontmatter, 正文)。沒有 frontmatter 時回傳空 dict。YAML 錯誤會丟出例外。"""
    if not text.startswith("---\n"):
        return {}, text
    match = re.search(r"\n---[ \t]*(\n|$)", text[3:])
    if not match:
        return {}, text
    raw = text[4 : 3 + match.start() + 1]
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter 不是 key: value 格式")
    return data, text[3 + match.end() :]


def split_notes(text: str, lang: str) -> tuple[str, str]:
    """把整份文字切成 (My notes 之前, My notes 區塊內容)。My notes 一定是最後一個區塊。"""
    heading = f"## {NOTES_HEADING[lang]}"
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.rstrip() == heading:
            return "\n".join(lines[:i]), "\n".join(lines[i + 1 :])
    return text, ""


def normalize(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().split("\n"))


def short_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def translation_hash(en_path: Path) -> str:
    """中文版 translated_from 要填的值：英文檔扣掉 My notes 後的雜湊。"""
    before, _ = split_notes(read_text(en_path), "en")
    return short_hash(normalize(before))


def notes_hash(notes: str) -> str:
    return short_hash(normalize(notes))


def file_hash(path: Path) -> str:
    """HTML 的 source-hash：對應 Markdown 全文的雜湊。"""
    return short_hash(read_text(path))


def sections(body: str) -> list[tuple[str, str]]:
    """依 `## ` 標題切分正文（略過程式碼區塊），回傳 [(標題, 內容)]。"""
    result: list[tuple[str, str]] = []
    current: str | None = None
    buf: list[str] = []
    in_fence = False
    for line in body.split("\n"):
        if line.strip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("## "):
            if current is not None:
                result.append((current, "\n".join(buf)))
            current, buf = line[3:].strip(), []
        elif current is not None:
            buf.append(line)
    if current is not None:
        result.append((current, "\n".join(buf)))
    return result


@dataclass
class Page:
    lang: str
    kind: str  # sources / concepts / topics / index
    slug: str
    path: Path
    text: str = ""
    fm: dict = field(default_factory=dict)
    body: str = ""
    error: str | None = None

    @property
    def key(self) -> str:
        return "index" if self.kind == "index" else f"{self.kind}/{self.slug}"

    @property
    def notes(self) -> str:
        return split_notes(self.text, self.lang)[1]

    @property
    def body_without_notes(self) -> str:
        return split_notes(self.body, self.lang)[0]


def load_page(path: Path, lang: str, kind: str) -> Page:
    page = Page(lang=lang, kind=kind, slug=path.stem, path=path)
    page.text = read_text(path)
    try:
        page.fm, page.body = split_frontmatter(page.text)
    except Exception as exc:  # YAML 錯誤
        page.error = f"frontmatter 無法解析：{exc}"
        page.body = page.text
    return page


def load_pages(lang: str) -> dict[str, Page]:
    """讀入 wiki/<lang>/ 的所有頁面（含 index.md），key 為 'sources/<slug>' 或 'index'。"""
    pages: dict[str, Page] = {}
    base = WIKI / lang
    index = base / "index.md"
    if index.exists():
        pages["index"] = load_page(index, lang, "index")
    for kind in KINDS:
        for path in sorted((base / kind).glob("*.md")):
            page = load_page(path, lang, kind)
            pages[page.key] = page
    return pages


def lang_hash(lang: str) -> str:
    """首頁的 source-hash：該語言所有頁面與 areas.yml 的雜湊。"""
    parts = []
    areas = WIKI / "areas.yml"
    if areas.exists():
        parts.append(read_text(areas))
    for kind in KINDS:
        for path in sorted((WIKI / lang / kind).glob("*.md")):
            parts.append(rel(path) + "\n" + read_text(path))
    return short_hash("\n\x00\n".join(parts))


def load_areas() -> dict:
    path = WIKI / "areas.yml"
    if not path.exists():
        return {}
    return yaml.safe_load(read_text(path)) or {}


def as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]
