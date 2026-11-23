---
title: "基於模型的強化學習（Model-based reinforcement learning）"
aliases: [model-based RL, MBRL, 模型式強化學習]
updated: 2026-11-24
areas: [reinforcement-learning, world-model]
sources: [2018-world-models, 2019-planet, 2020-dreamer, 2021-dreamerv2, 2023-dreamerv3, 2025-dreamer4]
translated_from: "3ff9aa86063f"
---

## 一句話定義

會學習或使用「環境如何回應動作」的模型，並用這個模型來決定如何行動或學習如何行動的強化學習。

## 說明

在強化學習（reinforcement learning）中，代理人（agent）在環境裡行動、得到獎勵（reward），並透過試誤學出一套策略（policy），也就是選擇動作的規則，讓長期累積的獎勵越多越好。無模型（model-free）方法直接從試誤中學習策略或價值函數。基於模型的方法先學一個動態模型，再加以利用：在做決定的當下拿來規劃，或拿來產生額外的經驗訓練策略。好的模型能讓學習大幅提高資料效率，也可能轉移到同一環境中的新任務。不過模型的錯誤可能誤導代理人，而從影像學到準確的模型並不容易。

## 各來源怎麼說

### World Models（2018）

[World Models](../sources/2018-world-models.md) 不使用獎勵學習世界模型，再訓練一個利用模型的小型控制器：先把模型當作特徵來源 (p.5)，接著完全取代真實環境 (p.7)。論文把自己定位為簡化版的示範，展示 1990 到 2015 年間一系列論文中「以 RNN 為基礎的世界模型加控制器」的想法 (p.2)。

### Learning Latent Dynamics for Planning from Pixels（2019）

[PlaNet](../sources/2019-planet.md) 是純粹基於模型的代理人：沒有策略網路或價值網路，每個動作都靠學到的模型規劃 (p.3)。論文列出用學習模型規劃預期的好處：更豐富的訓練訊號、不需透過 Bellman 備份傳遞獎勵、增加搜尋計算就能提升表現，以及動態模型可轉移到其他任務 (p.1)。它以平均約少 200 倍的回合，達到強大無模型代理人的表現 (p.2)。

### Dream to Control: Learning Behaviors by Latent Imagination（2020）

[Dreamer](../sources/2020-dreamer.md) 採用動態學習、行為學習與環境互動這套經典的代理人結構，而行為是在世界模型的潛在空間中學習 (p.2)。它主張世界模型能在過去經驗之間內插，並提供多步報酬的解析梯度，這是線上或用經驗回放訓練的無模型 actor-critic 做不到的 (p.1)。它用 500 萬環境步，就超越無模型的 D4PG 在 1 億步後的最終表現 (p.6, Fig. 6)。

### Mastering Atari with Discrete World Models（2021）

[DreamerV2](../sources/2021-dreamerv2.md) 指出 Atari 向來需要無模型演算法才能達到人類水準，過去的 Atari 世界模型都沒有競爭力 (p.2)。它與兩個基於模型的 Atari 代理人比較：在像素空間預測畫面再用來訓練 PPO 的 SimPLe，以及學習任務專屬的獎勵與價值預測、用於樹搜尋而不建模影像的 MuZero (pp.10-11, Table 3)。MuZero 很強，但用一張 GPU 訓練一個 Atari 代理人需要超過 2 個月，DreamerV2 只需 10 天 (p.11)。作者把 DreamerV2 視為基於模型的強化學習能在最具競爭性的評測上勝過頂尖無模型演算法的證明 (p.11)。

### Mastering Diverse Domains through World Models（2023）

[DreamerV3](../sources/2023-dreamerv3.md) 把自己定位為通用演算法，並與 PPO（穩健但很耗資料）以及 MuZero（強大但複雜且未公開）比較 (p.11)。它在所有測試領域都勝過 PPO，並以一小部分的計算量在 Atari 上勝過 MuZero (p.8)。在 Minecraft 中，它用 1 張 GPU 跑 9 天就從零開始挖到鑽石；VPT 則需要人類示範資料與 720 張 GPU 跑 9 天 (p.11)。

### Training Agents Inside of Scalable World Models（2025）

[Dreamer 4](../sources/2025-dreamer4.md) 主張世界模型原則上可以從固定資料集學習，讓代理人完全在想像中訓練、不需要線上互動 (p.2)。在離線的 Minecraft 設定中，它以少 100 倍的資料勝過 VPT 的離線代理人，也勝過從 Gemma 3 微調的 VLA 代理人 (p.9, Fig. 3)。在世界模型的表示上做行為克隆也勝過在 Gemma 3 上做，顯示影片預測學到了對決策有用的世界理解 (p.12)。

### 來源之間的比較

- [World Models](../sources/2018-world-models.md) 事先用模型訓練策略；做決定時，控制器根據模型的隱藏狀態直接反應，不往前規劃 (p.6)。
- [PlaNet](../sources/2019-planet.md) 沒有策略，只在做決定的當下用模型搜尋動作序列 (p.3)。
- 兩篇都警告純確定性的模型容易被利用：[World Models](../sources/2018-world-models.md) 是被控制器利用 (p.9)，[PlaNet](../sources/2019-planet.md) 是被規劃器利用 (p.4, Fig. 2)。
- [Dreamer](../sources/2020-dreamer.md) 回到像 World Models 一樣事先訓練策略，但改用梯度而非演化，並加上能看見想像視野之外的價值模型 (p.5)。
- Dreamer 指出像 PlaNet 那樣只在固定視野內規劃，在需要長期功勞分配的任務上很短視 (p.7, Fig. 7)。PlaNet 自己也把缺少價值函數列為限制（見 PlaNet 頁），所以這是說法一致，不是衝突。
- [DreamerV2](../sources/2021-dreamerv2.md) 保留 Dreamer 在想像中學習策略的方式，並證明它能在先前來源未達到的 Atari 上勝出 (p.2)。
- [DreamerV3](../sources/2023-dreamerv3.md) 把主張從「在單一評測上勝過無模型方法」轉為「不必重新調整就能在許多領域運作」(p.2)。
- [Dreamer 4](../sources/2025-dreamer4.md) 從線上學習轉為完全離線學習，模型成了代理人唯一能練習的地方 (p.10)。
- PlaNet、Dreamer、DreamerV2、DreamerV3 與 Dreamer 4 都引用 World Models，每一篇也都建立在前一篇之上；這段並列比較是本 Wiki 的整理。

## 相關概念

- [世界模型（World model）](world-model.md)：基於模型的方法所學的模型。
- [潛在空間規劃（Latent space planning）](latent-space-planning.md)：在做決定時使用模型。
- [在想像中學習（Learning in imagination）](learning-in-imagination.md)：用模型訓練策略。
- [離線強化學習（Offline reinforcement learning）](offline-reinforcement-learning.md)：像 Dreamer 4 一樣，不與環境互動地學習。
- [Actor-critic（演員－評論家）](actor-critic.md)：Dreamer 系列代理人在世界模型裡訓練的策略學習方法。

## 背景資料

（尚無）

## 我的筆記
