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

## [2026-11-24] ingest | Mastering Atari with Discrete World Models

- 閱讀範圍：PDF 第 1–26 頁全文（正文 pp.1-11、參考文獻 pp.12-15、附錄 A–K pp.16-26）。`status: to-read`（依擁有者原則）。
- 新增來源頁：`2021-dreamerv2`（ICLR 2021；areas：world-model、reinforcement-learning；pages: 26）。
- 新增概念頁（2 個）：
  - `categorical-latents`（把握度高：核心修改，p.3；42 勝 8 負，p.9）
  - `kl-balancing`（高：核心修改，p.4；44 勝 6 負，p.9）
- 更新既有頁面（新增 DreamerV2 小節，比較段擴充）：`recurrent-state-space-model`、`actor-critic`、`learning-in-imagination`、`world-model`、`model-based-reinforcement-learning`、`variational-autoencoder`（皆為高）。
- `actor-critic` 比較段：Atari 用 Reinforce、連續控制用穿過動態的梯度；DreamerV2 用目標網路與策略熵而 Dreamer 不需要。皆標為依領域或版本的設計差異，不是衝突。
- 取代（Superseded）：`2020-dreamer` 三處（高斯潛在變數 → 類別變數，p.9；free nats → KL 平衡，p.18；Atari 不具競爭力 → 達到人類水準，p.7）；主題頁 Open questions 一處。
- 來源關係：`2020-dreamer`、`2019-planet` 補上 DreamerV2。
- 刻意不連結：`latent-space-planning`（DreamerV2 不規劃，只把 MuZero 當對比）；`latent-overshooting`（未提及）；`2018-world-models`（只在相關研究中被列出一次）。
- 待確認：折扣 γ 在正文為 0.999（p.2），超參數表為 0.995（p.19），來源頁標 `(to be verified)`。
- 規則不清楚之處：附錄圖表編號如 `Fig. A.2`、`Fig. G.1` 不符合出處格式（只允許 `Fig. 3` 這類），改為只標頁碼。
- 寫作時被 `check.py` 擋下並修正：中文術語表「為 1」含數字，改為國字。
- `raw/README.md`：填入公開連結（arXiv 2010.02193）與來源頁。
- `build.py` 產生 34 個頁面，`check.py` 全部通過。

## [2026-11-24] ingest | Mastering Diverse Domains through World Models

- 閱讀範圍：PDF 第 1–40 頁全文（正文 pp.1-11、參考文獻 pp.12-16、方法與實作附錄 pp.17-22、補充材料 pp.23-40）。`status: to-read`（依擁有者原則）。
- 新增來源頁：`2023-dreamerv3`（arXiv 2023；areas：world-model、reinforcement-learning；pages: 40）。Wiki 來源達 5 篇，滿足作業最低要求。
- 新增概念頁（2 個）：
  - `symlog-predictions`（把握度高：核心技術，含 symexp twohot 損失，p.7）
  - `return-normalization`（高：核心技術，p.6；消融重要性第二，p.10）
- 更新既有頁面（新增 DreamerV3 小節，比較段擴充）：`kl-balancing`、`categorical-latents`（兩頁首次有兩個來源，新增比較段）、`recurrent-state-space-model`、`actor-critic`、`learning-in-imagination`、`world-model`、`model-based-reinforcement-learning`（皆高）、`variational-autoencoder`（中）。
- 取代（Superseded）：`2021-dreamerv2` 三處（actor 梯度依領域 → 一律 Reinforce；依領域的 KL 縮放 → 固定權重加 free bits；目標網路 → EMA 正則化，pp.5-6）；`2020-dreamer` 一處（連續控制穿過動態的梯度 → Reinforce，p.6）。
- 一致而非衝突：DreamerV2 與 DreamerV3 都指出影像重建是世界模型主要的學習訊號。
- 來源關係：`2021-dreamerv2`、`2020-dreamer`、`2019-planet` 補上 DreamerV3。
- 刻意不連結：`latent-space-planning`（V3 明確不做往前規劃）；`latent-overshooting`、`mixture-density-rnn`、`evolution-strategies`（未提及）；`2018-world-models`（只在一般引用中出現）。
- 待確認：想像視野正文為 16（p.5），超參數表為 15（p.21），來源頁標 `(to be verified)`。
- 寫作時被 `check.py` 擋下並修正：來源頁「相關概念」寫了 1% 卻沒有出處，改為不含數字的說法。
- `raw/README.md`：填入公開連結（arXiv 2301.04104）與來源頁。
- `build.py` 產生 40 個頁面，`check.py` 全部通過。

