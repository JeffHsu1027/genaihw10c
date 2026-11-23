---
title: "遞迴狀態空間模型（Recurrent state-space model）"
aliases: [RSSM]
updated: 2026-11-24
areas: [world-model]
sources: [2019-planet]
translated_from: "e40e4bf611b6"
---

## 一句話定義

一種潛在動態模型，狀態分成兩部分：由遞迴網路往前傳遞的確定性部分，以及每一步抽樣的隨機部分。

## 說明

純確定性的遞迴模型記憶力好，但只能預測單一的未來。純隨機的狀態空間模型能表達不確定性，卻難以在多個時間步之間保留資訊。兩者結合後，確定性路徑負責記憶，隨機路徑表達下一個狀態中不確定的部分。這類模型通常像序列版的變分自編碼器一樣訓練，用編碼器從觀測推斷潛在狀態。

> **解說（Explainer）：** 確定性部分像一本忠實記下已發生事情的日記；隨機部分則是對接下來可能發生什麼的猜測。

## 各來源怎麼說

### Learning Latent Dynamics for Planning from Pixels（2019）

[PlaNet](../sources/2019-planet.md) 提出 RSSM：RNN 根據前一步的確定性狀態、隨機狀態與動作更新確定性狀態，隨機狀態則在給定確定性狀態下從高斯分布抽樣，觀測與獎勵由兩者共同預測 (p.4, Eq. 4)。關於觀測的所有資訊都必須經過編碼器的抽樣步驟，以避免從輸入到重建出現確定性的捷徑 (p.4)。實驗中，兩條路徑在每個任務上都需要，而沒有隨機部分時代理人完全學不起來 (p.6, Fig. 4)。實作使用 200 個單元的 GRU 與 30 維的隨機狀態 (p.12)。與純隨機模型不同，RSSM 對使用 ReLU 或 ELU 激活函數並不敏感 (p.15, Fig. 9)。

## 相關概念

- [世界模型（World model）](world-model.md)：RSSM 是世界模型的一種設計。
- [變分自編碼器（Variational autoencoder）](variational-autoencoder.md)：RSSM 以序列 VAE 的方式訓練。
- [潛在超前預測（Latent overshooting）](latent-overshooting.md)：用多步預測訓練這類模型的額外目標。
- [混合密度遞迴神經網路（Mixture density RNN）](mixture-density-rnn.md)：另一種讓遞迴模型帶有隨機性的方法；它對輸出抽樣，RSSM 則對狀態的一部分抽樣。

## 背景資料

（尚無）

## 我的筆記
