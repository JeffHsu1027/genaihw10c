---
title: "World model"
aliases: [dynamics model, environment model, predictive model of the environment]
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
sources: [2018-world-models, 2019-planet, 2020-dreamer, 2021-dreamerv2, 2023-dreamerv3]
---

## One-line definition

A learned model of an environment that predicts what will happen next, usually given the current state and an action.

## Explanation

An agent that can predict the consequences of its actions does not have to try everything in the real world. A world model learns those predictions from experience, often in a compressed latent space instead of raw pixels. It can be used in two main ways: as a source of features that summarize the present and hint at the future, or as a simulator in which an agent can practise. Because it is learned, it is never perfect, and an agent that relies on it can be misled by its errors.

> **Explainer:** A world model is like the picture in a batter's head that tells them where a fastball will be before their eyes can follow it.

## What each source says

### World Models (2018)

[World Models](../sources/2018-world-models.md) builds the world model from two parts: a VAE that compresses each frame and an MDN-RNN that predicts the next compressed frame (p.2, Fig. 4). The world model is trained without rewards, and only the small controller sees the reward (p.5). The paper uses the world model in both ways: its hidden state gives the controller a sense of the future in Car Racing (p.5), and in VizDoom it fully replaces the real game during training (p.7).

### Learning Latent Dynamics for Planning from Pixels (2019)

[PlaNet](../sources/2019-planet.md) calls its world model a latent dynamics model: a transition model, an observation model, a reward model and an encoder, built as a recurrent state-space model (p.3). Because the model also predicts rewards, the planner can score action sequences purely in latent space without generating images (p.3). The model is trained on data that the agent keeps collecting by planning with the partially trained model, not only on random data (p.3).

### Dream to Control: Learning Behaviors by Latent Imagination (2020)

[Dreamer](../sources/2020-dreamer.md) uses the same world model as PlaNet and describes it as summarizing the agent's experience so that complex behaviors can be learned from it (p.1). The world model predicts rewards from actions and past observations, and any learning objective for it can be combined with Dreamer (p.2). The paper compares three objectives for learning it: image reconstruction works best, contrastive estimation solves about half of the tasks, and reward prediction alone is not enough (p.8, Fig. 8).

### Mastering Atari with Discrete World Models (2021)

[DreamerV2](../sources/2021-dreamerv2.md) describes world models as summarizing an agent's experience into a predictive model that can replace the environment for learning behaviors (p.2). Its world model adds a discount predictor, so that imagined trajectories can account for episode ends, and uses categorical latents with KL balancing (pp.3-4). The world model has about 20 million parameters (p.4), and it is accurate enough for an agent that learns only inside it to reach human-level Atari performance (p.2). The world model relies on image gradients: without them performance collapses, while stopping reward gradients changes little (p.9).

### Mastering Diverse Domains through World Models (2023)

[DreamerV3](../sources/2023-dreamerv3.md) describes the world model as giving the agent rich perception and the ability to imagine the future, and notes that learning and using world models robustly had been an open problem (p.2). Its performance rests mainly on the unsupervised reconstruction loss of the world model rather than on reward and value gradients, which the authors see as an opening for pretraining on unsupervised data (p.10). Larger world models, from 12 million to 400 million parameters, both score higher and need less environment interaction (p.10, Fig. 6).

### Comparing the sources

- Both learn a compressed latent state from pixels and a transition model over it: [World Models](../sources/2018-world-models.md) with a VAE and an MDN-RNN (p.2, Fig. 4), [PlaNet](../sources/2019-planet.md) with a recurrent state-space model (p.4, Eq. 4).
- [World Models](../sources/2018-world-models.md) trains its model once on random-policy data, and in Car Racing the model never sees rewards (p.5).
- [PlaNet](../sources/2019-planet.md) predicts rewards with the model and keeps retraining it on data collected by its own plans (p.3).
- Both warn that a purely deterministic model is easy to exploit: [World Models](../sources/2018-world-models.md) for its controller (p.9) and [PlaNet](../sources/2019-planet.md) for its planner (p.4, Fig. 2). This is agreement, not conflict.
- [Dreamer](../sources/2020-dreamer.md) keeps PlaNet's world model and changes only how behavior is derived from it, which shows that the same model can serve planning or policy learning (p.8).
- [DreamerV2](../sources/2021-dreamerv2.md) keeps the same overall design but changes the latent variables and the KL term, which is enough to move from simple control tasks to human-level Atari (p.2).
- [DreamerV2](../sources/2021-dreamerv2.md) and [DreamerV3](../sources/2023-dreamerv3.md) agree that image reconstruction, not reward prediction, is the main learning signal for the world model (p.10).
- PlaNet, Dreamer, DreamerV2 and DreamerV3 cite World Models (see their source pages); this side-by-side comparison is this Wiki's own summary.

## Related concepts

- [Variational autoencoder](variational-autoencoder.md): compresses observations for the world model.
- [Mixture density RNN](mixture-density-rnn.md): predicts the next state as a probability distribution.
- [Recurrent state-space model](recurrent-state-space-model.md): a world model design with deterministic and stochastic state.
- [Categorical latents](categorical-latents.md): discrete latent states used in DreamerV2's world model.
- [Model-based reinforcement learning](model-based-reinforcement-learning.md): reinforcement learning that uses a world model.
- [Learning in imagination](learning-in-imagination.md): training an agent inside a world model.

## Background

(None yet)

## My notes
