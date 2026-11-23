# 開場 prompt（階段 1，在 Claude Code 使用）

在專案資料夾（`genaihw10c`）開啟 Claude Code，把下面「開場 prompt」整段貼上。
開始前先確認：論文 PDF 已經放進 `raw/`，而且已經用 GitHub Desktop 建立 repository。

### 用 GitHub Desktop 建立 repository

1. GitHub Desktop → File → **Add local repository** → 選擇專案資料夾。
2. 它會提示這個資料夾還不是 git repository，點提示裡的 **create a repository**。
3. 名稱用資料夾名稱即可；Git ignore 選 **None**（專案已經有 `.gitignore`），不要勾選建立 README。
4. 建立後，看左側的變更清單或第一個 commit 的檔案清單，**確認沒有任何 `.pdf`**。
5. 現在先不要 Publish，等階段 1 結束、要發佈 GitHub Pages 時再 Publish（記得設為 Public）。

---

## 開場 prompt

```
這是 Karpathy 的 LLM Wiki 構想：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
（請先讀完這份原文。）
我想用它建立一個個人論文知識庫，收錄我讀過或有興趣的所有論文，第一個主題區是「世界模型」。
之後我還會用這個 Wiki 當唯一知識來源，產生一份教學型 HTML 簡報。

先不要建立任何檔案。

請先完整閱讀：
1. docs/decisions.md：我和 AI 已經討論並確定的決定與理由。
2. docs/reference/hw9-CLAUDE.md、docs/reference/hw9-log.md：我上週做的 Wiki 規則與紀錄，裡面有一些我想保留的規則。

然後訪談我，幫我釐清還沒決定的需求：
- 一次只問一個問題，等我回答後再問下一題，總共約 8–10 題。
- decisions.md 已經決定的事不要再問；以它第 9 節「待訪談決定的問題」為主，
  再加上你認為 decisions.md 沒有涵蓋到、但建 Wiki 前必須確定的事。
- 每一題可以附上你的建議選項，讓我直接選或修改。

問完後，把結果整理成 docs/requirements.md 的需求摘要給我確認，內容包含：
已沿用的決定（引用 decisions.md 的編號）、這次訪談新決定的事項，以及與上週規則的差異。
我確認之後，才可以產生 AGENTS.md、CLAUDE.md（只寫 @AGENTS.md）、範本、
scripts/build.py、scripts/check.py 與資料夾結構。

所有規則、腳本與連結一律使用相對於專案根目錄的路徑，不要寫入本機的絕對路徑。
不要執行任何 git 指令，commit 由我自己用 GitHub Desktop 做（見 decisions.md D11）。

產生完後，請逐條對照 requirements.md，列出每一項寫在 AGENTS.md 的哪裡，
找出遺漏的項目並補上。這一步還不要 ingest 任何論文。
```

---

## 後續 prompt（依序使用）

### 試跑：只 ingest 1 篇

```
請依 AGENTS.md 處理 raw/ 裡的 World Models（2018）這一篇。
完成後執行 scripts/build.py 與 scripts/check.py，回報結果，
並告訴我這次執行中，規則有哪些地方不清楚或不好用。先不要處理其他論文。
```

→ 自己打開產生的網頁看過。需要改規則的話，先改 AGENTS.md，在 log.md 記一筆，再用 GitHub Desktop commit。

### 依序 ingest 其餘論文

```
請依 docs/decisions.md 第 8.1 節的順序，處理下一篇論文。
```

→ 每篇完成並通過 check.py 後，用 GitHub Desktop commit 一次。

### 進入階段 2 之前

```
請執行一次完整的 lint 與 scripts/check.py，
並確認 docs/decisions.md 第 8 節「交接關卡」的三個條件是否都已達成。
```
