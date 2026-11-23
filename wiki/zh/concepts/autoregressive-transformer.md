---
title: "自迴歸 transformer（Autoregressive transformer）"
aliases: [decoder-only transformer, 因果 transformer, 下一個 token 預測, GPT 類模型]
updated: 2026-11-24
areas: [world-model]
sources: [2025-wham]
translated_from: "ca3142dbf593"
---

## 一句話定義

一次產生一個 token 的 transformer，每次都根據之前所有 token 預測下一個 token。

## 說明

因果注意力遮罩讓每個位置只能看到較早的位置，因此模型可以一次用整段序列訓練，預測每一個下一個 token。生成時，它抽樣出一個 token、接到序列後面，再重複這個過程。這是大型語言模型背後的設計，任何能寫成 token 序列的資料都適用，包括量化過的影像與離散化的動作。因為每個新 token 都取決於之前的 token，改變較早的 token 就會改變之後的所有內容。

## 各來源怎麼說

### World and Human Action Models towards gameplay ideation（2025）

[WHAM](../sources/2025-wham.md) 訓練一個 decoder-only transformer，預測影像與手把動作 token 交錯序列中的下一個 token，而且沒有明確的標記告訴它下一個該是影像還是動作 token (p.4, Fig. 2)。它建立在修改過的 nanoGPT（GPT-2 的實作）上 (p.10)。一次抽樣一個 token 的生成方式，讓影像或動作 token 能在生成途中被修改，因此可以透過編輯過的畫面或選定的動作來提示模型 (p.3)。最大的模型有 1.6B 個參數，脈絡為 5,560 個 token，也就是一秒的遊玩過程 (p.4, Fig. 2)。

## 相關概念

- [向量量化（Vector quantization）](vector-quantization.md)：產生 transformer 要預測的影像 token。
- [世界模型（World model）](world-model.md)：WHAM 以這種架構作為世界模型。
- [Shortcut forcing](shortcut-forcing.md)：另一種 transformer 世界模型設計，每格畫面用幾個去噪步驟生成，而不是逐個 token 生成。
- [動作條件（Action conditioning）](action-conditioning.md)：WHAM 把動作 token 與影像 token 交錯排列，讓預測取決於玩家的動作。
- [創作支援（Creativity support）](creativity-support.md)：WHAM 打造這個 transformer 世界模型的目的。

## 背景資料

（尚無）

## 我的筆記
