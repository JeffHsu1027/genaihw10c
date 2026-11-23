---
title: "世界模型（World models）"
area: world-model
updated: 2026-11-24
sources: [2018-world-models, 2019-planet, 2020-dreamer, 2021-dreamerv2, 2023-dreamerv3, 2025-dreamer4]
concepts: [world-model, model-based-reinforcement-learning, variational-autoencoder, mixture-density-rnn, recurrent-state-space-model, learning-in-imagination, latent-space-planning, latent-overshooting, actor-critic, categorical-latents, kl-balancing, symlog-predictions, return-normalization, shortcut-forcing, action-conditioning]
translated_from: "7de4af9756a8"
---

## 概述

世界模型是學出來的模擬器：讓代理人能預測環境會如何回應自己的行動。相關研究關心的是：如何從原始觀測學到這樣的模型、如何用它來選擇動作或訓練策略，以及如何避免代理人利用模型的錯誤。這個主題頁逐篇整理這條研究脈絡。

## 發展脈絡

- 2018：[World Models](../sources/2018-world-models.md) 把代理人拆成大型非監督式世界模型與小型控制器，並證明完全在模型夢境中訓練的策略可以在真實遊戲中運作 (p.7)。
- 2019：[PlaNet](../sources/2019-planet.md) 學出同時具有確定性與隨機部分的遞迴狀態空間模型，每個動作都在潛在空間中線上規劃，以平均約少 200 倍的回合達到強大無模型方法的表現 (p.2)。
- 2020：[Dreamer](../sources/2020-dreamer.md) 保留 PlaNet 的世界模型，但完全在想像中用 actor-critic 學習行為，價值模型能看見視野之外，在 20 個任務的平均上勝過 PlaNet 與無模型的 D4PG (p.6, Fig. 6)。
- 2021：[DreamerV2](../sources/2021-dreamerv2.md) 改用類別潛在變數與 KL 平衡，成為第一個完全在另外訓練的世界模型裡學習、就在 Atari 達到人類水準的代理人 (p.1)。
- 2023：[DreamerV3](../sources/2023-dreamerv3.md) 加入穩定技術，讓一組固定設定在 150 多個任務上勝過專門的方法，並成為第一個從零開始在 Minecraft 挖到鑽石的演算法 (p.1)。
- 2025：[Dreamer 4](../sources/2025-dreamer4.md) 改用以 shortcut forcing 訓練、可擴展的 transformer 世界模型，成為第一個完全只靠離線資料就在 Minecraft 拿到鑽石的代理人 (p.1)。

## 來源

| 年份 | 標題 | 狀態 | 一句話總結 |
|---|---|---|---|
| 2018 | [World Models](../sources/2018-world-models.md) | 已讀 | 由 VAE 加 MDN-RNN 組成的世界模型，搭配演化訓練的小型控制器；策略可以在模型的夢境中訓練。 |
| 2019 | [Learning Latent Dynamics for Planning from Pixels (PlaNet)](../sources/2019-planet.md) | 未讀 | 純粹基於模型的代理人，在學到的遞迴狀態空間模型中用 CEM 規劃。 |
| 2020 | [Dream to Control (Dreamer)](../sources/2020-dreamer.md) | 未讀 | 完全在 PlaNet 世界模型的潛在想像中學習 actor-critic，並把價值梯度穿過動態模型。 |
| 2021 | [Mastering Atari with Discrete World Models (DreamerV2)](../sources/2021-dreamerv2.md) | 未讀 | 加上類別潛在變數與 KL 平衡的 Dreamer；只在世界模型裡學習就達到 Atari 人類水準。 |
| 2023 | [Mastering Diverse Domains through World Models (DreamerV3)](../sources/2023-dreamerv3.md) | 未讀 | 穩定技術讓一組固定設定精通許多領域，包括在 Minecraft 挖到鑽石。 |
| 2025 | [Training Agents Inside of Scalable World Models (Dreamer 4)](../sources/2025-dreamer4.md) | 未讀 | 快速的 transformer 世界模型；只靠離線資料在想像中訓練，就在 Minecraft 拿到鑽石。 |

