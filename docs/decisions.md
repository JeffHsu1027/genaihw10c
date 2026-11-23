# 決策紀錄（階段 0：設計）

這份文件記錄第 10 週作業開工前，擁有者與 AI 討論後確定的決定與理由。
訪談（階段 1 第一步）以本文件為背景：**這裡已決定的事項不再重問**，只問第 9 節列出的待決問題。

- 建立日期：2026-11-23
- 討論對象：Claude（claude.ai 對話）
- 參考資料：`docs/reference/`（上週的 `CLAUDE.md` 與 `log.md`）；Karpathy 的 LLM Wiki 原文不放進 repo，見 <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>

---

## 1. 作業要求摘要

本週作業：先建立自己主題的 LLM Wiki，再以 Wiki 為唯一知識來源，產出一份教學型 HTML 簡報，並說明 loop / graph 設計與反思。

| 步驟 | 要求 |
|---|---|
| 一、建 Wiki | 主題自選；用「先討論、後生成」的方式建立；至少 ingest 5 篇 |
| 二、做簡報 | AI 以 Wiki 為知識來源，產出教學型 HTML 簡報，讓不熟悉主題的人能理解基本概念 |
| 三、說明流程 | loop / graph 設計：哪些步驟會重複、哪裡需要檢查或重新生成、為什麼這樣設計 |
| 四、反思 | 哪個節點最常出錯？檢查往前移到哪一步？是否因此修改 workflow / graph？為什麼？ |

9–10 分的條件：Wiki 與簡報內容有明確對應；loop / graph 設計合理且說明清楚；有實際執行與檢查紀錄；能反思出錯節點與檢查前移；簡報有清楚的教學結構。

其他繳交規範（第 9 週助教提醒，本週沿用）：
- GitHub repo 設為 **Public**；網頁連結用**無痕視窗**測試，不可交 `localhost`。
- 規則檔（`AGENTS.md`）放在 repo 內，寫清楚資料夾結構、命名與新資料的處理步驟。
- 推上 GitHub 前確認沒有個資、密碼、API Key；論文 PDF 不上傳。
- 說明中寫出**人的決策過程**：給誰用、解決什麼問題、AI 初版哪裡不好、怎麼改、學到什麼。

### 繳交項目 ↔ 素材來源

| 繳交項目 | 素材來源 |
|---|---|
| 1. Wiki 主題與簡介 | 個人論文 Wiki（所有讀過或有興趣的論文），第一個主題區是世界模型 |
| 2. Wiki 連結 | 本 repo 的 GitHub Pages |
| 3. 教學 HTML 簡報 | 「世界模型是什麼？（What is a World Model?）」，由第 7 節的 graph 產出 |
| 4. loop / graph 說明 | 第 7 節的流程圖，以及 `make-slides` skill |
| 5. 執行與檢查紀錄 | `decks/<topic>/report.md`，加上每過一關 commit 一次的 git log |
| 6. 反思 | `report.md` 的實際結果；第 10 節「與上週的差異」 |
| 加分：決策過程 | 本文件第 2 節 |

---

## 2. 決策與理由

### D1. 新開 repo 重建，不改上週的 repo

- **決定**：在新的 repo（本機資料夾 `genaihw10c`）從頭建立，上週的 `genaihw9withclaude` 保持原樣。
- **理由**：
  1. 上週繳交的 GitHub Pages 連結可能還在批改，改舊 repo 會改到已繳交的內容。
  2. 這次的修改是根本性的（主要語言、引用規則、建置方式），改舊檔的工作量不比重建少，還會留下中文為主的痕跡。
  3. 作業要求「先討論、後生成」，在舊檔上修改無法展示這個流程。
- **路徑原則**：所有規則、腳本與連結一律使用相對於 repo 根目錄的路徑，不寫本機的絕對路徑。資料夾改名或搬家都不受影響。
- **不是從零開始**：訪談時把上週的 `CLAUDE.md` 與 `log.md` 當作輸入，保留上週累積的好規則（例如更新既有頁面要附把握度、列出刻意不連結之處）。

### D2. Wiki 收錄所有論文，簡報只取其中一個主題

- **決定**：Wiki 是擁有者的個人論文庫，收錄所有讀過或有興趣的論文，不限領域。本週簡報的主題是「世界模型」。
- **理由**：Karpathy 的原意就是持續累積的知識庫；簡報只是從 Wiki 取用一部分。
- **影響**：需要用 `areas`、`status` 欄位與主題頁來組織（見第 4 節），簡報流程的覆蓋率關卡只計算該主題下的來源。

