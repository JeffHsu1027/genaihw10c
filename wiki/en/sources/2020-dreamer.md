---
title: "Dream to Control: Learning Behaviors by Latent Imagination"
authors: "Danijar Hafner et al."
year: 2020
venue: "ICLR 2020 (arXiv:1912.01603)"
url: "https://arxiv.org/abs/1912.01603"
raw: "raw/(dreamerv1)DREAM TO CONTROL LEARNING BEHAVIORSv3.pdf"
pages: 20
added: 2026-11-24
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
status: to-read
concepts: [actor-critic, learning-in-imagination, world-model, model-based-reinforcement-learning, recurrent-state-space-model, latent-overshooting, latent-space-planning, variational-autoencoder]
topics: [world-models]
---

## One-line summary

Dreamer learns a [world model](../concepts/world-model.md) from images and then learns its behavior purely by [latent imagination](../concepts/learning-in-imagination.md): an [actor-critic](../concepts/actor-critic.md) is trained on imagined trajectories, and the actor is improved by propagating analytic value gradients back through the learned dynamics (p.1).

## Research question

Policies or planners that only maximize rewards within a fixed imagination horizon behave shortsightedly, and earlier work often used derivative-free optimization instead of the gradients that neural network dynamics offer (p.1). Can an agent learn long-horizon behaviors from images purely inside a learned world model, while accounting for rewards beyond the imagination horizon (p.1)?

## Method

- **World model**: the same latent dynamics as PlaNet, with a [recurrent state-space model](../concepts/recurrent-state-space-model.md) as the transition model, a CNN encoder for the representation model, a transposed CNN as the observation model, and a dense reward model (p.6). The parts are trained jointly with a variational bound made of reconstruction terms for images and rewards plus a KL regularizer, as in a [variational autoencoder](../concepts/variational-autoencoder.md) (p.6, Eq. 10).
- **Three processes**: Dreamer learns the dynamics from its dataset of past experience, learns action and value models from imagined trajectories, and executes the action model in the environment to grow the dataset, either interleaved or in parallel (p.2, Alg. 1).
- **Imagination**: imagined trajectories start from the model states of sequences drawn from past experience and roll forward with the transition model, the reward model and the policy for a fixed horizon (p.3). The world model is kept fixed while behaviors are learned (p.5).
- **Actor and critic**: the action model outputs a tanh-transformed Gaussian whose sample is written as a deterministic function of the network output plus noise, so gradients can pass through sampling (p.4, Eq. 3). The value model estimates the imagined rewards that the action model will collect, including those beyond the horizon (p.4, Eq. 2). Value targets are λ-returns, an exponentially weighted average of estimates that add up imagined rewards for some steps and then use the value model for the rest (p.4, Eq. 6).
- **Learning**: the value model regresses the λ-return targets, and the action model maximizes them by backpropagating analytic gradients through the values, rewards, imagined states and actions (p.5). Unlike Reinforce-style methods such as A3C and PPO, Dreamer backpropagates through the value model, and unlike DDPG and SAC it also backpropagates through the learned transitions (p.5).
- **Discrete actions and early termination**: straight-through gradients are used for discrete actions, and in tasks that can end early the model also predicts a discount factor that down-weights imagined steps that are likely to come after the episode ended (p.5).
- **Representation learning**: three ways to learn the world model are compared: image reconstruction as in PlaNet, contrastive estimation that predicts states from images instead of images from states, and reward prediction alone (pp.5-6).

> **Explainer:** Like World Models, Dreamer practises inside its own imagination. Instead of trying random variations of its behavior and keeping what works, it asks the model how a small change in each action would change the predicted future, and moves in the direction that improves it.

Implementation details from the appendix: Dreamer reuses the convolutional encoder and decoder of World Models and the RSSM of PlaNet, and every other function is three dense layers of 300 units with ELU activations (p.14). The latent distributions are 30-dimensional diagonal Gaussians (p.14). Batches contain 50 sequences of length 50, and Adam uses learning rates of `6e-4` for the world model and `8e-5` for the value and action models (p.14). The imagination horizon is 15, with a discount of 0.99 and λ of 0.95 (p.14). The KL term is not scaled but is clipped below 3 free nats, as in PlaNet (p.14). Training starts from 5 random episodes and alternates 100 training steps with collecting one episode, using Normal(0, 0.3) exploration noise and an action repeat of 2 (p.14). Latent overshooting, an entropy bonus and target networks were not needed (p.14). Each run uses one V100 GPU and 10 CPU cores and takes about 3 hours per million environment steps, compared with 11 hours for PlaNet and 24 hours for D4PG to reach similar performance (p.8).

