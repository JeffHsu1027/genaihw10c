---
title: "世界模型（World models）"
area: world-model
updated: 2026-11-24
sources: [2018-world-models]
concepts: [world-model, variational-autoencoder, mixture-density-rnn, learning-in-imagination]
translated_from: "264d75e994ae"
---

## 概述

世界模型是學出來的模擬器：讓代理人能預測環境會如何回應自己的行動。相關研究關心的是：如何從原始觀測學到這樣的模型、如何用它來選擇動作或訓練策略，以及如何避免代理人利用模型的錯誤。這個主題頁逐篇整理這條研究脈絡。

## 發展脈絡

- 2018：[World Models](../sources/2018-world-models.md) 把代理人拆成大型非監督式世界模型與小型控制器，並證明完全在模型夢境中訓練的策略可以在真實遊戲中運作 (p.7)。

## 來源

| 年份 | 標題 | 狀態 | 一句話總結 |
|---|---|---|---|
| 2018 | [World Models](../sources/2018-world-models.md) | 已讀 | 由 VAE 加 MDN-RNN 組成的世界模型，搭配演化訓練的小型控制器；策略可以在模型的夢境中訓練。 |

## 關鍵概念

- [世界模型（World model）](../concepts/world-model.md)：預測環境如何變化的學習模型。
- [變分自編碼器（Variational autoencoder）](../concepts/variational-autoencoder.md)：把觀測壓縮成小的潛在向量。
- [混合密度遞迴神經網路（Mixture density RNN）](../concepts/mixture-density-rnn.md)：預測下一個潛在狀態的機率分布。
- [在想像中學習（Learning in imagination）](../concepts/learning-in-imagination.md)：用世界模型產生的經驗訓練策略。

## 術語表

- **潛在向量（latent vector）**：概括一次觀測的一小串數字。
- **Rollout**：代理人在環境中從一回合開始到結束的一次執行。
- **控制器／策略（controller / policy）**：代理人中負責選擇動作的部分。
- **基於模型的強化學習（model-based reinforcement learning）**：會學習或使用環境模型的強化學習。
- **模型被利用（model exploitation）**：代理人找到只因模型出錯才得高分的行為。
- **溫度（temperature）**：調整模型抽樣隨機程度的參數。

## 未解問題

- 在隨機策略無法涵蓋的環境中，代理人要如何充分探索來改進世界模型？[World Models](../sources/2018-world-models.md) 提出由好奇心驅動的迭代流程，但沒有實驗驗證 (pp.10-11)。
- 在想像中訓練的策略要如何避免利用模型的錯誤？[World Models](../sources/2018-world-models.md) 只用隨機模型與可調溫度部分解決了這個問題 (p.10)。

## 背景資料

（尚無）

## 我的筆記
