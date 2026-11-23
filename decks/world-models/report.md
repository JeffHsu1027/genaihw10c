# 簡報執行紀錄：世界模型是什麼？

依 `.claude/skills/make-slides/SKILL.md` 與 `docs/slides-plan.md` 執行。每次跑關卡記一筆，通過或退回都記。

## [2026-11-24] 準備：撰寫 skill 與關卡腳本

- 新增 `.claude/skills/make-slides/SKILL.md`（節點、關卡、退回規則、紀錄格式）。
- 新增關卡腳本 `gates.py`（`g1`、`g2`、`g4`、`render`）、溢出量測 `g4_overflow.js`、版面 `deck.css`。
- 設計取捨：
  - 渲染交給 `gates.py render` 機械轉換，確保節點 5「不改任何一個字」由程式保證，而不是靠 AI 自律。
  - 每頁是固定 16:9 的框，字級以框寬計算，溢出與否不受螢幕大小影響，G4 可以用程式量測。
  - G2 要求證據卡附上「Wiki 原文」逐字摘錄，讓「該頁確實有這段內容」變成腳本可檢查的條件。
- 開始條件：`check.py` 全部通過；已 ingest 7 篇；主題頁 `world-models` 存在且有 7 篇來源。
- 未做可選的對照組（一句話 prompt），由擁有者決定是否補做。

## [2026-11-24] G1 第 1 輪：通過

- 檢查方式：`python .claude/skills/make-slides/gates.py g1`
- 結果：主題頁 7 篇來源；`sources.md` 選出 7 篇，全部存在且屬於主題頁。
- 問題：無
- 退回：無