## 關鍵概念

- [世界模型（World model）](../concepts/world-model.md)：預測環境如何變化的學習模型。
- [基於模型的強化學習（Model-based reinforcement learning）](../concepts/model-based-reinforcement-learning.md)：會學習或使用這種模型的強化學習。
- [變分自編碼器（Variational autoencoder）](../concepts/variational-autoencoder.md)：把觀測壓縮成小的潛在向量。
- [混合密度遞迴神經網路（Mixture density RNN）](../concepts/mixture-density-rnn.md)：預測下一個潛在狀態的機率分布。
- [遞迴狀態空間模型（Recurrent state-space model）](../concepts/recurrent-state-space-model.md)：具有確定性記憶與隨機狀態的潛在動態模型。
- [在想像中學習（Learning in imagination）](../concepts/learning-in-imagination.md)：用世界模型產生的經驗訓練策略。
- [潛在空間規劃（Latent space planning）](../concepts/latent-space-planning.md)：在模型裡搜尋動作序列來選擇動作。
- [潛在超前預測（Latent overshooting）](../concepts/latent-overshooting.md)：用多步預測訓練潛在模型。
- [Actor-critic（演員－評論家）](../concepts/actor-critic.md)：同時學習策略與估計未來獎勵的價值函數。
- [類別潛在變數（Categorical latents）](../concepts/categorical-latents.md)：用離散選擇而非高斯分布描述潛在狀態。
- [KL 平衡（KL balancing）](../concepts/kl-balancing.md)：訓練潛在模型時，先驗更新得比後驗快。
- [Symlog 預測（Symlog predictions）](../concepts/symlog-predictions.md)：壓縮目標值，以預測任意量級的數值。
- [報酬正規化（Return normalization）](../concepts/return-normalization.md)：縮放報酬，讓一組探索設定適用每個環境。
- [Shortcut forcing](../concepts/shortcut-forcing.md)：只用幾個去噪步驟生成每一格影片畫面。
- [動作條件（Action conditioning）](../concepts/action-conditioning.md)：讓預測的未來取決於代理人的動作。

## 術語表

- **潛在向量（latent vector）**：概括一次觀測的一小串數字。
- **Rollout**：代理人在環境中從一回合開始到結束的一次執行。
- **控制器／策略（controller / policy）**：代理人中負責選擇動作的部分。
- **基於模型的強化學習（model-based reinforcement learning）**：會學習或使用環境模型的強化學習。
- **模型被利用（model exploitation）**：代理人找到只因模型出錯才得高分的行為。
- **溫度（temperature）**：調整模型抽樣隨機程度的參數。
- **部分可觀測馬可夫決策過程（POMDP）**：代理人的觀測無法呈現完整狀態的決策問題。
- **模型預測控制（model-predictive control，MPC）**：每次收到新觀測就重新規劃，每個計畫只執行第一個動作。
- **交叉熵方法（cross entropy method，CEM）**：反覆抽樣候選解、留下最好的幾個、再用它們重新擬合抽樣分布的搜尋方法。
- **動作重複（action repeat）**：把選定的動作連續執行好幾個環境步。
- **價值函數（value function）**：預測代理人從某個狀態出發能得到多少未來獎勵。
- **想像視野（imagination horizon）**：代理人想像時用世界模型往前推演的步數。
- **λ-return**：一種價值目標值，混合「先相信若干步真實或想像的獎勵、再依賴價值函數」的各種估計。
- **重參數化（reparameterization）**：把隨機樣本寫成雜訊的固定函數，讓梯度能穿過抽樣步驟。
- **Straight-through 估計（straight-through estimator）**：反向傳遞時把抽樣步驟當成恆等函數，讓梯度能穿過離散樣本。
- **Reinforce 梯度（Reinforce gradient）**：依抽樣動作的好壞提高其機率的策略梯度；無偏但雜訊大。
- **Sticky actions**：Atari 的一種評測設定，會隨機重複上一個動作，讓代理人無法死背固定的動作序列。
- **人類正規化分數（human-normalized score）**：把遊戲分數換算成以參考人類玩家或人類世界紀錄為一的尺度。
- **固定超參數（fixed hyperparameters）**：每個任務都用同一組設定，而不是依領域分別調整。
- **Free bits**：KL 項已低於某個小門檻時就不再懲罰它。
- **Replay ratio**：每收集一步新經驗，代理人要做多少訓練步。
- **PPO**：廣泛使用的無模型策略梯度演算法，常被當作穩健的基準。
- **Minecraft Diamond**：一個評測任務，代理人要在 Minecraft 中依序收集一連串物品，最後拿到鑽石，而且獎勵很稀少。
- **擴散模型（diffusion model）**：從隨機雜訊出發、逐步去除雜訊來產生資料的生成模型。
- **Tokenizer**：把影片畫面等原始輸入壓縮成較短表示序列、供另一個模型處理的網路。
- **行為克隆（behavior cloning）**：訓練策略去模仿資料集中記錄的動作。
- **離線強化學習（offline reinforcement learning）**：只用固定資料集改進策略，不與環境互動。
- **FVD（Fréchet Video Distance）**：衡量生成影片與真實影片有多接近的指標，越低越好。

