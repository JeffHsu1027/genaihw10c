---
title: "世界模型（World model）"
aliases: [動態模型, 環境模型, dynamics model, environment model]
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
sources: [2018-world-models, 2019-planet, 2020-dreamer, 2021-dreamerv2, 2023-dreamerv3, 2025-dreamer4, 2025-wham]
translated_from: "cb6687c19531"
---

## 一句話定義

一個從經驗中學到的環境模型，用來預測接下來會發生什麼，通常以目前的狀態與動作為條件。

## 說明

能預測自己行動後果的代理人，不必在真實世界裡把每件事都試一遍。世界模型從經驗中學會這些預測，通常在壓縮過的潛在空間（latent space）中進行，而不是直接處理原始像素。它主要有兩種用法：當作特徵來源，概括現在並暗示未來；或當作模擬器，讓代理人在裡面練習。因為它是學出來的，永遠不會完美，依賴它的代理人可能被它的錯誤誤導。

> **解說（Explainer）：** 世界模型就像打擊者腦中的畫面：在眼睛跟上快速球之前，就先告訴他球會到哪裡。

## 各來源怎麼說

### World Models（2018）

[World Models](../sources/2018-world-models.md) 用兩個部分組成世界模型：壓縮每張畫面的 VAE，以及預測下一張壓縮畫面的 MDN-RNN (p.2, Fig. 4)。世界模型的訓練不使用獎勵，只有小型控制器看得到獎勵 (p.5)。這篇論文兩種用法都用上了：在 Car Racing 中，世界模型的隱藏狀態讓控制器對未來有所掌握 (p.5)；在 VizDoom 中，它在訓練時完全取代了真實遊戲 (p.7)。

### Learning Latent Dynamics for Planning from Pixels（2019）

[PlaNet](../sources/2019-planet.md) 把它的世界模型稱為潛在動態模型：由轉移模型、觀測模型、獎勵模型與編碼器組成，架構是遞迴狀態空間模型 (p.3)。因為模型也預測獎勵，規劃器可以完全在潛在空間中為動作序列評分，不必產生影像 (p.3)。模型的訓練資料是代理人持續用尚未訓練完的模型規劃所收集的，而不只是隨機資料 (p.3)。

### Dream to Control: Learning Behaviors by Latent Imagination（2020）

[Dreamer](../sources/2020-dreamer.md) 使用與 PlaNet 相同的世界模型，並把它描述為概括代理人的經驗，讓複雜的行為能從中學習 (p.1)。世界模型根據動作與過去的觀測預測獎勵，任何學習世界模型的目標函數都能與 Dreamer 搭配 (p.2)。論文比較三種學習目標：影像重建效果最好，對比式估計約能解決一半的任務，只預測獎勵則不夠 (p.8, Fig. 8)。

### Mastering Atari with Discrete World Models（2021）

[DreamerV2](../sources/2021-dreamerv2.md) 把世界模型描述為把代理人的經驗濃縮成一個預測模型，可以代替環境來學習行為 (p.2)。它的世界模型多了折扣預測器，讓想像軌跡能考慮回合結束，並使用類別潛在變數與 KL 平衡 (pp.3-4)。世界模型約有 2000 萬個參數 (p.4)，準確到只在其中學習的代理人就能在 Atari 上達到人類水準 (p.2)。世界模型依賴影像梯度：拿掉後表現崩潰，截斷獎勵梯度則影響不大 (p.9)。

### Mastering Diverse Domains through World Models（2023）

[DreamerV3](../sources/2023-dreamerv3.md) 把世界模型描述為賦予代理人豐富的感知與想像未來的能力，並指出穩健地學習與使用世界模型過去一直是未解的問題 (p.2)。它的表現主要來自世界模型的非監督重建損失，而不是獎勵與價值的梯度，作者認為這為在無標記資料上預訓練開了一扇門 (p.10)。從 1200 萬到 4 億個參數，較大的世界模型分數更高，需要的環境互動也更少 (p.10, Fig. 6)。

### Training Agents Inside of Scalable World Models（2025）

[Dreamer 4](../sources/2025-dreamer4.md) 把世界模型描述為從影片學習一般知識、並模擬經驗以便在想像中訓練行為 (p.1)。它認為早期的世界模型代理人只在範圍窄的環境中準確，而大型可控影片模型仍抓不準物體互動、速度也太慢 (p.2)。它的 transformer 世界模型有 2B 個參數，在一張 GPU 上即時執行 (p.9)。玩家在其中完成 16 個 Minecraft 任務中的 14 個，大型 Oasis 模型只有 5 個 (p.13)。它的記憶仍然很短，物品欄的預測也不精確 (p.18)。

