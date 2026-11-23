---
title: "Training Agents Inside of Scalable World Models"
authors: "Danijar Hafner, Wilson Yan, Timothy Lillicrap"
year: 2025
venue: "arXiv:2509.24527"
url: "https://arxiv.org/abs/2509.24527"
raw: "raw/(dreamerv4)Training Agents Inside of Scalable World Modelsv1.pdf"
pages: 32
added: 2026-11-24
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
status: to-read
concepts: [shortcut-forcing, offline-reinforcement-learning, action-conditioning, world-model, learning-in-imagination, actor-critic, recurrent-state-space-model, symlog-predictions, return-normalization, model-based-reinforcement-learning]
topics: [world-models]
translated_from: "ff36faf3f3ee"
---

## 一句話總結

Dreamer 4 把早期 Dreamer 的遞迴世界模型換成以 [shortcut forcing](../concepts/shortcut-forcing.md) 訓練、可擴展的 transformer 世界模型，並成為第一個完全只靠離線資料、透過[在世界模型裡做強化學習](../concepts/learning-in-imagination.md)、不與環境互動就在 Minecraft 拿到鑽石的代理人 (p.1)。

## 研究問題

DreamerV3 這類早期的世界模型代理人在範圍窄的環境中又快又準，卻無法擬合複雜多樣的資料；大型可控影片模型能處理多樣的場景，卻仍抓不準物體互動，而且要很多張 GPU 才能即時執行 (p.2)。有沒有一個世界模型既夠準又夠快，能只靠固定的[離線](../concepts/offline-reinforcement-learning.md)資料集，在想像中訓練出有能力的代理人 (p.2)？

## 方法

- **三個階段**：先在影片（以及可有可無的動作）上預訓練 tokenizer 與動態模型；再加入任務輸入微調世界模型，讓它預測動作與獎勵；最後以想像訓練改進策略 (p.4)。
- **因果 tokenizer**：transformer 編碼器與解碼器把每張畫面壓縮成連續的表示，中間經過一個帶 tanh 激活的低維瓶頸，並以遮罩自編碼（masked autoencoding）、均方誤差加上感知損失訓練 (p.5)。
- **互動式動態模型**：transformer 從交錯排列的動作與加了雜訊的表示預測下一步的表示，使用 [shortcut forcing](../concepts/shortcut-forcing.md)，因此每張畫面只需要 4 次前向計算 (p.5)。網路直接預測乾淨的表示而不是速度，避免長時間推演時誤差累積；損失再以隨訊號程度上升的斜坡權重加權，讓訓練專注在學習訊號較多的程度 (p.6)。
- **[動作條件](../concepts/action-conditioning.md)**：滑鼠、鍵盤等每個動作成分都各自編碼成 token；沒有動作標註的影片只使用一個學到的佔位嵌入，因此模型可以用沒有動作的影片訓練 (p.5)。
- **代理人微調**：把帶有任務嵌入的代理人 token 插入 transformer 來預測策略與獎勵；其他 token 不能注意到代理人 token，避免世界模型受目前任務影響 (pp.6-7)。獎勵頭沿用 DreamerV3，使用 [symexp twohot](../concepts/symlog-predictions.md) 輸出 (p.7)。
- **想像訓練**：transformer 固定不動，只在世界模型從資料片段展開的 rollout 上訓練 policy 頭與 value 頭，每個片段只展開一次 (p.7)。Value 頭以折扣 0.997 學習 λ-return (p.7)。策略以 PMPO 訓練：對優勢為正與為負的狀態分別平均似然損失，再加上朝行為克隆策略的 KL 項，因此不需要報酬正規化 (pp.7-8)。見 [actor-critic](../concepts/actor-critic.md)。
- **高效 transformer**：分開的空間與時間注意力、每 4 層才做一次時間注意力、分組查詢注意力，以及交替使用短與長的訓練批次，讓推論變快 (p.8)。

> **解說（Explainer）：** 代理人先看幾千小時別人玩遊戲的影片，學會遊戲如何回應滑鼠和鍵盤；接著模仿玩家的操作；最後在自己學到的遊戲複製品裡自主練習，在那裡犯錯不用付出代價。

實作細節：模型有 2B 個參數，其中 tokenizer 為 400M、動態模型為 1.6B，在 256 到 1024 顆 TPU-v5p 上訓練 (p.9)。Minecraft 使用 256 個空間 token 與 192 格畫面的脈絡長度 (p.9)。主要資料集是 VPT 承包商資料集，包含 2541 小時、以 20 FPS 錄製的遊玩過程 (p.9)。生成時會把過去的輸入稍微加雜訊到訊號程度 0.1，讓模型能容忍自己的小錯誤 (p.6)。

