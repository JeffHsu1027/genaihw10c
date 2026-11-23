---
title: "Free bits"
aliases: [free nats, KL clipping, KL threshold]
updated: 2026-11-24
areas: [world-model]
sources: [2019-planet, 2020-dreamer, 2021-dreamerv2, 2023-dreamerv3]
---

## One-line definition

A training trick for variational models that stops penalizing a KL term while it is already below a small threshold.

## Explanation

Variational models such as VAEs and recurrent state-space models balance two goals: describing or predicting their inputs well, and keeping the KL divergence between posterior and prior small. If the KL penalty dominates, especially early in training, the model can stop putting information into its latent state, a failure often called posterior collapse. Free bits give the model an allowance: the KL term is clipped at a threshold, so it has no gradient while it is already below that value, and the model may use that much information at no cost. The threshold is counted in nats when natural logarithms are used, which is why the same idea is also called free nats.

> **Explainer:** It is like a phone plan with a free data allowance: below the allowance, using more costs nothing, so there is no reason to hold back.

## What each source says

### Learning Latent Dynamics for Planning from Pixels (2019)

[PlaNet](../sources/2019-planet.md) does not scale the KL terms relative to the reconstruction terms, but grants the model 3 free nats by clipping the KL loss below that value (p.12).

### Dream to Control: Learning Behaviors by Latent Imagination (2020)

[Dreamer](../sources/2020-dreamer.md) also leaves the KL regularizer unscaled and clips it below 3 free nats, as in PlaNet (p.14).

### Mastering Atari with Discrete World Models (2021)

[DreamerV2](../sources/2021-dreamerv2.md) drops free nats and uses KL balancing instead, scaling the prior and posterior parts of the KL loss separately so that the model learns an accurate temporal prior (p.18).

### Mastering Diverse Domains through World Models (2023)

[DreamerV3](../sources/2023-dreamerv3.md) brings the idea back as free bits: its dynamics loss and its representation loss are both clipped below 1 nat, about 1.44 bits, which switches them off once they are already small so that learning focuses on the prediction loss (p.5). The authors argue that combining free bits with a small representation loss lets one setting serve both visually rich environments, which call for a strong regularizer, and games in which single pixels matter, which call for a weak one (p.5). In the ablations, removing KL balancing and free bits together hurts the most of all robustness techniques (p.10).

### Comparing the sources

- [PlaNet](../sources/2019-planet.md) grants 3 free nats on an unscaled KL term (p.12), and [Dreamer](../sources/2020-dreamer.md) copies this setting (p.14).
- [DreamerV2](../sources/2021-dreamerv2.md) replaces free nats with KL balancing (p.18).
- [DreamerV3](../sources/2023-dreamerv3.md) combines the two, with a threshold of 1 nat on each of its two KL losses (p.5). Each paper builds on the previous one; this summary is this Wiki's own.

## Related concepts

- [KL balancing](kl-balancing.md): DreamerV2 uses it instead of free nats, and DreamerV3 combines the two.
- [Variational autoencoder](variational-autoencoder.md): the kind of model whose KL term free bits clip.
- [Recurrent state-space model](recurrent-state-space-model.md): the sequential latent model whose KL loss PlaNet and the Dreamer agents clip.

## Background

- [Kingma et al., Improved Variational Inference with Inverse Autoregressive Flow (2016)](https://arxiv.org/abs/1606.04934): the paper that introduced free bits for training VAEs.

## My notes
