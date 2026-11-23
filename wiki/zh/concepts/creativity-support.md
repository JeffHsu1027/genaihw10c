---
title: "創作支援（Creativity support）"
aliases: [創作支援工具, 創作發想, 一致性 多樣性 持續性]
updated: 2026-11-24
areas: [game-ai]
sources: [2025-wham]
translated_from: "a560ecfce79b"
---

## 一句話定義

以「多能幫助人想出並修改點子」來設計與評估 AI 系統，而不是以它自己能完成多少任務來評估。

## 說明

創作工作通常在「打開許多選項」與「透過許多小調整收斂」之間來回。要支援這種工作，工具必須提供多樣的建議，讓它們與作品的規則和風格保持一致，並讓人能直接引導結果。被訓練成「從提示產生一個好答案」的生成模型，常常無法滿足這些需求。因此，以創作者實際的工作方式來評估模型，可能把模型發展導向和任務完成評測不同的方向。

> **解說（Explainer）：** 好的創作助手不像販賣機，只吐出一個成品；而像一起畫草圖的夥伴，提供各種粗略的變化，並保留你的修改。

## 各來源怎麼說

### World and Human Action Models towards gameplay ideation（2025）

[WHAM](../sources/2025-wham.md) 訪談了 27 位遊戲開發創作者，發現兩個需求：發散思考要與遊戲世界保持一致，以及對反覆修改過程的掌控 (p.2)。從中導出生成模型的三種能力：一致性、多樣性與持續性 (p.3)。它把每一項都變成可量測的標準：一致性用 Fréchet Video Distance，多樣性用與人類動作的 Wasserstein 距離，持續性則由人工標註插入的元素是否留存 (pp.4-5)。作者主張模型評估應由創作者的需求來引導，這與一般著重任務完成度的評估方式形成對比 (p.7)。

## 相關概念

- [世界模型（World model）](world-model.md)：WHAM 是以這些標準評估的生成模型。
- [自迴歸 transformer（Autoregressive transformer）](autoregressive-transformer.md)：逐個 token 生成讓修改成為可能。

## 背景資料

（尚無）

## 我的筆記
