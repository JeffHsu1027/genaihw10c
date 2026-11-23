---
title: "世界模型（World model）"
aliases: [動態模型, 環境模型, dynamics model, environment model]
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
sources: [2018-world-models]
translated_from: "5965c140fe21"
---

## 一句話定義

一個從經驗中學到的環境模型，用來預測接下來會發生什麼，通常以目前的狀態與動作為條件。

## 說明

能預測自己行動後果的代理人，不必在真實世界裡把每件事都試一遍。世界模型從經驗中學會這些預測，通常在壓縮過的潛在空間（latent space）中進行，而不是直接處理原始像素。它主要有兩種用法：當作特徵來源，概括現在並暗示未來；或當作模擬器，讓代理人在裡面練習。因為它是學出來的，永遠不會完美，依賴它的代理人可能被它的錯誤誤導。

> **解說（Explainer）：** 世界模型就像打擊者腦中的畫面：在眼睛跟上快速球之前，就先告訴他球會到哪裡。

## 各來源怎麼說

### World Models（2018）

[World Models](../sources/2018-world-models.md) 用兩個部分組成世界模型：壓縮每張畫面的 VAE，以及預測下一張壓縮畫面的 MDN-RNN (p.2, Fig. 4)。世界模型的訓練不使用獎勵，只有小型控制器看得到獎勵 (p.5)。這篇論文兩種用法都用上了：在 Car Racing 中，世界模型的隱藏狀態讓控制器對未來有所掌握 (p.5)；在 VizDoom 中，它在訓練時完全取代了真實遊戲 (p.7)。

## 相關概念

- [變分自編碼器（Variational autoencoder）](variational-autoencoder.md)：為世界模型壓縮觀測。
- [混合密度遞迴神經網路（Mixture density RNN）](mixture-density-rnn.md)：以機率分布預測下一個狀態。
- [在想像中學習（Learning in imagination）](learning-in-imagination.md)：在世界模型裡訓練代理人。

## 背景資料

（尚無）

## 我的筆記
