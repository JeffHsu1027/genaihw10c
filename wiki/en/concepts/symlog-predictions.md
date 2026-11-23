---
title: "Symlog predictions"
aliases: [symlog, symexp, symlog squared error, symexp twohot loss, twohot encoding]
updated: 2026-11-24
areas: [reinforcement-learning, world-model]
sources: [2023-dreamerv3, 2025-dreamer4]
---

## One-line definition

A way to predict quantities whose scale is unknown by training a network on a log-like compressed version of the target, or on a classification over exponentially spaced bins, instead of on the raw value.

## Explanation

Rewards, values and observations can be tiny in one environment and huge in another. A squared loss on raw targets can diverge on large values, while absolute or Huber losses learn slowly, and normalizing by running statistics makes the targets keep shifting. The symlog function compresses large positive and negative values but stays close to the identity near zero, and its inverse, symexp, turns predictions back into the original scale. For noisy targets, a network can instead output probabilities over bins spaced in symlog space and be trained with a classification loss against a twohot target, which spreads the target over the two nearest bins; the gradient then no longer grows with the size of the target.

> **Explainer:** It is like measuring everything on a logarithmic ruler: a coin and a building can both be read without changing rulers.

## What each source says

### Mastering Diverse Domains through World Models (2023)

[DreamerV3](../sources/2023-dreamerv3.md) introduces the symlog squared error and the symexp twohot loss as a simple answer to targets of unknown scale (p.7). It applies symlog to vector observations for the encoder and decoder, and uses the symexp twohot loss for the reward predictor and the critic (p.7). The bins span symexp of the range from minus 20 to plus 20, and the output weights of twohot heads are initialized to zero so that the agent does not hallucinate rewards and values at the start (p.18). In the ablations, removing the symexp twohot loss and falling back to a Huber loss hurts performance on average, and removing observation symlog also hurts (p.10, Fig. 6).

### Training Agents Inside of Scalable World Models (2025)

[Dreamer 4](../sources/2025-dreamer4.md) parameterizes both its reward head and its value head as symexp twohot outputs, following DreamerV3, to learn rewards and values robustly across orders of magnitude (p.7).

### Comparing the sources

- [DreamerV3](../sources/2023-dreamerv3.md) introduces the technique for observations, rewards and values (p.7).
- [Dreamer 4](../sources/2025-dreamer4.md) keeps it for rewards and values even though most other parts of the agent change (p.7). Dreamer 4 builds on DreamerV3; this summary is this Wiki's own.

## Related concepts

- [Return normalization](return-normalization.md): the other DreamerV3 technique for handling reward scale.
- [Actor-critic](actor-critic.md): the critic is trained with the symexp twohot loss.
- [World model](world-model.md): its reward predictor and vector decoder use symlog.

## Background

(None yet)

## My notes