## 未解問題

- 在隨機策略無法涵蓋的環境中，代理人要如何充分探索來改進世界模型？[World Models](../sources/2018-world-models.md) 提出由好奇心驅動的迭代流程，但沒有實驗驗證 (pp.10-11)。
- 在想像中訓練的策略要如何避免利用模型的錯誤？[World Models](../sources/2018-world-models.md) 只用隨機模型與可調溫度部分解決了這個問題 (p.10)。
- 規劃型代理人要如何考慮規劃視野之外的獎勵？[PlaNet](../sources/2019-planet.md) 建議學習一個價值函數 (p.8)。

> **後續變更：** [Dreamer](../sources/2020-dreamer.md) 以在想像中學習價值模型回答了這個問題 (p.4, Fig. 4)。

- 世界模型應該用什麼目標訓練？[Dreamer](../sources/2020-dreamer.md) 發現像素重建最好、只預測獎勵不夠，並預期視覺複雜的環境需要更好的表示學習 (p.9)。
- 完全透過世界模型學習的代理人，能否在 Atari 這類離散動作領域具有競爭力？[Dreamer](../sources/2020-dreamer.md) 在那裡學到成功的行為，但還沒有競爭力 (p.16)。

> **後續變更：** [DreamerV2](../sources/2021-dreamerv2.md) 在 55 個 Atari 遊戲上達到人類水準 (p.7, Table 1)。

- 類別潛在變數為什麼比高斯好？[DreamerV2](../sources/2021-dreamerv2.md) 只提出假設 (p.9)。
- 以重建為基礎的世界模型，要如何掌握小而重要的物體？[DreamerV2](../sources/2021-dreamerv2.md) 在 Video Pinball 上失敗，因為球只有一個像素 (p.8)。
- 以世界模型為基礎的代理人，能不能穩定地在 Minecraft 找到鑽石，而不只是偶爾找到？[DreamerV3](../sources/2023-dreamerv3.md) 在預算結束時只有 0.4% 的回合拿到 (p.24, Fig. 9)。
- 世界模型能不能在網路影片這類無標記資料上預訓練，或在不同領域之間共用？[DreamerV3](../sources/2023-dreamerv3.md) 把這些列為未來方向 (p.11)。
- 世界模型需要多長的記憶？[Dreamer 4](../sources/2025-dreamer4.md) 保留 9.6 秒的脈絡，遠多於先前的 Minecraft 模型，但超過這個長度仍會遺忘，物品欄也會模糊 (p.13)。
- 從少量標註資料學到的動作條件，能否擴展到一般的網路影片？[Dreamer 4](../sources/2025-dreamer4.md) 顯示它能轉移到 Minecraft 中沒見過的部分，並把網路影片列為下一步 (p.15)。

## 背景資料

（尚無）

## 我的筆記
