---
title: "Model-based reinforcement learning"
aliases: [model-based RL, MBRL]
updated: 2026-11-24
areas: [reinforcement-learning, world-model]
sources: [2018-world-models, 2019-planet, 2020-dreamer, 2021-dreamerv2, 2023-dreamerv3, 2025-dreamer4]
---

## One-line definition

Reinforcement learning that learns or uses a model of how the environment responds to actions, and uses that model to decide how to act or to learn how to act.

## Explanation

In reinforcement learning, an agent acts in an environment, receives rewards, and learns by trial and error a policy, a rule for choosing actions, that collects as much reward as possible over time. Model-free methods learn a policy or a value function directly from trial and error. Model-based methods first learn a dynamics model and then use it, either to plan at decision time or to generate extra experience for training a policy. A good model can make learning much more data efficient and may transfer to new tasks in the same environment. Errors in the model, however, can mislead the agent, and learning accurate models from images is difficult.

## What each source says

### World Models (2018)

[World Models](../sources/2018-world-models.md) learns a world model without rewards and then trains a small controller that uses the model, first as a source of features (p.5) and then as a complete replacement for the environment (p.7). The paper presents itself as a simplified demonstration of RNN-based world model and controller ideas from a series of papers between 1990 and 2015 (p.2).

### Learning Latent Dynamics for Planning from Pixels (2019)

[PlaNet](../sources/2019-planet.md) is purely model-based: it has no policy or value network and chooses every action by planning with its learned model (p.3). The paper lists the benefits it expects from planning with learned models: a richer training signal, no need to propagate rewards through Bellman backups, better performance from more search compute, and dynamics that can transfer to other tasks (p.1). It reaches the performance of strong model-free agents with about 200 times fewer episodes on average (p.2).

### Dream to Control: Learning Behaviors by Latent Imagination (2020)

[Dreamer](../sources/2020-dreamer.md) follows the classical agent structure of dynamics learning, behavior learning and environment interaction, with behavior learned inside the latent space of the world model (p.2). It argues that world models can interpolate past experience and offer analytic gradients of multi-step returns, which model-free actor-critics trained online or by experience replay cannot (p.1). With 5 million environment steps, it exceeds the final performance that the model-free D4PG reaches after 100 million steps (p.6, Fig. 6).

### Mastering Atari with Discrete World Models (2021)

[DreamerV2](../sources/2021-dreamerv2.md) notes that Atari had historically required model-free algorithms to reach human-level performance, and that earlier world models of Atari were not competitive (p.2). It compares itself with two model-based Atari agents: SimPLe, which predicts frames in pixel space and trains PPO on them, and MuZero, which learns task-specific reward and value predictions for tree search without modeling images (pp.10-11, Table 3). MuZero is powerful but would need more than 2 months to train one Atari agent on a GPU, while DreamerV2 needs 10 days (p.11). The authors present DreamerV2 as proof that model-based RL can beat top model-free algorithms on the most competitive benchmarks (p.11).

### Mastering Diverse Domains through World Models (2023)

[DreamerV3](../sources/2023-dreamerv3.md) positions itself as a general algorithm and compares it with PPO, which is robust but data-hungry, and with MuZero, which is strong but complex and not publicly released (p.11). It outperforms PPO in every domain tested and MuZero on Atari with a fraction of the compute (p.8). In Minecraft it collects diamonds from scratch with 1 GPU for 9 days, while VPT needed human demonstrations and 720 GPUs for 9 days (p.11).

### Training Agents Inside of Scalable World Models (2025)

[Dreamer 4](../sources/2025-dreamer4.md) argues that world models can in principle learn from fixed datasets, which allows agents to be trained purely in imagination without online interaction (p.2). In the offline Minecraft setting it outperforms the VPT offline agent with 100 times less data, and a VLA agent finetuned from Gemma 3 (p.9, Fig. 3). Behavior cloning on top of the world model's representations also beats behavior cloning on Gemma 3, suggesting that video prediction learns an understanding of the world that is useful for decisions (p.12).

### Comparing the sources

- [World Models](../sources/2018-world-models.md) uses its model to train a policy ahead of time; at decision time the controller reacts to the model's hidden state without planning ahead (p.6).
- [PlaNet](../sources/2019-planet.md) has no policy and uses its model only at decision time, by searching over action sequences (p.3).
- Both warn that a purely deterministic model is easy to exploit: [World Models](../sources/2018-world-models.md) for its controller (p.9) and [PlaNet](../sources/2019-planet.md) for its planner (p.4, Fig. 2).
- [Dreamer](../sources/2020-dreamer.md) returns to training a policy ahead of time, like World Models, but with gradients instead of evolution and with a value model that looks beyond the imagination horizon (p.5).
- Dreamer reports that planning only within a fixed horizon, as PlaNet does, is shortsighted on tasks that need long-horizon credit assignment (p.7, Fig. 7). PlaNet itself pointed to the missing value function as a limitation (see the PlaNet page), so this is agreement rather than conflict.
- [DreamerV2](../sources/2021-dreamerv2.md) keeps Dreamer's policy learning in imagination and shows it can win on Atari, a benchmark the earlier sources did not reach (p.2).
- [DreamerV3](../sources/2023-dreamerv3.md) shifts the claim from beating model-free methods on one benchmark to working across many domains without retuning (p.2).
- [Dreamer 4](../sources/2025-dreamer4.md) moves from online learning to purely offline learning, where the model is the only place the agent can practise (p.10).
- PlaNet, Dreamer, DreamerV2, DreamerV3 and Dreamer 4 cite World Models, and each later paper builds on the previous one; this side-by-side comparison is this Wiki's own summary.

## Related concepts

- [World model](world-model.md): the model that model-based methods learn.
- [Latent space planning](latent-space-planning.md): using the model at decision time.
- [Learning in imagination](learning-in-imagination.md): using the model to train a policy.
- [Offline reinforcement learning](offline-reinforcement-learning.md): learning without environment interaction, as in Dreamer 4.
- [Actor-critic](actor-critic.md): the policy learner that the Dreamer agents train inside their world models.

## Background

(None yet)

## My notes
