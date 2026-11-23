---
title: "Mastering Diverse Domains through World Models"
authors: "Danijar Hafner et al."
year: 2023
venue: "arXiv:2301.04104"
url: "https://arxiv.org/abs/2301.04104"
raw: "raw/(dreamerv3)Mastering Diverse Domains through World Modelsv2.pdf"
pages: 40
added: 2026-11-24
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
status: to-read
concepts: [symlog-predictions, return-normalization, kl-balancing, categorical-latents, recurrent-state-space-model, actor-critic, learning-in-imagination, world-model, model-based-reinforcement-learning, variational-autoencoder]
topics: [world-models]
---

## One-line summary

DreamerV3 adds a set of robustness techniques, such as [symlog predictions](../concepts/symlog-predictions.md), [return normalization](../concepts/return-normalization.md) and [KL balancing](../concepts/kl-balancing.md) with free bits, so that one [world model](../concepts/world-model.md) agent with a single fixed configuration outperforms specialized methods across more than 150 tasks and collects diamonds in Minecraft from scratch (p.1).

## Research question

Reinforcement learning algorithms usually need expert tuning to work in a new domain, which makes them brittle and expensive to apply (p.2). Can a world-model agent learn across very different domains with one fixed set of hyperparameters, and does such an agent scale predictably with model size and compute (p.2)?

## Method

- **Three networks**: a world model predicts the outcomes of potential actions, a critic judges the value of each outcome, and an actor chooses actions to reach the best outcomes; all three are trained concurrently from replayed experience (p.3).
- **World model**: a [recurrent state-space model](../concepts/recurrent-state-space-model.md) with an encoder, a sequence model, a dynamics predictor, and reward, continue and decoder heads; the representations are vectors of [categorical latents](../concepts/categorical-latents.md) trained with straight-through gradients (pp.3-4). The world model learns its representations through autoencoding, as in a [variational autoencoder](../concepts/variational-autoencoder.md) (p.3).
- **World model loss**: a prediction loss, a dynamics loss and a representation loss weighted 1, 1 and 0.1, with both KL losses clipped below 1 nat of free bits (pp.4-5). The categorical distributions are mixed with 1% uniform noise to prevent spikes in the KL losses (p.5).
- **Behavior learning**: an [actor-critic](../concepts/actor-critic.md) is trained purely on trajectories imagined by the world model; actions in the environment are sampled from the actor without lookahead planning, so this is [learning in imagination](../concepts/learning-in-imagination.md) (p.5).
- **Critic**: it predicts a distribution over λ-returns, parameterized as a categorical distribution over exponentially spaced bins; it is also trained on replayed trajectories with a loss scale of 0.3 and regularized toward an exponential moving average of its own parameters (pp.5-6).
- **Actor**: it uses the Reinforce estimator for both discrete and continuous actions, with a fixed entropy scale of `3e-4` made possible by return normalization (p.6).
- **Robust predictions**: vector observations, rewards and values are handled with the symlog transform and a symexp twohot loss, so the size of the gradients does not depend on the size of the targets (p.7).

> **Explainer:** Earlier Dreamers were like a car that needed its mirrors and seat adjusted for every new driver. DreamerV3 adds automatic adjustments, so the same settings work whether the rewards are tiny or huge, frequent or rare.

Implementation details: training uses a uniform replay buffer with an online queue, and the amount of training is set by the replay ratio (p.18). Gradients are clipped adaptively per tensor and applied with the LaProp optimizer instead of Adam, which avoided occasional instabilities (p.18). The sequence model is a GRU with block-diagonal recurrent weights of 8 blocks (p.18). Model sizes range from 12 million to 400 million parameters, and the default model has 200 million (p.19). The text gives a prediction horizon of 16 (p.5), while the hyperparameter table lists an imagination horizon of 15 (p.21); the exact value is (to be verified). Every agent was trained on a single A100 GPU (p.19).

## Key results

