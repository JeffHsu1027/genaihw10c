# 節點 1 檢索：相關來源

- 主題：世界模型是什麼？（What is a World Model?）
- 讀者：知道 AI／神經網路，但沒聽過世界模型與強化學習的人。
- 只讀了：`wiki/zh/index.md`、`wiki/zh/topics/world-models.md`。
- 主題頁列出 7 篇來源，全部與主題直接相關，全部選用。7 篇剛好構成一條從 2018 到 2025 的發展脈絡，簡報可以用「同一個想法如何一步步變強、用途如何變廣」來教。

## 相關來源

| 年份 | 來源 | 為什麼相關 | 預計用在哪段教學 |
|---|---|---|---|
| 2018 | [World Models](../../zh/sources/2018-world-models.html) | 把代理人拆成世界模型與小型控制器，並在模型的「夢境」中訓練策略；是整個主題的起點與名稱來源 | 動機、核心概念、在夢裡學習 |
| 2019 | [PlaNet](../../zh/sources/2019-planet.html) | 第一個只在學到的潛在空間中規劃動作的代表；提出遞迴狀態空間模型 | 發展脈絡：用模型「規劃」 |
| 2020 | [Dreamer](../../zh/sources/2020-dreamer.html) | 從規劃改成在想像中學習策略（actor-critic） | 發展脈絡：在想像中學習 |
| 2021 | [DreamerV2](../../zh/sources/2021-dreamerv2.html) | 第一個只在世界模型中學習就達到 Atari 人類水準 | 發展脈絡：證明可行 |
| 2023 | [DreamerV3](../../zh/sources/2023-dreamerv3.html) | 一組固定設定跨越大量任務，並從零在 Minecraft 挖到鑽石 | 發展脈絡：通用化 |
| 2025 | [Dreamer 4](../../zh/sources/2025-dreamer4.html) | 可擴展的 transformer 世界模型，只靠離線資料學會挖鑽石 | 發展脈絡：不必真的去玩 |
| 2025 | [WHAM](../../zh/sources/2025-wham.html) | 世界模型不是給代理人用，而是支援遊戲設計師發想 | 用途變廣、比較 |

## 會用到的概念頁

- [世界模型（World model）](../../zh/concepts/world-model.html)：核心定義。
- [基於模型的強化學習（Model-based reinforcement learning）](../../zh/concepts/model-based-reinforcement-learning.html)：世界模型所屬的方法家族；讀者需要先知道強化學習是什麼。
- [變分自編碼器（Variational autoencoder）](../../zh/concepts/variational-autoencoder.html)、[混合密度遞迴神經網路（Mixture density RNN）](../../zh/concepts/mixture-density-rnn.html)：World Models 的兩個部件。
- [在想像中學習（Learning in imagination）](../../zh/concepts/learning-in-imagination.html)、[潛在空間規劃（Latent space planning）](../../zh/concepts/latent-space-planning.html)：使用世界模型的兩種方式。
- [遞迴狀態空間模型（Recurrent state-space model）](../../zh/concepts/recurrent-state-space-model.html)：PlaNet 到 DreamerV3 共用的模型。
- [離線強化學習（Offline reinforcement learning）](../../zh/concepts/offline-reinforcement-learning.html)：Dreamer 4 的設定。
- [創作支援（Creativity support）](../../zh/concepts/creativity-support.html)、[動作條件（Action conditioning）](../../zh/concepts/action-conditioning.html)：WHAM 的用途與機制。

## 刻意不用

- 細部技術（類別潛在變數、KL 平衡、自由位元、symlog、shortcut forcing 等）：對沒聽過世界模型的讀者太細，只在需要時一句帶過，不另開頁。
