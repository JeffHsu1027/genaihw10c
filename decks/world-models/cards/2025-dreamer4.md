# 證據卡：Training Agents Inside of Scalable World Models（Dreamer 4，2025）

只讀：`wiki/zh/sources/2025-dreamer4.md` 與它連到的概念頁。

## C1
- 主張：Dreamer 4 是第一個完全只靠離線資料、在世界模型裡做強化學習、不與環境互動就在 Minecraft 拿到鑽石的代理人。
- 出處：[Dreamer 4](../../zh/sources/2025-dreamer4.html) (p.1)
- Wiki 原文：「成為第一個完全只靠離線資料、透過在世界模型裡做強化學習、不與環境互動就在 Minecraft 拿到鑽石的代理人 (p.1)」

## C2
- 主張：Dreamer 4 把早期 Dreamer 的遞迴世界模型換成可擴展的 transformer 世界模型。
- 出處：[Dreamer 4](../../zh/sources/2025-dreamer4.html) (p.1)
- Wiki 原文：「Dreamer 4 把早期 Dreamer 的遞迴世界模型換成以 shortcut forcing 訓練、可擴展的 transformer 世界模型」

## C3
- 主張：DreamerV3 這類早期的世界模型代理人在範圍窄的環境中又快又準，卻無法擬合複雜多樣的資料。
- 出處：[Dreamer 4](../../zh/sources/2025-dreamer4.html) (p.2)
- Wiki 原文：「DreamerV3 這類早期的世界模型代理人在範圍窄的環境中又快又準，卻無法擬合複雜多樣的資料」

## C4
- 主張：訓練分三個階段：先在影片上預訓練世界模型；再微調讓它預測動作與獎勵；最後以想像訓練改進策略。
- 出處：[Dreamer 4](../../zh/sources/2025-dreamer4.html) (p.4)
- Wiki 原文：「先在影片（以及可有可無的動作）上預訓練 tokenizer 與動態模型；再加入任務輸入微調世界模型，讓它預測動作與獎勵；最後以想像訓練改進策略 (p.4)」

## C5
- 主張：沒有動作標註的影片只用一個學到的佔位嵌入，因此模型可以用沒有動作的影片訓練。
- 出處：[Dreamer 4](../../zh/sources/2025-dreamer4.html) (p.5)
- Wiki 原文：「沒有動作標註的影片只使用一個學到的佔位嵌入，因此模型可以用沒有動作的影片訓練 (p.5)」

## C6
- 主張：在離線鑽石挑戰中，Dreamer 4 到石鎬為止的成功率都超過 90%，鐵鎬為 29%，並有 0.7% 的回合拿到鑽石。
- 出處：[Dreamer 4](../../zh/sources/2025-dreamer4.html) (p.12)
- Wiki 原文：「Dreamer 4 到石鎬為止的成功率都超過 90%，鐵鎬為 29%，並有 0.7% 的回合拿到鑽石 (p.12)」

## C7
- 主張：Dreamer 4 勝過 VPT 的離線代理人，使用的資料卻少 100 倍。
- 出處：[Dreamer 4](../../zh/sources/2025-dreamer4.html) (p.9, Fig. 3)
- Wiki 原文：「Dreamer 4 勝過 VPT 的離線代理人，使用的資料卻少 100 倍 (p.9, Fig. 3)」

## C8
- 主張：在人類互動測試中，玩家在 Dreamer 4 世界模型裡完成了 16 個 Minecraft 任務中的 14 個，大型 Oasis 模型只有 5 個。
- 出處：[Dreamer 4](../../zh/sources/2025-dreamer4.html) (p.13)
- Wiki 原文：「在人類互動測試中，玩家在 Dreamer 4 世界模型裡完成了 16 個 Minecraft 任務中的 14 個，大型 Oasis 模型只有 5 個 (p.13)」

## C9
- 主張：世界模型離遊戲的完整複製還很遠：記憶短，物品欄的預測也不精確。
- 出處：[Dreamer 4](../../zh/sources/2025-dreamer4.html) (p.18)
- Wiki 原文：「世界模型離遊戲的完整複製還很遠：記憶短，物品欄的預測也不精確 (p.18)」

## C10
- 主張：離線強化學習只從事先收集好的固定資料集學習，學習期間不讓代理人與環境互動。
- 出處：[離線強化學習（Offline reinforcement learning）](../../zh/concepts/offline-reinforcement-learning.html)
- Wiki 原文：「只從事先收集好的固定資料集做強化學習，學習期間不讓代理人與環境互動。」

## C11
- 主張：線上靠實際嘗試改進策略可能很慢、不安全，對真實機器人或昂貴的系統甚至不可行。
- 出處：[離線強化學習（Offline reinforcement learning）](../../zh/concepts/offline-reinforcement-learning.html)
- Wiki 原文：「線上強化學習靠實際嘗試來改進策略，這可能很慢、不安全，對真實機器人或其他昂貴的系統甚至不可行。」

## C12
- 主張：在資料集上訓練出的世界模型提供一條出路：代理人在模型裡練習，產生新經驗而不碰觸真實環境。
- 出處：[離線強化學習（Offline reinforcement learning）](../../zh/concepts/offline-reinforcement-learning.html)
- Wiki 原文：「在資料集上訓練出的世界模型提供了一條出路：代理人可以在模型裡練習，產生新的經驗而不碰觸真實環境，同時保持接近資料中出現過的行為。」

## C13
- 主張：一個很有用的性質是：從無標註影片學到世界大部分的外觀與物理，只從少量有標註的資料學動作與結果之間的關係。
- 出處：[動作條件（Action conditioning）](../../zh/concepts/action-conditioning.html)
- Wiki 原文：「從無標註影片學到世界大部分的外觀與物理，只從少量有標註的資料學動作與結果之間的關係。」
