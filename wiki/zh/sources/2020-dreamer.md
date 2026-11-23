---
title: "Dream to Control: Learning Behaviors by Latent Imagination"
authors: "Danijar Hafner et al."
year: 2020
venue: "ICLR 2020 (arXiv:1912.01603)"
url: "https://arxiv.org/abs/1912.01603"
raw: "raw/(dreamerv1)DREAM TO CONTROL LEARNING BEHAVIORSv3.pdf"
pages: 20
added: 2026-11-24
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
status: to-read
concepts: [actor-critic, learning-in-imagination, world-model, model-based-reinforcement-learning, recurrent-state-space-model, latent-overshooting, latent-space-planning, variational-autoencoder]
topics: [world-models]
translated_from: "d78b6141421b"
---

## 一句話總結

Dreamer 先從影像學出[世界模型](../concepts/world-model.md)，再完全靠[潛在想像](../concepts/learning-in-imagination.md)學習行為：在想像的軌跡上訓練一個 [actor-critic](../concepts/actor-critic.md)，並把解析的價值梯度沿著學到的動態模型反向傳播來改進 actor (p.1)。

## 研究問題

只在固定想像視野內最大化獎勵的策略或規劃器會很短視，而過去的方法常用不需梯度的最佳化，沒有利用神經網路動態模型提供的梯度 (p.1)。代理人能不能完全在學到的世界模型裡，從影像學會需要長期規劃的行為，同時考慮想像視野之外的獎勵 (p.1)？

## 方法

- **世界模型**：與 PlaNet 相同的潛在動態模型：轉移模型是[遞迴狀態空間模型](../concepts/recurrent-state-space-model.md)，表示模型使用 CNN 編碼器，觀測模型是轉置 CNN，獎勵模型是全連接網路 (p.6)。各部分以變分下界一起訓練，包含影像與獎勵的重建項加上 KL 正則項，做法如同[變分自編碼器](../concepts/variational-autoencoder.md) (p.6, Eq. 10)。
- **三個流程**：Dreamer 從過去經驗的資料集學習動態模型、從想像的軌跡學習動作模型與價值模型，並在環境中執行動作模型來擴充資料集，三者交替或平行進行 (p.2, Alg. 1)。
- **想像**：想像軌跡從過去經驗中取出的序列的模型狀態出發，用轉移模型、獎勵模型與策略往前推演固定的視野 (p.3)。學習行為時，世界模型保持固定不動 (p.5)。
- **Actor 與 critic**：動作模型輸出經過 tanh 轉換的高斯分布，抽樣寫成網路輸出加上雜訊的確定性函數，讓梯度能穿過抽樣步驟 (p.4, Eq. 3)。價值模型估計動作模型將會得到的想像獎勵，包括視野之外的部分 (p.4, Eq. 2)。價值的目標值是 λ-return：把「先加總若干步想像獎勵、其餘交給價值模型」的各種估計做指數加權平均 (p.4, Eq. 6)。
- **學習**：價值模型回歸 λ-return 目標值，動作模型則把解析梯度穿過價值、獎勵、想像狀態與動作反向傳播來最大化目標值 (p.5)。和 A3C、PPO 這類 Reinforce 式方法不同，Dreamer 會穿過價值模型反向傳播；和 DDPG、SAC 不同，它也會穿過學到的轉移反向傳播 (p.5)。
- **離散動作與提前結束**：離散動作使用 straight-through 梯度；在可能提前結束的任務中，模型也預測折扣因子，降低回合可能已結束後的想像步驟的權重 (p.5)。
- **表示學習**：比較三種學習世界模型的方式：PlaNet 的影像重建、從影像預測狀態（而不是從狀態預測影像）的對比式估計，以及只預測獎勵 (pp.5-6)。

> **解說（Explainer）：** Dreamer 和 World Models 一樣在自己的想像中練習。但它不是隨機嘗試各種行為、留下有效的，而是直接問模型：每個動作稍微改變時，預測的未來會怎麼變，再往變好的方向調整。

附錄中的實作細節：Dreamer 沿用 World Models 的卷積編碼器與解碼器以及 PlaNet 的 RSSM，其他函數都是三層各 300 個單元、使用 ELU 激活的全連接層 (p.14)。潛在分布是 30 維的對角高斯分布 (p.14)。每批有 50 段長度 50 的序列，Adam 的學習率在世界模型為 `6e-4`，價值與動作模型為 `8e-5` (p.14)。想像視野為 15，折扣為 0.99，λ 為 0.95 (p.14)。KL 項不縮放，但與 PlaNet 一樣低於 3 個 free nats 時截斷 (p.14)。訓練從 5 個隨機回合開始，每 100 次訓練步就收集一個回合，探索雜訊為 Normal(0, 0.3)，動作重複為 2 (p.14)。潛在超前預測、熵獎勵與目標網路都不需要 (p.14)。每次訓練使用一張 V100 GPU 與 10 個 CPU 核心，每一百萬環境步約需 3 小時，相較之下 PlaNet 需要 11 小時，D4PG 達到相近表現需要 24 小時 (p.8)。

