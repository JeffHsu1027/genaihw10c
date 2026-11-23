---
title: "Learning Latent Dynamics for Planning from Pixels"
authors: "Danijar Hafner et al."
year: 2019
venue: "ICML 2019 (arXiv:1811.04551)"
url: "https://arxiv.org/abs/1811.04551"
raw: "raw/(planet)Learning Latent Dynamics for Planning from Pixels v5.pdf"
pages: 20
added: 2026-11-24
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
status: read
concepts: [model-based-reinforcement-learning, world-model, recurrent-state-space-model, latent-overshooting, latent-space-planning, variational-autoencoder]
topics: [world-models]
translated_from: "36877d136c59"
---

## 一句話總結

PlaNet（Deep Planning Network）是一個純粹[基於模型](../concepts/model-based-reinforcement-learning.md)的代理人：從影像學出潛在的[世界模型](../concepts/world-model.md)，每一個動作都靠在潛在空間中快速的線上規劃來決定，不使用策略網路或價值網路 (p.1)。

## 研究問題

從像素學到的動態模型，能不能準確到足以拿來規劃，並解決比過去「用學習模型規劃」更困難的控制任務 (p.1)？這類模型難學的原因包括：模型誤差、多步預測時誤差累積、需要表達多種可能的未來，以及在訓練分布之外過度自信的預測 (p.1)。

## 方法

- **問題設定**：每個任務都視為部分可觀測馬可夫決策過程（POMDP），因為單張影像無法呈現環境的完整狀態 (p.2)。
- **模型**：PlaNet 學習轉移模型、觀測模型、獎勵模型，以及一個從過去影像與動作推斷目前隱藏狀態信念的編碼器 (p.3)。觀測模型提供豐富的訓練訊號，但規劃時不會用到 (p.3)。
- **[遞迴狀態空間模型](../concepts/recurrent-state-space-model.md)（RSSM）**：潛在狀態分成由 RNN 傳遞的確定性部分，以及從高斯分布抽樣的隨機部分 (p.4, Eq. 4)。純確定性的 RNN 無法表達多種可能的未來，也容易讓規劃器鑽模型誤差的漏洞；純隨機的模型則難以在多個時間步之間記住資訊 (p.4, Fig. 2)。作者的關鍵發現是 "both stochastic and deterministic paths in the transition model are crucial for successful planning" (p.3)，也就是轉移模型中的隨機與確定兩條路徑對成功規劃都不可或缺。
- **訓練目標**：模型（包括類似[變分自編碼器](../concepts/variational-autoencoder.md)的編碼器）以變分下界訓練，由重建項，以及編碼器後驗與轉移先驗之間的 KL 項組成 (p.4, Eq. 3)。
- **[潛在超前預測](../concepts/latent-overshooting.md)（latent overshooting）**：一種推廣後的目標函數，直接在潛在空間訓練各種距離的多步預測，不需要額外解碼出影像 (p.5)。
- **[規劃](../concepts/latent-space-planning.md)**：每一步都用交叉熵方法（cross entropy method，CEM）在模型中搜尋最佳的動作序列，只執行第一個動作，做法如同模型預測控制（model-predictive control） (p.3)。每個候選序列的分數，是在潛在空間中把模型往前推演並加總預測的獎勵，因此規劃時完全不產生影像 (p.3)。
- **資料收集**：先用少數隨機動作的種子回合開始，接著交替進行模型訓練，以及用規劃（加上少量高斯探索雜訊）收集新回合；每個選定的動作會重複執行好幾次 (p.3)。

> **解說（Explainer）：** PlaNet 不是學反射動作，而是每一步都先想再動：在模型裡想像許多可能的行動計畫，留下最有希望的幾個、加以修正，最後只執行最佳計畫的第一步。

附錄中的實作細節：確定性路徑是 200 個單元的 GRU，其他函數是兩層各 200 個單元的全連接層，隨機狀態是 30 維的對角高斯分布 (p.12)。影像為 64x64x3 像素，位元深度降到 5 位元 (p.12)。訓練使用 Adam，學習率為 `1e-3`，每批 50 段、每段長度 50 的序列 (p.12)。KL 項低於 3 個 free nats 時不予懲罰 (p.12)。CEM 的規劃視野為 12、迭代 10 次、每次 1000 個候選，並以最好的 100 個重新擬合 (p.12)。訓練從 5 個種子回合開始，每 100 次更新收集一個新回合；動作重複次數依任務介於 2 到 8 (p.12)。在單張 V100 GPU 上訓練需要 10 到 20 小時 (p.6)。

