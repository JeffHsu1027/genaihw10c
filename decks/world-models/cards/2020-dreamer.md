# 證據卡：Dream to Control（Dreamer，2020）

只讀：`wiki/zh/sources/2020-dreamer.md` 與它連到的概念頁。

## C1
- 主張：Dreamer 先從影像學出世界模型，再完全靠潛在想像學習行為：在想像的軌跡上訓練 actor-critic，並把價值梯度沿著學到的動態模型反向傳播來改進 actor。
- 出處：[Dreamer](../../zh/sources/2020-dreamer.html) (p.1)
- Wiki 原文：「Dreamer 先從影像學出世界模型，再完全靠潛在想像學習行為：在想像的軌跡上訓練一個 actor-critic，並把解析的價值梯度沿著學到的動態模型反向傳播來改進 actor (p.1)」

## C2
- 主張：只在固定想像視野內最大化獎勵的策略或規劃器會很短視。
- 出處：[Dreamer](../../zh/sources/2020-dreamer.html) (p.1)
- Wiki 原文：「只在固定想像視野內最大化獎勵的策略或規劃器會很短視」

## C3
- 主張：Dreamer 的世界模型與 PlaNet 相同，轉移模型是遞迴狀態空間模型。
- 出處：[Dreamer](../../zh/sources/2020-dreamer.html) (p.6)
- Wiki 原文：「與 PlaNet 相同的潛在動態模型：轉移模型是遞迴狀態空間模型」

## C4
- 主張：價值模型估計動作模型將會得到的想像獎勵，包括視野之外的部分。
- 出處：[Dreamer](../../zh/sources/2020-dreamer.html) (p.4, Eq. 2)
- Wiki 原文：「價值模型估計動作模型將會得到的想像獎勵，包括視野之外的部分 (p.4, Eq. 2)」

## C5
- 主張：學習行為時，世界模型保持固定不動。
- 出處：[Dreamer](../../zh/sources/2020-dreamer.html) (p.5)
- Wiki 原文：「學習行為時，世界模型保持固定不動 (p.5)」

## C6
- 主張：經過 500 萬環境步後，Dreamer 平均分數為 823，PlaNet 為 332，無模型的 D4PG 在 1 億步後為 786。
- 出處：[Dreamer](../../zh/sources/2020-dreamer.html) (p.6, Fig. 6)
- Wiki 原文：「經過 500 萬環境步後，Dreamer 的平均分數為 823，相較之下 PlaNet 為 332，D4PG 在 1 億步後為 786 (p.6, Fig. 6)」

## C7
- 主張：沒有價值模型的方法很短視，只在反應式任務成功；Dreamer 也能解決需要長期功勞分配的任務。
- 出處：[Dreamer](../../zh/sources/2020-dreamer.html) (p.7, Fig. 7)
- Wiki 原文：「沒有價值模型時，兩種替代方法都很短視，只在 walker 這類反應式任務成功；Dreamer 則也能解決 acrobot、hopper 這類需要長期功勞分配的任務 (p.7, Fig. 7)」

## C8
- 主張：Dreamer 保有 PlaNet 的資料效率，同時超越最佳無模型代理人的最終表現。
- 出處：[Dreamer](../../zh/sources/2020-dreamer.html) (p.9)
- Wiki 原文：「Dreamer 保有 PlaNet 的資料效率，同時超越最佳無模型代理人的最終表現 (p.9)」

## C9
- 主張：Dreamer 每一百萬環境步約需 3 小時，PlaNet 需要 11 小時，D4PG 達到相近表現需要 24 小時。
- 出處：[Dreamer](../../zh/sources/2020-dreamer.html) (p.8)
- Wiki 原文：「每一百萬環境步約需 3 小時，相較之下 PlaNet 需要 11 小時，D4PG 達到相近表現需要 24 小時 (p.8)」

## C10
- 主張：Actor-critic 有兩個學習元件：負責選動作的 actor（策略），以及估計未來獎勵的 critic（價值函數）。
- 出處：[Actor-critic（演員－評論家）](../../zh/concepts/actor-critic.html)
- Wiki 原文：「一種有兩個學習元件的強化學習方法：負責選動作的 actor（策略），以及估計 actor 從每個狀態出發能得到多少未來獎勵的 critic（價值函數）。」

## C11
- 主張：有了 critic，actor 不必等到遙遠的獎勵真的發生，也能把它納入考量。
- 出處：[Actor-critic（演員－評論家）](../../zh/concepts/actor-critic.html)
- Wiki 原文：「有了 critic，actor 不必等到遙遠的獎勵真的發生，也能把它納入考量。」

## C12
- 主張：在想像中學習是用世界模型產生的經驗訓練策略；在想像的環境裡練習可能比真實環境便宜又快，學到的策略再搬回現實使用。
- 出處：[在想像中學習（Learning in imagination）](../../zh/concepts/learning-in-imagination.html)
- Wiki 原文：「代理人在這個想像的環境裡練習，成本可能比真實環境低、速度也更快，學到的策略再搬回現實使用。」
