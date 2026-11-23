---
title: "Categorical latents"
aliases: [discrete latents, categorical latent variables, discrete representations, straight-through gradients]
updated: 2026-11-24
areas: [world-model]
sources: [2021-dreamerv2]
---

## One-line definition

A latent representation made of several categorical variables, each taking one of a fixed set of classes, instead of continuous Gaussian variables.

## Explanation

A Gaussian latent describes a state with continuous numbers and one smooth bump of uncertainty. A vector of categorical variables describes it with discrete choices, so it can express several clearly separate possibilities and abrupt changes. Sampling a category is not differentiable, so training usually relies on the straight-through estimator: the forward pass uses the sampled one-hot vector, while the backward pass uses the gradient of the probabilities as if no sampling had happened. This gradient is biased but has low variance.

> **Explainer:** It is like describing a scene with a set of multiple-choice answers rather than with a slider for each property.

## What each source says

### Mastering Atari with Discrete World Models (2021)

[DreamerV2](../sources/2021-dreamerv2.md) represents the stochastic state as 32 categorical variables with 32 classes each, so a flattened sample is a sparse binary vector of length 1024 with 32 active bits (p.9). The categoricals are trained with straight-through gradients, which take three lines with automatic differentiation (p.3, Alg. 1). Categorical latents outperform Gaussian latents on 42 of 55 Atari games, lose on 8, and tie on 5 (p.9). The authors do not know why and offer hypotheses: a categorical prior can fit a mixture of posteriors exactly, the sparsity may help generalization, categoricals may be easier to optimize, and they may suit non-smooth events such as entering a new room (p.9). Using many binary latents instead was worse (p.18).

## Related concepts

- [Recurrent state-space model](recurrent-state-space-model.md): DreamerV2 uses categorical latents for the stochastic part of the RSSM.
- [KL balancing](kl-balancing.md): the other main change to the DreamerV2 world model.
- [Variational autoencoder](variational-autoencoder.md): the usual alternative with Gaussian latents and reparameterization gradients.

## Background

(None yet)

## My notes
