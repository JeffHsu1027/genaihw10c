---
title: "變分自編碼器（Variational autoencoder）"
aliases: [VAE, ConvVAE, 卷積變分自編碼器]
updated: 2026-11-24
areas: [world-model]
sources: [2018-world-models, 2019-planet, 2020-dreamer, 2021-dreamerv2]
translated_from: "c13bacbe1363"
---

## 一句話定義

一種神經網路，把輸入編碼成一個小而帶有隨機性的潛在向量，並學會把這個向量解碼回原本的輸入。

## 說明

編碼器輸出一個高斯分布的平均值與分散程度，從中抽樣出潛在向量，再由解碼器根據這個樣本重建輸入。訓練時要在重建品質與「讓潛在分布接近一個簡單的先驗分布」之間取得平衡。這個先驗限制了每個潛在向量能攜帶的資訊量，也讓潛在空間保持平滑，相近的向量會解碼出相似的輸入。

> **解說（Explainer）：** 可以把潛在向量想成一段對圖片的簡短描述，詳細到別人能照著它把圖重畫出來。

## 各來源怎麼說

### World Models（2018）

[World Models](../sources/2018-world-models.md) 用卷積 VAE 當作 V 模型，把每張畫面壓縮成潛在向量 z (p.3)。畫面先縮成 64x64 像素，再經過四層卷積層；Car Racing 的 z 是 32 維，Doom 是 64 維 (p.13)。VAE 以隨機策略收集的資料、用 L2 重建損失加上 KL 損失訓練一個 epoch (p.13)。作者指出，高斯先驗也讓世界模型對 M 產生的不合理潛在向量更穩健 (p.13)。因為 V 的訓練不看獎勵，它可能保留與任務無關的細節，卻漏掉有關的部分 (p.12)。

### Learning Latent Dynamics for Planning from Pixels（2019）

[PlaNet](../sources/2019-planet.md) 把它的遞迴狀態空間模型描述為一種序列 VAE 或非線性卡爾曼濾波器 (p.3)。它沿用 World Models 的卷積編碼器與反卷積解碼器 (p.12)，但編碼器是從整段觀測與動作的歷史推斷潛在狀態，而不是只看單張畫面 (p.3)。KL 項低於 3 個 free nats 時不予懲罰 (p.12)。

### Dream to Control: Learning Behaviors by Latent Imagination（2020）

[Dreamer](../sources/2020-dreamer.md) 以變分下界（ELBO），或更一般的變分資訊瓶頸，訓練世界模型，目標由影像與獎勵的重建項加上 KL 正則項組成 (p.6, Eq. 10)。它沿用 World Models 的卷積編碼器與解碼器 (p.14)。論文也把重建與一種不預測像素的對比式目標做比較，重建在多數任務上較好 (p.8, Fig. 8)。

### Mastering Atari with Discrete World Models（2021）

[DreamerV2](../sources/2021-dreamerv2.md) 指出它的世界模型損失是以動作為條件的隱藏馬可夫模型的 ELBO，因此世界模型可以看成序列 VAE：表示模型是後驗，轉移預測器是先驗 (p.4)。它把高斯潛在變數換成以 straight-through 梯度訓練的類別變數 (p.4)。它的 KL 平衡被描述為與 β-VAE 縮放 KL 項的做法不同、彼此獨立 (p.4)。

### 來源之間的比較

- [World Models](../sources/2018-world-models.md) 先單獨、逐張畫面訓練 VAE，再訓練動態模型；作者認為這比端到端訓練實際 (p.4)。
- [PlaNet](../sources/2019-planet.md) 用同一個變分目標一起訓練編碼器、解碼器與轉移模型 (p.4, Eq. 3)。

> **解說（Explainer）：** 一起訓練時，壓縮後的畫面描述不只要能把畫面畫回來，也要容易從前一步預測出來。

- [Dreamer](../sources/2020-dreamer.md) 保留 PlaNet 的聯合訓練，並直接比較出重建不是唯一的選擇，只是在它的實驗中最好的一種 (p.8, Fig. 8)。
- [DreamerV2](../sources/2021-dreamerv2.md) 保留變分的觀點，但改了其中兩部分：潛在變數的類型，以及 KL 項的權重方式 (p.4)。
- PlaNet 與 Dreamer 都沿用了 World Models 的網路（見各自的來源頁）；這段比較是本 Wiki 的整理。

## 相關概念

- [世界模型（World model）](world-model.md)：VAE 是世界模型中負責壓縮的一半。
- [混合密度遞迴神經網路（Mixture density RNN）](mixture-density-rnn.md)：預測由 VAE 定義的下一個潛在向量。
- [遞迴狀態空間模型（Recurrent state-space model）](recurrent-state-space-model.md)：把 VAE 的想法延伸到序列。
- [類別潛在變數（Categorical latents）](categorical-latents.md)：高斯潛在變數的離散替代方案。
- [KL 平衡（KL balancing）](kl-balancing.md)：改變 KL 項的訓練方式。

## 背景資料

（尚無）

## 我的筆記
