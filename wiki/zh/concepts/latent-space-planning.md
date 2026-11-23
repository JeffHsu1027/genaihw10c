---
title: "潛在空間規劃（Latent space planning）"
aliases: [在潛在空間規劃, 線上規劃, 模型預測控制, MPC, CEM 規劃]
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
sources: [2019-planet]
translated_from: "405f1f8239d5"
---

## 一句話定義

在學到的潛在動態模型裡搜尋候選動作序列、以預測的獎勵評分來選擇動作，過程中不產生觀測畫面。

## 說明

每一步，代理人先推斷目前的潛在狀態，用模型想像許多候選動作序列的結果，再挑出預測報酬最高的序列。在模型預測控制（model-predictive control）中，只執行第一個動作，看到下一個觀測後再重新搜尋，讓計畫能隨實際情況調整。交叉熵方法（cross entropy method）是常見的搜尋程序：抽樣一批序列、留下最好的幾個、用它們重新擬合抽樣分布，然後重複。在潛在空間規劃很快，因為不需要產生影像。

> **解說（Explainer）：** 就像棋手每走一步前先往後想幾步，看到對手回應後再重新思考。

## 各來源怎麼說

### Learning Latent Dynamics for Planning from Pixels（2019）

[PlaNet](../sources/2019-planet.md) 在模型中用 CEM 規劃，並像模型預測控制一樣每一步都重新規劃 (p.3)。每次收到新觀測後，動作序列的信念都從平均為零、變異數為一重新開始，以避免陷入局部最佳 (p.3)。每個候選序列只用一條抽樣軌跡評分，把計算預算留給更多不同的序列 (p.3)。設定為規劃視野 12、迭代 10 次、1000 個候選、以最好的 100 個重新擬合 (p.12)。用 CEM 反覆修正，在所有任務上都勝過從 1000 個隨機序列中挑最好的一個 (p.6, Fig. 5)。在 cheetah 上使用真實模擬器時，視野 6 太短，最佳視野約為 8，視野太長反而因搜尋空間變大而變差 (p.20, Fig. 12)。由於 PlaNet 沒有價值函數，視野之外的獎勵都被忽略，作者建議學習一個價值函數 (p.8)。

## 相關概念

- [基於模型的強化學習（Model-based reinforcement learning）](model-based-reinforcement-learning.md)：規劃是使用學習模型的一種方式。
- [遞迴狀態空間模型（Recurrent state-space model）](recurrent-state-space-model.md)：PlaNet 用來規劃的模型。
- [在想像中學習（Learning in imagination）](learning-in-imagination.md)：使用模型的另一種方式；它事先用想像的經驗訓練策略，規劃則是在做決定的當下搜尋。

## 背景資料

（尚無）

## 我的筆記
