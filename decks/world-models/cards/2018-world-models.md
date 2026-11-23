# 證據卡：World Models（2018）

只讀：`wiki/zh/sources/2018-world-models.md` 與它連到的概念頁。

## C1
- 主張：World Models 把代理人拆成兩部分：大型世界模型不靠獎勵就學會壓縮並預測看到的畫面，很小的控制器根據它的特徵行動。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.1)
- Wiki 原文：「把代理人（agent）拆成兩部分：一個大型的世界模型，不靠獎勵就學會壓縮並預測自己看到的畫面；以及一個很小的控制器，根據世界模型提供的特徵行動。」

## C2
- 主張：代理人甚至可以完全在世界模型自己產生的夢境裡訓練，再搬回真實環境使用。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.1)
- Wiki 原文：「代理人甚至可以完全在世界模型自己產生的夢境裡訓練，再搬回真實環境使用 (p.1)」

## C3
- 主張：V（視覺）用變分自編碼器把每張畫面壓縮成一個小的潛在向量 z。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.3)
- Wiki 原文：「V（視覺）：用變分自編碼器把每一張畫面壓縮成一個小的潛在向量（latent vector）z (p.3)」

## C4
- 主張：M（記憶）是 MDN-RNN，以高斯混合分布預測下一個潛在向量的機率分布。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.3)
- Wiki 原文：「M（記憶）：一個輸出層為混合密度網路的 LSTM，也就是 MDN-RNN，以高斯混合分布預測下一個潛在向量的機率分布」

## C5
- 主張：C（控制器）被刻意設計得很小，代理人幾乎所有的複雜度都放在 V 與 M。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.3)
- Wiki 原文：「它被刻意設計得很小，讓代理人幾乎所有的複雜度都放在 V 與 M (p.3)」

## C6
- 主張：控制器只有 867 個參數，VAE 有 4,348,547 個、MDN-RNN 有 422,368 個。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.5)
- Wiki 原文：「控制器只有 867 個參數，相較之下 VAE 有 4,348,547 個、MDN-RNN 有 422,368 個 (p.5)」

## C7
- 主張：V 與 M 用隨機策略收集的資料訓練，完全不使用獎勵；只有 C 看得到獎勵。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.5)
- Wiki 原文：「V 與 M 先用隨機策略收集的資料訓練，完全不使用獎勵訊號；只有 C 看得到獎勵 (p.5)」

## C8
- 主張：在 Car Racing 中同時使用 V 與 M，代理人在 100 次隨機試驗中得到 906 ± 21 分，是第一個被回報的解；先前的深度強化學習方法介於 591 到 652 分。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.6, Table 1)
- Wiki 原文：「同時使用 V 與 M 時，代理人在 100 次隨機試驗中得到 906 ± 21 分，是第一個被回報的解；先前的深度強化學習方法介於 591 到 652 分，排行榜最佳成績為 838 ± 11 (p.6, Table 1)」

## C9
- 主張：只用 V、沒有 M 時，代理人在急彎會搖晃，只得到 632 ± 251 分。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.5)
- Wiki 原文：「只用 V 時，代理人在急彎會搖晃，得分 632 ± 251」

## C10
- 主張：在 VizDoom 中，C 只在世界模型構成的虛擬環境裡訓練，之後再放到真實遊戲中執行。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.7)
- Wiki 原文：「C 只在這個虛擬環境裡訓練，之後再放到真實遊戲中執行 (p.7)」

## C11
- 主張：VizDoom: Take Cover 的解決標準是 100 次 rollout 平均存活超過 750 個時間步。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.7)
- Wiki 原文：「VizDoom: Take Cover 的解決標準是 100 次 rollout 的平均存活時間超過 750 個時間步 (p.7)」

## C12
- 主張：只在夢境中訓練的代理人，在夢裡大約存活 900 個時間步，搬到真實遊戲後大約存活 1100 個時間步。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.7) (p.8)
- Wiki 原文：「只在夢境中訓練的代理人，在夢裡大約存活 900 個時間步 (p.7)，搬到真實遊戲後大約存活 1100 個時間步 (p.8)」

## C13
- 主張：控制器會作弊：早期實驗中，它找到一種移動方式，讓夢裡的怪物永遠不發射火球，而這個漏洞在真實遊戲中並不存在。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.8)
- Wiki 原文：「控制器會作弊：早期實驗中，它找到一種移動方式，讓夢裡的怪物永遠不發射火球，而這個漏洞在真實遊戲中並不存在 (p.8)」

## C14
- 主張：溫度 τ = 0.1 時夢境幾乎是決定性的，策略在夢裡得到 2086 ± 140 分，在真實環境卻只有 193 ± 58 分。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.10, Table 2)
- Wiki 原文：「溫度很重要：τ = 0.1 時夢境幾乎是決定性的，怪物不再發射火球，策略在夢裡得到 2086 ± 140，在真實環境卻只有 193 ± 58」

