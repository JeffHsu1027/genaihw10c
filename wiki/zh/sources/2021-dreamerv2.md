---
title: "Mastering Atari with Discrete World Models"
authors: "Danijar Hafner et al."
year: 2021
venue: "ICLR 2021 (arXiv:2010.02193)"
url: "https://arxiv.org/abs/2010.02193"
raw: "raw/(dreamerv2)MASTERING ATARI WITH DISCRETE WORLD MODELSv4.pdf"
pages: 26
added: 2026-11-24
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
status: to-read
concepts: [categorical-latents, kl-balancing, world-model, recurrent-state-space-model, actor-critic, learning-in-imagination, model-based-reinforcement-learning, variational-autoencoder, free-bits]
topics: [world-models]
translated_from: "9a6b39f5c4d8"
---

## 一句話總結

DreamerV2 對 Dreamer 做了幾項小修改，主要是[類別潛在變數](../concepts/categorical-latents.md)與 [KL 平衡](../concepts/kl-balancing.md)，成為第一個完全在另外訓練的[世界模型](../concepts/world-model.md)裡學習行為、就在 Atari 評測上達到人類水準的代理人 (p.1)。

## 研究問題

世界模型過去一直不夠準確，無法在 Atari 上與最好的無模型方法競爭；而 Atari 這個評測向來需要無模型演算法才能達到人類水準 (pp.1-2)。只從世界模型的預測中學習的代理人，能不能只用一張 GPU，就在 Atari 上追上甚至勝過頂尖的無模型代理人 (p.2)？

## 方法

- **世界模型**：由影像編碼器、負責動態的[遞迴狀態空間模型](../concepts/recurrent-state-space-model.md)（RSSM），以及影像、獎勵與折扣因子的預測器組成 (p.2)。後驗狀態看得到目前的影像，先驗狀態則要在看不到影像的情況下預測它；想像時使用的是先驗 (p.3, Fig. 2)。
- **類別潛在變數**：隨機狀態是 32 個各有 32 類的類別變數組成的向量，取代 PlaNet 與 Dreamer 的高斯潛在變數，並以 straight-through 梯度訓練 (p.3, Fig. 2)。見[類別潛在變數](../concepts/categorical-latents.md)。
- **損失函數**：各部分一起訓練，預測影像、獎勵與折扣，再加上後驗與先驗之間的 KL 項；KL 項在 Atari 乘以 0.1，在連續控制乘以 1.0 (p.4, Eq. 2)。這個損失是以動作為條件的隱藏馬可夫模型的 ELBO，所以世界模型可視為序列版的[變分自編碼器](../concepts/variational-autoencoder.md) (p.4)。
- **KL 平衡**：KL 項對先驗的最小化速度比對後驗快，先驗的權重為 0.8、後驗為 0.2，避免表示被拉向訓練不足的先驗 (p.4, Alg. 2)。見 [KL 平衡](../concepts/kl-balancing.md)。
- **行為學習**：完全在想像的軌跡上訓練 [actor-critic](../concepts/actor-critic.md)，想像視野為 15，這一步中世界模型固定不動 (pp.4-5)。Critic 回歸 λ 目標值，並使用每 100 次梯度更新同步一次的目標網路 (p.6)。Actor 混合 Reinforce 梯度與穿過動態模型的 straight-through 梯度，再加上熵正則項 (p.6, Eq. 6)。
- **依領域不同的選擇**：Atari 用 Reinforce 梯度效果好得多，連續控制則是穿過動態模型反向傳播好得多 (p.6)。

> **後續變更：** [DreamerV3](2023-dreamerv3.md) 對離散與連續動作都使用 Reinforce 梯度，靠報酬正規化讓這個做法可行 (p.6)。

> **後續變更：** [DreamerV3](2023-dreamerv3.md) 以固定的損失權重與 free bits 取代依領域調整的 KL 縮放，所有領域通用 (p.5)。

> **後續變更：** [DreamerV3](2023-dreamerv3.md) 以「把 critic 拉向自己參數的指數移動平均」取代 critic 的目標網路 (p.6)。

> **解說（Explainer）：** 高斯潛在變數只能說*大概在這附近*。一組類別變數比較像一張勾選清單，記下一個個離散的事實，很適合房間會突然切換、敵人會消失、物品會出現的遊戲。

實作細節：世界模型約有 2000 萬個可訓練參數，actor 與 critic 各約 100 萬個 (pp.4-5)。影像從 84x84 灰階縮小為 64x64 像素，以便沿用 Dreamer 的卷積網路 (p.3)。每批訓練資料有 50 段長度 50 的序列 (p.2)。正文寫折扣為 0.999 (p.2)，超參數表卻列為 0.995 (p.19)；回報的結果實際用哪個值（待確認）。RSSM 使用 600 個單元，世界模型學習率為 `2e-4`，actor 與 critic 的學習率為 `4e-5` 與 `1e-4` (p.19)。和 Dreamer 相比，模型從 1300 萬個參數增加到 2200 萬個，探索方式也從外加的動作雜訊改成策略熵 (p.18)。

