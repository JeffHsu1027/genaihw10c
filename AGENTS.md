# AGENTS.md — 個人論文 Wiki

每次在此專案工作前先讀完本文件。需求與理由見 `docs/requirements.md`、`docs/decisions.md`。所有路徑相對於專案根目錄，不可寫入本機絕對路徑。

## 1. 目的與讀者

- 依 Karpathy 的 LLM Wiki 方式維護的個人論文庫，收錄擁有者讀過或有興趣的所有論文，不限領域。第一個主題區是世界模型。
- 擁有者把 PDF 放進 `raw/`；AI 讀完後寫 Markdown Wiki；HTML 一律由 `scripts/build.py` 產生。
- 知識要累積：新論文進來時要回頭更新相關的既有頁面，不只新增一頁。
- Wiki 讀者：擁有者與修課同學（資工碩士、懂基本 ML、沒讀過這些論文）。

## 2. 資料夾

```
AGENTS.md / CLAUDE.md(@AGENTS.md) / README.md / requirements.txt / .nojekyll
index.html          根入口（build 產生）
assets/style.css    全站唯一樣式表
docs/               決策、需求、參考資料
raw/                PDF（不進 git）＋ README.md 連結表
wiki/log.md         紀錄（中文，只能往下新增）
wiki/areas.yml      領域清單
wiki/.notes-snapshot.json   My notes 快照（只由 --accept-notes 寫入）
wiki/en/            英文 Markdown（主要版本）：index.md、sources/、concepts/、topics/
wiki/zh/            中文翻譯，結構與檔名同 en/
templates/          Markdown 範本與 HTML 範本
scripts/            build.py、check.py、common.py
en/  zh/            HTML 輸出（build 產生，不可手改）
```

## 3. 命名與領域

- 檔名只用小寫英文、數字、連字號。來源頁 `<年份>-<短標題>`（例 `2018-world-models`）；概念頁用英文名稱（例 `world-model`）；主題頁用領域複數名（例 `world-models`）。中英版檔名相同。`raw/` 的檔名維持原樣。
- `areas` 只能用 `wiki/areas.yml` 的 slug。需要新領域時在 ingest 計畫中提出，擁有者同意後先改 `areas.yml`（記 `rules`）再使用。
- 主題頁只在擁有者同意的計畫中建立；`world-models`（`area: world-model`）在第一篇 ingest 時建立。
- `index.md` 依 `areas.yml` 的領域分區，每區依序列主題頁、來源頁（依年份）、概念頁（依英文標題字母順序，中文版沿用英文版順序）；每行的寫法見 `index.md` 開頭說明。屬於多個領域的頁面在每區都列出。

## 4. 頁面格式

三種頁面：來源頁（一篇論文）、概念頁（一個名詞或想法）、主題頁（一個領域的入口）。新頁面一律複製 `templates/<type>.<lang>.md`，替換所有 `{{...}}`。

- 區塊的標題與順序以範本為準，不可增刪或改名。沒有內容時，來源頁寫 `(Not covered in this paper)`／「（本文未提及）」，其他頁寫 `(None yet)`／「（尚無）」。`My notes` 例外：保持空白。
- frontmatter 欄位以範本為準。`status`：`read`（讀過）、`skimmed`（略讀）、`to-read`（擁有者尚未讀）。`to-read` 的論文照常完整處理，網頁會自動顯示「未讀」標籤。
- 來源頁：`Key results` 要有具體數字與出處；`Related concepts` 連到概念頁；`Relation to other sources` 只寫確實存在的關聯，沒有就寫 `No directly related sources yet.`。
- 概念頁：`One-line definition` 與 `Explanation`（英文 ≤200 words、中文 ≤300 字）只寫通用知識，不放論文主張或數字；論文怎麼用、定義或挑戰這個概念，寫在 `What each source says` 的 `### <論文標題> (<年份>)` 小節並連回來源頁。有兩個以上來源時，最後加 `### Comparing the sources`；來源間沒有互相引用時註明這段比較是本 Wiki 的整理。
- 主題頁：`Overview` 與 `Key terms` 只寫通用知識；`Timeline` 由舊到新、每一步連到來源頁；`Sources` 是表格（年份｜標題｜狀態｜一句話）；`Key concepts` 連到概念頁並附一句話；`Key terms` 用一句話解釋該領域常見術語（含尚未建概念頁的）。
- 建立概念頁的條件（任一）：是該論文的核心貢獻或方法；已在兩篇以上來源出現。每篇新來源以新建 5 個概念頁為上限；超過時須在 ingest 計畫中逐項說明理由，擁有者同意才可破例。建立前先查 `index.md` 與既有概念頁的 `aliases`，有同義概念就更新它。順帶提到的名詞在來源頁內解釋即可。
- `My notes` 是擁有者專用：AI 建立時留空，之後永不修改、不翻譯；中英版各自獨立。

