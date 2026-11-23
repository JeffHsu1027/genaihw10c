# 證據卡：Mastering Atari with Discrete World Models（DreamerV2，2021）

只讀：`wiki/zh/sources/2021-dreamerv2.md` 與它連到的概念頁。

## C1
- 主張：DreamerV2 對 Dreamer 做了幾項小修改，成為第一個完全在另外訓練的世界模型裡學習行為、就在 Atari 達到人類水準的代理人。
- 出處：[DreamerV2](../../zh/sources/2021-dreamerv2.html) (p.1)
- Wiki 原文：「DreamerV2 對 Dreamer 做了幾項小修改，主要是類別潛在變數與 KL 平衡，成為第一個完全在另外訓練的世界模型裡學習行為、就在 Atari 評測上達到人類水準的代理人 (p.1)」

## C2
- 主張：過去世界模型一直不夠準確，無法在 Atari 上與最好的無模型方法競爭。
- 出處：[DreamerV2](../../zh/sources/2021-dreamerv2.html) (pp.1-2)
- Wiki 原文：「世界模型過去一直不夠準確，無法在 Atari 上與最好的無模型方法競爭；而 Atari 這個評測向來需要無模型演算法才能達到人類水準 (pp.1-2)」

## C3
- 主張：主要修改之一是類別潛在變數：隨機狀態是 32 個各有 32 類的類別變數，取代 PlaNet 與 Dreamer 的高斯潛在變數。
- 出處：[DreamerV2](../../zh/sources/2021-dreamerv2.html) (p.3, Fig. 2)
- Wiki 原文：「隨機狀態是 32 個各有 32 類的類別變數組成的向量，取代 PlaNet 與 Dreamer 的高斯潛在變數，並以 straight-through 梯度訓練 (p.3, Fig. 2)」

## C4
- 主張：行為完全在想像的軌跡上以 actor-critic 學習，這一步中世界模型固定不動。
- 出處：[DreamerV2](../../zh/sources/2021-dreamerv2.html) (pp.4-5)
- Wiki 原文：「完全在想像的軌跡上訓練 actor-critic，想像視野為 15，這一步中世界模型固定不動 (pp.4-5)」

## C5
- 主張：DreamerV2 在四種彙總指標上都勝過 IQN、Rainbow、C51 與 DQN 等無模型方法。
- 出處：[DreamerV2](../../zh/sources/2021-dreamerv2.html) (p.8)
- Wiki 原文：「DreamerV2 在四種彙總指標上都勝過 IQN、Rainbow、C51 與 DQN (p.8)」

## C6
- 主張：在一張 V100 GPU 上，不到 10 天就能跑完 2 億環境步。
- 出處：[DreamerV2](../../zh/sources/2021-dreamerv2.html) (p.6)
- Wiki 原文：「在一張 V100 GPU、單一環境實例下，不到 10 天就能跑完 2 億步 (p.6)」

## C7
- 主張：在 2 億環境步中，策略從 4680 億個想像的壓縮狀態學習，約為 5000 萬個真實輸入的 10,000 倍。
- 出處：[DreamerV2](../../zh/sources/2021-dreamerv2.html) (p.6)
- Wiki 原文：「在 2 億環境步中，策略從 4680 億個想像的壓縮狀態學習，約為 5000 萬個真實輸入的 10,000 倍 (p.6)」

## C8
- 主張：DreamerV2 在 Video Pinball 上表現很差，作者推測重建損失忽略了只佔一個像素的球。
- 出處：[DreamerV2](../../zh/sources/2021-dreamerv2.html) (p.8)
- Wiki 原文：「DreamerV2 在 Video Pinball 上表現很差；作者推測重建損失忽略了只佔一個像素的球 (p.8)」

## C9
- 主張：類別變數組成的向量用離散的選擇描述狀態，能表達幾個明顯分開的可能性，以及突然的變化。
- 出處：[類別潛在變數（Categorical latents）](../../zh/concepts/categorical-latents.html)
- Wiki 原文：「類別變數組成的向量則用離散的選擇描述狀態，因此能表達幾個明顯分開的可能性，以及突然的變化。」
