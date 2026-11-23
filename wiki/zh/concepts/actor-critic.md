---
title: "Actor-critic（演員－評論家）"
aliases: [演員評論家, 動作模型與價值模型, 策略與價值函數, λ-return, lambda-return]
updated: 2026-11-24
areas: [reinforcement-learning]
sources: [2020-dreamer, 2021-dreamerv2]
translated_from: "d8e2bbd5700a"
---

## 一句話定義

一種有兩個學習元件的強化學習方法：負責選動作的 actor（策略），以及估計 actor 從每個狀態出發能得到多少未來獎勵的 critic（價值函數）。

## 說明

Critic 學習預測從某個狀態出發的期望報酬，actor 則被更新成選擇 critic 評價高的動作。有了 critic，actor 不必等到遙遠的獎勵真的發生，也能把它納入考量。價值的目標值有好幾種建法，在偏差與變異之間取捨：只加總觀察到的獎勵、先加幾步獎勵再相信 critic，或像 λ-return 那樣把許多這類估計混合起來。Actor 可以用抽樣的策略梯度改進；當動作到價值之間全部可微分時，也可以把 critic 的價值直接反向傳播到 actor。

> **解說（Explainer）：** Actor 是球員，critic 是告訴球員每個局面有多大希望的教練；球員學著往教練看好的局面移動。

## 各來源怎麼說

### Dream to Control: Learning Behaviors by Latent Imagination（2020）

[Dreamer](../sources/2020-dreamer.md) 完全在世界模型想像出的軌跡上訓練動作模型與價值模型 (p.4)。價值模型的目標值是 λ-return，把想像的獎勵與固定步數之後的價值估計混合起來 (p.4, Eq. 6)。動作模型把解析梯度穿過想像的狀態、獎勵與價值反向傳播來最大化這些目標值，這點不同於 A3C、PPO 這類 Reinforce 式方法，也不同於不穿過學到的轉移反向傳播的 DDPG 與 SAC (p.5)。沒有價值模型時，同一個代理人會變得短視，在需要長期功勞分配的任務上失敗 (p.7, Fig. 7)。價值目標使用折扣 0.99 與 λ 0.95，而且不需要目標網路或熵獎勵 (p.14)。

### Mastering Atari with Discrete World Models（2021）

[DreamerV2](../sources/2021-dreamerv2.md) 也完全在想像的軌跡上訓練 actor 與 critic，想像視野為 15，並使用 λ 目標值 (p.5, Eq. 4)。Critic 使用每 100 次梯度更新同步一次的目標網路 (p.6)。Actor 的損失混合了無偏但雜訊大的 Reinforce 梯度，以及穿過動態模型、有偏但變異小的 straight-through 梯度，再加上熵正則項 (p.6, Eq. 6)。Atari 用 Reinforce 梯度效果好得多，連續控制則是穿過動態模型反向傳播好得多 (p.6)。只用 straight-through 梯度時，55 個 Atari 遊戲中有 44 個變差 (p.10)。

### 來源之間的比較

- [Dreamer](../sources/2020-dreamer.md) 只靠把價值梯度穿過學到的動態模型反向傳播來訓練 actor，任務都是連續控制 (p.5)。
- [DreamerV2](../sources/2021-dreamerv2.md) 在連續控制上保留這種估計方式，但在 Atari 上主要依靠 Reinforce 梯度 (p.6)。兩篇並不衝突：最好的估計方式取決於領域。
- [Dreamer](../sources/2020-dreamer.md) 不需要目標網路或熵獎勵 (p.14)。
- [DreamerV2](../sources/2021-dreamerv2.md) 兩者都用，並以策略熵取代外加的動作雜訊來探索 (p.18)。這是版本之間的設計差異，不是互相矛盾的主張；DreamerV2 建立在 Dreamer 之上，這段整理是本 Wiki 的。

## 相關概念

- [在想像中學習（Learning in imagination）](learning-in-imagination.md)：Dreamer 訓練 actor 與 critic 的地方。
- [潛在空間規劃（Latent space planning）](latent-space-planning.md)：在做決定時搜尋動作、而非學習策略的另一種做法。
- [基於模型的強化學習（Model-based reinforcement learning）](model-based-reinforcement-learning.md)：Dreamer 的 actor-critic 依賴學到的模型。

## 背景資料

（尚無）

## 我的筆記
