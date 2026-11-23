# 更新紀錄

只能往下新增，不可修改既有紀錄。標題格式：`## [YYYY-MM-DD] 類型 | 標題`，類型為 `ingest`、`query`、`lint`、`rules`（`setup` 只用於第一筆）。

## [2026-11-24] setup | 建立專案

- 依 `docs/requirements.md`（擁有者已確認）建立 `AGENTS.md`、`CLAUDE.md`、`README.md`、`requirements.txt`、`.nojekyll`。
- 範本：`templates/` 下來源、概念、主題頁的中英 Markdown 範本，以及 `page.html`、`home.html`、`landing.html`；樣式表 `assets/style.css`。
- 腳本：`scripts/build.py`、`scripts/check.py`、`scripts/common.py`。
- Wiki：`wiki/areas.yml`（world-model、reinforcement-learning、game-ai）、空的 `wiki/en/index.md` 與 `wiki/zh/index.md`。
- `raw/README.md` 列出 `raw/` 現有的 7 個 PDF，公開連結與來源頁待 ingest 時填入。
- 尚未 ingest 任何論文。

## [2026-11-24] rules | 簡報規則移出 AGENTS.md

- 依擁有者要求，把 `AGENTS.md` 中與教學簡報有關的內容（簡報讀者、語言、只讀 Wiki、進入階段 2 的條件、`decks/` 資料夾）移到新檔 `docs/slides-plan.md`，建完 Wiki 後才執行。
- `docs/slides-plan.md` 同時整理了 `docs/decisions.md` 第 7 節的簡報 graph 與關卡 G1–G4。
- `docs/requirements.md` 新增 P23，並更新第 8 節對照表。
- 沒有修改任何 Wiki 頁面。

## [2026-11-24] rules | 簡報計畫加入課堂 loop / graph 規格與繳交清單

- 依第 10 週講義〈把你的工作拆成 AI 能做的流程〉，在 `docs/slides-plan.md` 補上：每個節點只能看什麼、改什麼；loop 五件事與剎車；每輪只修報告列出的問題；錯在哪關退回哪關；大圈少、小圈快。
- 核對完整作業需求後補上遺漏：開始條件加上「全 Wiki 至少 ingest 5 篇」。`docs/requirements.md` 新增 P24 與第 9 節「與 Karpathy 原文的差異」草稿。
- `AGENTS.md` 與 Wiki 頁面都沒有修改。

## [2026-11-24] ingest | World Models

- 閱讀範圍：PDF 第 1–21 頁全文（正文 pp.1-12、附錄 A.1–A.5 pp.13-15、參考文獻 pp.16-21）。`status: read`（擁有者確認）。
- 新增來源頁：`2018-world-models`（areas：world-model、reinforcement-learning）。
- 新增主題頁：`world-models`（第一篇 ingest 時建立，依 `AGENTS.md` 第 3 節）。
- 新增概念頁（5 個，達每篇上限）：
  - `world-model`（把握度高：論文主題）
  - `variational-autoencoder`（高：V 元件，pp.3、13）
  - `mixture-density-rnn`（高：M 元件，pp.3、14）
  - `evolution-strategies`（高：以 CMA-ES 訓練 C，pp.4、12、14）
  - `learning-in-imagination`（中：在夢境中訓練是核心貢獻，但名稱由本 Wiki 取，別名含 dream training、latent imagination，以便之後與 Dreamer 系列共用）
- 更新既有頁面：無（第一篇來源）。
- 刻意不連結：`model-based-reinforcement-learning` 暫不建頁（本篇提到但非其貢獻，等 PlaNet 進來有兩篇來源再建）；不加 `game-ai` 領域（遊戲只是測試環境，擁有者同意）；迭代訓練與好奇心探索只寫在來源頁（論文未做實驗）；Learning to Think、PILCO 等不在 Wiki 中，`Relation to other sources` 寫無。
- 取代與衝突：無。
- `raw/README.md`：填入公開連結（arXiv 1803.10122，PDF 第 1 頁）與來源頁。
- 以上頁面皆有中英版；`build.py` 產生 14 個頁面，`check.py` 全部通過。

## [2026-11-24] rules | 試跑後調整規則