## 5. 內容標記（每句話屬於下列一種）

| 類型 | 寫法 |
|---|---|
| 論文主張 | 句尾、句號前標出處：`(p.7)`、`(pp.7-8)`；來自圖表、公式或演算法框時 `(p.7, Fig. 3)`、`(p.7, Table 2)`、`(p.4, Eq. 2)`、`(p.3, Alg. 1)`。頁碼以 PDF 檔頁數為準，不可超過來源頁 frontmatter 的 `pages`（PDF 總頁數，ingest 時填）。 |
| 原文引用 | `"..." (p.7)`；每句 ≤25 個英文字，每頁最多 2 句。中文版保留英文原句不翻譯，後面可接中文註解。 |
| 外部資料 | 只能放在 `## Background`，每項是一個清單項目並附連結。 |
| Wiki 的解釋或比喻 | 英文 `> **Explainer:** ...`，中文 `> **解說（Explainer）：** ...`；不可含數字，不可扭曲原意。 |

- 概念頁與主題頁引用論文主張時，同一句要連到該來源頁並標出處。
- 含數字的句子必須有出處（`Background`、`My notes` 除外）。不算數字的：年份、模型或資料集名稱（DreamerV3、Atari 100k）、章節／圖表／公式編號、連結文字、程式碼。名稱中有獨立數字（如 `Dreamer 4`）時，加到 `scripts/check.py` 的 `NUMBERED_NAMES`（記 `rules`）。
- 雙引號只用於原文引用；強調或比喻性用語改用斜體。
- 不確定的內容標 `(to be verified)`／「（待確認）」，不可猜測或補上論文沒寫的數字。
- 取代（後續論文改掉前作的做法）：舊來源頁的主張不改，在旁加 `> **Superseded:** ...`／`> **後續變更：** ...`，連到新來源並標出處。
- 衝突（不同來源說法不一）：兩邊都保留，寫在概念頁 `Comparing the sources`，以 `> **Conflict:** ...`／`> **衝突：** ...` 標出差異，不自行裁決。
- 不硬湊關聯；不複製論文圖表，需要時用文字描述並標圖號。
- 語氣清楚直接，像寫給同學的讀書筆記；不用行銷語氣與表情符號。

## 6. 中文翻譯

- 本文件、`wiki/log.md`、`docs/` 用繁體中文；`wiki/en/` 用英文，不可出現中文字元（`My notes` 除外）。
- 英文版是主要版本，先寫完英文，再在獨立的一步翻成中文。中文的資訊量、數字、出處、連結、區塊結構、標記數量必須與英文一致，不可只寫摘要。
- 繁體中文（台灣用語）；專有名詞第一次出現寫「中文（English）」。論文標題、作者、模型與資料集名稱保留原文。站內連結指向同語言頁面。
- 中文頁 frontmatter 的 `translated_from` 填 `python scripts/check.py --hash wiki/en/<路徑>` 的輸出，不可自己計算。英文版有任何修改（`My notes` 除外），中文版要在同一次工作中重譯該處並更新雜湊。
- 中文版的 frontmatter 除 `title`、`aliases`、`translated_from` 外，值與英文版相同。

## 7. 工作流程

### 7.1 Ingest（擁有者說「處理新論文」或指定檔名）

一次只處理一篇，不批次。順序依 `docs/decisions.md` 8.1（依年代）。

1. 比對 `raw/` 與 `raw/README.md`、`wiki/en/index.md`，找出要處理的 PDF。
2. 讀完全文，**正文與附錄全部讀完**，不可只讀摘要。大型 PDF 只讀文字層。
3. 回報計畫並等擁有者同意：一句話總結；要新建與更新的頁面，每項附把握度（高：論文明確寫到；中／低：需本 Wiki 自行連結）與理由；「刻意不連結」的地方與原因；預計標記的取代或衝突。指令含「直接處理」時不等待，計畫寫進最後回報。
4. 寫英文來源頁。
5. 新建或更新英文概念頁。更新既有頁面只新增或修訂相關小節，不整頁重寫。
6. 更新英文主題頁（`Timeline`、`Sources`、`Key concepts`、`Key terms`）。
7. 檢查既有來源頁：有真實關聯才補 `Relation to other sources`；需要時加 `Superseded`。
8. 更新 `wiki/en/index.md`。
9. 把第 4–8 步所有新增與變動的頁面翻成 `wiki/zh/`（第 6 節）。
10. `raw/README.md`：填這篇的公開連結與來源頁（新 PDF 則新增一列）。找不到公開連結寫「（待確認）」並在回報中說明。
11. 在 `wiki/log.md` 最下方新增一筆 `ingest`（格式見 7.5），列出新增與修改的頁面、把握度、刻意不連結之處、取代與衝突。
12. 執行 `python scripts/build.py`，再執行 `python scripts/check.py`；不通過就修到通過。
13. 依 7.6 commit（不 push）。回報：新增與修改的檔案、檢查結果、規則不清楚之處、commit 編號。