### D3. 論文筆記以英文為主，規則與紀錄用中文

- **決定**：
  | 檔案 | 語言 |
  |---|---|
  | `AGENTS.md`、skill 檔、`log.md`、`docs/` | 繁體中文 |
  | `wiki/en/*.md` | 英文（主要版本，先寫） |
  | `wiki/zh/*.md` | 繁體中文（由 LLM 從英文版翻譯） |
- **理由**：論文都是英文，用英文整理可以保留原文用詞、減少轉譯誤差；規則與紀錄是寫給擁有者看的，用中文最清楚。
- **風險與對策**：規則是中文，英文頁可能混入中文 → `check.py` 檢查 `wiki/en/` 不得出現中文字元。

### D4. 中文版由 LLM 翻譯，不用程式翻譯

- **決定**：英文版寫完後，由 LLM 在獨立的一步翻成中文版。
- **理由**：擁有者判斷程式翻譯的品質不夠好。
- **同步機制**：中文版 frontmatter 記錄翻譯當時英文版的雜湊值（`translated_from`），`check.py` 比對不符就報「中文版過期」，不靠 AI 記得同步。

### D5. HTML 一律由 `build.py` 從 Markdown 產生

- **決定**：AI 只寫 Markdown；中英 HTML 全由腳本產生並 commit 進 repo（不使用 GitHub Actions）。
- **理由**：上週每頁 4 個檔案由 AI 手動同步，耗 token 又容易不一致；改成腳本，符合課堂「做完了是腳本說了算」的原則。
- **對上週規則的調整**：
  - 「不使用建置工具」改為「建置工具只在本機執行，網站本身仍是純靜態、不使用 JavaScript」。
  - 「不可引入外部套件」放寬為允許 Python 的 `markdown` 套件（或同等工具，訪談決定）。

### D6. 放寬 Wiki 端的引用規則，但每句話都要標出來源類型

- **決定**：Wiki 允許適度引用原文、加入外部資料、改寫成幫助讀者理解的說法，以正確性與清楚易懂為優先。但內容依第 5 節分成四種類型並標記。
- **理由**：擁有者希望筆記能讓讀者更直觀理解原文；標記類型是為了讓簡報的忠實度檢查知道每句話該拿什麼比對。

### D7. 簡報端維持嚴格：只能讀 Wiki

- **決定**：簡報流程的所有節點只能讀 Wiki，不可搜尋網路、不可讀 PDF。外部資料必須先寫進 Wiki，簡報才能使用。簡報上的每個事實都標註 Wiki 出處頁面（超連結）。
- **理由**：作業與課堂要求「以 Wiki 為知識來源」，評分看「Wiki 資料與簡報內容有明確對應」。D6 的放寬只發生在 Wiki 端，不會讓簡報脫離 Wiki。
- **例外**：簡報可以新寫教學用的比喻或過場，但不可含數字或論文主張；忠實度檢查只確認它沒有扭曲原意。

### D8. 規則檔不全拆，只把簡報流程拆成 skill

- **決定**：`AGENTS.md` 維持一份，包含 Wiki 的規則（結構、命名、格式、ingest / query / lint）。簡報流程獨立寫成 `.claude/skills/make-slides/SKILL.md`。`CLAUDE.md` 只寫 `@AGENTS.md`。
- **理由**：
  - 長度不是問題：規則維持中文，預估與上週相近（上週 6,882 字元，低於 Antigravity 的 12,000 字元上限）。
  - 簡報流程就是作業要說明的 graph，獨立成檔繳交時可以直接指給助教看；課堂也建議把流程寫成獨立的 workflow 檔。
  - 平常 ingest 用不到簡報流程，不需要每次都讀。

### D9. 分兩階段：先建 Wiki，再做簡報

- **決定**：階段 1 建 Wiki，通過交接關卡後才進入階段 2 做簡報（見第 8 節）。
- **理由**：簡報流程的第一關需要 Wiki 已存在；Wiki 內容固定，簡報的出處才有不會變動的頁面可連；兩階段分開，反思時能清楚區分錯誤出在 ingest 還是做簡報。
- **允許往回走**：做簡報時發現 Wiki 缺內容，退回階段 1 補 ingest 或補頁面，不在簡報裡直接補。

### D10. 設計在 claude.ai 完成，執行改用 Claude Code

