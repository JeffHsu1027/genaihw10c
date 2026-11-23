---
title: "World Models"
authors: "David Ha, Jürgen Schmidhuber"
year: 2018
venue: "arXiv:1803.10122"
url: "https://arxiv.org/abs/1803.10122"
raw: "raw/world modelv4.pdf"
pages: 21
added: 2026-11-24
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
status: read
concepts: [world-model, variational-autoencoder, mixture-density-rnn, evolution-strategies, learning-in-imagination, model-based-reinforcement-learning]
topics: [world-models]
translated_from: "30e74b928049"
---

## 一句話總結

把代理人（agent）拆成兩部分：一個大型的[世界模型](../concepts/world-model.md)，不靠獎勵就學會壓縮並預測自己看到的畫面；以及一個很小的控制器，根據世界模型提供的特徵行動。代理人甚至可以完全在世界模型自己產生的*夢境*裡訓練，再搬回真實環境使用 (p.1)。

## 研究問題

強化學習（reinforcement learning）代理人能不能把大部分容量放在一個大型、非監督式的世界模型上，只保留很小的策略，讓困難的功勞分配（credit assignment）問題在很小的搜尋空間裡解決 (p.2)？如果世界模型夠準確，能不能在訓練時取代真實環境 (p.6)？

## 方法

代理人有三個元件，靈感大致來自人類的知覺與記憶 (p.2, Fig. 4)：

- **V（視覺）**：用[變分自編碼器](../concepts/variational-autoencoder.md)把每一張畫面壓縮成一個小的潛在向量（latent vector）z (p.3)。畫面先縮成 64x64 的 RGB 影像，再經過四層卷積層編碼；Car Racing 的 z 是 32 維，Doom 是 64 維 (p.13)。
- **M（記憶）**：一個輸出層為混合密度網路的 LSTM，也就是 [MDN-RNN](../concepts/mixture-density-rnn.md)，以高斯混合分布預測下一個潛在向量的機率分布 `P(z[t+1] | a[t], z[t], h[t])` (p.3)。溫度參數 τ 控制抽樣出來的未來有多隨機 (p.3)。
- **C（控制器）**：單層線性模型，把潛在向量 z 與 RNN 的隱藏狀態 h 對應到動作 `a = Wc [z h] + bc` (p.3, Eq. 1)。它被刻意設計得很小，讓代理人幾乎所有的複雜度都放在 V 與 M (p.3)。

V 與 M 先用隨機策略收集的資料訓練，完全不使用獎勵訊號；只有 C 看得到獎勵 (p.5)。接著用 CMA-ES 最佳化 C；CMA-ES 是一種[演化策略](../concepts/evolution-strategies.md)，適合最多幾千個參數的解空間 (p.4)。V 與 M 分開訓練比端到端訓練實際，各自在單一 GPU 上不到一小時就訓練完成 (p.4)。

Car Racing 的流程是：收集 10,000 次隨機策略的 rollout，訓練 V、訓練 M、定義 C，再用 CMA-ES 求出 C 的權重 (p.5)。在 VizDoom: Take Cover 中，M 還要預測代理人下一格畫面會不會死亡，這讓 M 變成一個介面和真實遊戲相同的完整虛擬環境 (p.7)。C 只在這個虛擬環境裡訓練，之後再放到真實遊戲中執行 (p.7)；真實的 VizDoom 環境只用來收集隨機策略的資料 (p.15)。

> **解說（Explainer）：** V 是代理人的眼睛，M 是猜測接下來會發生什麼的記憶，C 則是根據眼睛看到的和記憶預期的立即反應。在 M 裡訓練 C，就像只在腦中排練一項運動，然後上場比真正的比賽。

附錄中的訓練細節：VAE 以 L2 重建損失加上 KL 損失訓練一個 epoch (p.13)；MDN-RNN 使用 5 個高斯混合成分，Car Racing 用 256 個隱藏單元、Doom 用 512 個，訓練 20 個 epoch (p.14)；CMA-ES 的族群大小為 64，每個候選解的適應度是它在 16 次 rollout 中的平均獎勵 (p.14)。

## 主要結果

