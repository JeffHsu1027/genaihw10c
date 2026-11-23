---
title: 目錄
translated_from: "5df98ed0c990"
---

# 目錄

所有頁面的目錄，依領域分區（見 `wiki/areas.yml`）。每個領域依序列出主題頁、來源頁（依年份）、概念頁（依英文標題字母順序）。每行寫成 `- [標題](連結) — 一句話`；擁有者尚未閱讀的來源在行尾加「（未讀）」。屬於多個領域的頁面在每個領域都列出。

## 世界模型

- [世界模型（World models）](topics/world-models.md) — 主題入口：讓代理人能預測與練習的學習型模擬器。
- [World Models](sources/2018-world-models.md) — 由 VAE 加 MDN-RNN 組成的世界模型，搭配演化訓練的小型控制器，部分訓練在自己的夢境中進行。
- [Learning Latent Dynamics for Planning from Pixels](sources/2019-planet.md) — PlaNet：在遞迴狀態空間模型中用 CEM 規劃的純粹基於模型的代理人。（未讀）
- [Dream to Control: Learning Behaviors by Latent Imagination](sources/2020-dreamer.md) — Dreamer：完全在世界模型的潛在想像中學習的 actor-critic。（未讀）
- [Mastering Atari with Discrete World Models](sources/2021-dreamerv2.md) — DreamerV2：類別潛在變數與 KL 平衡；只在世界模型裡學習就達到 Atari 人類水準。（未讀）
- [類別潛在變數（Categorical latents）](concepts/categorical-latents.md) — 用離散類別變數而非高斯分布組成的潛在狀態。
- [KL 平衡（KL balancing）](concepts/kl-balancing.md) — 訓練潛在模型時，先驗更新得比後驗快。
- [潛在超前預測（Latent overshooting）](concepts/latent-overshooting.md) — 在潛在空間用多步預測訓練潛在模型。
- [潛在空間規劃（Latent space planning）](concepts/latent-space-planning.md) — 在學到的潛在模型裡搜尋動作序列來選擇動作。
- [在想像中學習（Learning in imagination）](concepts/learning-in-imagination.md) — 用世界模型產生的經驗訓練策略。
- [混合密度遞迴神經網路（Mixture density RNN）](concepts/mixture-density-rnn.md) — 預測高斯混合分布的遞迴網路。
- [基於模型的強化學習（Model-based reinforcement learning）](concepts/model-based-reinforcement-learning.md) — 會學習或使用環境模型的強化學習。
- [遞迴狀態空間模型（Recurrent state-space model）](concepts/recurrent-state-space-model.md) — 具有確定性記憶與隨機狀態的潛在動態模型。
- [變分自編碼器（Variational autoencoder）](concepts/variational-autoencoder.md) — 把輸入編碼成小而隨機的潛在向量，再解碼回來。
- [世界模型（World model）](concepts/world-model.md) — 預測環境如何變化的學習模型。

## 強化學習

- [World Models](sources/2018-world-models.md) — 由 VAE 加 MDN-RNN 組成的世界模型，搭配演化訓練的小型控制器，部分訓練在自己的夢境中進行。
- [Learning Latent Dynamics for Planning from Pixels](sources/2019-planet.md) — PlaNet：在遞迴狀態空間模型中用 CEM 規劃的純粹基於模型的代理人。（未讀）
- [Dream to Control: Learning Behaviors by Latent Imagination](sources/2020-dreamer.md) — Dreamer：完全在世界模型的潛在想像中學習的 actor-critic。（未讀）
- [Mastering Atari with Discrete World Models](sources/2021-dreamerv2.md) — DreamerV2：類別潛在變數與 KL 平衡；只在世界模型裡學習就達到 Atari 人類水準。（未讀）
- [Actor-critic（演員－評論家）](concepts/actor-critic.md) — 同時學習策略與估計未來獎勵的價值函數。
- [演化策略（Evolution strategies）](concepts/evolution-strategies.md) — 不用梯度、對一群候選解做最佳化。
- [潛在空間規劃（Latent space planning）](concepts/latent-space-planning.md) — 在學到的潛在模型裡搜尋動作序列來選擇動作。
- [在想像中學習（Learning in imagination）](concepts/learning-in-imagination.md) — 用世界模型產生的經驗訓練策略。
- [基於模型的強化學習（Model-based reinforcement learning）](concepts/model-based-reinforcement-learning.md) — 會學習或使用環境模型的強化學習。
- [世界模型（World model）](concepts/world-model.md) — 預測環境如何變化的學習模型。

## 遊戲 AI

（尚無）
