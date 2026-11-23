---
title: "基於模型的強化學習（Model-based reinforcement learning）"
aliases: [model-based RL, MBRL, 模型式強化學習]
updated: 2026-11-24
areas: [reinforcement-learning, world-model]
sources: [2018-world-models, 2019-planet]
translated_from: "4af7567cce1d"
---

## 一句話定義

會學習或使用「環境如何回應動作」的模型，並用這個模型來決定如何行動或學習如何行動的強化學習。

## 說明

無模型（model-free）方法直接從試誤中學習策略或價值函數。基於模型的方法先學一個動態模型，再加以利用：在做決定的當下拿來規劃，或拿來產生額外的經驗訓練策略。好的模型能讓學習大幅提高資料效率，也可能轉移到同一環境中的新任務。不過模型的錯誤可能誤導代理人，而從影像學到準確的模型並不容易。

## 各來源怎麼說

### World Models（2018）

[World Models](../sources/2018-world-models.md) 不使用獎勵學習世界模型，再訓練一個利用模型的小型控制器：先把模型當作特徵來源 (p.5)，接著完全取代真實環境 (p.7)。論文把自己定位為簡化版的示範，展示 1990 到 2015 年間一系列論文中「以 RNN 為基礎的世界模型加控制器」的想法 (p.2)。

### Learning Latent Dynamics for Planning from Pixels（2019）

[PlaNet](../sources/2019-planet.md) 是純粹基於模型的代理人：沒有策略網路或價值網路，每個動作都靠學到的模型規劃 (p.3)。論文列出用學習模型規劃預期的好處：更豐富的訓練訊號、不需透過 Bellman 備份傳遞獎勵、增加搜尋計算就能提升表現，以及動態模型可轉移到其他任務 (p.1)。它以平均約少 200 倍的回合，達到強大無模型代理人的表現 (p.2)。

### 來源之間的比較

- [World Models](../sources/2018-world-models.md) 事先用模型訓練策略；做決定時，控制器根據模型的隱藏狀態直接反應，不往前規劃 (p.6)。
- [PlaNet](../sources/2019-planet.md) 沒有策略，只在做決定的當下用模型搜尋動作序列 (p.3)。
- 兩篇都警告純確定性的模型容易被利用：[World Models](../sources/2018-world-models.md) 是被控制器利用 (p.9)，[PlaNet](../sources/2019-planet.md) 是被規劃器利用 (p.4, Fig. 2)。
- PlaNet 把 World Models 列為從想像經驗學習的混合式代理人；這段並列比較是本 Wiki 的整理。

## 相關概念

- [世界模型（World model）](world-model.md)：基於模型的方法所學的模型。
- [潛在空間規劃（Latent space planning）](latent-space-planning.md)：在做決定時使用模型。
- [在想像中學習（Learning in imagination）](learning-in-imagination.md)：用模型訓練策略。

## 背景資料

（尚無）

## 我的筆記