- **決定**：階段 0（本文件）在 claude.ai 對話完成；階段 1、2 在本機用 Claude Code 執行。
- **理由**：執行需要 git commit、跑 `build.py` / `check.py`、用瀏覽器截圖檢查簡報溢出、讀本機 PDF，這些都需要能在本機跑指令。

### D11. git 由擁有者自己操作，AI 不執行 git

- **決定**：commit 與 push 由擁有者用 GitHub Desktop 操作（沿用上週的做法）。AI 不執行任何 git 指令；每完成一個階段性步驟（一篇 ingest、一個簡報關卡），AI 停下來提醒擁有者 commit，並提供建議的 commit 訊息。
- **理由**：擁有者電腦的終端機沒有安裝 git，上週也是自己 commit；這樣每次發佈都經過擁有者確認。
- **取捨**：課堂建議讓 AI 使用 git。改由人 commit 會多一些手動步驟，但每關的執行紀錄仍保留在 `report.md` 與 `log.md`，commit 歷史一樣能當佐證。
- **影響**：`check.py` 不可依賴 git 指令；「My notes 未被更動」改用快照檔比對（見第 6 節）。

---

## 3. 資料夾結構（草案，訪談時確認）

```
/
├── AGENTS.md               規則（中文）
├── CLAUDE.md               只有一行：@AGENTS.md
├── README.md               專案簡介（給 GitHub 訪客）
├── .claude/skills/
│   └── make-slides/SKILL.md   簡報 graph（階段 2 撰寫）
├── docs/                   決策、需求摘要、參考資料
├── raw/                    論文 PDF（不上傳）+ README.md 連結清單
├── wiki/
│   ├── log.md              紀錄（中文）
│   ├── en/                 英文版（主要）
│   │   ├── index.md
│   │   ├── sources/        一篇論文一頁
│   │   ├── concepts/       一個概念一頁
│   │   └── topics/         主題頁（領域入口）
│   └── zh/                 中文翻譯版，結構與 en/ 相同
├── templates/              HTML 範本（build.py 使用）
├── scripts/
│   ├── build.py            Markdown → HTML
│   └── check.py            第 6 節的檢查
├── site/                   build.py 的輸出（GitHub Pages 發佈這裡或根目錄，訪談決定）
└── decks/<topic>/          簡報流程的所有中間檔與成品（階段 2）
```

---

## 4. Wiki 範圍與組織

- **來源頁 frontmatter 新增**：
  - `areas: [world-model, reinforcement-learning, game-ai, ...]`：所屬領域，可以多個。
  - `status: read | skimmed | to-read`：區分讀過、略讀、有興趣但還沒讀。
- **`index.md` 依領域分區**，篇數變多後 AI 只需讀相關區塊。
- **新增第三種頁面「主題頁」**（`wiki/*/topics/`）：一個領域的入口，列出相關來源與概念，並寫一段發展脈絡。也是簡報流程檢索的起點。
- 上週規則中的「每篇最多新建 5 個概念頁」「建立前先查別名」等規則沿用。

---

## 5. 內容的四種類型與標記方式（草案）

| 類型 | 寫法 | 檢查方式 |
|---|---|---|
| 論文主張 | 句尾標頁碼 `(p.7)`，頁碼以 PDF 檔頁數為準 | 對照 PDF |
| 原文引用 | `"..." (p.7)`；每句 25 個英文字以內，每頁最多 2 句 | 對照原文 |
| 外部資料 | 只能放在 `## Background` 區塊，每項附連結 | 連結有效 |
| Wiki 的解釋或比喻 | `> **Explainer:** ...`；不可含數字 | 只檢查沒有扭曲原意 |

- 不確定的內容標 `(to be verified)`，不可猜測。
- 不同來源說法衝突時兩邊都保留、寫出差異，不自行裁決（沿用上週）。

---

## 6. 檢查清單統整

### 6.1 `check.py`（Wiki，每次 ingest 後執行）

**語言與翻譯**
- [ ] `wiki/en/` 沒有中文字元。
- [ ] 每個英文頁都有對應的中文頁，反之亦然。
- [ ] 中文版的 `translated_from` 與英文版目前內容的雜湊相符（不符 → 中文版過期）。
- [ ] 中英版的區塊標題數量與順序一致、`(p.X)` 頁碼集合一致、連結集合一致。

