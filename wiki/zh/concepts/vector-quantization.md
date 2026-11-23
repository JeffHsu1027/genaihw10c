---
title: "向量量化（Vector quantization）"
aliases: [VQGAN, VQ-VAE, ViT-VQGAN, 離散影像 token, 影像 tokenizer]
updated: 2026-11-24
areas: [world-model]
sources: [2025-wham]
translated_from: "5b2668568c4c"
---

## 一句話定義

把影像等輸入壓縮成一小串「學到的碼本（codebook）中的條目」，讓它能以離散 token 表示。

## 說明

編碼器把輸入轉成一格格的向量，每個向量再換成碼本中最接近的條目，該條目的索引就成為一個 token。解碼器則學習從 token 重建輸入。VQGAN 類的模型再加上感知損失與對抗損失，讓重建的影像更清晰。結果是影像可以像句子中的字詞一樣處理，容易與其他離散資料結合，也能用處理文字的同一類序列模型來建模。每張影像用多少 token，是在重建品質與序列長度、速度之間的取捨。

## 各來源怎麼說

### World and Human Action Models towards gameplay ideation（2025）

[WHAM](../sources/2025-wham.md) 把遊玩過程視為離散 token 的序列，並用 VQGAN 影像編碼器把每格畫面轉成 token (p.3)。較小的模型使用約 60M 參數的 VQGAN，把 128 乘 128 的影像對應到詞彙量 4,096 中的 256 個 token (p.10)。1.6B 模型使用約 300M 參數的 ViT-VQGAN，把 300 乘 180 的影像對應到詞彙量 16,384 中的 540 個 token (p.10)。每張影像的 token 數是關鍵超參數，在影像品質與生成速度、脈絡長度之間取捨 (p.3)。較高解析度的 tokenizer 提高了重建品質的上限，也改善了 FVD (p.4)。

## 相關概念

- [自迴歸 transformer（Autoregressive transformer）](autoregressive-transformer.md)：為量化器產生的 token 序列建模。
- [變分自編碼器（Variational autoencoder）](variational-autoencoder.md)：相關的自編碼器，但潛在變數是連續的，而非離散的。
- [類別潛在變數（Categorical latents）](categorical-latents.md)：另一種離散表示，是在世界模型內部抽樣，而不是從碼本查表。

## 背景資料

（尚無）

## 我的筆記
