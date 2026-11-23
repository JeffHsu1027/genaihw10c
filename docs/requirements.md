# 需求摘要（階段 1：訪談結果）

- 建立日期：2026-11-24
- 依據：`docs/decisions.md`（以下簡稱 DEC）、`docs/reference/hw9-CLAUDE.md`（以下簡稱 hw9）、`docs/reference/hw9-log.md`、Karpathy LLM Wiki 原文
- 狀態：**擁有者已確認（2026-11-24）**，附帶要求：注意 `AGENTS.md` 的長度（見 P14）。實作時的調整記在第 7 節。

每一項都有編號（A＝沿用、N＝訪談新決定、P＝AI 提議的補充），之後會用這些編號逐條對照 `AGENTS.md`。

---

## 1. 已沿用的決定（引用 DEC 編號）

| 編號 | 內容 | 出處 |
|---|---|---|
| A1 | 新 repo 重建；所有規則、腳本、連結一律用相對於專案根目錄的路徑，不寫本機絕對路徑 | DEC D1 |
| A2 | Wiki 收錄所有讀過或有興趣的論文，不限領域；第一個主題區是世界模型，簡報只取這個主題 | DEC D2 |
| A3 | 來源頁 frontmatter 有 `areas`（可多個）與 `status: read \| skimmed \| to-read` | DEC §4 |
| A4 | 語言：`AGENTS.md`、skill、`log.md`、`docs/` 用繁體中文；`wiki/en/` 英文為主要版本、先寫；`wiki/zh/` 由 LLM 從英文版翻譯 | DEC D3 |
| A5 | `wiki/en/` 不得出現中文字元，由 `check.py` 檢查 | DEC D3 |
| A6 | 中文版由 LLM 在獨立的一步翻譯；中文版 frontmatter 記錄 `translated_from`（英文版雜湊），不符即報「中文版過期」 | DEC D4 |
| A7 | AI 只寫 Markdown；中英 HTML 全由 `scripts/build.py` 產生並 commit；不使用 GitHub Actions；網站純靜態、不使用 JavaScript；建置工具只在本機執行 | DEC D5 |
| A8 | Wiki 端放寬引用規則，但每句話標出四種內容類型之一 | DEC D6、§5 |
| A9 | 簡報流程只能讀 Wiki，不可搜尋網路、不可讀 PDF；每個事實標 Wiki 出處超連結；比喻可新寫但不可含數字或論文主張 | DEC D7 |
| A10 | `AGENTS.md` 一份包含 Wiki 規則；簡報流程另寫 `.claude/skills/make-slides/SKILL.md`（階段 2）；`CLAUDE.md` 只寫 `@AGENTS.md` | DEC D8 |
| A11 | 分兩階段，通過交接關卡（`check.py` 全過、`topics/world-models` 存在、主題下 ≥3 篇來源）才做簡報；簡報發現 Wiki 缺內容時退回階段 1 補 | DEC D9、§8 |
| A12 | AI 不執行任何 git 指令；每完成一篇 ingest 或一個簡報關卡，停下提醒擁有者用 GitHub Desktop commit，並提供建議的 commit 訊息 | DEC D11 |
| A13 | `check.py` 不依賴 git；「My notes 未被更動」改用快照檔比對 | DEC D11、§6.1 |
| A14 | `index.md` 依領域分區；新增第三種頁面「主題頁」`wiki/*/topics/` | DEC §4 |
| A15 | 不確定的內容標 `(to be verified)`／「（待確認）」，不可猜測 | DEC §5、hw9 §7 |
| A16 | `check.py` 檢查項目照 DEC §6.1 全部實作（語言與翻譯、格式、連結與結構、紀錄與保護） | DEC §6.1 |
| A17 | ingest 順序依年代（DEC §8.1）；第一篇只試跑 World Models（2018），確認後再處理其餘 | DEC §8、§8.1 |
| A18 | WHAM 的 PDF 只讀文字層 | DEC §8.1 |
| A19 | 論文 PDF 不進 git；推上 GitHub 前確認沒有個資、密碼、API Key | DEC §1 |

### 沿用上週（hw9）的規則

