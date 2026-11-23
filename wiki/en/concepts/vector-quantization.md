---
title: "Vector quantization"
aliases: [VQGAN, VQ-VAE, ViT-VQGAN, discrete image tokens, image tokenizer]
updated: 2026-11-24
areas: [world-model]
sources: [2025-wham]
---

## One-line definition

Compressing an input such as an image into a short sequence of entries from a learned codebook, so that it can be represented as discrete tokens.

## Explanation

An encoder turns the input into a grid of vectors, and each vector is replaced by the closest entry in a learned codebook; the index of that entry becomes a token. A decoder learns to rebuild the input from the tokens. VQGAN-style models add perceptual and adversarial losses so that the reconstructions look sharp. The result lets images be handled like words in a sentence, which makes them easy to combine with other discrete data and to model with the same sequence models used for text. The number of tokens per image trades reconstruction quality against sequence length and speed.

## What each source says

### World and Human Action Models towards gameplay ideation (2025)

[WHAM](../sources/2025-wham.md) frames gameplay as a sequence of discrete tokens and uses a VQGAN image encoder to turn each frame into tokens (p.3). The smaller models use a VQGAN of about 60M parameters that maps 128 by 128 images to 256 tokens from a vocabulary of 4,096 (p.10). The 1.6B model uses a ViT-VQGAN of about 300M parameters that maps 300 by 180 images to 540 tokens from a vocabulary of 16,384 (p.10). The number of tokens per image is a key hyperparameter that trades image quality against generation speed and context length (p.3). The higher-resolution tokenizer raises the ceiling on reconstruction quality and improves FVD (p.4).

## Related concepts

- [Autoregressive transformer](autoregressive-transformer.md): models the token sequences produced by the quantizer.
- [Variational autoencoder](variational-autoencoder.md): a related autoencoder with continuous, not discrete, latents.
- [Categorical latents](categorical-latents.md): another discrete representation, sampled inside a world model rather than looked up from a codebook.

## Background

(None yet)

## My notes
