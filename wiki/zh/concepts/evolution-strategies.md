---
title: "演化策略（Evolution strategies）"
aliases: [ES, CMA-ES, 共變異數矩陣調適演化策略]
updated: 2026-11-24
areas: [reinforcement-learning]
sources: [2018-world-models]
translated_from: "5e3ebc0845b3"
---

## 一句話定義

一類黑箱最佳化方法：對一群候選解反覆抽樣、評分、保留較好的，過程中不需要計算梯度。

## 說明

每一代抽樣出許多組參數，實際執行並評分，再把抽樣分布移向得分最高的那些。CMA-ES 還會調整抽樣分布的共變異數，學到參數空間中哪些方向比較重要。因為只需要最後的分數，演化策略能應付稀疏或延遲的獎勵，也很容易平行執行，但參數非常多時效率會變差。

## 各來源怎麼說

### World Models（2018）

[World Models](../sources/2018-world-models.md) 用 CMA-ES 訓練小型控制器，因為這個方法適合最多幾千個參數的解空間 (p.4)。作者指出，演化策略只需要最後的累積獎勵，而且容易平行化 (p.12)。族群大小為 64，每個候選解的適應度是它在 16 次 rollout 中的平均獎勵 (p.14)。在 Car Racing 中，最佳代理人在 1800 代之後，於 1024 次 rollout 中達到平均 900.46 分 (p.14)。

## 相關概念

- [在想像中學習（Learning in imagination）](learning-in-imagination.md)：在 VizDoom 中，每個候選控制器都在想像的環境裡評分。

## 背景資料

（尚無）

## 我的筆記
