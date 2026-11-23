---
title: "Autoregressive transformer"
aliases: [decoder-only transformer, causal transformer, next-token prediction, GPT-style model]
updated: 2026-11-24
areas: [world-model]
sources: [2025-wham]
---

## One-line definition

A transformer that generates a sequence one token at a time, each time predicting the next token from all the tokens before it.

## Explanation

A causal attention mask lets each position see only earlier positions, so the model can be trained on whole sequences at once to predict every next token. At generation time, it samples a token, appends it, and repeats. This is the design behind large language models, and it works for any data that can be written as a sequence of tokens, including images that have been quantized and actions that have been discretized. Because each new token depends on the tokens before it, changing an earlier token changes everything that follows.

## What each source says

### World and Human Action Models towards gameplay ideation (2025)

[WHAM](../sources/2025-wham.md) trains a decoder-only transformer to predict the next token in a sequence of interleaved image and controller-action tokens, with no explicit marker telling it whether an image or action token comes next (p.4, Fig. 2). It is built on a modified nanoGPT implementation of GPT-2 (p.10). Generating by sampling one token at a time allows image or action tokens to be modified during generation, which enables prompting through edited frames or chosen actions (p.3). The largest model has 1.6B parameters and a context of 5,560 tokens, or one second of gameplay (p.4, Fig. 2).

## Related concepts

- [Vector quantization](vector-quantization.md): produces the image tokens the transformer predicts.
- [World model](world-model.md): WHAM uses this architecture as its world model.
- [Shortcut forcing](shortcut-forcing.md): a different transformer world model design, which generates each frame with a few denoising steps instead of token by token.
- [Action conditioning](action-conditioning.md): WHAM interleaves action tokens with image tokens so that predictions depend on the player's actions.
- [Creativity support](creativity-support.md): the purpose WHAM builds its transformer world model for.

## Background

(None yet)

## My notes
