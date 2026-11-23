---
title: "離線強化學習（Offline reinforcement learning）"
aliases: [offline RL, 批次強化學習, 從固定資料集學習]
updated: 2026-11-24
areas: [reinforcement-learning]
sources: [2025-dreamer4]
translated_from: "9dc549a10b17"
---

## 一句話定義

只從事先收集好的固定資料集做強化學習，學習期間不讓代理人與環境互動。

## 說明

線上強化學習靠實際嘗試來改進策略，這可能很慢、不安全，對真實機器人或其他昂貴的系統甚至不可行。離線強化學習則只從記錄下來的經驗學習，例如人類或早期代理人的錄影。困難在於代理人無法驗證資料中從未出現的動作會帶來什麼結果，因此天真的方法會對沒看過的動作過度自信。在資料集上訓練出的世界模型提供了一條出路：代理人可以在模型裡練習，產生新的經驗而不碰觸真實環境，同時保持接近資料中出現過的行為。

## 各來源怎麼說

### Training Agents Inside of Scalable World Models（2025）

[Dreamer 4](../sources/2025-dreamer4.md) 主張離線學習對實體機器人這類應用很重要，因為部署訓練到一半的策略並不安全，而重置場景與即時給予獎勵也很困難 (p.10)。它只從 VPT 承包商資料集的 2.5K 小時資料學習，完全不與環境互動 (p.10)。它的強化學習發生在世界模型內部，所以即使在想像中是 on-policy，仍算是離線方法 (p.11)。朝行為克隆策略的 KL 項讓學到的策略保持在合理行為的範圍內 (p.8)。Dreamer 4 是第一個完全只靠離線資料在 Minecraft 拿到鑽石的代理人 (p.1)。

## 相關概念

- [在想像中學習（Learning in imagination）](learning-in-imagination.md)：在世界模型裡練習，是 Dreamer 4 離線改進的方式。
- [基於模型的強化學習（Model-based reinforcement learning）](model-based-reinforcement-learning.md)：在這裡，學到的模型讓離線改進成為可能。
- [動作條件（Action conditioning）](action-conditioning.md)：世界模型必須學會資料中的動作如何改變世界。

## 背景資料

（尚無）

## 我的筆記
