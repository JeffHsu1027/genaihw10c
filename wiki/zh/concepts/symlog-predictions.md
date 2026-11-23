---
title: "Symlog 預測（Symlog predictions）"
aliases: [symlog, symexp, symlog 平方誤差, symexp twohot 損失, twohot 編碼]
updated: 2026-11-24
areas: [reinforcement-learning, world-model]
sources: [2023-dreamerv3]
translated_from: "cb3d7960804f"
---

## 一句話定義

預測量級未知的數值的一種方法：讓網路學習目標值經過類似對數壓縮後的版本，或改成在指數間隔的分箱上做分類，而不是直接學原始數值。

## 說明

獎勵、價值與觀測在某個環境可能很小，在另一個環境卻很大。對原始目標用平方損失，遇到大數值可能發散；用絕對值或 Huber 損失又學得很慢；用移動統計量正規化，則會讓目標不斷變動。Symlog 函數會壓縮很大的正值與負值，但在零附近幾乎等於恆等函數；它的反函數 symexp 再把預測轉回原本的尺度。對帶有雜訊的目標，網路也可以改為輸出在 symlog 空間等距分箱上的機率，並以 twohot 目標（把目標值分攤到最近的兩個分箱）做分類訓練；這樣梯度就不會隨目標值變大而變大。

> **解說（Explainer）：** 就像改用對數刻度的尺來量東西：硬幣和大樓都能用同一把尺讀出來。

## 各來源怎麼說

### Mastering Diverse Domains through World Models（2023）

[DreamerV3](../sources/2023-dreamerv3.md) 提出 symlog 平方誤差與 symexp twohot 損失，作為處理未知量級目標的簡單解法 (p.7)。它對編碼器與解碼器的向量觀測使用 symlog，並在獎勵預測器與 critic 使用 symexp twohot 損失 (p.7)。分箱涵蓋從負 20 到正 20 的 symexp 範圍，twohot 輸出頭的權重初始化為零，讓代理人在一開始不會幻想出獎勵與價值 (p.18)。消融實驗中，拿掉 symexp twohot 損失改用 Huber 損失會讓平均表現變差，拿掉觀測的 symlog 也會變差 (p.10, Fig. 6)。

## 相關概念

- [報酬正規化（Return normalization）](return-normalization.md)：DreamerV3 處理獎勵尺度的另一項技術。
- [Actor-critic（演員－評論家）](actor-critic.md)：critic 以 symexp twohot 損失訓練。
- [世界模型（World model）](world-model.md)：它的獎勵預測器與向量解碼器使用 symlog。

## 背景資料

（尚無）

## 我的筆記