- CarRacing-v0 的「解決」標準是連續 100 次試驗的平均獎勵達到 900 (p.4)。
- 同時使用 V 與 M 時，代理人在 100 次隨機試驗中得到 906 ± 21 分，是第一個被回報的解；先前的深度強化學習方法介於 591 到 652 分，排行榜最佳成績為 838 ± 11 (p.6, Table 1)。
- 只用 V 時，代理人在急彎會搖晃，得分 632 ± 251；在 C 加一層隱藏層後提高到 788 ± 141，仍不足以解決任務 (p.5)。
- 控制器只有 867 個參數，相較之下 VAE 有 4,348,547 個、MDN-RNN 有 422,368 個 (p.5)。
- VizDoom: Take Cover 的「解決」標準是 100 次 rollout 的平均存活時間超過 750 個時間步 (p.7)。
- 只在夢境中訓練的代理人，在夢裡大約存活 900 個時間步 (p.7)，搬到真實遊戲後大約存活 1100 個時間步 (p.8)。
- 溫度很重要：τ = 0.1 時夢境幾乎是決定性的，怪物不再發射火球，策略在夢裡得到 2086 ± 140，在真實環境卻只有 193 ± 58；最佳的轉移成績 1092 ± 556 出現在 τ = 1.15 (p.10, Table 2)。
- 當時 Gym 排行榜上 Take Cover 的最佳成績是 820 ± 58 (p.10)。

## 限制與未解問題

- 控制器會*作弊*：早期實驗中，它找到一種移動方式，讓夢裡的怪物永遠不發射火球，而這個漏洞在真實遊戲中並不存在 (p.8)。作者這樣描述這個弱點："it'll find a policy that looks good under our dynamics model, but will fail in the actual environment" (p.9)，也就是策略在模型裡看起來很好，到了真實環境就失敗。
- 隨機的 M 和較高的溫度 τ 能讓這類漏洞較難被利用，但隨機性太高會讓夢境難到學不到東西，所以 τ 需要調整 (p.10)。
- V 是單獨訓練且不看獎勵，因此可能把容量花在無關的細節上：它重現了 Doom 牆上的磚紋，卻漏掉 Car Racing 中與任務有關的路面磚塊 (p.12)。
- 以 LSTM 為基礎的世界模型容量有限，收集更多資料後可能發生災難性遺忘（catastrophic forgetting） (p.12)。
- 模型一次只模擬一個時間步的未來，沒有階層式規劃或抽象推理 (p.13)。
- 兩個任務都夠簡單，用隨機策略資料訓練的世界模型就足夠；更困難的環境需要交替進行探索與模型訓練的迭代流程，可能由好奇心驅動，論文提出了這個構想但沒有實驗 (pp.10-11)。

## 相關概念

- [世界模型](../concepts/world-model.md)：本篇的 V 與 M 合起來。
- [變分自編碼器](../concepts/variational-autoencoder.md)：V 元件。
- [混合密度遞迴神經網路](../concepts/mixture-density-rnn.md)：M 元件。
- [演化策略](../concepts/evolution-strategies.md)：訓練 C 的方法（CMA-ES）。
- [在想像中學習](../concepts/learning-in-imagination.md)：在夢境中訓練 C。
- [基於模型的強化學習](../concepts/model-based-reinforcement-learning.md)：本篇所屬的更大研究方向。

## 與其他來源的關係

- [Learning Latent Dynamics for Planning from Pixels](2019-planet.md)（PlaNet，2019）引用本篇、沿用本篇的卷積編碼器與解碼器，並把本篇列為從想像經驗學習策略的混合式代理人。PlaNet 不在夢境中訓練控制器，而是每一步都用學到的模型規劃。David Ha 是兩篇論文的共同作者。
- [Dream to Control: Learning Behaviors by Latent Imagination](2020-dreamer.md)（Dreamer，2020）也引用本篇，把本篇描述為在想像中演化出線性控制器，並沿用本篇的卷積編碼器與解碼器。Dreamer 和本篇一樣在學到的模型裡訓練行為，但改用梯度與價值模型，而不是演化策略。
- [Training Agents Inside of Scalable World Models](2025-dreamer4.md)（Dreamer 4，2025）把本篇列為最早準確到能從像素規劃的世界模型之一。和本篇的 VizDoom 代理人一樣，Dreamer 4 訓練策略時不碰真實遊戲，但用的是大型人類資料集，而不是隨機遊玩。
- [World and Human Action Models towards gameplay ideation](2025-wham.md)（WHAM，2025）在世界模型相關研究脈絡的開頭引用本篇。它同樣學習遊戲的生成模型，但用來支援人類遊戲設計師，而不是訓練代理人。

## 背景資料

- [論文的互動版本](https://worldmodels.github.io)：作者製作的網頁版，可以直接操作 VAE 與夢境環境的示範。

## 我的筆記