**格式**
- [ ] frontmatter 必填欄位齊全（含 `areas`、`status`）。
- [ ] 區塊依範本順序，沒有被刪除的區塊。
- [ ] 含數字的句子有 `(p.X)`（`Background` 與 `Explainer` 除外）。
- [ ] `Explainer` 區塊不含數字；`Background` 每項都有連結；直接引用不超過長度上限。

**連結與結構**
- [ ] 所有站內連結指向存在的檔案（Markdown 與 HTML 都查）。
- [ ] 來源頁 ↔ 概念頁 ↔ 主題頁雙向連結。
- [ ] `index.md` 列出所有頁面；沒有孤兒頁。
- [ ] HTML 沒有殘留的 `{{`。

**紀錄與保護**
- [ ] `log.md` 新紀錄的標題格式為 `## [YYYY-MM-DD] 類型 | 標題`。
- [ ] `raw/README.md` 列出 `raw/` 裡每個 PDF；PDF 沒有進入 git。
- [ ] 「My notes」區塊沒有被 AI 更動：`check.py` 把每頁 My notes 的雜湊存在快照檔，與上次快照比對（不依賴 git）。

### 6.2 簡報流程的關卡（階段 2，詳見第 7 節）

- **G1 覆蓋率**（腳本）：主題下 ≥3 篇來源，否則停下並回報缺什麼。
- **G2 出處**（腳本）：每張證據卡的每個主張都有 Wiki 頁面連結與 `(p.X)`，且該頁確實存在這段內容。
- **人工關卡**：擁有者確認大綱。
- **G3 忠實度**（AI 審查，開新對話，只給逐頁稿與證據卡）：主張是否忠於 Wiki、有沒有講反、比喻有沒有扭曲原意。
- **G4 渲染**（腳本＋截圖）：頁數 8–15、沒有文字溢出、所有出處連結有效。

---

## 7. 簡報 graph 草案（階段 2 定稿）

```
[0 主題＋讀者] → [1 檢索 Wiki：讀 topics/world-models 與 index]
                          ↓
                    ◆G1 覆蓋率關卡（腳本）
                       └ 相關來源 <3 → 停下，回報缺什麼
                          ↓
              [2 證據卡] 一篇一張，只能讀該篇的 Wiki 頁
                          ↓
                    ◆G2 出處檢查（腳本）
                       └ 不合格 → 只重做該張卡
                          ↓
              [3 大綱] → 👤 擁有者確認
                       └ 退回 → 修大綱，或回到 1 補檢索
                          ↓
              [4 逐頁稿]（內圈 loop：寫 → 查出處 → 修，最多 2 輪）
                          ↓
                    ◆G3 忠實度審查（新對話）
                       ├ 某頁有錯 → 只退回該頁
                       └ 證據卡本身錯 → 退回 2 重做該卡
                          ↓
              [5 渲染 HTML]（內圈 loop：產生 → 截圖 → 修版）
                          ↓
                    ◆G4 渲染檢查（腳本＋截圖）
                       └ 字太多 → 退回 4 縮短，不准在 5 硬塞
                          ↓
              [6 交件：deck.html + report.md]
```

- **剎車**：每個關卡最多退回 3 次，超過就停下交給擁有者決定。
- **狀態都是檔案**：`decks/world-models/` 下有 `sources.md`、`cards/`、`outline.md`、`drafts/`、`deck.html`、`report.md`。
- **每過一關 commit 一次**（AI 提醒、擁有者用 GitHub Desktop commit），git log 是執行紀錄的佐證。
- **`report.md` 每次退回都記一筆**：哪一關、第幾輪、什麼錯、退回哪裡。這是反思的資料來源。
- **跨階段退回**：Wiki 缺內容 → 退回階段 1 補 ingest 或補頁面。

---

## 8. 執行階段

### 階段 1：建 Wiki（Claude Code）

1. 訪談：貼上 `docs/kickoff-prompt.md`。AI 一次問一題，結果寫成 `docs/requirements.md`，擁有者確認後才產生 `AGENTS.md`、`CLAUDE.md`、範本、`build.py`、`check.py`。
2. 對照：逐條確認 `requirements.md` 的每一項都寫進了 `AGENTS.md`。
3. 試跑：**只 ingest 1 篇**（World Models 2018），執行 build 與 check，擁有者 commit。檢查格式、翻譯、建置都正常後，再決定規則要不要修改。
4. 依年代 ingest 其餘論文（第 8.1 節），每篇完成後擁有者 commit 一次。
5. lint、`check.py` 全過後，擁有者 commit、push 並設定 GitHub Pages。

