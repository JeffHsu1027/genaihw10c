# 論文 Wiki（Paper Wiki）

依 [Karpathy 的 LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 構想維護的個人論文知識庫，收錄讀過或有興趣的論文，第一個主題區是世界模型（world models）。

- 網站：GitHub Pages 從本 repo 根目錄發佈，入口是 `index.html`（中文 `zh/`、英文 `en/`）。
- 規則：[`AGENTS.md`](AGENTS.md)（資料夾結構、命名、ingest / query / lint 流程）。
- 設計決策與需求：[`docs/decisions.md`](docs/decisions.md)、[`docs/requirements.md`](docs/requirements.md)。
- 紀錄：[`wiki/log.md`](wiki/log.md)。

## 運作方式

1. 論文 PDF 放在 `raw/`（只留在本機，不上傳；清單見 [`raw/README.md`](raw/README.md)）。
2. AI 依 `AGENTS.md` 讀完論文，寫英文 Markdown（`wiki/en/`），再翻成繁體中文（`wiki/zh/`）。
3. `python scripts/build.py` 由 Markdown 產生全站 HTML；`python scripts/check.py` 檢查格式、出處、翻譯同步與連結。

第一次使用前安裝套件：`python -m pip install -r requirements.txt`。
