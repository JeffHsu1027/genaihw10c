---
title: "遞迴狀態空間模型（Recurrent state-space model）"
aliases: [RSSM]
updated: 2026-11-24
areas: [world-model]
sources: [2019-planet, 2020-dreamer, 2021-dreamerv2, 2023-dreamerv3]
translated_from: "ab266a73e7a5"
---

## 一句話定義

一種潛在動態模型，狀態分成兩部分：由遞迴網路往前傳遞的確定性部分，以及每一步抽樣的隨機部分。

## 說明

純確定性的遞迴模型記憶力好，但只能預測單一的未來。純隨機的狀態空間模型能表達不確定性，卻難以在多個時間步之間保留資訊。兩者結合後，確定性路徑負責記憶，隨機路徑表達下一個狀態中不確定的部分。這類模型通常像序列版的變分自編碼器一樣訓練，用編碼器從觀測推斷潛在狀態。

> **解說（Explainer）：** 確定性部分像一本忠實記下已發生事情的日記；隨機部分則是對接下來可能發生什麼的猜測。

## 各來源怎麼說

### Learning Latent Dynamics for Planning from Pixels（2019）

[PlaNet](../sources/2019-planet.md) 提出 RSSM：RNN 根據前一步的確定性狀態、隨機狀態與動作更新確定性狀態，隨機狀態則在給定確定性狀態下從高斯分布抽樣，觀測與獎勵由兩者共同預測 (p.4, Eq. 4)。關於觀測的所有資訊都必須經過編碼器的抽樣步驟，以避免從輸入到重建出現確定性的捷徑 (p.4)。實驗中，兩條路徑在每個任務上都需要，而沒有隨機部分時代理人完全學不起來 (p.6, Fig. 4)。實作使用 200 個單元的 GRU 與 30 維的隨機狀態 (p.12)。與純隨機模型不同，RSSM 對使用 ReLU 或 ELU 激活函數並不敏感 (p.15, Fig. 9)。

### Dream to Control: Learning Behaviors by Latent Imagination（2020）

[Dreamer](../sources/2020-dreamer.md) 以 PlaNet 的 RSSM 作為轉移模型，並把 RSSM 與作用在影像上的 CNN 結合成表示模型 (p.6)。它的潛在分布與 PlaNet 相同，是 30 維的對角高斯分布 (p.14)。在五張脈絡畫面之後只給動作，RSSM 往後預測 45 步仍夠準確，足以讓 Dreamer 在潛在空間中學習行為 (p.5, Fig. 5)。

### Mastering Atari with Discrete World Models（2021）

[DreamerV2](../sources/2021-dreamerv2.md) 保留 RSSM 的結構：GRU 計算確定性的遞迴狀態，後驗隨機狀態看得到目前的影像，先驗隨機狀態則在看不到影像時預測它 (pp.2-3)。不過隨機狀態改成 32 個各有 32 類的類別變數向量，不再是高斯分布 (p.3, Fig. 2)。RSSM 使用 600 個單元 (p.19)，在它的 GRU 中加入層正規化幾乎沒有幫助 (p.18)。

### Mastering Diverse Domains through World Models（2023）

[DreamerV3](../sources/2023-dreamerv3.md) 仍以 RSSM 實作世界模型，包含序列模型、編碼器、動態預測器，以及獎勵、是否繼續與重建的輸出頭 (pp.3-4)。序列模型是遞迴權重為 8 個區塊對角的 GRU，能有大量記憶單元而參數不會呈平方成長 (p.18)。給定 5 張脈絡畫面與動作後，模型能在 DMLab 與機器人場景中往後預測 45 格畫面 (p.4, Fig. 4)，在 Minecraft 中也一樣 (p.23, Fig. 7)。

### 來源之間的比較

- [PlaNet](../sources/2019-planet.md) 提出 RSSM 並用於規劃 (p.4)。
- [Dreamer](../sources/2020-dreamer.md) 原封不動地沿用它來學習策略 (p.6)。因此同一個模型支援兩種不同的動作選擇方式；Dreamer 直接建立在 PlaNet 之上，這段整理是本 Wiki 的。
- [DreamerV2](../sources/2021-dreamerv2.md) 保留確定性與隨機兩條路徑，但把高斯隨機狀態換成類別變數，在多數 Atari 遊戲上有幫助 (p.9)。
- [DreamerV3](../sources/2023-dreamerv3.md) 在 150 多個任務上保留這個結構，主要只改了遞迴單元與訓練損失 (p.18)。

## 相關概念

- [世界模型（World model）](world-model.md)：RSSM 是世界模型的一種設計。
- [變分自編碼器（Variational autoencoder）](variational-autoencoder.md)：RSSM 以序列 VAE 的方式訓練。
- [潛在超前預測（Latent overshooting）](latent-overshooting.md)：用多步預測訓練這類模型的額外目標。
- [混合密度遞迴神經網路（Mixture density RNN）](mixture-density-rnn.md)：另一種讓遞迴模型帶有隨機性的方法；它對輸出抽樣，RSSM 則對狀態的一部分抽樣。
- [類別潛在變數（Categorical latents）](categorical-latents.md)：DreamerV2 使用的離散隨機狀態。
- [KL 平衡（KL balancing）](kl-balancing.md)：訓練 RSSM 先驗的一種方式。

## 背景資料

（尚無）

## 我的筆記
