---
title: "報酬正規化（Return normalization）"
aliases: [百分位數報酬正規化, retnorm]
updated: 2026-11-24
areas: [reinforcement-learning]
sources: [2023-dreamerv3]
translated_from: "d99770f9ad59"
---

## 一句話定義

以穩健估計的報酬範圍來縮放訓練策略所用的報酬，讓「追求獎勵」與「探索」之間的平衡不受環境獎勵尺度影響。

## 說明

帶有熵獎勵的策略學習要平衡兩項：報酬會隨獎勵的縮放而變，熵則不會。獎勵很大時，熵獎勵變得無足輕重；獎勵很小或很稀少時，探索則永遠佔上風。正規化優勢值或除以標準差，在獎勵稀少時可能放大雜訊。改成除以低百分位數與高百分位數之間的差距，並且只縮小大的報酬、不放大小的報酬，就能讓熵係數在各種環境中保有意義，也不怕極端值。

## 各來源怎麼說

### Mastering Diverse Domains through World Models（2023）

[DreamerV3](../sources/2023-dreamerv3.md) 正規化報酬，讓它大致落在 0 到 1 之間，因此能在各領域使用固定的熵係數 `3e-4` (p.6)。縮放尺度是第 5 到第 95 百分位數報酬的範圍，再以指數移動平均平滑；只有這個尺度大於 1 時才除以它，以免在獎勵稀少時放大雜訊 (p.6)。論文主張，優勢值正規化、以標準差正規化，以及限制熵的目標，都無法在各領域找到穩定的超參數 (p.6)。消融實驗中，報酬正規化是重要性僅次於 KL 目標的穩定技術 (p.10)。

## 相關概念

- [Actor-critic（演員－評論家）](actor-critic.md)：報酬正規化縮放 actor 的學習訊號。
- [Symlog 預測（Symlog predictions）](symlog-predictions.md)：DreamerV3 處理獎勵尺度的另一項技術。

## 背景資料

（尚無）

## 我的筆記
