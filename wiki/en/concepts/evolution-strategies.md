---
title: "Evolution strategies"
aliases: [ES, CMA-ES, covariance matrix adaptation evolution strategy]
updated: 2026-11-24
areas: [reinforcement-learning]
sources: [2018-world-models]
---

## One-line definition

A family of black-box optimization methods that improve a population of candidate solutions by sampling, scoring and keeping the better ones, without computing gradients.

## Explanation

Each generation samples many parameter vectors, scores each one by running it, and shifts the sampling distribution toward the best scorers. CMA-ES also adapts the covariance of the sampling distribution, learning which directions in parameter space matter. Because only a final score is needed, evolution strategies cope with sparse or delayed rewards and are easy to run in parallel, but they become inefficient when there are very many parameters.

## What each source says

### World Models (2018)

[World Models](../sources/2018-world-models.md) trains its small controller with CMA-ES because the method works well for solution spaces of up to a few thousand parameters (p.4). The authors point out that evolution strategies only need the final cumulative reward and are easy to parallelize (p.12). They use a population of 64, and each candidate's fitness is its average reward over 16 rollouts (p.14). In Car Racing, the best agent reached an average of 900.46 over 1024 rollouts after 1800 generations (p.14).

## Related concepts

- [Learning in imagination](learning-in-imagination.md): in VizDoom, each candidate controller is scored inside the imagined environment.

## Background

(None yet)

## My notes
