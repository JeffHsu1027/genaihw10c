# 證據卡：Mastering Diverse Domains through World Models（DreamerV3，2023）

只讀：`wiki/zh/sources/2023-dreamerv3.md` 與它連到的概念頁。

## C1
- 主張：DreamerV3 讓一個以世界模型為核心、只用一組固定設定的代理人，在 150 多個任務上勝過專門的方法，並從零開始在 Minecraft 挖到鑽石。
- 出處：[DreamerV3](../../zh/sources/2023-dreamerv3.html) (p.1)
- Wiki 原文：「讓一個以世界模型為核心、只用一組固定設定的代理人，在 150 多個任務上勝過專門的方法，並從零開始在 Minecraft 中挖到鑽石 (p.1)」

## C2
- 主張：強化學習演算法用到新領域時通常需要專家調整，因此很脆弱、成本也高。
- 出處：[DreamerV3](../../zh/sources/2023-dreamerv3.html) (p.2)
- Wiki 原文：「強化學習演算法要應用到新領域時，通常需要專家調整，因此很脆弱、成本也高 (p.2)」

## C3
- 主張：DreamerV3 有三個網路：世界模型預測可能動作的結果，critic 評估每個結果的價值，actor 選擇能達到最佳結果的動作。
- 出處：[DreamerV3](../../zh/sources/2023-dreamerv3.html) (p.3)
- Wiki 原文：「世界模型預測可能動作的結果，critic 評估每個結果的價值，actor 選擇能達到最佳結果的動作；三者在代理人與環境互動時，同時從回放的經驗中訓練 (p.3)」

## C4
- 主張：在環境中行動時直接從 actor 抽樣、不做往前規劃，因此屬於在想像中學習。
- 出處：[DreamerV3](../../zh/sources/2023-dreamerv3.html) (p.5)
- Wiki 原文：「在環境中行動時直接從 actor 抽樣，不做往前規劃，因此屬於在想像中學習 (p.5)」

## C5
- 主張：在 Minecraft 上訓練的 10 個 DreamerV3 代理人全部在 1 億環境步內找到鑽石，IMPALA、Rainbow 與 PPO 最多只做到鐵鎬。
- 出處：[DreamerV3](../../zh/sources/2023-dreamerv3.html) (p.10, Fig. 5)
- Wiki 原文：「在 Minecraft 上訓練的 10 個 Dreamer 代理人全部在 1 億環境步內找到鑽石，而 IMPALA、Rainbow 與 PPO 最多只做到鐵鎬 (p.10, Fig. 5)」

## C6
- 主張：在 Minecraft 上，DreamerV3 用 1 張 GPU 跑 9 天；VPT 用 720 張 GPU 跑 9 天，而且依賴人類資料。
- 出處：[DreamerV3](../../zh/sources/2023-dreamerv3.html) (p.11)
- Wiki 原文：「Dreamer 在 Minecraft 上用 1 張 GPU 跑 9 天；VPT 則用 720 張 GPU 跑 9 天，而且依賴人類資料 (p.11)」

## C7
- 主張：在訓練預算結束時，只有 0.4% 的回合拿到鑽石。
- 出處：[DreamerV3](../../zh/sources/2023-dreamerv3.html) (p.24, Fig. 9)
- Wiki 原文：「在訓練預算結束時，Dreamer 有 0.4% 的回合拿到鑽石 (p.24, Fig. 9)」

## C8
- 主張：從 1200 萬到 4 億個參數，較大的模型分數更高，需要的環境互動也更少。
- 出處：[DreamerV3](../../zh/sources/2023-dreamerv3.html) (p.10, Fig. 6)
- Wiki 原文：「從 1200 萬到 4 億個參數，較大的模型分數更高，需要的環境互動也更少；提高 replay ratio 同樣能穩定地提升表現 (p.10, Fig. 6)」

## C9
- 主張：表現主要來自世界模型的非監督重建損失，而不是獎勵與價值的梯度。
- 出處：[DreamerV3](../../zh/sources/2023-dreamerv3.html) (p.10, Fig. 6)
- Wiki 原文：「表現主要來自世界模型的非監督重建損失，而不是獎勵與價值的梯度 (p.10, Fig. 6)」

## C10
- 主張：作者提到的未來方向包括在網路影片上預訓練世界模型，以及學習一個跨領域的世界模型。
- 出處：[DreamerV3](../../zh/sources/2023-dreamerv3.html) (p.11)
- Wiki 原文：「作者提到的未來方向包括：在網路影片上預訓練世界模型，以及學習一個跨領域的世界模型 (p.11)」