- 依 World Models 試跑時發現的問題，經擁有者同意修改：
  - 概念頁上限：每篇仍以新建 5 個為上限，超過時須在 ingest 計畫中逐項說明理由、擁有者同意才可破例（`AGENTS.md` §4）。
  - `index.md` 概念頁排序：依英文標題字母順序，中文版沿用英文版順序（`AGENTS.md` §3、中英 `index.md` 開頭說明）。
  - 首頁卡片摘要：`build.py` 改取第一個區塊的第一句，太長時英文在字的邊界截斷，避免切在字中間。
  - 頁碼上限：來源頁 frontmatter 新增 `pages`（PDF 總頁數，ingest 時填）；`check.py` 檢查來源頁的出處不超過它，概念頁與主題頁的出處則對照同一行最近連到的來源頁（`AGENTS.md` §5、`templates/source.*.md`、`scripts/check.py`）。
- 補上 `2018-world-models` 的 `pages: 22`，中文版與中文 `index.md` 重新取得雜湊。
- 新增 `.claude/launch.json`（本機預覽伺服器 `python -m http.server 8000`），用來在瀏覽器檢查網頁排版。

## [2026-11-24] rules | 讀檔時去掉 BOM

- 測試時發現檔案開頭有 BOM（部分編輯器存 UTF-8 時會加）時，`check.py` 讀不到 frontmatter。經擁有者同意，`scripts/common.py` 改用 `utf-8-sig` 讀檔，自動去掉 BOM。
- 既有檔案沒有 BOM，雜湊不受影響；`build.py`、`check.py` 全部通過。

## [2026-11-24] rules | AI 自動 commit

- 依擁有者要求取代 `docs/decisions.md` D11：AI 可以執行 git。`AGENTS.md` 新增 7.6，修改 7.1 第 13 步與 §10；`docs/slides-plan.md` 第 6 節同步修改；`docs/requirements.md` 新增 P26。
- 規則：每個階段性步驟在 build、check 通過後自動 commit；commit 前確認沒有 PDF 與機密；push 只在擁有者明確說「push」時執行；不可 force push 或改寫歷史。
- 依擁有者指示，把目前尚未 commit 的工作分成兩個 commit：規則與工具、World Models ingest。

## [2026-11-24] ingest | Learning Latent Dynamics for Planning from Pixels

- 閱讀範圍：PDF 第 1–20 頁全文（正文 pp.1-8、參考文獻 pp.9-11、附錄 A–J pp.12-20）。`status: read`（擁有者確認），檔名用正式發表年份 `2019-planet`（ICML 2019）。
- 新增來源頁：`2019-planet`（areas：world-model、reinforcement-learning；pages: 20）。
- 新增概念頁（4 個）：
  - `recurrent-state-space-model`（把握度高：核心貢獻，p.4）
  - `latent-overshooting`（高：核心貢獻，但最終代理人未使用，pp.5、12、14）
  - `latent-space-planning`（中：CEM＋MPC 是核心方法，名稱由本 Wiki 取，別名含 MPC、CEM planning）
  - `model-based-reinforcement-learning`（高：上次延後，現有 World Models 與 PlaNet 兩篇來源）
- 更新既有頁面：
  - `world-model`：新增 PlaNet 小節與「來源之間的比較」（把握度中：PlaNet 用 dynamics model 一詞，已是本頁別名）。兩篇都指出純確定性模型容易被利用（WM p.9、PlaNet p.4），標為一致而非衝突。
  - `variational-autoencoder`：新增 PlaNet 小節與比較（高：PlaNet 自稱 sequential VAE，p.3；沿用 World Models 的網路，p.12）。
  - `2018-world-models`：`Relation to other sources` 補上 PlaNet（高：PlaNet 引用本篇，pp.7、12、17）；`concepts` 加入 `model-based-reinforcement-learning`；**更正 `pages` 為 21**（上次由文字切頁數多算一頁，這次以 form feed 數確認）。
  - `world-models` 主題頁：Timeline、Sources、Key concepts、Key terms（POMDP、MPC、CEM、action repeat）、Open questions。
- 刻意不連結：`learning-in-imagination`（PlaNet 不在想像中訓練策略，只在決策時評估動作序列；差異寫在 `latent-space-planning` 的相關概念）；`mixture-density-rnn`（PlaNet 用單一高斯與 GRU）；`evolution-strategies`（CEM 雖是族群式最佳化，但最佳化的是動作序列而非權重）。
- 取代與衝突：無。
- `raw/README.md`：填入公開連結（arXiv 1811.04551）與來源頁。
- 規則不清楚之處：出處格式不允許 `Algorithm`，原寫的 `(p.3, Algorithm 1)` 改為 `(p.3)`。
- `build.py` 產生 24 個頁面，`check.py` 全部通過。

