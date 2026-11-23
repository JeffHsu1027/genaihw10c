---
title: "Variational autoencoder"
aliases: [VAE, ConvVAE, convolutional variational autoencoder]
updated: 2026-11-24
areas: [world-model]
sources: [2018-world-models]
---

## One-line definition

A neural network that encodes an input into a small random latent vector and learns to decode that vector back into the input.

## Explanation

The encoder outputs the mean and spread of a Gaussian distribution, a latent vector is sampled from it, and the decoder reconstructs the input from the sample. Training balances reconstruction quality against keeping the latent distribution close to a simple prior. The prior limits how much information each latent vector can carry and keeps the latent space smooth, so nearby vectors decode into similar inputs.

> **Explainer:** Think of the latent vector as a short description of a picture that is detailed enough for someone to redraw the picture from it.

## What each source says

### World Models (2018)

[World Models](../sources/2018-world-models.md) uses a convolutional VAE as the V model to compress each frame into a latent vector z (p.3). Frames are resized to 64x64 pixels and passed through four convolutional layers; z has 32 dimensions in Car Racing and 64 in Doom (p.13). The VAE is trained for one epoch on random-policy data with an L2 reconstruction loss plus a KL loss (p.13). The authors note that the Gaussian prior also makes the world model more robust to unrealistic latent vectors produced by M (p.13). Because V is trained without rewards, it can keep task-irrelevant details and miss relevant ones (p.12).

## Related concepts

- [World model](world-model.md): the VAE is the compression half of the world model.
- [Mixture density RNN](mixture-density-rnn.md): predicts the next latent vector that the VAE defines.

## Background

(None yet)

## My notes
