---
title: "Actor-critic"
aliases: [actor critic, action model and value model, policy and value function, lambda-return, λ-return]
updated: 2026-11-24
areas: [reinforcement-learning]
sources: [2020-dreamer]
---

## One-line definition

A reinforcement learning method with two learned parts: an actor (policy) that chooses actions and a critic (value function) that estimates how much future reward the actor will collect from each state.

## Explanation

The critic learns to predict the return expected from a state, and the actor is updated to choose actions that the critic rates highly. The critic lets the actor account for rewards far in the future without waiting for them to happen. Value targets can be built in several ways that trade bias against variance: adding up observed rewards only, adding a few rewards and then trusting the critic, or blending many such estimates, as the λ-return does. Actors can be improved with sampled policy gradients, or, when everything between action and value is differentiable, by backpropagating the critic's value directly into the actor.

> **Explainer:** The actor is the player and the critic is the coach who says how promising each position looks; the player learns to move toward positions the coach likes.

## What each source says

### Dream to Control: Learning Behaviors by Latent Imagination (2020)

[Dreamer](../sources/2020-dreamer.md) trains an action model and a value model entirely on trajectories imagined by its world model (p.4). The value model's targets are λ-returns that mix imagined rewards with value estimates beyond a fixed number of steps (p.4, Eq. 6). The action model maximizes these targets by backpropagating analytic gradients through the imagined states, rewards and values, which differs from Reinforce-style methods such as A3C and PPO and from DDPG and SAC, which do not backpropagate through learned transitions (p.5). Without the value model, the same agent becomes shortsighted and fails on tasks that need long-horizon credit assignment (p.7, Fig. 7). The value targets use a discount of 0.99 and λ of 0.95, and no target network or entropy bonus was needed (p.14).

## Related concepts

- [Learning in imagination](learning-in-imagination.md): where Dreamer trains its actor and critic.
- [Latent space planning](latent-space-planning.md): the alternative that searches actions at decision time instead of learning a policy.
- [Model-based reinforcement learning](model-based-reinforcement-learning.md): Dreamer's actor-critic relies on a learned model.

## Background

(None yet)

## My notes