### World and Human Action Models towards gameplay ideation（2025）

[WHAM](../sources/2025-wham.md) 把自己放在以遞迴網路、遞迴狀態空間模型與 transformer 捕捉環境動態的世界模型研究脈絡中 (p.3)。它從人類遊玩資料建模一款 3D 多人遊戲的動態，同時預測遊戲畫面與玩家的手把動作 (p.3)。它不是拿世界模型來訓練代理人，而是用來支援人類的創作發想，並以一致性、多樣性與使用者修改的持續性來評估 (p.3)。1.6B 模型能生成長達 2 分鐘、保持一致的遊玩過程 (p.4)。

### 來源之間的比較

- 兩篇都從像素學出壓縮的潛在狀態與其上的轉移模型：[World Models](../sources/2018-world-models.md) 用 VAE 加 MDN-RNN (p.2, Fig. 4)，[PlaNet](../sources/2019-planet.md) 用遞迴狀態空間模型 (p.4, Eq. 4)。
- [World Models](../sources/2018-world-models.md) 只用隨機策略的資料訓練一次模型，而且在 Car Racing 中模型完全看不到獎勵 (p.5)。
- [PlaNet](../sources/2019-planet.md) 讓模型預測獎勵，並持續用自己規劃收集的資料重新訓練模型 (p.3)。
- 兩篇都警告純確定性的模型容易被利用：[World Models](../sources/2018-world-models.md) 是被控制器利用 (p.9)，[PlaNet](../sources/2019-planet.md) 是被規劃器利用 (p.4, Fig. 2)。這是兩篇說法一致，不是衝突。
- [Dreamer](../sources/2020-dreamer.md) 保留 PlaNet 的世界模型，只改變從模型得出行為的方式，顯示同一個模型既能用於規劃，也能用於學習策略 (p.8)。
- [DreamerV2](../sources/2021-dreamerv2.md) 保留相同的整體設計，只改變潛在變數與 KL 項，就足以從簡單的控制任務進展到 Atari 上的人類水準 (p.2)。
- [DreamerV2](../sources/2021-dreamerv2.md) 與 [DreamerV3](../sources/2023-dreamerv3.md) 都認為世界模型主要的學習訊號是影像重建，而不是獎勵預測 (p.10)。
- [Dreamer 4](../sources/2025-dreamer4.md) 把從 PlaNet 到 DreamerV3 使用的遞迴世界模型換成 transformer，因為遞迴設計雖然有效率，卻很難擴展到多樣的資料 (p.29)。
- [WHAM](../sources/2025-wham.md) 是這裡唯一一個世界模型不給代理人用來行動的來源；它的模型服務的是探索遊戲點子的人 (p.3)。
- [Dreamer 4](../sources/2025-dreamer4.md) 與 [WHAM](../sources/2025-wham.md) 都是以人類遊玩資料訓練的大型 3D 遊戲 transformer 世界模型，一個在 Minecraft 中給代理人用，一個在 Bleeding Edge 中用於發想。兩篇互不引用；這個配對是本 Wiki 的觀察。
- PlaNet、Dreamer、DreamerV2、DreamerV3、Dreamer 4 與 WHAM 都引用了 World Models（見各自的來源頁）；這段並列比較是本 Wiki 的整理。

## 相關概念

- [變分自編碼器（Variational autoencoder）](variational-autoencoder.md)：為世界模型壓縮觀測。
- [混合密度遞迴神經網路（Mixture density RNN）](mixture-density-rnn.md)：以機率分布預測下一個狀態。
- [遞迴狀態空間模型（Recurrent state-space model）](recurrent-state-space-model.md)：同時具有確定性與隨機狀態的世界模型設計。
- [類別潛在變數（Categorical latents）](categorical-latents.md)：DreamerV2 世界模型使用的離散潛在狀態。
- [Shortcut forcing](shortcut-forcing.md)：Dreamer 4 的 transformer 世界模型所用的訓練目標。
- [動作條件（Action conditioning）](action-conditioning.md)：讓預測取決於代理人的動作。
- [自迴歸 transformer（Autoregressive transformer）](autoregressive-transformer.md)：WHAM 世界模型逐個 token 生成的架構。
- [創作支援（Creativity support）](creativity-support.md)：WHAM 用世界模型幫助人產生點子。
- [基於模型的強化學習（Model-based reinforcement learning）](model-based-reinforcement-learning.md)：使用世界模型的強化學習。
- [在想像中學習（Learning in imagination）](learning-in-imagination.md)：在世界模型裡訓練代理人。

## 背景資料

（尚無）

## 我的筆記
