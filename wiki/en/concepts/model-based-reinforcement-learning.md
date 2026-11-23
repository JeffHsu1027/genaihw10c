---
title: "Model-based reinforcement learning"
aliases: [model-based RL, MBRL]
updated: 2026-11-24
areas: [reinforcement-learning, world-model]
sources: [2018-world-models, 2019-planet]
---

## One-line definition

Reinforcement learning that learns or uses a model of how the environment responds to actions, and uses that model to decide how to act or to learn how to act.

## Explanation

Model-free methods learn a policy or a value function directly from trial and error. Model-based methods first learn a dynamics model and then use it, either to plan at decision time or to generate extra experience for training a policy. A good model can make learning much more data efficient and may transfer to new tasks in the same environment. Errors in the model, however, can mislead the agent, and learning accurate models from images is difficult.

## What each source says

### World Models (2018)

[World Models](../sources/2018-world-models.md) learns a world model without rewards and then trains a small controller that uses the model, first as a source of features (p.5) and then as a complete replacement for the environment (p.7). The paper presents itself as a simplified demonstration of RNN-based world model and controller ideas from a series of papers between 1990 and 2015 (p.2).

### Learning Latent Dynamics for Planning from Pixels (2019)

[PlaNet](../sources/2019-planet.md) is purely model-based: it has no policy or value network and chooses every action by planning with its learned model (p.3). The paper lists the benefits it expects from planning with learned models: a richer training signal, no need to propagate rewards through Bellman backups, better performance from more search compute, and dynamics that can transfer to other tasks (p.1). It reaches the performance of strong model-free agents with about 200 times fewer episodes on average (p.2).

### Comparing the sources

- [World Models](../sources/2018-world-models.md) uses its model to train a policy ahead of time; at decision time the controller reacts to the model's hidden state without planning ahead (p.6).
- [PlaNet](../sources/2019-planet.md) has no policy and uses its model only at decision time, by searching over action sequences (p.3).
- Both warn that a purely deterministic model is easy to exploit: [World Models](../sources/2018-world-models.md) for its controller (p.9) and [PlaNet](../sources/2019-planet.md) for its planner (p.4, Fig. 2).
- PlaNet cites World Models as a hybrid agent that learns from imagined experience; this side-by-side comparison is this Wiki's own summary.

## Related concepts

- [World model](world-model.md): the model that model-based methods learn.
- [Latent space planning](latent-space-planning.md): using the model at decision time.
- [Learning in imagination](learning-in-imagination.md): using the model to train a policy.

## Background

(None yet)

## My notes