| 編號 | 內容 | hw9 出處 |
|---|---|---|
| A20 | 檔名一律小寫英文、數字、連字號；來源頁 `<年份>-<短標題>`、概念頁用英文名稱；同一頁各語言版本檔名相同；`raw/` 檔名維持原樣 | §3 |
| A21 | 區塊順序與標題不可更動；沒有內容寫 `(Not covered in this paper)`／「（本文未提及）」，不可刪除區塊 | §4 |
| A22 | 概念頁建立條件：論文核心貢獻或已在兩篇以上出現；每篇最多新建 5 個概念頁；建立前先查 `index.md` 與 `aliases` | §5 |
| A23 | ingest 前先回報計畫：一句話總結、要新建與更新的頁面（每項附把握度高／中／低與理由）、「刻意不連結」之處與原因；等擁有者同意；指令含「直接處理」時可跳過等待 | §6.1 第 3 步 |
| A24 | 更新既有頁面只新增或修訂相關小節，不整頁重寫 | §6.1 第 5 步 |
| A25 | 「與其他來源的關係」只寫確實存在的關聯；不硬湊關聯 | §4.1、§7 |
| A26 | 概念頁有兩個以上來源時加 `Comparing the sources`；若來源間沒有互相引用，註明這段比較是本 Wiki 的整理 | §4.2 |
| A27 | `log.md` 只能往下新增，標題格式 `## [YYYY-MM-DD] 類型 \| 標題`，下方列出新增與修改的頁面 | §6.1 第 11 步、hw9-log |
| A28 | 回答問題：先讀 `index.md`，依 Wiki 回答並指出出處；Wiki 沒有就明說；記一筆 `query` | §6.2 |
| A29 | lint 只回報，等擁有者決定後再修改，記一筆 `lint` | §6.3 |
| A30 | 「My notes」由擁有者專用：AI 建立時留空，之後永不修改、不翻譯 | §4.1 |
| A31 | 禁止事項：不可改動 `raw/` 內 PDF（只能在 `raw/README.md` 新增列）；不可改 `.gitignore` 排除 PDF 的設定；不可刪除 Wiki 頁面；不可自行改頁面格式或範本（先提建議）；不可自行新增頁面類型 | §10 |
| A32 | 中文版：繁體中文（台灣用語），專有名詞第一次出現寫「中文（English）」；論文標題、作者、模型與資料集名稱保留原文；站內連結指向同語言頁面 | §7 雙語 |
| A33 | 語氣清楚直接，像寫給同學的讀書筆記；不用行銷語氣與表情符號；不複製論文圖表，以文字描述並標圖號 | §7 正確性 |
| A34 | 視覺風格沿用：暖色紙底與上週配色、Noto Serif TC／Noto Sans TC、內文寬 720px、行高 1.8、強調色同時附文字標籤、手機單欄；所有樣式只在一個 `assets/style.css`，HTML 不寫 `<style>` 或行內樣式 | §8 |

---

## 2. 本次訪談新決定的事項

