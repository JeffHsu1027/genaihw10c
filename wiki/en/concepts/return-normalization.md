---
title: "Return normalization"
aliases: [percentile return normalization, retnorm]
updated: 2026-11-24
areas: [reinforcement-learning]
sources: [2023-dreamerv3, 2025-dreamer4]
---

## One-line definition

Scaling the returns used to train a policy by a robust estimate of their range, so that the balance between maximizing reward and exploring does not depend on the reward scale of the environment.

## Explanation

Policy learning with an entropy bonus has to balance two terms: the return, which depends on how rewards are scaled, and the entropy, which does not. If rewards are large, the entropy bonus becomes irrelevant; if they are small or rare, exploration dominates forever. Normalizing advantages or dividing by a standard deviation can amplify noise when rewards are sparse. Dividing returns by the spread between a low and a high percentile, and only shrinking large returns while leaving small ones untouched, keeps the entropy scale meaningful across environments and stays robust to outliers.

## What each source says

### Mastering Diverse Domains through World Models (2023)

[DreamerV3](../sources/2023-dreamerv3.md) normalizes returns so that they fall roughly into the interval from 0 to 1, which lets it use a fixed entropy scale of `3e-4` across domains (p.6). The scale is the range between the 5th and 95th return percentiles, smoothed with an exponential moving average, and returns are divided by it only when it exceeds 1, so that noise under sparse rewards is not amplified (p.6). The paper argues that advantage normalization, normalization by standard deviation and constrained entropy targets all failed to give stable hyperparameters across domains (p.6). In the ablations, return normalization is the second most important robustness technique after the KL objective (p.10).

### Training Agents Inside of Scalable World Models (2025)

[Dreamer 4](../sources/2025-dreamer4.md) no longer uses return normalization: its PMPO policy loss depends only on the sign of the advantages, which removes the need to normalize returns or advantages and gives equal focus to tasks with different return scales (p.7). The paper contrasts this explicitly with the return normalization and entropy regularizer of DreamerV3 (p.29).

### Comparing the sources

- [DreamerV3](../sources/2023-dreamerv3.md) needs return normalization so that a fixed entropy scale works across domains (p.6).
- [Dreamer 4](../sources/2025-dreamer4.md) avoids the problem by changing the policy loss instead of rescaling returns (p.7). The two are not in conflict; Dreamer 4 builds on DreamerV3, and this summary is this Wiki's own.

## Related concepts

- [Actor-critic](actor-critic.md): return normalization scales the actor's learning signal.
- [Symlog predictions](symlog-predictions.md): the other DreamerV3 technique for handling reward scale.

## Background

(None yet)

## My notes