- With fixed hyperparameters, Dreamer is evaluated on 8 domains with over 150 tasks and outperforms tuned expert algorithms across them, as well as a high-quality PPO baseline in all domains (p.8).
- On 57 Atari games with 200 million frames, Dreamer outperforms MuZero while using a fraction of its computational resources, and also beats Rainbow and IQN (p.8).
- On DMLab, Dreamer at 100 million frames exceeds IMPALA and R2D2+ at 1 billion steps, a data-efficiency gain of over 1000% (p.8).
- Dreamer sets new state-of-the-art results on Proprio Control, Visual Control and BSuite, and beats IRIS, TWM, SPR and SimPLe on Atari100k (pp.9-10).
- All 10 Dreamer agents trained on Minecraft discover diamonds within 100 million environment steps, while IMPALA, Rainbow and PPO reach the iron pickaxe at most (p.10, Fig. 5).
- At the end of the budget, Dreamer obtains a diamond in 0.4% of episodes (p.24, Fig. 9).
- Dreamer used 1 GPU for 9 days on Minecraft, compared with 720 GPUs for 9 days for VPT, which also relied on human data (p.11).
- Ablations show that every robustness technique helps on average; the KL objective matters most, followed by return normalization and symexp twohot regression (p.10, Fig. 6).
- Performance rests mainly on the unsupervised reconstruction loss of the world model, not on reward and value gradients (p.10, Fig. 6).
- Larger models, from 12 million to 400 million parameters, both score higher and need less environment interaction, and higher replay ratios also improve performance predictably (p.10, Fig. 6).

## Limitations and open questions

- Diamonds are found reliably during training, but only in 0.4% of episodes at the budget, which the authors leave as a challenge for future research (p.24, Fig. 9).
- The Minecraft setup uses a block-breaking action of prior work, because the original action space makes it hard for stochastic policies to keep a key pressed (p.10).
- Uniform replay was used for simplicity, even though prioritized replay also improved Dreamer (p.18).
- DMLab was evaluated at 100 million steps because longer runs were infeasible, and ProcGen used a single seed (p.19).
- Future directions named by the authors include pretraining world models on internet videos and learning one world model across domains (p.11).

## Related concepts

- [Symlog predictions](../concepts/symlog-predictions.md): robust prediction of targets of any scale.
- [Return normalization](../concepts/return-normalization.md): makes one entropy scale work across domains.
- [KL balancing](../concepts/kl-balancing.md): kept from DreamerV2 and combined with free bits.
- [Categorical latents](../concepts/categorical-latents.md): kept from DreamerV2, with a small amount of uniform mixing.
- [Recurrent state-space model](../concepts/recurrent-state-space-model.md): the world model architecture.
- [Actor-critic](../concepts/actor-critic.md): behavior learning with a distributional critic and Reinforce actor.
- [Learning in imagination](../concepts/learning-in-imagination.md): behaviors are learned only from imagined trajectories.
- [World model](../concepts/world-model.md): the core of the agent.
- [Model-based reinforcement learning](../concepts/model-based-reinforcement-learning.md): compared with PPO, MuZero and VPT.
- [Variational autoencoder](../concepts/variational-autoencoder.md): the world model learns representations by autoencoding.

## Relation to other sources

- [Mastering Atari with Discrete World Models](2021-dreamerv2.md): DreamerV3 is the next generation after DreamerV2, which surpassed human performance on Atari; DreamerV3 adds the robustness techniques, a new network architecture, a new optimizer and a larger replay buffer (p.20).
- [Dream to Control: Learning Behaviors by Latent Imagination](2020-dreamer.md): the paper describes DreamerV1 as limited to continuous control (p.20).
- [Learning Latent Dynamics for Planning from Pixels](2019-planet.md): the world model is still the RSSM introduced by PlaNet (p.3).

## Background

- [DreamerV3 project page](https://danijar.com/dreamerv3): public implementation that reproduces the results, linked from the paper.

## My notes
