---
title: "KL balancing"
aliases: [KL balance, balanced KL loss]
updated: 2026-11-24
areas: [world-model]
sources: [2021-dreamerv2]
---

## One-line definition

A way of training latent dynamics models in which the KL term between posterior and prior updates the prior faster than it updates the posterior.

## Explanation

In a sequential variational model, the KL term does two jobs: it trains the prior, which predicts the next state without seeing the next observation, toward the posterior, and it pulls the posterior toward the prior. Early in training the prior is poor, so pulling the posterior toward it can damage the representation. KL balancing splits the KL term into these two directions and gives them different weights, so the model mostly lowers the KL by improving its prior dynamics rather than by making its representations vaguer. It is different from simply scaling the whole KL term, as in a β-VAE.

## What each source says

### Mastering Atari with Discrete World Models (2021)

[DreamerV2](../sources/2021-dreamerv2.md) introduces KL balancing with a weight of 0.8 for the prior and 0.2 for the posterior, implemented with stop-gradients (p.4, Alg. 2). It argues that an accurate prior is critical because the prior is what generates imagined trajectories for policy learning (p.9). KL balancing outperforms the standard KL term on 44 of 55 Atari games, loses on 6, and ties on 5 (p.9). It replaces the free nats used in Dreamer (p.18). The authors suggest it may also help other probabilistic models with learned priors (p.9).

## Related concepts

- [Categorical latents](categorical-latents.md): the other main change to the DreamerV2 world model.
- [Variational autoencoder](variational-autoencoder.md): KL balancing changes the KL term of the variational bound.
- [Recurrent state-space model](recurrent-state-space-model.md): the model whose prior is trained this way.

## Background

(None yet)

## My notes
