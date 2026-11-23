---
title: "潛在超前預測（Latent overshooting）"
aliases: [overshooting, 超前預測, 多步潛在目標]
updated: 2026-11-24
areas: [world-model]
sources: [2019-planet]
translated_from: "915135069984"
---

## 一句話定義

潛在序列模型的一種訓練目標：除了一步預測之外，也訓練多步預測，做法是在潛在空間中把預測拉向由真實觀測推斷出的狀態。

## 說明

標準的變分訓練只教轉移模型往前預測一步。在容量有限的情況下，一步預測最好的模型不一定是多步預測最好的模型，但規劃需要準確預測很遠的未來。超前預測從較早的狀態把轉移模型往前推好幾步，再把每個預測狀態拉向由實際觀測推斷出的狀態。在潛在空間做這件事，就不必解碼出額外的影像，也就省下大量計算。

## 各來源怎麼說

### Learning Latent Dynamics for Planning from Pixels（2019）

[PlaNet](../sources/2019-planet.md) 提出潛在超前預測，作為標準變分下界的推廣：訓練一直到最大距離為止的每一種距離的預測，每種距離各有一個權重 (pp.5-6, Eq. 7)。它與觀測超前預測做對比：後者把每個多步預測都解碼成影像，在影像領域通常太昂貴 (p.5, Fig. 3)。距離較長時，後驗分布的梯度會被截斷，讓預測往有資訊的後驗靠攏，而不是反過來 (p.6)。實驗中，潛在超前預測大幅改善了一個叫 DRNN 的模型，卻讓 RSSM 的表現略微下降 (p.14, Fig. 8)。因此最終的 PlaNet 代理人並沒有使用它 (p.12)。

## 相關概念

- [遞迴狀態空間模型（Recurrent state-space model）](recurrent-state-space-model.md)：結果不需要超前預測的那個模型。
- [潛在空間規劃（Latent space planning）](latent-space-planning.md)：多步預測之所以重要的原因。

## 背景資料

（尚無）

## 我的筆記
