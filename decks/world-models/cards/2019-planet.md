# 證據卡：Learning Latent Dynamics for Planning from Pixels（PlaNet，2019）

只讀：`wiki/zh/sources/2019-planet.md` 與它連到的概念頁。

## C1
- 主張：PlaNet 是純粹基於模型的代理人：從影像學出潛在的世界模型，每個動作都靠在潛在空間中線上規劃來決定，不使用策略網路或價值網路。
- 出處：[PlaNet](../../zh/sources/2019-planet.html) (p.1)
- Wiki 原文：「PlaNet（Deep Planning Network）是一個純粹基於模型的代理人：從影像學出潛在的世界模型，每一個動作都靠在潛在空間中快速的線上規劃來決定，不使用策略網路或價值網路 (p.1)」

## C2
- 主張：PlaNet 的潛在狀態分成由 RNN 傳遞的確定性部分，以及從高斯分布抽樣的隨機部分（遞迴狀態空間模型，RSSM）。
- 出處：[PlaNet](../../zh/sources/2019-planet.html) (p.4, Eq. 4)
- Wiki 原文：「潛在狀態分成由 RNN 傳遞的確定性部分，以及從高斯分布抽樣的隨機部分 (p.4, Eq. 4)」

## C3
- 主張：作者的關鍵發現：轉移模型中的隨機與確定兩條路徑，對成功規劃都不可或缺。
- 出處：[PlaNet](../../zh/sources/2019-planet.html) (p.3)
- Wiki 原文：「也就是轉移模型中的隨機與確定兩條路徑對成功規劃都不可或缺。」

## C4
- 主張：拿掉任一條路徑在所有任務上都會變差；確定性部分幫助模型記憶，沒有隨機部分時代理人完全學不起來。
- 出處：[PlaNet](../../zh/sources/2019-planet.html) (p.6, Fig. 4)
- Wiki 原文：「拿掉任一條路徑在所有任務上都會變差；確定性部分幫助模型記憶，而沒有隨機部分時代理人完全學不起來 (p.6, Fig. 4)」

## C5
- 主張：PlaNet 每一步都用交叉熵方法（CEM）在模型中搜尋最佳的動作序列，只執行第一個動作，如同模型預測控制。
- 出處：[PlaNet](../../zh/sources/2019-planet.html) (p.3)
- Wiki 原文：「每一步都用交叉熵方法（cross entropy method，CEM）在模型中搜尋最佳的動作序列，只執行第一個動作，做法如同模型預測控制（model-predictive control） (p.3)」

## C6
- 主張：候選序列的分數是在潛在空間中推演並加總預測的獎勵，所以規劃時完全不產生影像。
- 出處：[PlaNet](../../zh/sources/2019-planet.html) (p.3)
- Wiki 原文：「每個候選序列的分數，是在潛在空間中把模型往前推演並加總預測的獎勵，因此規劃時完全不產生影像 (p.3)」

## C7
- 主張：500 個回合後，PlaNet 的表現與以影像訓練 100,000 回合的無模型方法 D4PG 相近（finger spin 例外）。
- 出處：[PlaNet](../../zh/sources/2019-planet.html) (p.6)
- Wiki 原文：「500 個回合後，PlaNet 的表現與以影像訓練 100,000 回合的 D4PG 相近，只有 finger spin 例外 (p.6)」

## C8
- 主張：相較 D4PG，PlaNet 平均約少用 200 倍的回合。
- 出處：[PlaNet](../../zh/sources/2019-planet.html) (p.2)
- Wiki 原文：「平均約少用 200 倍的回合 (p.2)」

## C9
- 主張：潛在空間規劃是在學到的潛在動態模型裡搜尋候選動作序列、以預測的獎勵評分來選擇動作，過程中不產生觀測畫面。
- 出處：[潛在空間規劃（Latent space planning）](../../zh/concepts/latent-space-planning.html)
- Wiki 原文：「在學到的潛在動態模型裡搜尋候選動作序列、以預測的獎勵評分來選擇動作，過程中不產生觀測畫面。」

## C10
- 主張：在模型預測控制中，只執行第一個動作，看到下一個觀測後再重新搜尋，讓計畫能隨實際情況調整。
- 出處：[潛在空間規劃（Latent space planning）](../../zh/concepts/latent-space-planning.html)
- Wiki 原文：「在模型預測控制（model-predictive control）中，只執行第一個動作，看到下一個觀測後再重新搜尋，讓計畫能隨實際情況調整。」

## C11
- 主張：遞迴狀態空間模型結合兩者：確定性路徑負責記憶，隨機路徑表達下一個狀態中不確定的部分。
- 出處：[遞迴狀態空間模型（Recurrent state-space model）](../../zh/concepts/recurrent-state-space-model.html)
- Wiki 原文：「兩者結合後，確定性路徑負責記憶，隨機路徑表達下一個狀態中不確定的部分。」
