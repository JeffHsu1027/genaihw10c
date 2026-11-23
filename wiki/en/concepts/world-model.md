---
title: "World model"
aliases: [dynamics model, environment model, predictive model of the environment]
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
sources: [2018-world-models, 2019-planet]
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

### Comparing the sources

- Both learn a compressed latent state from pixels and a transition model over it: [World Models](../sources/2018-world-models.md) with a VAE and an MDN-RNN (p.2, Fig. 4), [PlaNet](../sources/2019-planet.md) with a recurrent state-space model (p.4, Eq. 4).
- [World Models](../sources/2018-world-models.md) trains its model once on random-policy data, and in Car Racing the model never sees rewards (p.5).
- [PlaNet](../sources/2019-planet.md) predicts rewards with the model and keeps retraining it on data collected by its own plans (p.3).
- Both warn that a purely deterministic model is easy to exploit: [World Models](../sources/2018-world-models.md) for its controller (p.9) and [PlaNet](../sources/2019-planet.md) for its planner (p.4, Fig. 2). This is agreement, not conflict.
- PlaNet cites World Models (see the PlaNet source page); this side-by-side comparison is this Wiki's own summary.

## Related concepts

- [Variational autoencoder](variational-autoencoder.md): compresses observations for the world model.
- [Mixture density RNN](mixture-density-rnn.md): predicts the next state as a probability distribution.
- [Recurrent state-space model](recurrent-state-space-model.md): a world model design with deterministic and stochastic state.
- [Model-based reinforcement learning](model-based-reinforcement-learning.md): reinforcement learning that uses a world model.
- [Learning in imagination](learning-in-imagination.md): training an agent inside a world model.

## Background

(None yet)

## My notes