## [2026-11-24] ingest | Training Agents Inside of Scalable World Models

- 閱讀範圍：PDF 第 1–32 頁全文（正文 pp.1-18、參考文獻 pp.19-24、附錄 A–H pp.25-32）。`status: to-read`（依擁有者原則）。
- 新增來源頁：`2025-dreamer4`（arXiv 2025；areas：world-model、reinforcement-learning；pages: 32）。
- 新增概念頁（3 個）：
  - `shortcut-forcing`（把握度高：核心技術，pp.5-6、16；擴散與 flow matching 背景寫在本頁）
  - `offline-reinforcement-learning`（高：本篇核心設定，pp.2、10）
  - `action-conditioning`（中：重要發現，pp.14-15；名稱由本 Wiki 取，預計 WHAM 也會用到）
- 更新既有頁面（新增 Dreamer 4 小節，比較段擴充）：`world-model`、`learning-in-imagination`、`actor-critic`、`recurrent-state-space-model`、`symlog-predictions`、`return-normalization`（後兩頁首次有兩個來源，新增比較段）、`model-based-reinforcement-learning`（皆高）。
- 取代（Superseded）：`2023-dreamerv3` 三處（RSSM → transformer＋shortcut forcing；報酬正規化與熵正則 → PMPO＋行為先驗；想像訓練凍結 transformer、每片段一次 rollout，pp.7、29）。
- 一致而非衝突：`recurrent-state-space-model` 比較段註明換掉 RSSM 是為了規模，不代表它在先前較小的領域中是錯的；`return-normalization` 比較段註明 Dreamer 4 改變的是策略損失。
- 來源關係：`2023-dreamerv3`、`2019-planet`、`2018-world-models` 補上 Dreamer 4（p.17 引用 World Models 與 PlaNet 為早期可從像素規劃的世界模型）。
- 刻意不連結：`categorical-latents`（Dreamer 4 用 tanh 連續表示，論文未說明是取代）；`variational-autoencoder`（tokenizer 是遮罩自編碼器，非變分）；`kl-balancing`、`latent-overshooting`、`latent-space-planning`。
- 寫法：論文中的「Dreamer 3」在 Wiki 一律寫成 `DreamerV3`，不必修改 `NUMBERED_NAMES`。
- `raw/README.md`：填入公開連結（arXiv 2509.24527）與來源頁。
- `build.py` 產生 48 個頁面，`check.py` 全部通過。

## [2026-11-24] ingest | World and Human Action Models towards gameplay ideation

- 閱讀範圍：PDF 第 1–23 頁的文字層（正文 pp.1-7、參考文獻 pp.8、12、方法 pp.9-12、延伸資料圖 pp.13-23）。PDF 有 127 MB，依 decisions.md 只讀文字層；延伸資料圖多為影像，只讀到圖說，Table 1 的細項數字未能從文字層取得，只使用正文與表說中的數字。
- `status: read`（擁有者指定 World Models 與 WHAM 為已讀）。
- 新增來源頁：`2025-wham`（Nature 2025；areas：world-model、game-ai，是第一篇 game-ai 來源；pages: 23）。
- 新增概念頁（3 個）：
  - `creativity-support`（把握度高：核心貢獻，pp.2-3；area：game-ai）
  - `vector-quantization`（高：VQGAN 影像 token 化，pp.3、10）
  - `autoregressive-transformer`（高：交錯影像與動作 token 的下一個 token 預測，p.3）
- 更新既有頁面：`world-model`（新增 WHAM 小節；比較段註明 WHAM 是唯一不給代理人用的世界模型，並把 Dreamer 4 與 WHAM 並列為本 Wiki 的觀察）、`action-conditioning`（新增 WHAM 小節與比較段）、`2018-world-models` 與 `2021-dreamerv2`（WHAM 在 p.3 引用兩篇）、`world-models` 主題頁、中英 `index.md`（遊戲 AI 區首次有內容）。
- 寫作時自行核對並修正兩處頁碼：「不是可直接整合的工具」在 p.9（概念原型在 p.6），模型大小一句橫跨 pp.3-4。
- 取代與衝突：無。
- 刻意不連結：`learning-in-imagination`、`actor-critic`、`offline-reinforcement-learning`、`model-based-reinforcement-learning`（WHAM 不訓練代理人）；`variational-autoencoder`（VQGAN 非變分，只在 `vector-quantization` 相關概念中提及）；`2025-dreamer4`（互不引用，只在 `world-model` 比較段並列）；規模定律只寫在來源頁。
- `raw/README.md`：填入公開連結（DOI 10.1038/s41586-025-08600-3）與來源頁。至此 `raw/` 中 7 個 PDF 全部 ingest 完成。
- `build.py` 產生 56 個頁面，`check.py` 全部通過。