| 編號 | 題目 | 決定 |
|---|---|---|
| N1 | 讀者 | **Wiki** 寫給擁有者與修課同學（資工碩士、懂基本 ML、沒讀過這些論文）。**簡報**寫給知道 AI／神經網路是什麼、但沒聽過「世界模型」與強化學習的人；術語第一次出現都要解釋。 |
| N2 | 頁面區塊 | 見下方 2.1。來源頁、概念頁沿用上週區塊並加 `Background`；概念頁另加 `My notes`；主題頁 8 個區塊（含術語表 `Key terms`）。`Explainer` 可出現在任何區塊內。 |
| N3 | 出處細度 | 一律 `(p.7)`，跨頁 `(pp.7-8)`；主張或數字來自圖表或公式時加編號：`(p.7, Fig. 3)`、`(p.7, Table 2)`、`(p.4, Eq. 2)`。頁碼以 PDF 檔頁數為準。`check.py` 與簡報 G2 都用這個格式。 |
| N4 | 四種內容標記 | 照 DEC §5：論文主張 `(p.X)`；原文引用 `"..." (p.X)`，每句 ≤25 個英文字、每頁 ≤2 句；外部資料只在 `## Background`、每項附連結；Wiki 的解釋寫 `> **Explainer:** ...`、不含數字。**另補三條**：<br>① 概念頁 `One-line definition`／`Explanation`、主題頁 `Overview`／`Key terms` 屬「Wiki 的解釋」，只寫通用知識，不可含論文主張或數字；概念頁與主題頁引用論文主張時，同一句要連到來源頁並標 `(p.X)`。<br>② 中文版寫 `> **解說（Explainer）：** ...`；原文引用保留英文原句不翻譯，後面可接中文註解。<br>③ 以下不算「含數字」：年份、模型／資料集名稱（DreamerV3、Atari 100k、VQ-VAE）、章節／圖表／公式編號、連結文字、程式碼；其餘數字都要 `(p.X)`。 |
| N5 | 矛盾與取代 | 區分兩種：**取代**（後續論文改掉前作做法）：舊來源頁的主張不改，在旁加 `> **Superseded:** ...`（中文 `> **後續變更：** ...`），連到新來源並標頁碼。**衝突**（不同來源說法不一）：兩邊都保留，寫在概念頁 `Comparing the sources`，用 `> **Conflict:** ...`（中文 `> **衝突：** ...`）標出，不自行裁決。兩者都寫進該次 ingest 的 log。 |
| N6 | ingest 方式 | 一次一篇，先回報計畫等擁有者同意（A23）。**正文與附錄全部讀完**，不可只讀摘要或跳過附錄。不批次處理。 |
| N7 | 輸出 | 除網站與簡報外不另產出其他檔案。簡報**只做繁體中文**（術語寫「中文（English）」），出處連到同名的中文 Wiki HTML 頁。問答不另建頁面：只記 log；答案有值得保留的整理時，提議寫進既有概念頁或主題頁，經擁有者同意後才改。維持三種頁面類型。 |
| N8 | lint 的 AI 檢查 | 在 `check.py` 之外，AI 檢查：未標記的衝突或取代、多頁提到卻沒有自己頁面的概念、別名重疊、缺少的交叉連結、主題頁 `Timeline`／`Key terms`／`Sources` 是否跟上新來源、`Explainer` 是否扭曲原意、建議可補的論文。**另做兩種抽查**：每個來源頁隨機抽 3 個帶 `(p.X)` 的主張回 PDF 核對；每個中文頁隨機抽 3 段與英文版對照，查譯錯或漏譯。只回報，不修改（A29）。 |
| N9 | 網站 | GitHub Pages 從**根目錄**發佈（不用 Actions 時無法發佈 `site/`，DEC §3 草案的 `site/` 取消）。根 `index.html` 是簡介＋選語言入口；HTML 輸出到 `zh/` 與 `en/`（同一層，相對路徑一致）；樣式在 `assets/style.css`。沿用上週風格（A34），主題頁新增強調色 `#4338CA` 與標籤「主題／Topic」。 |
| N10 | 建置工具 | 使用 Python 套件 `markdown` 與 `pyyaml`，列在根目錄 `requirements.txt`，擁有者執行一次 `python -m pip install -r requirements.txt`。（目前環境：Python 3.10.7，兩個套件尚未安裝。） |
| N11 | to-read 論文 | `to-read` 的論文**照常建立完整頁面**（AI 一樣完整讀 PDF），只用 `status` 標註擁有者尚未讀，並在網頁上顯示（見 P8）。第 8、9 篇（GUI Agents、LLM Game Rule）等擁有者放入 PDF 後再處理。 |

### 2.1 三種頁面的區塊（N2 的完整內容）

英文標題為主，中文版標題對照寫在範本中。

