---
title: "Recurrent state-space model"
aliases: [RSSM]
updated: 2026-11-24
areas: [world-model]
sources: [2019-planet]
---

## One-line definition

A latent dynamics model whose state has a deterministic part, carried forward by a recurrent network, and a stochastic part sampled at every step.

## Explanation

A purely deterministic recurrent model remembers well but can only predict a single future. A purely stochastic state-space model can represent uncertainty but struggles to keep information across many steps. Combining both lets the deterministic path act as memory while the stochastic path represents what is uncertain about the next state. The model is usually trained like a sequential variational autoencoder, with an encoder that infers the latent state from observations.

> **Explainer:** The deterministic part is a diary that faithfully keeps what has happened; the stochastic part is a guess about what might happen next.

## What each source says

### Learning Latent Dynamics for Planning from Pixels (2019)

[PlaNet](../sources/2019-planet.md) introduces the RSSM: an RNN updates the deterministic state from the previous deterministic state, stochastic state and action, the stochastic state is sampled from a Gaussian given the deterministic state, and observations and rewards are predicted from both (p.4, Eq. 4). All information about the observations must pass through the sampling step of the encoder, to avoid a deterministic shortcut from inputs to reconstructions (p.4). In the experiments, both paths are needed on every task, and without the stochastic part the agent does not learn at all (p.6, Fig. 4). The implementation uses a GRU with 200 units and a 30-dimensional stochastic state (p.12). Unlike a purely stochastic model, the RSSM is robust to the choice between ReLU and ELU activations (p.15, Fig. 9).

## Related concepts

- [World model](world-model.md): the RSSM is a design for the world model.
- [Variational autoencoder](variational-autoencoder.md): the RSSM is trained like a sequential VAE.
- [Latent overshooting](latent-overshooting.md): an extra objective for training such models on multi-step predictions.
- [Mixture density RNN](mixture-density-rnn.md): another way to add randomness to a recurrent model; it samples the output, while the RSSM samples part of the state.

## Background

(None yet)

## My notes
