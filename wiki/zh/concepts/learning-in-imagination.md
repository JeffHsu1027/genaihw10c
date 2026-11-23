---
title: "在想像中學習（Learning in imagination）"
aliases: [夢境訓練, 在夢裡學習, 幻覺環境, 潛在想像, latent imagination]
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
sources: [2018-world-models, 2020-dreamer, 2021-dreamerv2]
translated_from: "3f8d8dac63d8"
---

## 一句話定義

用學到的世界模型所產生的經驗來訓練代理人的策略，而不是用真實環境產生的經驗。

## 說明

如果世界模型能預測觀測、獎勵以及一回合何時結束，它就能代替環境。代理人在這個想像的環境裡練習，成本可能比真實環境低、速度也更快，學到的策略再搬回現實使用。主要風險是模型被利用（model exploitation）：代理人可能找到只因為模型出錯才得高分的行為，而這種行為在真實環境中會失敗。讓想像的環境帶有更多不確定性，是讓這類漏洞較難被利用的方法之一。

> **解說（Explainer）：** 在腦中練習只有在想像夠真實時才有用；太寬容的夢境只會養成壞習慣。

## 各來源怎麼說

### World Models（2018）

[World Models](../sources/2018-world-models.md) 讓 MDN-RNN 預測代理人是否死亡，把它包裝成虛擬環境，完全在裡面訓練控制器，再放到 VizDoom 執行 (p.7)。代理人在夢裡大約存活 900 個時間步 (p.7)，在真實遊戲中大約存活 1100 個 (p.8)。在潛在空間中訓練比較便宜，因為不需要渲染畫面，也不必執行遊戲引擎 (p.15)。早期代理人學會利用模型的漏洞，讓怪物永遠不發射火球 (p.8)。溫度 τ 在真實度與可被利用程度之間取捨，最佳的轉移成績 1092 ± 556 出現在 τ = 1.15 (p.10, Table 2)。

### Dream to Control: Learning Behaviors by Latent Imagination（2020）

[Dreamer](../sources/2020-dreamer.md) 完全靠潛在想像學習行為：想像軌跡從真實過去序列的狀態出發，由世界模型與策略往前推演，不產生影像 (p.3)。動作模型與價值模型在這些軌跡上訓練，動作模型則用穿過想像動態的解析梯度改進 (p.5)。因為潛在狀態很小，可以平行想像數千條軌跡 (p.2)。學習行為時，世界模型保持固定 (p.5)。

### Mastering Atari with Discrete World Models（2021）

[DreamerV2](../sources/2021-dreamerv2.md) 完全在另外訓練的世界模型裡學習行為，並藉此在 Atari 上達到人類水準 (p.2)。因為學習行為時不預測影像，它能在一張 GPU 上平行模擬 2500 條潛在軌跡 (p.4)。在 2 億環境步中，策略從 4680 億個想像狀態學習，約為真實輸入的 10,000 倍 (p.6)。作者把這次成功視為世界模型準確表示環境的證據 (p.2)。

### 來源之間的比較

- [World Models](../sources/2018-world-models.md) 在想像中用 CMA-ES 訓練控制器，只需要每次 rollout 的最終獎勵 (p.12)。
- [Dreamer](../sources/2020-dreamer.md) 則把價值梯度穿過想像軌跡反向傳播，並把 World Models 描述為在想像中演化線性控制器 (p.7)。
- 在 [World Models](../sources/2018-world-models.md) 中，代理人只在一個由隨機策略資料建成的夢境裡訓練一次，然後部署 (p.7)。
- [Dreamer](../sources/2020-dreamer.md) 則持續交替：在想像中訓練行為，以及在真實環境中行動、擴充用來訓練世界模型的資料 (p.2)。
- [DreamerV2](../sources/2021-dreamerv2.md) 顯示只在想像中學習，也能在過去世界模型沒有競爭力的 Atari 上達到人類水準 (p.2)。
- 只有 World Models 明確討論模型被利用的問題；Dreamer 與 DreamerV2 都沒有回報類似的失敗。這個差異是本 Wiki 的觀察，不是任何一篇論文的主張。

## 相關概念

- [世界模型（World model）](world-model.md)：產生想像經驗的模型。
- [混合密度遞迴神經網路（Mixture density RNN）](mixture-density-rnn.md)：它的抽樣溫度決定想像環境有多不確定。
- [演化策略（Evolution strategies）](evolution-strategies.md)：World Models 在夢境中訓練控制器的最佳化方法。
- [Actor-critic（演員－評論家）](actor-critic.md)：Dreamer 在想像中學習所用的方法。
- [潛在空間規劃（Latent space planning）](latent-space-planning.md)：在做決定時使用模型、而不訓練策略的另一種做法。

## 背景資料

（尚無）

## 我的筆記
