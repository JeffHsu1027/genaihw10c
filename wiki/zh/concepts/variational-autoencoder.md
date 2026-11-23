---
title: "變分自編碼器（Variational autoencoder）"
aliases: [VAE, ConvVAE, 卷積變分自編碼器]
updated: 2026-11-24
areas: [world-model]
sources: [2018-world-models]
translated_from: "714a8c9c10c4"
---

## 一句話定義

一種神經網路，把輸入編碼成一個小而帶有隨機性的潛在向量，並學會把這個向量解碼回原本的輸入。

## 說明

編碼器輸出一個高斯分布的平均值與分散程度，從中抽樣出潛在向量，再由解碼器根據這個樣本重建輸入。訓練時要在重建品質與「讓潛在分布接近一個簡單的先驗分布」之間取得平衡。這個先驗限制了每個潛在向量能攜帶的資訊量，也讓潛在空間保持平滑，相近的向量會解碼出相似的輸入。

> **解說（Explainer）：** 可以把潛在向量想成一段對圖片的簡短描述，詳細到別人能照著它把圖重畫出來。

## 各來源怎麼說

### World Models（2018）

[World Models](../sources/2018-world-models.md) 用卷積 VAE 當作 V 模型，把每張畫面壓縮成潛在向量 z (p.3)。畫面先縮成 64x64 像素，再經過四層卷積層；Car Racing 的 z 是 32 維，Doom 是 64 維 (p.13)。VAE 以隨機策略收集的資料、用 L2 重建損失加上 KL 損失訓練一個 epoch (p.13)。作者指出，高斯先驗也讓世界模型對 M 產生的不合理潛在向量更穩健 (p.13)。因為 V 的訓練不看獎勵，它可能保留與任務無關的細節，卻漏掉有關的部分 (p.12)。

## 相關概念

- [世界模型（World model）](world-model.md)：VAE 是世界模型中負責壓縮的一半。
- [混合密度遞迴神經網路（Mixture density RNN）](mixture-density-rnn.md)：預測由 VAE 定義的下一個潛在向量。

## 背景資料

（尚無）

## 我的筆記