## 主要結果

- 在 55 個使用 sticky actions 的 Atari 遊戲、2 億環境步的設定下，DreamerV2 的玩家正規化中位數為 2.15，截斷後的紀錄正規化平均為 0.28；IQN 分別為 1.29 與 0.21，Rainbow 為 1.47 與 0.17 (p.7, Table 1)。
- DreamerV2 在四種彙總指標上都勝過 IQN、Rainbow、C51 與 DQN (p.8)。
- 在一張 V100 GPU、單一環境實例下，不到 10 天就能跑完 2 億步 (p.6)。
- 在 2 億環境步中，策略從 4680 億個想像的壓縮狀態學習，約為 5000 萬個真實輸入的 10,000 倍 (p.6)。
- 消融實驗：類別潛在變數在 42 個遊戲勝過高斯、8 個較差；KL 平衡在 44 個遊戲勝過標準 KL 項、6 個較差 (p.9)。
- 截斷影像梯度後表現幾乎崩潰，截斷後的紀錄正規化平均從 0.25 掉到 0.01；截斷獎勵梯度則影響不大 (p.9, Table 2)。
- Actor 只用 straight-through 梯度時，有 44 個遊戲變差，因此 Atari 代理人主要依靠 Reinforce 梯度 (p.10)。
- 只靠像素，DreamerV2 就在 Humanoid Walk 任務中學會站起來並行走，作者認為這是第一個此類的已發表結果 (p.16)。
- 改用較低的折扣 0.99 時，DreamerV2 在 Montezuma's Revenge 上追平了明確探索方法 ICM (p.17)。
- 作者建議改報告截斷後的紀錄正規化平均，因為玩家中位數會忽略一半的遊戲，玩家平均則被少數極端值主導 (p.8)。

## 限制與未解問題

- DreamerV2 在 Video Pinball 上表現很差；作者推測重建損失忽略了只佔一個像素的球 (p.8)。
- 類別潛在變數為什麼有幫助還不清楚；論文只列出假設，例如更能貼合整體後驗、稀疏性、較容易最佳化，以及較適合不平滑的遊戲事件 (p.9)。
- 消融結果使用的是稍早版本的代理人，附錄中的曲線也只有兩個隨機種子 (p.22)。
- 對每一項修改做完整消融不可行，因為每一項都需要超過 60,000 GPU 小時 (p.18)。
- 轉移、多任務學習、實體機器人與基於不確定性的探索等好處只被列為未來方向，沒有實驗 (p.11)。

## 相關概念

- [類別潛在變數](../concepts/categorical-latents.md)：對世界模型的主要修改。
- [KL 平衡](../concepts/kl-balancing.md)：對世界模型損失的第二項關鍵修改。
- [世界模型](../concepts/world-model.md)：準確到足以達到人類水準的 Atari 表現。
- [遞迴狀態空間模型](../concepts/recurrent-state-space-model.md)：動態模型，現在使用類別隨機狀態。
- [Actor-critic](../concepts/actor-critic.md)：行為學習演算法。
- [在想像中學習](../concepts/learning-in-imagination.md)：行為完全從想像的軌跡學習。
- [基於模型的強化學習](../concepts/model-based-reinforcement-learning.md)：與 SimPLe、MuZero 比較。
- [變分自編碼器](../concepts/variational-autoencoder.md)：世界模型是序列 VAE。
- [自由位元（Free bits）](../concepts/free-bits.md)：KL 平衡所取代的技巧。

## 與其他來源的關係

- [Dream to Control: Learning Behaviors by Latent Imagination](2020-dreamer.md)：DreamerV2 是 Dreamer 的演進版，本篇稱原版為 DreamerV1 (p.2)。附錄 C 列出所有修改，也包括沒有幫助的嘗試，例如二元潛在變數與在 GRU 中加入層正規化 (p.18)。
- [Mastering Diverse Domains through World Models](2023-dreamerv3.md)（DreamerV3，2023）是下一代。它保留類別潛在變數與 KL 平衡，但加入穩定技術，讓一組設定能用在許多領域，而不只是 Atari。
- [World and Human Action Models towards gameplay ideation](2025-wham.md)（WHAM，2025）把本篇列為遞迴狀態空間世界模型的例子，自己則改用建立在離散 token 上的 transformer。
- [Learning Latent Dynamics for Planning from Pixels](2019-planet.md)：DreamerV2 建立在 PlaNet 提出的世界模型上，並把它的高斯潛在變數換成類別變數 (p.2)。

## 背景資料

- [DreamerV2 專案頁面](https://danijar.com/dreamerv2)：論文中提供的影片、程式碼與 JSON 格式的訓練曲線。

## 我的筆記
