---
title: "自由位元（Free bits）"
aliases: [free nats, 自由 nats, KL 截斷, KL 門檻]
updated: 2026-11-24
areas: [world-model]
sources: [2019-planet, 2020-dreamer, 2021-dreamerv2, 2023-dreamerv3]
translated_from: "6ee7439bd534"
---

## 一句話定義

訓練變分模型的一種技巧：KL 項已經低於某個小門檻時，就不再懲罰它。

## 說明

VAE 與遞迴狀態空間模型這類變分模型要兼顧兩個目標：把輸入描述或預測好，以及讓後驗與先驗之間的 KL 散度（KL divergence）保持很小。如果 KL 懲罰太強，尤其在訓練初期，模型可能乾脆不把資訊放進潛在狀態，這種失敗常稱為後驗崩塌（posterior collapse）。自由位元給模型一份額度：把 KL 項在門檻處截斷，低於門檻時沒有梯度，模型可以免費使用這麼多資訊。用自然對數計算時，門檻的單位是 nat，所以同一個想法也叫 free nats。

> **解說（Explainer）：** 就像手機方案裡的免費流量：在額度之內多用不用多付錢，所以沒有理由省著用。

## 各來源怎麼說

### Learning Latent Dynamics for Planning from Pixels（2019）

[PlaNet](../sources/2019-planet.md) 不調整 KL 項相對於重建項的權重，而是把 KL 損失在 3 個 free nats 以下截斷，等於免費給模型這麼多額度 (p.12)。

### Dream to Control: Learning Behaviors by Latent Imagination（2020）

[Dreamer](../sources/2020-dreamer.md) 同樣不縮放 KL 正則項，並比照 PlaNet 在 3 個 free nats 以下截斷 (p.14)。

### Mastering Atari with Discrete World Models（2021）

[DreamerV2](../sources/2021-dreamerv2.md) 拿掉 free nats，改用 KL 平衡：分別縮放 KL 損失中先驗與後驗的部分，讓模型學出準確的時間先驗 (p.18)。

### Mastering Diverse Domains through World Models（2023）

[DreamerV3](../sources/2023-dreamerv3.md) 以 free bits 的名稱重新採用這個想法：動態損失與表示損失都在 1 nat（約 1.44 bits）以下截斷，已經夠小時就關掉，讓學習集中在預測損失上 (p.5)。作者認為，把 free bits 和較小的表示損失結合，一組設定就能同時適用需要強正則化的視覺豐富環境，以及單一像素就很重要、需要弱正則化的遊戲 (p.5)。在消融實驗中，同時拿掉 KL 平衡與 free bits 是所有穩定技術中傷害最大的 (p.10)。

### 來源之間的比較

- [PlaNet](../sources/2019-planet.md) 在不縮放的 KL 項上給 3 個 free nats (p.12)，[Dreamer](../sources/2020-dreamer.md) 沿用這個設定 (p.14)。
- [DreamerV2](../sources/2021-dreamerv2.md) 用 KL 平衡取代 free nats (p.18)。
- [DreamerV3](../sources/2023-dreamerv3.md) 把兩者結合，兩個 KL 損失各自以 1 nat 為門檻 (p.5)。每篇都建立在前一篇之上；這段整理是本 Wiki 的。

## 相關概念

- [KL 平衡（KL balancing）](kl-balancing.md)：DreamerV2 用它取代 free nats，DreamerV3 則把兩者結合。
- [變分自編碼器（Variational autoencoder）](variational-autoencoder.md)：自由位元截斷的正是這類模型的 KL 項。
- [遞迴狀態空間模型（Recurrent state-space model）](recurrent-state-space-model.md)：PlaNet 與 Dreamer 系列代理人截斷其 KL 損失的序列潛在模型。

## 背景資料

- [Kingma et al., Improved Variational Inference with Inverse Autoregressive Flow (2016)](https://arxiv.org/abs/1606.04934)：提出用 free bits 訓練 VAE 的論文。

## 我的筆記
