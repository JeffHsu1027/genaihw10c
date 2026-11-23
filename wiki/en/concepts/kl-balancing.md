---
title: "KL balancing"
aliases: [KL balance, balanced KL loss]
updated: 2026-11-24
areas: [world-model]
sources: [2021-dreamerv2, 2023-dreamerv3]
---

## One-line definition

A way of training latent dynamics models in which the KL term between posterior and prior updates the prior faster than it updates the posterior.

## Explanation

In a sequential variational model, the KL term does two jobs: it trains the prior, which predicts the next state without seeing the next observation, toward the posterior, and it pulls the posterior toward the prior. Early in training the prior is poor, so pulling the posterior toward it can damage the representation. KL balancing splits the KL term into these two directions and gives them different weights, so the model mostly lowers the KL by improving its prior dynamics rather than by making its representations vaguer. It is different from simply scaling the whole KL term, as in a β-VAE.

## What each source says

### Mastering Atari with Discrete World Models (2021)

[DreamerV2](../sources/2021-dreamerv2.md) introduces KL balancing with a weight of 0.8 for the prior and 0.2 for the posterior, implemented with stop-gradients (p.4, Alg. 2). It argues that an accurate prior is critical because the prior is what generates imagined trajectories for policy learning (p.9). KL balancing outperforms the standard KL term on 44 of 55 Atari games, loses on 6, and ties on 5 (p.9). It replaces the free nats used in Dreamer (p.18). The authors suggest it may also help other probabilistic models with learned priors (p.9).

### Mastering Diverse Domains through World Models (2023)

[DreamerV3](../sources/2023-dreamerv3.md) writes the two directions as separate losses: a dynamics loss that trains the prior toward the representations and a representation loss that makes the representations predictable, weighted 1 and 0.1 (p.4). Both are clipped below 1 nat of free bits, so they switch off once they are small and learning focuses on prediction (p.5). The authors argue that this combination removes the need to tune the regularizer for each domain's visual complexity (p.5). In the ablations, removing KL balancing and free bits hurts the most of all robustness techniques (p.10).

### Comparing the sources

- [DreamerV2](../sources/2021-dreamerv2.md) introduces KL balancing to replace free nats and still scales the KL term differently for Atari and continuous control (p.4).
- [DreamerV3](../sources/2023-dreamerv3.md) brings free bits back and combines them with balancing, so one setting works across domains (p.5). DreamerV3 builds on DreamerV2; this summary is this Wiki's own.

## Related concepts

- [Categorical latents](categorical-latents.md): the other main change to the DreamerV2 world model.
- [Variational autoencoder](variational-autoencoder.md): KL balancing changes the KL term of the variational bound.
- [Recurrent state-space model](recurrent-state-space-model.md): the model whose prior is trained this way.
- [Free bits](free-bits.md): the KL clipping that DreamerV2 replaces and DreamerV3 combines with balancing.

## Background

(None yet)

## My notes
