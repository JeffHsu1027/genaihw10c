---
title: "Mastering Atari with Discrete World Models"
authors: "Danijar Hafner et al."
year: 2021
venue: "ICLR 2021 (arXiv:2010.02193)"
url: "https://arxiv.org/abs/2010.02193"
raw: "raw/(dreamerv2)MASTERING ATARI WITH DISCRETE WORLD MODELSv4.pdf"
pages: 26
added: 2026-11-24
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
status: to-read
concepts: [categorical-latents, kl-balancing, world-model, recurrent-state-space-model, actor-critic, learning-in-imagination, model-based-reinforcement-learning, variational-autoencoder]
topics: [world-models]
---

## One-line summary

DreamerV2 makes small changes to Dreamer, mainly [categorical latent variables](../concepts/categorical-latents.md) and [KL balancing](../concepts/kl-balancing.md), and becomes the first agent to reach human-level performance on the Atari benchmark by learning behaviors purely inside a separately trained [world model](../concepts/world-model.md) (p.1).

## Research question

World models had not been accurate enough to compete with the best model-free methods on Atari, a benchmark that had always required model-free algorithms to reach human-level performance (pp.1-2). Can an agent that learns only from the predictions of a world model match or beat top model-free agents there, on a single GPU (p.2)?

## Method

- **World model**: an image encoder, a [recurrent state-space model](../concepts/recurrent-state-space-model.md) (RSSM) for the dynamics, and predictors for the image, the reward and the discount factor (p.2). The posterior state sees the current image, while the prior state tries to predict it without the image; the prior is what is used for imagination (p.3, Fig. 2).
- **Categorical latents**: the stochastic state is a vector of 32 categorical variables with 32 classes each, instead of the Gaussian latents of PlaNet and Dreamer, and it is trained with straight-through gradients (p.3, Fig. 2). See [categorical latents](../concepts/categorical-latents.md).
- **Loss**: all parts are trained jointly to predict images, rewards and discounts, plus a KL term between posterior and prior, scaled by 0.1 for Atari and 1.0 for continuous control (p.4, Eq. 2). This loss is the ELBO of an action-conditioned hidden Markov model, so the world model can be seen as a sequential [variational autoencoder](../concepts/variational-autoencoder.md) (p.4).
- **KL balancing**: the KL term is minimized faster with respect to the prior than with respect to the posterior, using a weight of 0.8 for the prior and 0.2 for the posterior, so that the representations are not pulled toward a poorly trained prior (p.4, Alg. 2). See [KL balancing](../concepts/kl-balancing.md).
- **Behavior learning**: an [actor-critic](../concepts/actor-critic.md) is trained purely on imagined trajectories with a horizon of 15, and the world model is fixed during this step (pp.4-5). The critic regresses λ-targets with a target network that is updated every 100 gradient steps (p.6). The actor mixes Reinforce gradients and straight-through gradients through the dynamics, plus an entropy regularizer (p.6, Eq. 6).
- **Domain-specific choices**: for Atari, Reinforce gradients work substantially better, while for continuous control, backpropagating through the dynamics works substantially better (p.6).

> **Superseded:** [DreamerV3](2023-dreamerv3.md) uses Reinforce gradients for both discrete and continuous actions, made workable by return normalization (p.6).

> **Superseded:** [DreamerV3](2023-dreamerv3.md) replaces the per-domain KL scale with fixed loss weights and free bits that work across all domains (p.5).

> **Superseded:** [DreamerV3](2023-dreamerv3.md) replaces the critic's target network with a regularizer toward an exponential moving average of the critic's own parameters (p.6).

> **Explainer:** A Gaussian latent can only say *somewhere around here*. A set of categorical latents is more like a checklist of discrete facts, which suits games where rooms switch, enemies vanish and items appear.

Implementation details: the world model has about 20 million trainable parameters, and the actor and critic have about 1 million each (pp.4-5). Images are downscaled from 84x84 grayscale to 64x64 pixels so that Dreamer's convolutional networks can be reused (p.3). Training batches contain 50 sequences of length 50 (p.2). The text states a discount of 0.999 (p.2), while the hyperparameter table lists 0.995 (p.19); which value was used for the reported results is (to be verified). The RSSM uses 600 units, the world model learning rate is `2e-4`, and the actor and critic learning rates are `4e-5` and `1e-4` (p.19). Compared with Dreamer, the model grew from 13 million to 22 million parameters, and policy entropy replaced external action noise for exploration (p.18).