## 主要結果

- 評測使用 DeepMind Control Suite 中六個以影像為輸入的任務：cartpole swingup、reacher easy、cheetah run、finger spin、cup catch 與 walker walk，觀測都是 64x64x3 的影像 (p.6)。
- 在 100 個回合內，PlaNet 在所有任務上都勝過以本體感測狀態訓練 100,000 回合的 A3C (p.6)。
- 500 個回合後，PlaNet 的表現與以影像訓練 100,000 回合的 D4PG 相近，只有 finger spin 例外 (p.6)。
- PlaNet 訓練 1,000 回合與 D4PG 訓練 100,000 回合的最終分數：cartpole 821 對 862、reacher 832 對 967、cheetah 662 對 524、finger 700 對 985、cup 930 對 980、walker 951 對 968 (p.7, Table 1)。
- 在 cheetah running 上，PlaNet 比 D4PG 的最終表現相對高出 26% (p.6)。相較 D4PG 的資料效率提升依任務從 40 倍到超過 500 倍 (p.7, Table 1)，平均約少用 200 倍的回合 (p.2)。
- 模型消融實驗：拿掉任一條路徑在所有任務上都會變差；確定性部分幫助模型記憶，而沒有隨機部分時代理人完全學不起來 (p.6, Fig. 4)。
- 代理人消融實驗：用規劃線上收集資料在所有任務上都有幫助，且對 cartpole、finger、walker 是必要的；用 CEM 反覆修正計畫，勝過從 1000 個隨機序列中挑最好的一個 (p.6, Fig. 5)。
- 一個代理人同時訓練六個任務、不告訴它正在做哪個任務，仍能解決全部任務，只是學得比較慢 (p.6)。
- 潛在超前預測大幅改善另一種模型（DRNN），卻讓 RSSM 的表現略微下降，所以最終的代理人不需要它 (p.14, Fig. 8)。
- RSSM 在 cheetah 任務上能做出往後 50 步、像素層級準確的開迴路影片預測 (p.18, Fig. 10)。

## 限制與未解問題

- 規劃器只看得到規劃視野內的獎勵；作者建議學習價值函數來涵蓋視野之外的獎勵 (p.8)。
- 動作重複次數是人工固定的；學習時間上的抽象（可能透過階層式模型）留待未來研究 (p.8)。
- 每一步都要評估數千個動作序列，因此所有計算都必須留在潛在空間 (p.3)。以梯度為基礎的規劃可能讓代理人更有效率 (p.8)。
- 模型靠重建影像來訓練；不靠重建的表示學習，可能有助於視覺更多樣的任務 (p.8)。
- 最終表現在 finger spin（700 對 985）與 reacher（832 對 967）上仍低於 D4PG (p.7, Table 1)。
- 提出的兩項技術之一，潛在超前預測，最終的代理人並不需要 (p.5)。

## 相關概念

- [基於模型的強化學習](../concepts/model-based-reinforcement-learning.md)：PlaNet 是純粹基於模型的代理人。
- [世界模型](../concepts/world-model.md)：PlaNet 的潛在動態模型。
- [遞迴狀態空間模型](../concepts/recurrent-state-space-model.md)：本篇提出的模型架構。
- [潛在超前預測](../concepts/latent-overshooting.md)：本篇提出的多步預測目標。
- [潛在空間規劃](../concepts/latent-space-planning.md)：PlaNet 選擇動作的方式。
- [變分自編碼器](../concepts/variational-autoencoder.md)：RSSM 以序列 VAE 的方式訓練。

## 與其他來源的關係

- [World Models](2018-world-models.md)：PlaNet 沿用 World Models 的卷積編碼器與反卷積解碼器 (p.12)，並把 World Models 列為從想像經驗學習策略的混合式代理人 (p.17)。World Models 在夢境中訓練小型控制器，PlaNet 則完全沒有策略，每一步都用模型重新規劃 (p.3)。David Ha 是兩篇論文的共同作者 (p.1)。

## 背景資料

- [PlaNet 專案頁面](https://danijar.com/planet)：論文中提供的程式碼與訓練後代理人的影片。

## 我的筆記