```
來源頁 wiki/<lang>/sources/<year>-<short-title>.md
  ## One-line summary              一句話總結
  ## Research question             研究問題
  ## Method                        方法
  ## Key results                   主要結果
  ## Limitations and open questions 限制與未解問題
  ## Related concepts              相關概念
  ## Relation to other sources     與其他來源的關係
  ## Background                    背景資料
  ## My notes                      我的筆記

概念頁 wiki/<lang>/concepts/<english-name>.md
  ## One-line definition           一句話定義
  ## Explanation                   說明（英文 ≤200 words／中文 ≤300 字，沿用 hw9）
  ## What each source says         各來源怎麼說
     ### <Source title> (<year>)
     ### Comparing the sources     來源之間的比較（≥2 個來源時）
  ## Related concepts              相關概念
  ## Background                    背景資料
  ## My notes                      我的筆記

主題頁 wiki/<lang>/topics/<topic-slug>.md
  ## Overview                      概述
  ## Timeline                      發展脈絡（由舊到新，每一步連到來源頁）
  ## Sources                       來源（表格：年份｜標題｜狀態｜一句話總結）
  ## Key concepts                  關鍵概念（連結＋一句話）
  ## Key terms                     術語表（一句話解釋，含尚未建概念頁的術語）
  ## Open questions                未解問題
  ## Background                    背景資料
  ## My notes                      我的筆記
```

---

## 3. AI 提議的補充規則（訪談未涵蓋，請確認時一併檢查）

| 編號 | 項目 | 提議 |
|---|---|---|
| P1 | My notes 與雜湊 | 中英版的 `My notes` 各自獨立，擁有者可用任一語言寫，AI 不翻譯。`translated_from` 的雜湊只計算英文版**正文扣掉 `My notes` 區塊**，避免擁有者寫筆記就讓中文版被判過期。 |
| P2 | My notes 快照 | 快照存在 `wiki/.notes-snapshot.json`。擁有者自己修改筆記後執行 `python scripts/check.py --accept-notes` 更新快照。**AI 不可執行 `--accept-notes`**。新頁面第一次出現時自動加入快照（內容必須為空）。 |
| P3 | 領域清單 | `areas` 只能用 `AGENTS.md` 列出的值，初始為 `world-model`、`reinforcement-learning`、`game-ai`；需要新領域時在 ingest 計畫中提出，擁有者同意後先加進 `AGENTS.md` 再使用。`check.py` 檢查 `areas` 不在清單內就報錯。 |
| P4 | 主題頁何時建立 | 主題頁只在擁有者同意的 ingest 計畫中建立；`world-models`（`area: world-model`）在第一篇 ingest 時建立。其他領域先只在 `index.md` 分區，不強制有主題頁。 |
| P5 | frontmatter 欄位 | 來源頁：`title, authors, year, venue, url, raw, added, updated, areas, status, concepts, topics`。概念頁：`title, aliases, updated, areas, sources`。主題頁：`title, area, updated, sources, concepts`。中文版另加 `translated_from`。英文版 `title` 只寫英文；中文版概念與主題頁 `title` 寫「中文名稱（English Name）」。 |
| P6 | `index.md` 格式 | `wiki/en/index.md` 與 `wiki/zh/index.md` 依領域分區，每區依序列主題頁、來源頁（依年份）、概念頁；每行 `- [標題](相對連結) — 一句話`，`to-read` 的來源行尾加 `(to-read)`／「（未讀）」。一頁屬於多個領域時在各區都列出。 |
| P7 | 首頁與卡片 | 上週的首頁卡片與「標記註解」規則取消：`zh/index.html`、`en/index.html` 由 `build.py` 依 `index.md` 與 frontmatter 自動產生（卡片、來源數量、狀態），AI 不手動編輯任何 HTML。 |
| P8 | 未讀標註（N11） | `build.py` 在來源頁標題下方顯示狀態標籤：已讀／略讀／未讀（Read / Skimmed / To read），`to-read` 另用文字「擁有者尚未閱讀」說明；首頁卡片與主題頁 `Sources` 表格也顯示狀態。簡報 G1 覆蓋率計算該領域所有來源頁，不論狀態（內容都由 AI 完整讀過 PDF）。 |
| P9 | log 類型 | 類型為 `setup`（只用於建立專案的第一筆）、`ingest`、`query`、`lint`，另新增 `rules`：修改 `AGENTS.md`、範本或腳本時記一筆（上週把規則修改記成 `lint`，類型混用）。 |
| P10 | `raw/README.md` | 表格欄位：本機檔名｜論文標題與年份｜公開連結｜來源頁。找不到公開連結寫「（待確認）」並在回報中說明。`check.py` 檢查 `raw/` 每個 PDF 都在表中。因為不能用 git，「PDF 沒進 git」改為檢查 `.gitignore` 仍含 `raw/*.pdf`。 |
| P11 | GitHub Pages 細節 | 根目錄放空檔 `.nojekyll`，避免 Pages 用 Jekyll 處理 Markdown 或忽略檔案。 |
| P12 | `check.py` 行為 | 只讀不寫（`--accept-notes` 除外）；結果依類別列出，全部通過時 exit code 為 0，否則非 0；ingest 完成的定義是 `build.py` 與 `check.py` 都通過。 |
| P13 | ingest 步驟 | ① 找出未處理的 PDF → ② 讀完全文（含附錄）→ ③ 回報計畫並等待 → ④ 寫英文來源頁 → ⑤ 新建／更新英文概念頁 → ⑥ 更新英文主題頁 → ⑦ 補既有來源頁的關係、`Superseded` → ⑧ 更新英文 `index.md` → ⑨ 翻譯所有新增或變動的頁面到 `wiki/zh/`（獨立一步）→ ⑩ `raw/README.md` 新增一列 → ⑪ `wiki/log.md` 記一筆 → ⑫ 執行 `build.py`、`check.py`，不過就修到過 → ⑬ 回報新增與修改的檔案、把握度與刻意不連結之處，提供建議 commit 訊息，停下等擁有者 commit。 |

