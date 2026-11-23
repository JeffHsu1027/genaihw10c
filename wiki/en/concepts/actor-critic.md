---
title: "Actor-critic"
aliases: [actor critic, action model and value model, policy and value function, lambda-return, λ-return]
updated: 2026-11-24
areas: [reinforcement-learning]
sources: [2020-dreamer, 2021-dreamerv2, 2023-dreamerv3]
---

## One-line definition

A reinforcement learning method with two learned parts: an actor (policy) that chooses actions and a critic (value function) that estimates how much future reward the actor will collect from each state.

## Explanation

The critic learns to predict the return expected from a state, and the actor is updated to choose actions that the critic rates highly. The critic lets the actor account for rewards far in the future without waiting for them to happen. Value targets can be built in several ways that trade bias against variance: adding up observed rewards only, adding a few rewards and then trusting the critic, or blending many such estimates, as the λ-return does. Actors can be improved with sampled policy gradients, or, when everything between action and value is differentiable, by backpropagating the critic's value directly into the actor.

> **Explainer:** The actor is the player and the critic is the coach who says how promising each position looks; the player learns to move toward positions the coach likes.

## What each source says

### Dream to Control: Learning Behaviors by Latent Imagination (2020)

[Dreamer](../sources/2020-dreamer.md) trains an action model and a value model entirely on trajectories imagined by its world model (p.4). The value model's targets are λ-returns that mix imagined rewards with value estimates beyond a fixed number of steps (p.4, Eq. 6). The action model maximizes these targets by backpropagating analytic gradients through the imagined states, rewards and values, which differs from Reinforce-style methods such as A3C and PPO and from DDPG and SAC, which do not backpropagate through learned transitions (p.5). Without the value model, the same agent becomes shortsighted and fails on tasks that need long-horizon credit assignment (p.7, Fig. 7). The value targets use a discount of 0.99 and λ of 0.95, and no target network or entropy bonus was needed (p.14).

### Mastering Atari with Discrete World Models (2021)

[DreamerV2](../sources/2021-dreamerv2.md) also trains its actor and critic purely on imagined trajectories, with a horizon of 15 and λ-targets (p.5, Eq. 4). The critic uses a target network that is updated every 100 gradient steps (p.6). The actor loss mixes Reinforce gradients, which are unbiased but noisy, with straight-through gradients through the dynamics, which are biased but low-variance, and adds an entropy regularizer (p.6, Eq. 6). Reinforce gradients work substantially better for Atari, while backpropagating through the dynamics works substantially better for continuous control (p.6). Using only straight-through gradients is worse on 44 of 55 Atari games (p.10).

### Mastering Diverse Domains through World Models (2023)

[DreamerV3](../sources/2023-dreamerv3.md) trains its critic to predict a distribution over λ-returns, as a categorical distribution over exponentially spaced bins, because returns can be multi-modal and vary by orders of magnitude (p.5). The critic is also trained on replayed trajectories and is regularized toward an exponential moving average of its own parameters, which plays the role of a target network (p.6). The actor uses the Reinforce estimator for both discrete and continuous actions, with returns normalized by their percentile range so that one entropy scale works everywhere (p.6).

### Comparing the sources

- [Dreamer](../sources/2020-dreamer.md) trains the actor only by backpropagating value gradients through the learned dynamics, on continuous control tasks (p.5).
- [DreamerV2](../sources/2021-dreamerv2.md) keeps that estimator for continuous control but relies on Reinforce gradients for Atari (p.6). The two papers do not conflict: the best estimator depends on the domain.
- [Dreamer](../sources/2020-dreamer.md) did not need a target network or an entropy bonus (p.14).
- [DreamerV2](../sources/2021-dreamerv2.md) uses both, with policy entropy replacing external action noise for exploration (p.18). This is a design difference between versions, not a contradictory claim; DreamerV2 builds on Dreamer, and this summary is this Wiki's own.
- [DreamerV3](../sources/2023-dreamerv3.md) drops the domain-specific choice and uses Reinforce gradients for continuous control as well, together with a distributional critic and return normalization (p.6). This replaces the earlier design rather than contradicting the earlier results, which were obtained under per-domain settings.

## Related concepts

- [Learning in imagination](learning-in-imagination.md): where Dreamer trains its actor and critic.
- [Latent space planning](latent-space-planning.md): the alternative that searches actions at decision time instead of learning a policy.
- [Model-based reinforcement learning](model-based-reinforcement-learning.md): Dreamer's actor-critic relies on a learned model.
- [Return normalization](return-normalization.md): DreamerV3's way of scaling the actor's learning signal.
- [Symlog predictions](symlog-predictions.md): DreamerV3's critic is trained with the symexp twohot loss.

## Background

(None yet)

## My notes