### 交接關卡（進入階段 2 的條件）

- [ ] `check.py` 全部通過
- [ ] `topics/world-models` 主題頁存在
- [ ] 主題頁下 ≥3 篇來源

### 階段 2：做簡報（Claude Code）

1. 撰寫 `.claude/skills/make-slides/SKILL.md` 與關卡腳本。
2. 執行第 7 節的 graph，產出 `deck.html` 與 `report.md`。
3. 依 `report.md` 撰寫反思，必要時修改 graph 並記錄原因。

### 8.1 ingest 順序

依年代排序，後面的論文寫「與其他來源的關係」時才有前面的頁面可以連。

| 順序 | 論文 | 年份 | 頁數 | 領域 |
|---|---|---|---|---|
| 1 | World Models（Ha & Schmidhuber） | 2018 | — | world-model |
| 2 | PlaNet: Learning Latent Dynamics for Planning from Pixels | 2018/19 | 20 | world-model, RL |
| 3 | Dreamer: Dream to Control | ICLR 2020 | 20 | world-model, RL |
| 4 | DreamerV2: Mastering Atari with Discrete World Models | ICLR 2021 | 26 | world-model, RL |
| 5 | DreamerV3: Mastering Diverse Domains through World Models | 2023 | 40 | world-model, RL |
| 6 | Dreamer 4: Training Agents Inside of Scalable World Models | 2025 | 32 | world-model, RL |
| 7 | World and Human Action Models towards gameplay ideation（WHAM） | 2025 | — | world-model, game-ai |
| 8 | GUI Agents for Continual Game Generation | 2026 | — | game-ai |
| 9 | LLM Game Rule Understanding through Out-of-Distribution Fine-Tuning | 2025 | — | game-ai |

- 1–7 是簡報需要的；8、9 展示 Wiki 不只收世界模型，可以最後再做。
- Hafner 系列附錄很長，ingest 讀到哪裡由訪談決定。WHAM 的 PDF 有 133 MB，只讀文字層。

---

## 9. 待訪談決定的問題

訪談只需要問這些，以及 AI 認為本文件沒有涵蓋到的地方：

1. **讀者**：Wiki 與簡報分別寫給誰（自己？同學？完全不懂的人？）
2. **頁面類型**：來源頁、概念頁、主題頁的區塊要不要調整？主題頁要包含哪些區塊？
3. **出處細度**：頁碼就夠，還是要到章節或圖表編號？
4. **論文互相矛盾**：沿用上週「兩邊都保留」，還是需要更多規則？
5. **ingest 方式**：一次一篇並逐篇確認，還是可以批次？讀多少附錄？
6. **輸出**：除了網站與簡報，還要產出什麼？簡報要不要也做中英雙語？
7. **lint**：除了第 6 節的腳本檢查，還要 AI 檢查什麼？
8. **網站**：GitHub Pages 發佈根目錄還是 `site/`？沿用上週的視覺風格嗎？
9. **第 5 節的標記方式**：上限數字與寫法是否同意？

---

## 10. 與上週的差異（反思素材）

| 項目 | 上週（第 9 週） | 本週（第 10 週） | 原因 |
|---|---|---|---|
| 建立方式 | 照 Karpathy 原文直接產生規則檔 | 先訪談、確認需求摘要後才產生 | 作業要求；讓規則反映自己的需求 |
| 規則檔 | `CLAUDE.md` 一份 | `AGENTS.md` ＋ `make-slides` skill | 簡報流程需要獨立說明與重用 |
| Wiki 範圍 | 遊戲 × AI | 所有讀過或有興趣的論文 | 知識庫要能長期累積 |
| 主要語言 | 中文為主，英文同步 | 英文為主，中文由 LLM 翻譯 | 論文是英文，減少轉譯誤差 |
| HTML | AI 手動同步，每頁 4 個檔案 | `build.py` 自動產生 | 省 token、避免不一致 |
| 檢查 | AI 逐項對照清單 | `check.py` 腳本 | 「做完了」由腳本判斷 |
| 中英同步 | 靠 AI 記得 | 雜湊比對自動偵測過期 | 可執行的檢查 |
| 引用規則 | 只能改寫，引用限一兩句 | 允許引用、外部資料、解釋，但分類標記 | 讀者更易理解，同時保留可追溯性 |
| 頁面類型 | 來源頁、概念頁 | 加上主題頁 | Wiki 範圍變大，需要領域入口 |