---

## 4. 確認後的資料夾結構

```
/
├── AGENTS.md                規則（中文）
├── CLAUDE.md                只有一行：@AGENTS.md
├── README.md                專案簡介（給 GitHub 訪客）
├── requirements.txt         markdown、pyyaml
├── .nojekyll                空檔（P11）
├── index.html               根入口：簡介＋選語言（build.py 產生）
├── assets/style.css         全站唯一樣式表
├── .claude/skills/make-slides/SKILL.md   （階段 2 才寫）
├── docs/                    decisions.md、requirements.md、kickoff-prompt.md、reference/
├── raw/                     論文 PDF（不上傳）＋ README.md 連結清單
├── wiki/
│   ├── log.md               紀錄（中文）
│   ├── .notes-snapshot.json My notes 快照（P2）
│   ├── en/                  英文 Markdown（主要）
│   │   ├── index.md
│   │   ├── sources/  concepts/  topics/
│   └── zh/                  中文 Markdown，結構同 en/
├── templates/               Markdown 範本（source/concept/topic × en/zh）與 HTML 範本
├── scripts/
│   ├── build.py             wiki/ → en/、zh/、index.html
│   └── check.py             DEC §6.1 ＋ 本文件的檢查
├── en/                      英文 HTML（build.py 產生，不手改）
├── zh/                      中文 HTML（build.py 產生，不手改）
└── decks/world-models/      簡報流程的中間檔與成品（階段 2）
```

與 DEC §3 草案的差異：取消 `site/`，HTML 改輸出到根目錄的 `en/`、`zh/`、`index.html`（N9）；新增 `assets/`、`requirements.txt`、`.nojekyll`、快照檔；`templates/` 同時放 Markdown 與 HTML 範本。

---

## 5. 與上週規則（hw9-CLAUDE.md）的差異