> **Superseded:** [DreamerV2](2021-dreamerv2.md) replaces the Gaussian latents with 32 categorical variables of 32 classes each, which helps on 42 of 55 Atari games (p.9).

> **Superseded:** [DreamerV2](2021-dreamerv2.md) replaces the free nats with KL balancing (p.18).

## Key results

- The benchmark is 20 visual control tasks from the DeepMind Control Suite with 64x64x3 image observations, an action repeat of 2, and the same hyperparameters for all tasks (p.8).
- After 5 million environment steps, Dreamer reaches an average score of 823 across tasks, compared with 332 for PlaNet and 786 for D4PG after 100 million steps (p.6, Fig. 6).
- Dreamer keeps the data efficiency of PlaNet while exceeding the final performance of the best model-free agents (p.9).
- Learning a value model makes Dreamer robust to the length of the imagination horizon, while an action model trained without values and online planning with PlaNet both depend strongly on the horizon (p.4, Fig. 4).
- Without a value model, both alternatives behave shortsightedly and only succeed in reactive tasks such as the walker domain, while Dreamer also solves tasks that need long-horizon credit assignment such as acrobot and hopper (p.7, Fig. 7).
- With a horizon of 20, Dreamer outperforms both alternatives on 16 of 20 tasks with 4 ties; the same paragraph also mentions 19 tasks, so the exact count is (to be verified) (p.9).
- Pixel reconstruction gives the best world model on most tasks, contrastive estimation solves about half of the tasks, and predicting rewards alone was not sufficient (p.8, Fig. 8).
- Dreamer also learns successful behaviors on a subset of Atari games and a DeepMind Lab level with discrete actions and early termination (p.16, Fig. 9).
- An action repeat of 2 works best across tasks (p.19, Fig. 12).

## Limitations and open questions

- How well Dreamer works depends on the representation learning objective; reward prediction alone fails, and the authors expect better representation learning to be needed for visually more complex environments (p.9).
- In domains with discrete actions such as Atari and DeepMind Lab, agents that learn purely through world models are not yet competitive (p.16).

> **Superseded:** [DreamerV2](2021-dreamerv2.md) reaches human-level performance on 55 Atari games after 200 million steps and beats IQN and Rainbow (p.7, Table 1).

- Behaviors are learned only from imagined trajectories while the world model is held fixed, so they can only be as good as the model's predictions (p.5).
- The evaluation of the action repeat used an earlier hyperparameter setting and only 2 seeds (p.19, Fig. 12).

## Related concepts

- [Actor-critic](../concepts/actor-critic.md): the behavior learning algorithm, trained in imagination.
- [Learning in imagination](../concepts/learning-in-imagination.md): Dreamer learns behaviors purely by latent imagination.
- [World model](../concepts/world-model.md): the learned latent dynamics model.
- [Model-based reinforcement learning](../concepts/model-based-reinforcement-learning.md): the family Dreamer belongs to.
- [Recurrent state-space model](../concepts/recurrent-state-space-model.md): the transition model, taken from PlaNet.
- [Latent overshooting](../concepts/latent-overshooting.md): not needed by Dreamer.
- [Latent space planning](../concepts/latent-space-planning.md): the alternative Dreamer replaces.
- [Variational autoencoder](../concepts/variational-autoencoder.md): the reconstruction objective is a variational bound.

## Relation to other sources

- [Learning Latent Dynamics for Planning from Pixels](2019-planet.md): Dreamer learns the same world model as PlaNet but chooses actions with a learned action model instead of online planning (p.8). It re-runs PlaNet with the same action repeat for a fair comparison (p.8), and reports it as shortsighted on long-horizon tasks (p.7, Fig. 7).
- [Mastering Atari with Discrete World Models](2021-dreamerv2.md) (DreamerV2, 2021) is the direct successor of this paper, which it calls DreamerV1. It keeps the overall agent but switches to categorical latents, KL balancing and, for Atari, Reinforce gradients for the actor.
- [World Models](2018-world-models.md): Dreamer describes World Models as learning latent dynamics in a two-stage process to evolve linear controllers in imagination (p.7), and reuses its convolutional encoder and decoder (p.14).

## Background

- [Dreamer project page](https://danijar.com/dreamer): code and videos, linked from the paper.

## My notes
