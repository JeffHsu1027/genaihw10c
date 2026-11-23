---
title: "Latent space planning"
aliases: [planning in latent space, online planning, model-predictive control, MPC, CEM planning]
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
sources: [2019-planet, 2020-dreamer]
---

## One-line definition

Choosing actions by searching over candidate action sequences inside a learned latent dynamics model and scoring them by predicted rewards, without generating observations.

## Explanation

At each step, the agent infers its current latent state, imagines the outcome of many candidate action sequences with the model, and picks the sequence with the highest predicted return. In model-predictive control, only the first action is executed and the search is repeated after the next observation, so the plan can adapt to what actually happens. The cross entropy method is a common search procedure: sample sequences, keep the best ones, refit the sampling distribution to them, and repeat. Planning in the latent space is fast because no images need to be produced.

> **Explainer:** It is like a chess player who looks a few moves ahead before every move, then thinks again after seeing the opponent's reply.

## What each source says

### Learning Latent Dynamics for Planning from Pixels (2019)

[PlaNet](../sources/2019-planet.md) plans with CEM inside its model and replans at every step, as in model-predictive control (p.3). After each new observation the search starts again from a zero-mean, unit-variance belief over action sequences, to avoid local optima (p.3). It scores each candidate with a single sampled trajectory, which leaves more of the compute budget for evaluating many different sequences (p.3). The settings are a horizon of 12, 10 iterations, 1000 candidates, and refitting to the best 100 (p.12). Iterative refinement with CEM beats choosing the best of 1000 random sequences on all tasks (p.6, Fig. 5). With the true simulator on cheetah, a horizon of 6 is too short and the best horizon is near 8, while much longer horizons hurt because the search space grows (p.20, Fig. 12). Because PlaNet has no value function, rewards beyond the horizon are ignored, and the authors suggest learning one (p.8).

### Dream to Control: Learning Behaviors by Latent Imagination (2020)

[Dreamer](../sources/2020-dreamer.md) compares its learned action and value models with online planning by PlaNet on the same world model (p.4, Fig. 4). Planning, like an action model trained without values, considers only rewards within the horizon and behaves shortsightedly, succeeding only in reactive tasks such as walker (p.7, Fig. 7). Dreamer also trains faster: about 3 hours per million environment steps, against 11 hours for online planning with PlaNet (p.8).

### Comparing the sources

- [PlaNet](../sources/2019-planet.md) argues that planning can improve just by spending more search compute and that learned dynamics can transfer across tasks (p.1).
- [Dreamer](../sources/2020-dreamer.md) shows that, without a value function, planning within a fixed horizon is shortsighted, and replaces it with a learned policy and value (p.7, Fig. 7).
- These are not in conflict: [PlaNet](../sources/2019-planet.md) already named the missing value function as a limitation (p.8). Dreamer builds on PlaNet, and this summary is this Wiki's own.

## Related concepts

- [Model-based reinforcement learning](model-based-reinforcement-learning.md): planning is one way to use a learned model.
- [Recurrent state-space model](recurrent-state-space-model.md): the model PlaNet plans with.
- [Learning in imagination](learning-in-imagination.md): the other way to use a model; it trains a policy on imagined experience ahead of time, while planning searches at decision time.
- [Actor-critic](actor-critic.md): the learned policy and value that Dreamer uses instead of planning.

## Background

(None yet)

## My notes