| 項目 | 上週 | 本週 | 依據 |
|---|---|---|---|
| 規則檔 | `CLAUDE.md` 一份 | `AGENTS.md`＋`CLAUDE.md`（`@AGENTS.md`）＋階段 2 的 `make-slides` skill | A10 |
| Wiki 範圍 | 遊戲 × AI | 所有論文，以 `areas`、`status`、主題頁組織 | A2、A3、A14 |
| 主要語言 | 中文先寫，英文同步 | 英文先寫，中文由 LLM 在獨立一步翻譯 | A4、A6 |
| 中英同步 | 靠 AI 記得 | `translated_from` 雜湊自動偵測過期 | A6、P1 |
| HTML | AI 手寫，每頁 4 檔；首頁手動插卡片 | `build.py` 產生全部 HTML 與首頁卡片；AI 不碰 HTML | A7、P7 |
| 網頁版面 | 中文在根目錄、英文在 `en/`，層數不同 | 根入口頁＋`zh/`、`en/` 同層 | N9 |
| 建置工具與套件 | 不用建置工具、不可用外部套件 | 本機 Python 腳本，允許 `markdown`、`pyyaml` | A7、N10 |
| 檢查 | AI 逐項對照清單 | `check.py` 腳本＋AI 語意 lint＋PDF 與翻譯抽查 | A16、N8 |
| 頁面類型 | 來源頁、概念頁 | 加上主題頁；概念頁加 `My notes` | A14、N2 |
| 引用規則 | 只能改寫，引用限一兩句 | 四種內容類型分類標記，引用 ≤25 字、每頁 ≤2 句 | A8、N4 |
| 出處 | 頁碼 | 頁碼＋圖表／公式編號（有才加） | N3 |
| 外部資料 | 未規範 | 只能放 `## Background`，每項附連結 | N4 |
| 矛盾 | 兩邊保留、不裁決 | 區分「取代」與「衝突」，各有標記 | N5 |
| ingest 閱讀範圍 | 完整閱讀含實驗與限制 | 正文＋附錄全讀 | N6 |
| 讀者 | 擁有者與同學（Wiki） | Wiki 同上；簡報另針對外行讀者 | N1 |
| log 類型 | `setup`、`ingest`、`query`、`lint` | 加上 `rules` | P9 |
| 未讀論文 | 無此概念 | `status` 欄位＋網頁狀態標籤 | A3、N11、P8 |
| My notes 保護 | 靠 AI 自律 | 快照檔比對，擁有者用 `--accept-notes` 更新 | A13、P2 |

---

## 6. 確認後要產生的檔案

1. `AGENTS.md`、`CLAUDE.md`
2. `templates/`：Markdown 範本（來源、概念、主題 × 英、中）與 HTML 範本
3. `assets/style.css`
4. `scripts/build.py`、`scripts/check.py`、`requirements.txt`
5. 資料夾與初始檔：`wiki/log.md`（`setup` 紀錄）、空的 `wiki/en/index.md`、`wiki/zh/index.md`、`raw/README.md`、`README.md`、`.nojekyll`
6. 產生後逐條對照本文件的 A／N／P 編號，列出每項寫在 `AGENTS.md` 的哪裡，補上遺漏。不 ingest 任何論文。

---

## 7. 確認後、實作時的調整

