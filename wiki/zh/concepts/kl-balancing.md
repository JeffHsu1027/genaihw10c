---
title: "KL 平衡（KL balancing）"
aliases: [KL balance, 平衡 KL 損失]
updated: 2026-11-24
areas: [world-model]
sources: [2021-dreamerv2]
translated_from: "ba3de6199d3d"
---

## 一句話定義

訓練潛在動態模型的一種方式：後驗與先驗之間的 KL 項，更新先驗的速度比更新後驗快。

## 說明

在序列變分模型中，KL 項同時做兩件事：把先驗（不看下一個觀測就預測下一個狀態）訓練得更接近後驗，以及把後驗拉向先驗。訓練初期先驗很差，把後驗拉向它可能破壞表示。KL 平衡把 KL 項拆成這兩個方向並給不同的權重，讓模型主要透過改進先驗動態來降低 KL，而不是讓表示變得模糊。這和像 β-VAE 那樣單純縮放整個 KL 項不同。

## 各來源怎麼說

### Mastering Atari with Discrete World Models（2021）

[DreamerV2](../sources/2021-dreamerv2.md) 提出 KL 平衡，先驗權重為 0.8、後驗為 0.2，以截斷梯度實作 (p.4, Alg. 2)。它主張準確的先驗非常關鍵，因為策略學習所用的想像軌跡就是由先驗產生的 (p.9)。在 55 個 Atari 遊戲中，KL 平衡在 44 個勝過標準 KL 項、6 個較差、5 個平手 (p.9)。它取代了 Dreamer 使用的 free nats (p.18)。作者認為它也可能幫助其他具有學習先驗的機率模型 (p.9)。

## 相關概念

- [類別潛在變數（Categorical latents）](categorical-latents.md)：DreamerV2 世界模型的另一項主要修改。
- [變分自編碼器（Variational autoencoder）](variational-autoencoder.md)：KL 平衡改變了變分下界中的 KL 項。
- [遞迴狀態空間模型（Recurrent state-space model）](recurrent-state-space-model.md)：以這種方式訓練先驗的模型。

## 背景資料

（尚無）

## 我的筆記
