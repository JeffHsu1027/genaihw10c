---
title: "Mastering Diverse Domains through World Models"
authors: "Danijar Hafner et al."
year: 2023
venue: "arXiv:2301.04104"
url: "https://arxiv.org/abs/2301.04104"
raw: "raw/(dreamerv3)Mastering Diverse Domains through World Modelsv2.pdf"
pages: 40
added: 2026-11-24
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
status: to-read
concepts: [symlog-predictions, return-normalization, kl-balancing, categorical-latents, recurrent-state-space-model, actor-critic, learning-in-imagination, world-model, model-based-reinforcement-learning, variational-autoencoder]
topics: [world-models]
translated_from: "ba58034f2de4"
---

## 一句話總結

DreamerV3 加入一組穩定學習的技術，例如 [symlog 預測](../concepts/symlog-predictions.md)、[報酬正規化](../concepts/return-normalization.md)，以及搭配 free bits 的 [KL 平衡](../concepts/kl-balancing.md)，讓一個以[世界模型](../concepts/world-model.md)為核心、只用一組固定設定的代理人，在 150 多個任務上勝過專門的方法，並從零開始在 Minecraft 中挖到鑽石 (p.1)。

## 研究問題

強化學習演算法要應用到新領域時，通常需要專家調整，因此很脆弱、成本也高 (p.2)。以世界模型為基礎的代理人，能不能只用一組固定的超參數，在差異很大的領域中都學得好？這樣的代理人能不能隨模型大小與計算量穩定地變強 (p.2)？

## 方法

- **三個網路**：世界模型預測可能動作的結果，critic 評估每個結果的價值，actor 選擇能達到最佳結果的動作；三者在代理人與環境互動時，同時從回放的經驗中訓練 (p.3)。
- **世界模型**：[遞迴狀態空間模型](../concepts/recurrent-state-space-model.md)，包含編碼器、序列模型、動態預測器，以及獎勵、是否繼續與解碼的輸出頭；表示是以 straight-through 梯度訓練的[類別潛在變數](../concepts/categorical-latents.md)向量 (pp.3-4)。世界模型透過自編碼學習表示，做法如同[變分自編碼器](../concepts/variational-autoencoder.md) (p.3)。
- **世界模型損失**：預測損失、動態損失與表示損失，權重分別為 1、1 與 0.1，兩個 KL 損失都在 1 nat 的 free bits 以下截斷 (pp.4-5)。類別分布混入 1% 的均勻分布，避免 KL 損失突然暴衝 (p.5)。
- **行為學習**：[actor-critic](../concepts/actor-critic.md) 完全在世界模型想像出的軌跡上訓練；在環境中行動時直接從 actor 抽樣，不做往前規劃，因此屬於[在想像中學習](../concepts/learning-in-imagination.md) (p.5)。
- **Critic**：預測 λ-return 的分布，以指數間隔分箱上的類別分布表示；它也在回放的軌跡上訓練（損失權重 0.3），並被拉向自己參數的指數移動平均 (pp.5-6)。
- **Actor**：離散與連續動作都使用 Reinforce 估計，熵係數固定為 `3e-4`，這要靠報酬正規化才可行 (p.6)。
- **穩健的預測**：向量觀測、獎勵與價值都以 symlog 轉換與 symexp twohot 損失處理，讓梯度大小不隨目標值大小而變 (p.7)。

> **後續變更：** [Dreamer 4](2025-dreamer4.md) 以 shortcut forcing 訓練的 transformer tokenizer 與動態模型取代 RSSM，因為 RSSM 很難擴展到多樣的資料 (p.29)。

> **後續變更：** [Dreamer 4](2025-dreamer4.md) 以 PMPO 策略損失加上朝行為克隆先驗的 KL 項，取代報酬正規化與熵正則項 (p.29)。

> **後續變更：** [Dreamer 4](2025-dreamer4.md) 在想像訓練時凍結世界模型 transformer，只訓練 policy 頭與 value 頭，並且每個資料片段只展開一次 rollout (p.7)。

> **解說（Explainer）：** 早期的 Dreamer 像一台每換一個駕駛就要重調座椅和後照鏡的車。DreamerV3 加上自動調整，不論獎勵很小或很大、頻繁或稀少，同一組設定都能用。

實作細節：訓練使用帶線上佇列的均勻回放緩衝區，訓練量由 replay ratio 決定 (p.18)。梯度以每個張量自適應截斷，並改用 LaProp 優化器取代 Adam，避免偶發的不穩定 (p.18)。序列模型是遞迴權重為 8 個區塊對角的 GRU (p.18)。模型大小從 1200 萬到 4 億個參數，預設為 2 億 (p.19)。正文寫預測視野為 16 (p.5)，超參數表卻列想像視野為 15 (p.21)；確切數值（待確認）。每個代理人都在一張 A100 GPU 上訓練 (p.19)。

