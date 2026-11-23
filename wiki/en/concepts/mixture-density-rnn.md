---
title: "Mixture density RNN"
aliases: [MDN-RNN, mixture density network, MDN]
updated: 2026-11-24
areas: [world-model]
sources: [2018-world-models]
---

## One-line definition

A recurrent neural network whose output layer gives the parameters of a mixture of Gaussians, so it predicts a probability distribution over the next value instead of a single value.

## Explanation

A recurrent network carries a hidden state that summarizes the past. A mixture density output layer turns that state into the weights, means and variances of several Gaussian components. Sampling from the mixture can produce clearly different outcomes from the same past, which a single Gaussian cannot do well. A temperature parameter scales the randomness of sampling: a low temperature gives nearly deterministic predictions, a high temperature gives more varied ones.

## What each source says

### World Models (2018)

[World Models](../sources/2018-world-models.md) uses an LSTM with a mixture density output layer as the M model, predicting the distribution of the next latent vector from the current action, latent vector and hidden state (p.3). The mixture is useful for discrete random events, such as whether a monster decides to shoot a fireball (p.9). The implementation uses 5 Gaussian mixtures, 256 hidden units for Car Racing and 512 for Doom, and 20 training epochs (p.14). In Doom, the model also predicts whether the agent dies, and the episode ends when that probability is above 50% (p.14). At a very low temperature the model collapses to one mode and the monsters stop shooting, which makes the dream useless for training (p.9).

## Related concepts

- [World model](world-model.md): the MDN-RNN is the prediction half of the world model.
- [Variational autoencoder](variational-autoencoder.md): defines the latent vectors that the MDN-RNN predicts.
- [Learning in imagination](learning-in-imagination.md): sampling from the MDN-RNN generates the imagined environment.
- [Recurrent state-space model](recurrent-state-space-model.md): a later latent dynamics model that adds a deterministic memory path.

## Background

(None yet)

## My notes
