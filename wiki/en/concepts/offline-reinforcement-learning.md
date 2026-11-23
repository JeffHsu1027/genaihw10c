---
title: "Offline reinforcement learning"
aliases: [offline RL, batch reinforcement learning, learning from fixed datasets]
updated: 2026-11-24
areas: [reinforcement-learning]
sources: [2025-dreamer4]
---

## One-line definition

Reinforcement learning from a fixed, previously collected dataset, without letting the agent interact with the environment while it learns.

## Explanation

Online reinforcement learning improves a policy by trying it out, which can be slow, unsafe or impossible for real robots and other costly systems. Offline reinforcement learning instead learns only from logged experience, such as recordings of people or earlier agents. The difficulty is that the agent cannot check what happens when it does something the data never shows, so naive methods become overconfident about unseen actions. A world model trained on the dataset offers one way out: the agent can practise inside the model, which generates new experience without touching the real environment, while staying close to behavior seen in the data.

## What each source says

### Training Agents Inside of Scalable World Models (2025)

[Dreamer 4](../sources/2025-dreamer4.md) argues that learning offline matters for applications such as physical robots, where deploying partially trained policies is unsafe and resetting scenes and providing rewards is hard (p.10). It learns only from the 2.5K hours of the VPT contractor dataset, with no environment interaction (p.10). Its reinforcement learning happens inside the world model, so it counts as offline even though it is on-policy within imagination (p.11). A KL term toward the behavior-cloned policy keeps the learned policy within the space of reasonable behaviors (p.8). Dreamer 4 is the first agent to obtain diamonds in Minecraft purely from offline data (p.1).

## Related concepts

- [Learning in imagination](learning-in-imagination.md): practising inside a world model is how Dreamer 4 improves offline.
- [Model-based reinforcement learning](model-based-reinforcement-learning.md): the learned model is what makes offline improvement possible here.
- [Action conditioning](action-conditioning.md): the world model must learn how actions in the logged data change the world.

## Background

(None yet)

## My notes
