---
title: "動作條件（Action conditioning）"
aliases: [以動作為條件的影片預測, 動作接地, 從無標註影片學習]
updated: 2026-11-24
areas: [world-model]
sources: [2025-dreamer4]
translated_from: "169b9daa687e"
---

## 一句話定義

讓世界模型的預測取決於所採取的動作，使得從同一個情境出發的不同動作，會導向相應不同的預測未來。

## 說明

沒有動作的影片模型只能預測接下來通常會發生什麼。要當作代理人的世界模型，它還必須預測未來如何隨代理人的選擇而改變。學這件事需要搭配產生該影片的動作，而這類資料遠比大量沒有標註的影片稀少。因此一個很有用的性質是：從無標註影片學到世界大部分的外觀與物理，只從少量有標註的資料學「動作與結果之間的關係」。

> **解說（Explainer）：** 就像大部分靠看別人玩來學一個遊戲，最後只需要拿手把玩一小段時間，就知道哪個按鈕做什麼。

## 各來源怎麼說

### Training Agents Inside of Scalable World Models（2025）

[Dreamer 4](../sources/2025-dreamer4.md) 把滑鼠、鍵盤等每個動作成分各自編碼成 token，影片沒有動作時只使用一個學到的嵌入，因此能混合使用有標註與無標註的影片 (p.5)。用 VPT 全部 2541 小時的影片訓練、但只有 100 小時附動作時，它達到全部附動作模型 85% 的 PSNR 與 100% 的 SSIM (p.14)。只提供 Overworld 的動作時，動作條件能轉移到只出現在無標註影片中的 Nether 與 End，達到 76% 的 PSNR 與 80% 的 SSIM (p.15)。作者的結論是，世界模型的知識大部分可以從無標註影片吸收，這指向從網路影片學習的方向 (p.14)。

## 相關概念

- [世界模型（World model）](world-model.md)：動作條件把影片模型變成世界模型。
- [Shortcut forcing](shortcut-forcing.md)：Dreamer 4 中以動作為條件的動態模型所用的訓練目標。
- [離線強化學習（Offline reinforcement learning）](offline-reinforcement-learning.md)：世界模型只用記錄下來的動作訓練。

## 背景資料

（尚無）

## 我的筆記