## [2026-11-24] lint | 完整檢查（7 篇來源）

- 範圍：7 個來源頁、20 個概念頁、1 個主題頁，中英各 28 頁。本次只回報，沒有修改任何 Wiki 頁面。
- `check.py`：全部通過。
- PDF 抽查（每個來源頁隨機抽 3 個帶出處的主張，固定亂數種子，對照該頁 PDF 文字層，共 21 項）：全部相符。
  - `2018-world-models`：CMA-ES 適用參數量（p.4）、世界模型與控制器的分工（p.1）、能否取代真實環境的提問（p.6）。
  - `2019-planet`：隨機與確定路徑都需要的引文（p.3）、最終代理人不需要 latent overshooting（p.5）、單一代理人學六個任務（p.6）。
  - `2020-dreamer`：action repeat 2 最好（p.19）、λ-returns 的定義（p.4）、horizon 20 時 16/20 任務勝出且同段另寫 19 個任務（p.9，已標待確認）。
  - `2021-dreamerv2`：discount 0.99 時在 Montezuma's Revenge 與 ICM 相當（p.17）、以類別變數取代 PlaNet 的高斯潛在變數（p.2）、批次 50 條長度 50 的序列（p.2）。
  - `2023-dreamerv3`：世界模型元件與 straight-through 梯度（pp.3-4）、穩健性技巧與單一固定設定（p.1）、仍沿用 PlaNet 的 RSSM（p.3）。
  - `2025-dreamer4`：三個訓練階段（p.4）、獎勵頭沿用 DreamerV3 的 symexp twohot（p.7）、記憶短且物品欄預測不精確（p.18）。
  - `2025-wham`：同時建模世界與玩家動作（p.3）、Demonstrator 是概念原型（p.6）、使用者研究歸納出一致性、多樣性與持續性（p.1）。
- 翻譯抽查（每個中文頁隨機抽 3 段與英文版逐段對照，共 84 段）：28 頁中英段落數全部相同；抽查段落的數字、出處、連結與意思都一致，沒有發現漏譯或譯錯。
- 語意檢查結果（待擁有者決定是否修改）：
  - 過時說法：主題頁 `world-models` 的 Overview 以「代理人」為中心描述世界模型，WHAM 加入後已不完全適用；概念頁 `world-model` 的 Explanation 只列兩種用途（特徵、模擬器），可補「供人類構思」與「離線訓練」。
  - 缺少的反向交叉連結：`categorical-latents`→`vector-quantization`、`variational-autoencoder`→`vector-quantization`、`shortcut-forcing`→`autoregressive-transformer`、`model-based-reinforcement-learning`→`actor-critic`、`latent-space-planning`→`latent-overshooting`、`mixture-density-rnn`→`recurrent-state-space-model`、`learning-in-imagination`→`model-based-reinforcement-learning`、`autoregressive-transformer`→`action-conditioning`、`creativity-support`。其餘單向連結（如 `world-model`→`categorical-latents`）屬合理的上位到下位關係，不建議補。
  - 主題頁 Key concepts 未列：`offline-reinforcement-learning`、`evolution-strategies`、`creativity-support`（後者屬 game-ai，可只在 Key terms 提及）。
  - 多頁提到但沒有自己頁面的概念：free nats／free bits（PlaNet、Dreamer、DreamerV2、DreamerV3）、行為複製（behavior cloning，Dreamer 4）、Reinforce 與 PPO 等策略梯度方法、Atari 與 Minecraft 等基準。free nats／free bits 已在四篇來源出現，符合建立條件。
  - 別名重疊：`categorical-latents` 的別名 straight-through gradients 也被 DreamerV2 用於 actor 梯度，容易混淆。
  - 未標記的衝突或取代：沒有發現。Dreamer 不用 target network、DreamerV2 改用，已在比較段寫成設計差異。
  - Explainer：逐一檢查，沒有發現扭曲原意。
  - 待確認（論文內部不一致，無法由 Wiki 解決）：Dreamer p.9 任務數 19 或 20；DreamerV2 discount 0.999（p.2）與 0.995（p.19）；DreamerV3 想像 horizon 16（p.5）與 15（p.21）。
  - 建議可補的論文：Genie（Dreamer 4 與 WHAM 都引用）、MuZero（DreamerV2、DreamerV3 引用）、IRIS 或 DIAMOND（transformer／擴散世界模型），以及預定的第 8、9 篇。
  - 規則缺口：附錄圖號如 `Fig. A.2` 不符合出處格式，目前只能標頁碼。