## Key results

- On 55 Atari games with sticky actions and 200 million environment steps, DreamerV2 reaches a gamer-normalized median of 2.15 and a clipped record-normalized mean of 0.28, compared with 1.29 and 0.21 for IQN and 1.47 and 0.17 for Rainbow (p.7, Table 1).
- DreamerV2 outperforms IQN, Rainbow, C51 and DQN on all four aggregation metrics (p.8).
- Training reaches 200 million steps in under 10 days on one V100 GPU with a single environment instance (p.6).
- Over 200 million environment steps, the policy learns from 468 billion imagined compact states, about 10,000 times more than the 50 million real inputs (p.6).
- Ablations: categorical latents beat Gaussian latents on 42 games and lose on 8, and KL balancing beats the standard KL term on 44 games and loses on 6 (p.9).
- Stopping image gradients into the representation almost destroys performance, with the clipped record mean falling from 0.25 to 0.01, while stopping reward gradients changes little (p.9, Table 2).
- Using only straight-through gradients for the actor is worse on 44 games, so the Atari agent relies mostly on Reinforce gradients (p.10).
- From pixels alone, DreamerV2 learns to stand up and walk in the Humanoid Walk task, which the authors believe is the first published result of this kind (p.16).
- With a lower discount of 0.99, DreamerV2 matches the explicit exploration method ICM on Montezuma's Revenge (p.17).
- The authors recommend reporting the clipped record-normalized mean, because the gamer median ignores half of the games and the gamer mean is dominated by a few outliers (p.8).

## Limitations and open questions

- DreamerV2 performs poorly on Video Pinball; the authors suspect that the reconstruction loss ignores the ball, which occupies a single pixel (p.8).
- Why categorical latents help is not known; the paper only lists hypotheses, such as a better fit to the aggregate posterior, sparsity, easier optimization and a better match for non-smooth game events (p.9).
- The ablation results use a slightly earlier version of the agent and, for the curves in the appendix, only two seeds (p.22).
- A full ablation of every change was infeasible because it would need more than 60,000 GPU hours per change (p.18).
- Benefits such as transfer, multi-task learning, robots and uncertainty-based exploration are named as future directions but not tested (p.11).

## Related concepts

- [Categorical latents](../concepts/categorical-latents.md): the main change to the world model.
- [KL balancing](../concepts/kl-balancing.md): the second key change to the world model loss.
- [World model](../concepts/world-model.md): accurate enough to reach human-level Atari performance.
- [Recurrent state-space model](../concepts/recurrent-state-space-model.md): the dynamics model, now with categorical stochastic states.
- [Actor-critic](../concepts/actor-critic.md): the behavior learning algorithm.
- [Learning in imagination](../concepts/learning-in-imagination.md): behaviors are learned purely from imagined trajectories.
- [Model-based reinforcement learning](../concepts/model-based-reinforcement-learning.md): compared with SimPLe and MuZero.
- [Variational autoencoder](../concepts/variational-autoencoder.md): the world model is a sequential VAE.

## Relation to other sources

- [Dream to Control: Learning Behaviors by Latent Imagination](2020-dreamer.md): DreamerV2 is an evolution of Dreamer, called DreamerV1 in this paper (p.2). Appendix C lists every change, including the ones that did not help, such as binary latents and layer normalization in the GRU (p.18).
- [Mastering Diverse Domains through World Models](2023-dreamerv3.md) (DreamerV3, 2023) is the next generation. It keeps categorical latents and KL balancing but adds robustness techniques so that one configuration works across many domains, not only Atari.
- [World and Human Action Models towards gameplay ideation](2025-wham.md) (WHAM, 2025) cites this paper as an example of recurrent state-space world models, and uses a transformer over discrete tokens instead.
- [Learning Latent Dynamics for Planning from Pixels](2019-planet.md): DreamerV2 builds on the world model introduced by PlaNet and replaces its Gaussian latents with categorical variables (p.2).

## Background

- [DreamerV2 project page](https://danijar.com/dreamerv2): videos, source code and training curves, linked from the paper.

## My notes