> **後續變更：** [DreamerV2](2021-dreamerv2.md) 把高斯潛在變數換成 32 個各有 32 類的類別變數，在 55 個 Atari 遊戲中有 42 個因此變好 (p.9)。

> **後續變更：** [DreamerV2](2021-dreamerv2.md) 以 KL 平衡取代 free nats (p.18)。

## 主要結果

- 評測使用 DeepMind Control Suite 的 20 個視覺控制任務，觀測為 64x64x3 影像，動作重複為 2，所有任務使用相同超參數 (p.8)。
- 經過 500 萬環境步後，Dreamer 的平均分數為 823，相較之下 PlaNet 為 332，D4PG 在 1 億步後為 786 (p.6, Fig. 6)。
- Dreamer 保有 PlaNet 的資料效率，同時超越最佳無模型代理人的最終表現 (p.9)。
- 學習價值模型讓 Dreamer 對想像視野長度不敏感，而沒有價值的動作模型與 PlaNet 的線上規劃都高度依賴視野長度 (p.4, Fig. 4)。
- 沒有價值模型時，兩種替代方法都很短視，只在 walker 這類反應式任務成功；Dreamer 則也能解決 acrobot、hopper 這類需要長期功勞分配的任務 (p.7, Fig. 7)。
- 視野為 20 時，Dreamer 在 20 個任務中的 16 個勝過兩種替代方法、4 個平手；同一段也提到 19 個任務，因此確切數量（待確認） (p.9)。
- 像素重建在多數任務上得到最好的世界模型，對比式估計約能解決一半的任務，只預測獎勵則不夠 (p.8, Fig. 8)。
- Dreamer 在部分具離散動作與提前結束的 Atari 遊戲與一個 DeepMind Lab 關卡上也學到成功的行為 (p.16, Fig. 9)。
- 動作重複為 2 在各任務上效果最好 (p.19, Fig. 12)。

## 限制與未解問題

- Dreamer 的效果取決於表示學習的目標；只預測獎勵會失敗，作者預期在視覺更複雜的環境需要更好的表示學習 (p.9)。
- 在 Atari、DeepMind Lab 這類離散動作領域，完全透過世界模型學習的代理人還沒有競爭力 (p.16)。

> **後續變更：** [DreamerV2](2021-dreamerv2.md) 在 55 個 Atari 遊戲、2 億步後達到人類水準，並勝過 IQN 與 Rainbow (p.7, Table 1)。

- 行為只從想像的軌跡學習，且學習時世界模型固定不動，因此行為最多只能和模型的預測一樣好 (p.5)。
- 動作重複的評估使用較早的超參數設定，且只有 2 個隨機種子 (p.19, Fig. 12)。

## 相關概念

- [Actor-critic](../concepts/actor-critic.md)：行為學習演算法，在想像中訓練。
- [在想像中學習](../concepts/learning-in-imagination.md)：Dreamer 完全靠潛在想像學習行為。
- [世界模型](../concepts/world-model.md)：學到的潛在動態模型。
- [基於模型的強化學習](../concepts/model-based-reinforcement-learning.md)：Dreamer 所屬的研究方向。
- [遞迴狀態空間模型](../concepts/recurrent-state-space-model.md)：沿用自 PlaNet 的轉移模型。
- [潛在超前預測](../concepts/latent-overshooting.md)：Dreamer 不需要。
- [潛在空間規劃](../concepts/latent-space-planning.md)：Dreamer 取代的另一種做法。
- [變分自編碼器](../concepts/variational-autoencoder.md)：重建目標是一個變分下界。

## 與其他來源的關係

- [Learning Latent Dynamics for Planning from Pixels](2019-planet.md)：Dreamer 學習與 PlaNet 相同的世界模型，但用學到的動作模型取代線上規劃來選擇動作 (p.8)。為了公平比較，它以相同的動作重複重新執行 PlaNet (p.8)，並指出 PlaNet 在需要長期規劃的任務上很短視 (p.7, Fig. 7)。
- [Mastering Atari with Discrete World Models](2021-dreamerv2.md)（DreamerV2，2021）是本篇的直接後繼，它把本篇稱為 DreamerV1。它保留整體代理人架構，但改用類別潛在變數、KL 平衡，並在 Atari 上以 Reinforce 梯度訓練 actor。
- [World Models](2018-world-models.md)：Dreamer 把 World Models 描述為以兩階段學習潛在動態、在想像中演化出線性控制器 (p.7)，並沿用它的卷積編碼器與解碼器 (p.14)。

## 背景資料

- [Dreamer 專案頁面](https://danijar.com/dreamer)：論文中提供的程式碼與影片。

## 我的筆記