### 7.2 Query（回答問題）

先讀 `wiki/en/index.md`，依 Wiki 內容回答並指出出處頁面。Wiki 沒有的就明說，不可用自己的印象補充。不另建頁面；答案有值得保留的整理時，提議寫進既有概念頁或主題頁，擁有者同意後才改（照 7.1 第 9、12 步同步與檢查）。回答後記一筆 `query`。

### 7.3 Lint（擁有者說「檢查 Wiki」）

1. 執行 `python scripts/check.py`。
2. 語意檢查：未標記的衝突或取代、已被較新來源取代的舊說法、在多頁提到卻沒有自己頁面的概念、別名重疊、缺少的交叉連結、主題頁是否跟上新來源、`Explainer` 是否扭曲原意、建議可補的論文或問題。
3. 抽查：每個來源頁隨機抽 3 個帶出處的主張回 PDF 核對；每個中文頁隨機抽 3 段與英文版對照，查譯錯或漏譯。
4. 只回報，不修改；擁有者決定後再改。記一筆 `lint`（含抽查了哪些項目與結果）。

### 7.4 修改規則

修改本文件、`templates/`、`scripts/`、`wiki/areas.yml` 或 `assets/style.css` 前，先向擁有者提出建議，同意後才改，並記一筆 `rules`。本文件上限 12,000 字元（`check.py` 會檢查）；細節放範本或腳本，這裡只寫規則與指向。

### 7.5 紀錄格式

`wiki/log.md` 每筆標題為 `## [YYYY-MM-DD] 類型 | 標題`，類型為 `ingest`、`query`、`lint`、`rules`（`setup` 只用於第一筆）。標題下用清單列出內容。不可修改既有紀錄。

### 7.6 Git

- 每完成一個階段性步驟（一篇 ingest、一次規則修改、一次依 lint 的修改）且 build、check 都通過後，AI 自動 commit；check 沒通過不可 commit。
- commit 前執行 `git status`，確認沒有 `.pdf`、個資、密碼或 API Key；只加入這次相關的檔案。
- 訊息第一行 `<類型>: <標題>`（類型同 log），內文列出重點。
- **不可 push**，只在擁有者明確說「push」時執行；不可 force push，不可改寫歷史（amend、rebase、reset 等）。

## 8. 腳本

- 第一次使用先執行 `python -m pip install -r requirements.txt`（`markdown`、`pyyaml`）。
- `python scripts/build.py`：由 `wiki/` 產生 `index.html`、`en/`、`zh/` 的所有 HTML（含首頁卡片、狀態標籤、語言切換），並刪除沒有對應 Markdown 的舊 HTML。
- `python scripts/check.py`：檢查語言與翻譯、格式、出處、連結與結構、紀錄與保護（項目見腳本開頭說明）。全部通過時結束碼為 0。**一篇 ingest 完成的定義是 build 與 check 都通過。**
- `python scripts/check.py --hash <英文檔>`：輸出翻譯用的雜湊。
- `python scripts/check.py --accept-notes`：擁有者修改自己的 `My notes` 後更新快照。**AI 不可執行。**

## 9. 網站

- GitHub Pages 從 repo 根目錄發佈（`.nojekyll` 讓 Pages 不做額外處理）。純靜態 HTML＋CSS，不使用 JavaScript；建置只在本機執行，不使用 GitHub Actions。
- AI 不手寫或修改任何 HTML；版面改 `templates/*.html`，樣式改 `assets/style.css`（都需依 7.4 先提議）。HTML 內不寫 `<style>` 或行內樣式。
- 視覺：暖色紙本筆記風格；來源、概念、主題頁以強調色區分（`#B45309`、`#0F766E`、`#4338CA`），同時一定有文字標籤。

## 10. 禁止事項

- 不可修改、搬移、改名或刪除 `raw/` 的 PDF；`raw/README.md` 只能新增列或填空格。
- 不可把 PDF 加入版本控制，不可修改 `.gitignore` 中的 `raw/*.pdf`。
- 不可在 check 未通過時 commit；不可自行 push 或改寫 git 歷史（見 7.6）。
- 不可刪除 Wiki 頁面；認為該刪除時先詢問。
- 不可修改 `My notes`，不可執行 `--accept-notes`。
- 不可新增頁面類型，不可自行修改頁面格式、範本、腳本或樣式（先依 7.4 提議）。
- 不可在 repo 中寫入個資、密碼、API Key 或本機絕對路徑。
