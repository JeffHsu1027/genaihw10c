---
title: "Recurrent state-space model"
aliases: [RSSM]
updated: 2026-11-24
areas: [world-model]
sources: [2019-planet, 2020-dreamer, 2021-dreamerv2, 2023-dreamerv3]
---

## One-line definition

A latent dynamics model whose state has a deterministic part, carried forward by a recurrent network, and a stochastic part sampled at every step.

## Explanation

A purely deterministic recurrent model remembers well but can only predict a single future. A purely stochastic state-space model can represent uncertainty but struggles to keep information across many steps. Combining both lets the deterministic path act as memory while the stochastic path represents what is uncertain about the next state. The model is usually trained like a sequential variational autoencoder, with an encoder that infers the latent state from observations.

> **Explainer:** The deterministic part is a diary that faithfully keeps what has happened; the stochastic part is a guess about what might happen next.

## What each source says

### Learning Latent Dynamics for Planning from Pixels (2019)

[PlaNet](../sources/2019-planet.md) introduces the RSSM: an RNN updates the deterministic state from the previous deterministic state, stochastic state and action, the stochastic state is sampled from a Gaussian given the deterministic state, and observations and rewards are predicted from both (p.4, Eq. 4). All information about the observations must pass through the sampling step of the encoder, to avoid a deterministic shortcut from inputs to reconstructions (p.4). In the experiments, both paths are needed on every task, and without the stochastic part the agent does not learn at all (p.6, Fig. 4). The implementation uses a GRU with 200 units and a 30-dimensional stochastic state (p.12). Unlike a purely stochastic model, the RSSM is robust to the choice between ReLU and ELU activations (p.15, Fig. 9).

### Dream to Control: Learning Behaviors by Latent Imagination (2020)

[Dreamer](../sources/2020-dreamer.md) implements its transition model as the RSSM of PlaNet, and builds the representation model by combining the RSSM with a CNN applied to the image (p.6). Its latent distributions are 30-dimensional diagonal Gaussians, as in PlaNet (p.14). Given only the actions after five context frames, the RSSM predicts 45 steps ahead accurately enough for Dreamer to learn behaviors in its latent space (p.5, Fig. 5).

### Mastering Atari with Discrete World Models (2021)

[DreamerV2](../sources/2021-dreamerv2.md) keeps the RSSM structure: a GRU computes the deterministic recurrent state, a posterior stochastic state sees the current image, and a prior stochastic state predicts it without the image (pp.2-3). The stochastic state, however, becomes a vector of 32 categorical variables with 32 classes each instead of a Gaussian (p.3, Fig. 2). The RSSM uses 600 units (p.19), and adding layer normalization to its GRU gave little or no benefit (p.18).

### Mastering Diverse Domains through World Models (2023)

[DreamerV3](../sources/2023-dreamerv3.md) still implements its world model as an RSSM, with a sequence model, an encoder, a dynamics predictor and heads for reward, continuation and reconstruction (pp.3-4). The sequence model is a GRU with block-diagonal recurrent weights of 8 blocks, which allows many memory units without a quadratic growth in parameters (p.18). Given 5 context frames and the actions, the model predicts 45 frames ahead in DMLab and robot scenes (p.4, Fig. 4) and in Minecraft (p.23, Fig. 7).

### Comparing the sources

- [PlaNet](../sources/2019-planet.md) introduces the RSSM and uses it for planning (p.4).
- [Dreamer](../sources/2020-dreamer.md) reuses it unchanged for policy learning (p.6). The same model therefore supports two different ways of choosing actions; Dreamer builds directly on PlaNet, and this summary is this Wiki's own.
- [DreamerV2](../sources/2021-dreamerv2.md) keeps the deterministic and stochastic paths but swaps the Gaussian stochastic state for categorical variables, which helps on most Atari games (p.9).
- [DreamerV3](../sources/2023-dreamerv3.md) keeps this structure across more than 150 tasks and changes mainly the recurrent cell and the training losses (p.18).

## Related concepts

- [World model](world-model.md): the RSSM is a design for the world model.
- [Variational autoencoder](variational-autoencoder.md): the RSSM is trained like a sequential VAE.
- [Latent overshooting](latent-overshooting.md): an extra objective for training such models on multi-step predictions.
- [Mixture density RNN](mixture-density-rnn.md): another way to add randomness to a recurrent model; it samples the output, while the RSSM samples part of the state.
- [Categorical latents](categorical-latents.md): the discrete stochastic state used in DreamerV2.
- [KL balancing](kl-balancing.md): a way to train the RSSM prior.

## Background

(None yet)

## My notes