## C15
- 主張：隨機的 M 和較高的溫度讓這類漏洞較難被利用，但隨機性太高會讓夢境難到學不到東西。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.10)
- Wiki 原文：「隨機的 M 和較高的溫度 τ 能讓這類漏洞較難被利用，但隨機性太高會讓夢境難到學不到東西，所以 τ 需要調整 (p.10)」

## C16
- 主張：V 單獨訓練且不看獎勵，可能把容量花在無關的細節上。
- 出處：[World Models](../../zh/sources/2018-world-models.html) (p.12)
- Wiki 原文：「V 是單獨訓練且不看獎勵，因此可能把容量花在無關的細節上」

## C17
- 主張：世界模型是從經驗中學到的環境模型，用來預測接下來會發生什麼，通常以目前的狀態與動作為條件。
- 出處：[世界模型（World model）](../../zh/concepts/world-model.html)
- Wiki 原文：「一個從經驗中學到的環境模型，用來預測接下來會發生什麼，通常以目前的狀態與動作為條件。」

## C18
- 主張：能預測自己行動後果的代理人，不必在真實世界裡把每件事都試一遍；世界模型通常在壓縮過的潛在空間中做預測。
- 出處：[世界模型（World model）](../../zh/concepts/world-model.html)
- Wiki 原文：「能預測自己行動後果的代理人，不必在真實世界裡把每件事都試一遍。世界模型從經驗中學會這些預測，通常在壓縮過的潛在空間（latent space）中進行，而不是直接處理原始像素。」

## C19
- 主張：世界模型有三種用法：當作特徵來源、當作讓代理人練習的模擬器（包括只能用錄下來的資料時）、產生可能的未來讓人探索。
- 出處：[世界模型（World model）](../../zh/concepts/world-model.html)
- Wiki 原文：「它可以當作特徵來源，概括現在並暗示未來；可以當作模擬器，讓代理人在裡面練習，包括代理人只能從錄下來的資料學習的情況；也可以產生可能的未來，讓人去探索。」

## C20
- 主張：世界模型是學出來的，永遠不會完美，依賴它的代理人可能被它的錯誤誤導。
- 出處：[世界模型（World model）](../../zh/concepts/world-model.html)
- Wiki 原文：「因為它是學出來的，永遠不會完美，依賴它的代理人可能被它的錯誤誤導。」

## C21
- 主張：強化學習中，代理人在環境裡行動、得到獎勵，透過試誤學出選擇動作的規則（策略），讓長期累積的獎勵越多越好。
- 出處：[基於模型的強化學習（Model-based reinforcement learning）](../../zh/concepts/model-based-reinforcement-learning.html)
- Wiki 原文：「在強化學習（reinforcement learning）中，代理人（agent）在環境裡行動、得到獎勵（reward），並透過試誤學出一套策略（policy），也就是選擇動作的規則，讓長期累積的獎勵越多越好。」

## C22
- 主張：無模型方法直接從試誤中學習；基於模型的方法先學一個動態模型，再拿來規劃或產生額外的經驗訓練策略。
- 出處：[基於模型的強化學習（Model-based reinforcement learning）](../../zh/concepts/model-based-reinforcement-learning.html)
- Wiki 原文：「無模型（model-free）方法直接從試誤中學習策略或價值函數。基於模型的方法先學一個動態模型，再加以利用：在做決定的當下拿來規劃，或拿來產生額外的經驗訓練策略。」

## C23
- 主張：好的模型能讓學習大幅提高資料效率。
- 出處：[基於模型的強化學習（Model-based reinforcement learning）](../../zh/concepts/model-based-reinforcement-learning.html)
- Wiki 原文：「好的模型能讓學習大幅提高資料效率，也可能轉移到同一環境中的新任務。」

## C24
- 主張：變分自編碼器把輸入編碼成一個小而帶有隨機性的潛在向量，並學會把它解碼回原本的輸入。
- 出處：[變分自編碼器（Variational autoencoder）](../../zh/concepts/variational-autoencoder.html)
- Wiki 原文：「一種神經網路，把輸入編碼成一個小而帶有隨機性的潛在向量，並學會把這個向量解碼回原本的輸入。」

## C25
- 主張：MDN-RNN 的輸出層給出高斯混合分布的參數，因此預測的是下一個值的機率分布，而不是單一數值。
- 出處：[混合密度遞迴神經網路（Mixture density RNN）](../../zh/concepts/mixture-density-rnn.html)
- Wiki 原文：「一種遞迴神經網路，輸出層給出高斯混合分布的參數，因此預測的是下一個值的機率分布，而不是單一數值。」

## C26
- 主張：在想像中學習的主要風險是模型被利用：代理人找到只因模型出錯才得高分的行為，這種行為在真實環境中會失敗。
- 出處：[在想像中學習（Learning in imagination）](../../zh/concepts/learning-in-imagination.html)
- Wiki 原文：「主要風險是模型被利用（model exploitation）：代理人可能找到只因為模型出錯才得高分的行為，而這種行為在真實環境中會失敗。」