## [2026-11-24] rules | 出處格式接受附錄圖表編號

- 依上一筆 lint 的規則缺口，擁有者同意（「Apply all」）。
- `scripts/check.py` 的 `REF_OK`：圖、表、公式、演算法編號允許「大寫字母＋可選的點」前綴，例如 `(p.7, Fig. A.2)`、`(p.7, Table A1)`。原有寫法不受影響。
- `AGENTS.md`、範本不變。既有只標頁碼的附錄圖出處不回頭修改。

## [2026-11-24] lint | 依完整檢查結果修正

- 擁有者指示「Apply all」，依同日 lint 紀錄修正；規則缺口已另記一筆 `rules`。
- 過時說法：主題頁 `world-models` 的 Overview 不再只以代理人為中心，補上「在不接觸真實環境下訓練策略」與「讓人探索可能的未來」兩種用途；`index.md` 的主題頁摘要同步修改。概念頁 `world-model` 的 Explanation 從兩種用途改為四種（特徵、模擬器、只能用錄製資料時的模擬器、供人探索的生成器）。兩處都只寫通用知識，不含數字。
- 反向交叉連結（Related concepts 新增）：`categorical-latents`、`variational-autoencoder`→`vector-quantization`；`shortcut-forcing`→`autoregressive-transformer`；`model-based-reinforcement-learning`→`actor-critic`；`latent-space-planning`→`latent-overshooting`；`mixture-density-rnn`→`recurrent-state-space-model`；`learning-in-imagination`→`model-based-reinforcement-learning`；`autoregressive-transformer`→`action-conditioning`、`creativity-support`。
- 主題頁 Key concepts 與 frontmatter 新增：`evolution-strategies`、`offline-reinforcement-learning`、`creativity-support`、`free-bits`。
- 新增概念頁 `free-bits`（把握度高：PlaNet p.12、Dreamer p.14、DreamerV2 p.18、DreamerV3 p.5 與 p.10 都明確寫到，已回 PDF 核對）。別名含 free nats。`2019-planet`、`2020-dreamer`、`2021-dreamerv2`、`2023-dreamerv3` 的 frontmatter 與 Related concepts、`kl-balancing`、`variational-autoencoder`、`recurrent-state-space-model` 的 Related concepts 連到它；`index.md` 世界模型區加入。Background 列出提出 free bits 的 Kingma et al. (2016)。
- 別名重疊：`categorical-latents` 移除別名 straight-through gradients（中文版同步移除 straight-through 梯度）；這個名詞仍在該頁 Explanation 與主題頁 Key terms 解釋。
- 未處理：行為複製、Reinforce／PPO、基準環境不符合建立概念頁的條件（只出現在一篇來源或只是順帶提到），維持在來源頁與 Key terms 中解釋；建議補的論文（Genie、MuZero、IRIS、DIAMOND）需要擁有者先把 PDF 放進 `raw/`；三處論文內部不一致維持「待確認」。
- 中文版：上述所有頁面同步翻譯並更新 `translated_from`。
- `build.py` 產生 58 個頁面，`check.py` 全部通過。

## [2026-11-24] query | 簡報退回：補上強化學習的基本定義

- 起因：做簡報（`decks/world-models/`）的節點 2 發現，Wiki 沒有任何一頁解釋強化學習本身（代理人、獎勵、策略），而簡報讀者沒學過強化學習。依 `docs/slides-plan.md` 第 6 節「跨階段退回」，回到 Wiki 補頁面，不在簡報裡補。
- 修改：概念頁 `model-based-reinforcement-learning` 的 Explanation 開頭新增一句強化學習的通用定義（中英版同步，更新 `translated_from`）。只寫通用知識，不含數字。選這頁是因為它被 6 篇來源頁連到，證據卡可以引用。
- 沒有新增頁面。`build.py`、`check.py` 全部通過。
