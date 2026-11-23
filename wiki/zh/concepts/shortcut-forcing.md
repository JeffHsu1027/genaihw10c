---
title: "Shortcut forcing"
aliases: [shortcut model, diffusion forcing, flow matching, x-prediction, 捷徑模型]
updated: 2026-11-24
areas: [world-model]
sources: [2025-dreamer4]
translated_from: "acadd7ad3484"
---

## 一句話定義

影片世界模型的一種訓練目標：結合讓序列中每一格畫面有各自雜訊程度的 diffusion forcing，以及學會跨大步去噪的 shortcut model，讓每一格新畫面只需幾次網路計算就能生成。

## 說明

擴散模型與 flow matching 模型從雜訊出發、一步步去除雜訊來生成資料，通常需要很多次網路計算。Shortcut model 還會告訴網路這一步要跨多大，並訓練大步的結果要等於兩個小步，因此少數幾步就能取代很多步。Diffusion forcing 對序列中的每一格畫面分別加雜訊，讓模型能根據乾淨或只有少許雜訊的歷史生成下一格，這正是互動式世界模型需要的。直接預測乾淨的畫面，而不是預測從雜訊指向資料的方向，往往會得到更平滑的輸出，逐格生成時累積的誤差也較少。

> **解說（Explainer）：** 一般的擴散模型像是從濃霧走到清楚畫面，要走很多小步。Shortcut model 學會跨幾個大步，而 diffusion forcing 讓它能一格一格地畫，同時回頭參考已經畫好的畫面。

## 各來源怎麼說

### Training Agents Inside of Scalable World Models（2025）

[Dreamer 4](../sources/2025-dreamer4.md) 提出 shortcut forcing 來訓練動態模型，建立在 diffusion forcing 與 shortcut model 之上 (p.5)。它預測乾淨的表示而不是速度，因為預測速度會產生高頻的輸出，在長時間逐格推演時造成誤差累積 (p.6)。隨訊號程度線性上升的斜坡權重，讓損失專注在雜訊較少、學習訊號較多的輸入上 (p.6)。生成時每格畫面使用 4 個取樣步驟 (p.6)。4 步的 shortcut forcing 品質接近 64 步的 diffusion forcing，生成速度快 16 倍 (p.16, Fig. 8)。直接預測乾淨表示、在同一空間計算損失，再加上斜坡權重，大幅提升了生成品質，對長時間生成尤其明顯 (p.16)。

## 相關概念

- [世界模型（World model）](world-model.md)：shortcut forcing 用來訓練 Dreamer 4 的世界模型。
- [動作條件（Action conditioning）](action-conditioning.md)：動作也輸入同一個動態 transformer。
- [遞迴狀態空間模型（Recurrent state-space model）](recurrent-state-space-model.md)：較早、以變分目標訓練的動態模型。
- [自迴歸 transformer（Autoregressive transformer）](autoregressive-transformer.md)：WHAM 採用的替代設計，逐個 token 產生每一格畫面，而不是靠去噪。

## 背景資料

（尚無）

## 我的筆記
