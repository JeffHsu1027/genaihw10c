---
title: "類別潛在變數（Categorical latents）"
aliases: [離散潛在變數, 離散表示, straight-through 梯度, discrete latents]
updated: 2026-11-24
areas: [world-model]
sources: [2021-dreamerv2, 2023-dreamerv3]
translated_from: "9beb41364b13"
---

## 一句話定義

由多個類別變數組成的潛在表示，每個變數從一組固定的類別中取一個，用來取代連續的高斯變數。

## 說明

高斯潛在變數用連續數值描述狀態，不確定性是一個平滑的單峰。類別變數組成的向量則用離散的選擇描述狀態，因此能表達幾個明顯分開的可能性，以及突然的變化。抽樣出一個類別這個步驟不可微分，所以訓練時通常使用 straight-through 估計：前向傳遞使用抽樣出的 one-hot 向量，反向傳遞則把機率的梯度當作沒有抽樣一樣傳回去。這種梯度有偏差，但變異很小。

> **解說（Explainer）：** 就像用一組選擇題的答案來描述一個場景，而不是為每個屬性各拉一條滑桿。

## 各來源怎麼說

### Mastering Atari with Discrete World Models（2021）

[DreamerV2](../sources/2021-dreamerv2.md) 把隨機狀態表示成 32 個各有 32 類的類別變數，攤平後的樣本是長度 1024、只有 32 個位元為 1 的稀疏二元向量 (p.9)。類別變數以 straight-through 梯度訓練，用自動微分只要三行程式 (p.3, Alg. 1)。在 55 個 Atari 遊戲中，類別潛在變數在 42 個勝過高斯、8 個較差、5 個平手 (p.9)。作者不知道原因，只提出假設：類別先驗能完全貼合後驗的混合、稀疏性可能有助於泛化、類別變數可能更容易最佳化，以及它們可能更適合「進入新房間」這類不平滑的事件 (p.9)。改用大量二元潛在變數則比較差 (p.18)。

### Mastering Diverse Domains through World Models（2023）

[DreamerV3](../sources/2023-dreamerv3.md) 仍從一組 softmax 分布抽樣出表示，並使用 straight-through 梯度 (p.4)。因為觀察到 KL 損失偶爾暴衝，它在每個類別分布中混入 1% 的均勻分布，讓分布永遠不會變成確定性的 (p.5)。Actor 也使用同樣的混合，避免出現零機率與無限大的對數機率 (p.18)。每個潛在變數的類別數會隨模型大小增加 (p.20)。

### 來源之間的比較

- [DreamerV2](../sources/2021-dreamerv2.md) 提出類別潛在變數，並證明它在 Atari 上的好處 (p.9)。
- [DreamerV3](../sources/2023-dreamerv3.md) 在所有領域都保留它，並加入均勻混合來穩定訓練 (p.5)。DreamerV3 建立在 DreamerV2 之上；這段整理是本 Wiki 的。

## 相關概念

- [遞迴狀態空間模型（Recurrent state-space model）](recurrent-state-space-model.md)：DreamerV2 把類別潛在變數用在 RSSM 的隨機部分。
- [KL 平衡（KL balancing）](kl-balancing.md)：DreamerV2 世界模型的另一項主要修改。
- [變分自編碼器（Variational autoencoder）](variational-autoencoder.md)：常見的替代做法，使用高斯潛在變數與重參數化梯度。

## 背景資料

（尚無）

## 我的筆記
