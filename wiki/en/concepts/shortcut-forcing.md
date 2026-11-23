---
title: "Shortcut forcing"
aliases: [shortcut models, diffusion forcing, flow matching, x-prediction]
updated: 2026-11-24
areas: [world-model]
sources: [2025-dreamer4]
---

## One-line definition

A training objective for video world models that combines diffusion forcing, which lets every frame of a sequence have its own noise level, with shortcut models, which learn to take large denoising steps, so each new frame can be generated in only a few network passes.

## Explanation

Diffusion and flow matching models generate data by starting from noise and removing it step by step, which usually takes many network passes. Shortcut models also tell the network how large a step to take and train large steps to match two smaller ones, so a few steps can replace many. Diffusion forcing applies noise to each frame of a sequence separately, so a model can generate the next frame from a clean or lightly noised history, which is what an interactive world model needs. Predicting the clean frame directly, rather than the direction from noise to data, tends to produce smoother outputs that accumulate fewer errors when frames are generated one after another.

> **Explainer:** A usual diffusion model walks from fog to a clear picture in many tiny steps. A shortcut model learns to take a few long strides, and diffusion forcing lets it do this one frame at a time while looking back at frames it has already drawn.

## What each source says

### Training Agents Inside of Scalable World Models (2025)

[Dreamer 4](../sources/2025-dreamer4.md) introduces shortcut forcing to train its dynamics model, building on diffusion forcing and shortcut models (p.5). It predicts clean representations instead of velocities, because velocity prediction produces high-frequency outputs that cause errors to accumulate in long frame-by-frame rollouts (p.6). A ramp weight that grows linearly with the signal level focuses the loss on less noisy inputs, which carry more learning signal (p.6). Generation uses 4 sampling steps per frame (p.6). Shortcut forcing with 4 steps approaches the quality of diffusion forcing with 64 steps, making generation 16 times faster (p.16, Fig. 8). Predicting clean representations, computing the loss in that space, and adding the ramp weight substantially improve quality, especially for long generations (p.16).

## Related concepts

- [World model](world-model.md): shortcut forcing trains the Dreamer 4 world model.
- [Action conditioning](action-conditioning.md): actions are fed to the same dynamics transformer.
- [Recurrent state-space model](recurrent-state-space-model.md): the earlier, variational alternative for the dynamics.
- [Autoregressive transformer](autoregressive-transformer.md): the WHAM alternative, which generates each frame token by token instead of by denoising.

## Background

(None yet)

## My notes