| 編號 | 調整 | 原因 |
|---|---|---|
| P14 | `AGENTS.md` 上限 12,000 字元（DEC D8 的 Antigravity 上限），`check.py` 會檢查。細節放到範本與腳本，`AGENTS.md` 只寫規則與指向。 | 擁有者確認時要求注意長度 |
| P15 | 新增 `scripts/common.py`：`build.py` 與 `check.py` 共用的解析與雜湊函式，避免兩邊算法不一致。 | 雜湊、區塊切分只能有一種算法 |
| P16 | 領域清單改放 `wiki/areas.yml`（slug 與中英名稱），`check.py` 與 `build.py` 都讀它；`AGENTS.md` 只指向這個檔。修改它要記一筆 `rules`。 | 清單只有一個出處（取代 P3 的「列在 `AGENTS.md`」） |
| P17 | 中文版的 `translated_from` 由 `python scripts/check.py --hash <英文檔>` 取得，AI 不自己算。 | 避免 AI 算錯雜湊 |
| P18 | P2 修正：`check.py` 不寫入快照；頁面不在快照中時，`My notes` 必須是空的。擁有者寫了筆記後執行 `--accept-notes` 才把它納入快照。 | 與 P12「check.py 只讀」一致 |
| P19 | P10 修正：`raw/README.md` 在建立專案時就列出 `raw/` 現有的每個 PDF，公開連結與來源頁欄先寫「（ingest 時填入）」；ingest 時填這兩格，新 PDF 則新增一列。 | 否則 `check.py`「每個 PDF 都在表中」一開始就不會過 |
| P20 | `build.py` 在每個 HTML 寫入對應 Markdown 的雜湊，`check.py` 比對；不符代表忘了重新 build。 | 讓「HTML 與 Markdown 一致」可由腳本判斷 |
| P21 | `check.py` 另外掃描規則、腳本、範本、Wiki 與 HTML 是否含本機絕對路徑（如 `C:\`、`/Users/`）。 | A1 可執行化 |
| P22 | 雙引號只用於原文引用，強調改用斜體。 | `check.py` 把所有雙引號當成引用計數與要求出處 |
| P23 | 簡報相關規則全部移出 `AGENTS.md`，集中到 `docs/slides-plan.md`；建完 Wiki、通過開始條件後才執行，執行時再依它撰寫 `make-slides` skill。`AGENTS.md` 只保留 Wiki 規則。 | 擁有者要求（2026-11-24）：建 Wiki 期間不需要、也不應受簡報規則影響 |
| P26 | **取代 DEC D11 與 A12**：AI 可以執行 git。每個階段性步驟在 build、check 通過後自動 commit；push 只在擁有者明確說「push」時執行；不可 force push 或改寫歷史（`AGENTS.md` 7.6、§10）。 | 擁有者要求自動更新 git（2026-11-24）；確認本機終端機可執行 git 2.56.1 |
| P25 | 試跑 World Models 後（擁有者同意）：概念頁上限 5 個可經擁有者同意破例；`index.md` 概念頁依英文標題字母排序；首頁卡片摘要取第一句；來源頁新增 `pages`，`check.py` 檢查出處頁碼不超過它。 | 試跑時發現的問題，見 `wiki/log.md` 2026-11-24 rules |
| P24 | `docs/slides-plan.md` 依第 10 週講義補上：每個節點只能看什麼、改什麼；loop 五件事（目標、限制、完成標準、停止條件、觸發）與剎車；「每輪只修報告列出的問題」「錯在哪關退回哪關」「大圈少、小圈快」；開始條件加上「全 Wiki 至少 ingest 5 篇」；最後由 AI 統整繳交內容成 `docs/submission.md`。（繳交檢查清單曾加入，擁有者自行保存後移除。） | 擁有者要求做簡報時使用課堂的 loop / graph；核對完整作業需求時發現的遺漏 |

---

## 9. 與 Karpathy 原文的差異（繳交用草稿）

課堂要求說明「針對個人需求做了哪些設定、與 Karpathy 原始架構有何不同」。保留原文的三層架構（不可變的 `raw/`、LLM 維護的 Wiki、規則檔）與 ingest / query / lint 三種操作、`index.md` 與 `log.md`；以下是不同之處。

| 項目 | Karpathy 原文 | 本 Wiki | 原因 |
|---|---|---|---|
| 規則檔怎麼來 | 把構想交給代理，一起做出自己的版本 | 先訪談 11 題、整理需求摘要並確認，才產生 `AGENTS.md`，再逐條對照 | 讓規則反映自己的需求，而不是 AI 的猜測 |
| 頁面類型 | 摘要、實體、概念、比較、總覽等，自由決定 | 固定三種（來源、概念、主題），每種有固定區塊的範本 | 格式固定，腳本才能檢查 |
| frontmatter | 選用 | 必填欄位，加上 `areas`、`status` | 收錄所有論文，需要依領域與閱讀狀態組織 |
| 出處 | 回答時附引用 | 每句話分成四種類型（論文主張、原文引用、外部資料、解釋）並標記，頁碼到圖表編號 | 讓簡報的忠實度檢查知道每句話該拿什麼比對 |
| 矛盾 | 標出與舊說法的矛盾 | 分成「取代」與「衝突」兩種標記，不自行裁決 | 同一條研究脈絡的改版和不同團隊的衝突性質不同 |
| 語言 | 未規範 | 英文為主，中文由 LLM 翻譯；雜湊偵測中文版過期 | 論文是英文，減少轉譯誤差；同步不靠 AI 記得 |
| 瀏覽方式 | Obsidian | `build.py` 產生純靜態網站，發佈到 GitHub Pages | 作業要可公開瀏覽 |
| 健檢 | LLM 定期 lint | `check.py` 腳本＋AI 語意 lint＋回 PDF 與翻譯抽查 | 「做完了」由腳本判斷 |
| 好的問答 | 存回 Wiki 成為新頁面 | 不另建頁，提議併入既有概念或主題頁 | 維持三種頁面類型，避免 Wiki 分散 |
| 人的筆記 | 未規範（人幾乎不寫 Wiki） | `My notes` 區塊由擁有者專用，快照保護 | 保留自己的想法，不被 AI 覆寫 |
| ingest | 可逐篇或批次 | 一次一篇，先回報計畫（附把握度與刻意不連結之處），正文與附錄全讀 | 上週經驗：把握度與不連結的理由讓擁有者能推翻 |
| 版本控制 | Wiki 是 git repo | 擁有者用 GitHub Desktop commit，AI 不執行 git | 電腦沒有安裝 git 指令；每次發佈都經過擁有者確認 |

---

## 8. 對照：每一項寫在 `AGENTS.md` 的哪裡（2026-11-24）

「補」表示第一版 `AGENTS.md` 遺漏、對照後補上的項目。§ 指 `AGENTS.md` 的節次；「腳本」表示由 `check.py` 或 `build.py` 強制執行。

| 項目 | 位置 | 項目 | 位置 | 項目 | 位置 |
|---|---|---|---|---|---|
| A1 | 開頭、§10、腳本 | A13 | §8、腳本 | A25 | §4、§5 |
| A2 | §1 | A14 | §3（補 index 格式）、§4 | A26 | §4 |
| A3 | §3、§4 | A15 | §5 | A27 | §7.5、腳本 |
| A4 | §6（補：規則與紀錄用中文） | A16 | §8、腳本 | A28 | §7.2 |
| A5 | §6（補）、腳本 | A17 | §7.1（補：依 8.1 順序） | A29 | §7.3 |
| A6 | §6、腳本 | A18 | §7.1 第 2 步 | A30 | §4、§10、腳本 |
| A7 | §8、§9（補：不用 Actions） | A19 | §10、腳本 | A31 | §10 |
| A8 | §5 | A20 | §3 | A32 | §6 |
| A9 | `slides-plan.md` §2 | A21 | §4、腳本 | A33 | §5 |
| A10 | `CLAUDE.md`、`slides-plan.md`（skill 於階段 2 撰寫） | A22 | §4 | A34 | §9、`assets/style.css` |
| A11 | `slides-plan.md` §1、§4 | A23 | §7.1 第 3 步 | | |
| A12 | §7.1 第 13 步、§10 | A24 | §7.1 第 5 步 | | |
| N1 | §1（Wiki）、`slides-plan.md` §2（簡報） | N5 | §5 | N9 | §2、§9 |
| N2 | §4、`templates/`、腳本 | N6 | §7.1 | N10 | §8、`requirements.txt` |
| N3 | §5、腳本 | N7 | §7.2、`slides-plan.md` §2 | N11 | §4、`build.py` |
| N4 | §4、§5、§6、腳本 | N8 | §7.3 | | |
| P1 | §4、§6、腳本 | P8 | §4、`build.py`、`slides-plan.md` §1 | P15 | §2 |
| P2 / P18 | §4、§8、§10、腳本 | P9 | §7.4、§7.5、腳本 | P16 / P3 | §3、`wiki/areas.yml`、腳本 |
| P4 | §3 | P10 / P19 | §7.1 第 10 步、§10、腳本 | P17 | §6、腳本 |
| P5 | §4、`templates/` | P11 | §2、§9（補說明） | P20 | §8、腳本 |
| P6 | §3（補）、`index.md` 開頭 | P12 | §8 | P21 | §10、腳本 |
| P7 | §8、§9、`build.py` | P13 | §7.1 | P22 | §5（補） |
| P14 | §7.4（補）、腳本 | P23 | `docs/slides-plan.md` | | |

不寫進 `AGENTS.md` 的：
- 所有簡報規則（讀者、語言、只讀 Wiki、開始條件、G1–G4、退回規則），依 P23 集中在 `docs/slides-plan.md`，建完 Wiki 才執行。
- 第 8、9 篇論文等 PDF 放入後再處理，屬於執行順序，不是規則。
