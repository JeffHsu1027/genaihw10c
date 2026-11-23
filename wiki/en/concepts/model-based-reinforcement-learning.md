---
title: "Model-based reinforcement learning"
aliases: [model-based RL, MBRL]
updated: 2026-11-24
areas: [reinforcement-learning, world-model]
sources: [2018-world-models, 2019-planet, 2020-dreamer]
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

### Dream to Control: Learning Behaviors by Latent Imagination (2020)

[Dreamer](../sources/2020-dreamer.md) follows the classical agent structure of dynamics learning, behavior learning and environment interaction, with behavior learned inside the latent space of the world model (p.2). It argues that world models can interpolate past experience and offer analytic gradients of multi-step returns, which model-free actor-critics trained online or by experience replay cannot (p.1). With 5 million environment steps, it exceeds the final performance that the model-free D4PG reaches after 100 million steps (p.6, Fig. 6).

### Comparing the sources

- [World Models](../sources/2018-world-models.md) uses its model to train a policy ahead of time; at decision time the controller reacts to the model's hidden state without planning ahead (p.6).
- [PlaNet](../sources/2019-planet.md) has no policy and uses its model only at decision time, by searching over action sequences (p.3).
- Both warn that a purely deterministic model is easy to exploit: [World Models](../sources/2018-world-models.md) for its controller (p.9) and [PlaNet](../sources/2019-planet.md) for its planner (p.4, Fig. 2).
- [Dreamer](../sources/2020-dreamer.md) returns to training a policy ahead of time, like World Models, but with gradients instead of evolution and with a value model that looks beyond the imagination horizon (p.5).
- Dreamer reports that planning only within a fixed horizon, as PlaNet does, is shortsighted on tasks that need long-horizon credit assignment (p.7, Fig. 7). PlaNet itself pointed to the missing value function as a limitation (see the PlaNet page), so this is agreement rather than conflict.
- PlaNet and Dreamer cite World Models, and Dreamer builds on PlaNet; this side-by-side comparison is this Wiki's own summary.

## Related concepts

- [World model](world-model.md): the model that model-based methods learn.
- [Latent space planning](latent-space-planning.md): using the model at decision time.
- [Learning in imagination](learning-in-imagination.md): using the model to train a policy.

## Background

(None yet)

## My notes
