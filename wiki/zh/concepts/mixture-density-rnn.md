---
title: "混合密度遞迴神經網路（Mixture density RNN）"
aliases: [MDN-RNN, 混合密度網路, MDN]
updated: 2026-11-24
areas: [world-model]
sources: [2018-world-models]
translated_from: "2f7ae3a4e368"
---

## 一句話定義

一種遞迴神經網路，輸出層給出高斯混合分布的參數，因此預測的是下一個值的機率分布，而不是單一數值。

## 說明

遞迴網路帶著一個概括過去的隱藏狀態。混合密度輸出層把這個狀態轉成好幾個高斯成分的權重、平均值與變異數。從混合分布抽樣，可以從同樣的過去得到明顯不同的結果，這是單一高斯分布做不好的。溫度參數調整抽樣的隨機程度：溫度低時預測幾乎是決定性的，溫度高時結果更多樣。

## 各來源怎麼說

### World Models（2018）

[World Models](../sources/2018-world-models.md) 用輸出層為混合密度網路的 LSTM 當作 M 模型，根據目前的動作、潛在向量與隱藏狀態，預測下一個潛在向量的分布 (p.3)。混合分布適合處理離散的隨機事件，例如怪物要不要發射火球 (p.9)。實作上使用 5 個高斯混合成分，Car Racing 用 256 個隱藏單元、Doom 用 512 個，訓練 20 個 epoch (p.14)。在 Doom 中，模型也預測代理人是否死亡，機率超過 50% 時就結束這一回合 (p.14)。溫度非常低時，模型會塌縮到單一模態，怪物不再發射火球，夢境也就無法用來訓練 (p.9)。

## 相關概念

- [世界模型（World model）](world-model.md)：MDN-RNN 是世界模型中負責預測的一半。
- [變分自編碼器（Variational autoencoder）](variational-autoencoder.md)：定義了 MDN-RNN 要預測的潛在向量。
- [在想像中學習（Learning in imagination）](learning-in-imagination.md)：從 MDN-RNN 抽樣就能產生想像中的環境。

## 背景資料

（尚無）

## 我的筆記