## 主要結果

- 在固定超參數下，Dreamer 在 8 個領域、150 多個任務上評測，勝過調校過的專家演算法，也在所有領域勝過高品質的 PPO 基準 (p.8)。
- 在 57 個 Atari 遊戲、2 億影格的設定下，Dreamer 只用一小部分計算資源就勝過 MuZero，也勝過 Rainbow 與 IQN (p.8)。
- 在 DMLab 上，Dreamer 用 1 億影格就超越 IMPALA 與 R2D2+ 在 10 億步的表現，資料效率提升超過 1000% (p.8)。
- Dreamer 在 Proprio Control、Visual Control 與 BSuite 上創下新的最佳成績，在 Atari100k 上勝過 IRIS、TWM、SPR 與 SimPLe (pp.9-10)。
- 在 Minecraft 上訓練的 10 個 Dreamer 代理人全部在 1 億環境步內找到鑽石，而 IMPALA、Rainbow 與 PPO 最多只做到鐵鎬 (p.10, Fig. 5)。
- 在訓練預算結束時，Dreamer 有 0.4% 的回合拿到鑽石 (p.24, Fig. 9)。
- Dreamer 在 Minecraft 上用 1 張 GPU 跑 9 天；VPT 則用 720 張 GPU 跑 9 天，而且依賴人類資料 (p.11)。
- 消融實驗顯示每一項穩定技術平均都有幫助；KL 目標最重要，其次是報酬正規化與 symexp twohot 回歸 (p.10, Fig. 6)。
- 表現主要來自世界模型的非監督重建損失，而不是獎勵與價值的梯度 (p.10, Fig. 6)。
- 從 1200 萬到 4 億個參數，較大的模型分數更高，需要的環境互動也更少；提高 replay ratio 同樣能穩定地提升表現 (p.10, Fig. 6)。

## 限制與未解問題

- 訓練過程中能穩定找到鑽石，但在預算結束時只有 0.4% 的回合拿到，作者把這留給未來研究 (p.24, Fig. 9)。
- Minecraft 實驗採用先前研究的「破壞方塊」動作設定，因為原始動作空間讓隨機策略很難長時間按住按鍵 (p.10)。
- 為了實作簡單使用均勻回放，雖然優先回放也能改善 Dreamer (p.18)。
- DMLab 只評測到 1 億步，因為更長的訓練不可行；ProcGen 只跑了一個隨機種子 (p.19)。
- 作者提到的未來方向包括：在網路影片上預訓練世界模型，以及學習一個跨領域的世界模型 (p.11)。

## 相關概念

- [Symlog 預測](../concepts/symlog-predictions.md)：穩健地預測任意量級的目標。
- [報酬正規化](../concepts/return-normalization.md)：讓一個熵係數適用所有領域。
- [KL 平衡](../concepts/kl-balancing.md)：沿用自 DreamerV2，並與 free bits 結合。
- [類別潛在變數](../concepts/categorical-latents.md)：沿用自 DreamerV2，並混入少量均勻分布。
- [遞迴狀態空間模型](../concepts/recurrent-state-space-model.md)：世界模型的架構。
- [Actor-critic](../concepts/actor-critic.md)：以分布式 critic 與 Reinforce actor 學習行為。
- [在想像中學習](../concepts/learning-in-imagination.md)：行為只從想像的軌跡學習。
- [世界模型](../concepts/world-model.md)：代理人的核心。
- [基於模型的強化學習](../concepts/model-based-reinforcement-learning.md)：與 PPO、MuZero、VPT 比較。
- [變分自編碼器](../concepts/variational-autoencoder.md)：世界模型以自編碼學習表示。

## 與其他來源的關係

- [Training Agents Inside of Scalable World Models](2025-dreamer4.md)（Dreamer 4，2025）是下一代。它保留 symexp twohot 輸出頭，但把遞迴世界模型換成可擴展的 transformer，並把 Minecraft 從「以抽象合成動作線上學習」改為「以滑鼠鍵盤完全離線學習」。
- [Mastering Atari with Discrete World Models](2021-dreamerv2.md)：DreamerV3 是 DreamerV2 之後的下一代；DreamerV2 在 Atari 上超越人類，DreamerV3 則加入穩定技術、新的網路架構、新的優化器與更大的回放緩衝區 (p.20)。
- [Dream to Control: Learning Behaviors by Latent Imagination](2020-dreamer.md)：論文把 DreamerV1 描述為只限於連續控制 (p.20)。
- [Learning Latent Dynamics for Planning from Pixels](2019-planet.md)：世界模型仍是 PlaNet 提出的 RSSM (p.3)。

## 背景資料

- [DreamerV3 專案頁面](https://danijar.com/dreamerv3)：論文中提供、能重現所有結果的公開實作。

## 我的筆記