## 主要結果

- 在離線鑽石挑戰中（1000 個、每個 60 分鐘的回合），Dreamer 4 到石鎬為止的成功率都超過 90%，鐵鎬為 29%，並有 0.7% 的回合拿到鑽石 (p.12)。
- 微調過的 VPT 代理人只做到木棍（53% 的回合），以 Gemma 3 為基礎的 VLA 代理人則在 11% 的回合做到鐵鎬 (p.12)。
- Dreamer 4 勝過 VPT 的離線代理人，使用的資料卻少 100 倍 (p.9, Fig. 3)。
- 想像訓練同時提升成功率與達成里程碑的速度，里程碑越難，提升越明顯 (p.12)。
- 在世界模型的表示上做行為克隆，勝過在 Gemma 3 上或從零開始做行為克隆 (p.12)。
- 在人類互動測試中，玩家在 Dreamer 4 世界模型裡完成了 16 個 Minecraft 任務中的 14 個，大型 Oasis 模型只有 5 個 (p.13)。
- 世界模型在單張 H100 GPU 上超過 20 FPS，脈絡長度為 9.6 秒，先前的 Minecraft 世界模型只有 0.8 到 1.6 秒 (p.13)。
- 2541 小時影片中只有 100 小時附動作時，動作條件生成就達到全部附動作時 85% 的 PSNR 與 100% 的 SSIM (p.14)。
- 只提供 Overworld 的動作時，動作條件仍能轉移到 Nether 與 End，達到完整標註模型 76% 的 PSNR 與 80% 的 SSIM (p.15)。
- 4 步取樣的 shortcut forcing 品質接近 64 步的 diffusion forcing，速度快 16 倍 (p.16, Fig. 8)；完整設計的 FVD 為 57，單純的 diffusion forcing transformer 為 306 (p.16)。

## 限制與未解問題

- 世界模型離遊戲的完整複製還很遠：記憶短，物品欄的預測也不精確 (p.18)。
- 時間一致性受限於 9.6 秒的脈絡，物品欄中的物品有時不清楚或會隨時間改變 (p.13)。
- 拿到鑽石的評測回合不到 1% (p.12)。
- 想像訓練時只訓練 policy 頭與 value 頭；微調整個 transformer 只帶來少許好處，但成本更高 (p.7)。
- 作者提到的未來方向包括：在一般網路影片上預訓練、長期記憶、語言理解、少量的修正用線上資料，以及自動發現目標 (p.18)。

## 相關概念

- [Shortcut forcing](../concepts/shortcut-forcing.md)：動態模型的訓練目標。
- [離線強化學習](../concepts/offline-reinforcement-learning.md)：鑽石挑戰的設定。
- [動作條件](../concepts/action-conditioning.md)：從少量有標註的影片學到。
- [世界模型](../concepts/world-model.md)：現在是可擴展的 transformer。
- [在想像中學習](../concepts/learning-in-imagination.md)：最後一個訓練階段。
- [Actor-critic](../concepts/actor-critic.md)：以 PMPO 與 λ-return 訓練的 policy 頭與 value 頭。
- [遞迴狀態空間模型](../concepts/recurrent-state-space-model.md)：本篇取代的早期架構。
- [Symlog 預測](../concepts/symlog-predictions.md)：用於獎勵頭與價值頭。
- [報酬正規化](../concepts/return-normalization.md)：使用 PMPO 後不再需要。
- [基於模型的強化學習](../concepts/model-based-reinforcement-learning.md)：與 VPT、VLA 代理人比較。

## 與其他來源的關係

- [Mastering Diverse Domains through World Models](2023-dreamerv3.md)：DreamerV3 以低解析度輸入與抽象合成動作、透過線上互動從零開始收集鑽石；Dreamer 4 則從高解析度影像、以低階滑鼠鍵盤動作、完全離線地做到 (p.29)。它保留 symexp twohot 輸出頭，但取代了 RSSM、報酬正規化與熵正則項 (p.29)。
- [Learning Latent Dynamics for Planning from Pixels](2019-planet.md) 與 [World Models](2018-world-models.md)：Dreamer 4 把這兩篇列為最早準確到能從像素規劃的世界模型 (p.17)。

## 背景資料

- [Dreamer 4 專案頁面](https://danijar.com/dreamer4)：論文中提供的連結。

## 我的筆記