## [2026-11-24] rules | 出處允許演算法框、頁碼檢查對照連到的來源

- 經擁有者同意（Dreamer ingest 計畫中一併提出）：
  - 出處格式新增 `(p.3, Alg. 1)`，PlaNet 與 Dreamer 的方法都寫在演算法框中（`AGENTS.md` §5、`scripts/check.py` 的 `REF_OK`）。
  - 頁碼上限檢查：來源頁上連到另一篇來源頁的那一行（例如 Superseded、與其他來源的關係），出處改對照那一篇的 `pages`，避免在短論文頁上引用長論文頁碼時誤判。限制：同一行內所有出處都視為屬於連到的那篇，本篇的出處要寫在另一行。
- 在 scratchpad 副本測試：`Alg. 1` 格式通過，連到 PlaNet 的那一行引用 `p.21` 被正確判為超過 20 頁。

## [2026-11-24] rules | 修正：只有引用區塊改對照連到的來源

- 上一筆的頁碼檢查會把「與其他來源的關係」段落中的出處也判給連到的那篇，但那裡的出處通常是本篇頁碼（例如 PlaNet 頁「沿用 World Models 的網路 (p.12)」）。改為：來源頁上只有引用區塊（`>` 開頭，如 Superseded、Conflict）中連到另一篇時，出處才對照那一篇的 `pages`。
- 在 scratchpad 副本測試：關係段落的 `p.21` 視為本篇（21 頁，通過），Superseded 區塊的 `p.21` 正確判為超過 PlaNet 的 20 頁。

## [2026-11-24] ingest | Dream to Control: Learning Behaviors by Latent Imagination

- 閱讀範圍：PDF 第 1–20 頁全文（正文 pp.1-9、參考文獻 pp.10-13、附錄 A–G pp.14-20）。
- **閱讀狀態（擁有者決定）**：除了 World Models 與 WHAM，其他論文一律先填 `status: to-read`。本篇填 `to-read`，並把已 ingest 的 `2019-planet` 從 `read` 改為 `to-read`（中英版、主題頁 Sources 表、`index.md`）。
- 新增來源頁：`2020-dreamer`（ICLR 2020；areas：world-model、reinforcement-learning；pages: 20）。
- 新增概念頁（1 個）：`actor-critic`（把握度高：核心方法；λ-return 與穿過動態模型的價值梯度寫在本頁，不另建頁）。
- 更新既有頁面（皆新增 Dreamer 小節與「來源之間的比較」）：
  - `learning-in-imagination`（高：標題即 latent imagination；比較 World Models 的 ES 與 Dreamer 的解析梯度）
  - `world-model`、`model-based-reinforcement-learning`、`variational-autoencoder`（高）
  - `recurrent-state-space-model`、`latent-overshooting`（高：Dreamer 沿用 RSSM、同樣不需要 overshooting，pp.6、14）
  - `latent-space-planning`（高：Dreamer 顯示固定視野的規劃短視，pp.4、7）
  - `2018-world-models`、`2019-planet`：`Relation to other sources` 補上 Dreamer。
  - `world-models` 主題頁：Timeline、Sources、Key concepts、Key terms（value function、imagination horizon、λ-return、reparameterization）、Open questions。
- **取代（Superseded）**：`2019-planet` 的規劃方法與「缺少價值函數」限制各加一個 Superseded 區塊（Dreamer pp.4、7）；主題頁 Open questions 中的同一問題也加一個。
- 一致而非衝突：Dreamer 指出固定視野的規劃短視，PlaNet 自己也把缺少價值函數列為限制。
- 刻意不連結：`evolution-strategies`（Dreamer 未使用，只作為不需梯度方法的對比，寫在 `learning-in-imagination` 比較段）；`mixture-density-rnn`。
- 待確認：Dreamer p.9 同一段同時寫「19 個任務」與「20 個任務中 16 個勝出、4 個平手」，來源頁標為 `(to be verified)`。
- `raw/README.md`：填入公開連結（arXiv 1912.01603）與來源頁。
- `build.py` 產生 28 個頁面，`check.py` 全部通過。

