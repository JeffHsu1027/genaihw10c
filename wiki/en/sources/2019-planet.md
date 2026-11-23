---
title: "Learning Latent Dynamics for Planning from Pixels"
authors: "Danijar Hafner et al."
year: 2019
venue: "ICML 2019 (arXiv:1811.04551)"
url: "https://arxiv.org/abs/1811.04551"
raw: "raw/(planet)Learning Latent Dynamics for Planning from Pixels v5.pdf"
pages: 20
added: 2026-11-24
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
status: read
concepts: [model-based-reinforcement-learning, world-model, recurrent-state-space-model, latent-overshooting, latent-space-planning, variational-autoencoder]
topics: [world-models]
---

## One-line summary

PlaNet (Deep Planning Network) is a purely [model-based](../concepts/model-based-reinforcement-learning.md) agent that learns a latent [world model](../concepts/world-model.md) from images and chooses every action by fast online planning in latent space, without a policy or value network (p.1).

## Research question

Can a dynamics model learned from pixels be accurate enough to plan with, on control tasks harder than those previously solved by planning with learned models (p.1)? Such models are hard to learn because of model errors, errors that accumulate over multi-step predictions, the need to capture several possible futures, and overconfident predictions outside the training distribution (p.1).

## Method

- **Setting**: each task is treated as a partially observable Markov decision process, because a single image does not reveal the full state of the environment (p.2).
- **Model**: PlaNet learns a transition model, an observation model, a reward model, and an encoder that infers a belief over the current hidden state from past images and actions (p.3). The observation model provides a rich training signal but is not used for planning (p.3).
- **[Recurrent state-space model](../concepts/recurrent-state-space-model.md) (RSSM)**: the latent state is split into a deterministic part carried by an RNN and a stochastic part sampled from a Gaussian (p.4, Eq. 4). A purely deterministic RNN cannot capture several possible futures and lets the planner exploit model errors, while a purely stochastic model has trouble remembering information over many steps (p.4, Fig. 2). The authors' key finding is that "both stochastic and deterministic paths in the transition model are crucial for successful planning" (p.3).
- **Training objective**: the model, including the encoder in the style of a [variational autoencoder](../concepts/variational-autoencoder.md), is trained with a variational bound made of a reconstruction term and a KL term between the encoder's posterior and the transition prior (p.4, Eq. 3).
- **[Latent overshooting](../concepts/latent-overshooting.md)**: a generalized objective that also trains multi-step predictions of every distance directly in latent space, without decoding extra images (p.5).
- **[Planning](../concepts/latent-space-planning.md)**: at every step, the cross entropy method (CEM) searches for the best action sequence under the model, and only the first action is executed, as in model-predictive control (p.3). Each candidate sequence is scored by rolling the model forward in latent space and summing the predicted rewards, so no images are generated during planning (p.3).
- **Data collection**: starting from a few random seed episodes, PlaNet alternates between training the model and collecting a new episode by planning with small Gaussian exploration noise; each chosen action is repeated several times (p.3).

> **Explainer:** Instead of learning reflexes, PlaNet thinks before every move: it imagines many possible action plans inside its model, keeps the most promising ones, refines them, and then takes only the first step of the best plan.

Implementation details from the appendix: the deterministic path is a GRU with 200 units, other functions are two fully connected layers of 200 units, and the stochastic state is a 30-dimensional diagonal Gaussian (p.12). Images are 64x64x3 pixels with the bit depth reduced to 5 bits (p.12). Training uses Adam with a learning rate of `1e-3` on batches of 50 sequence chunks of length 50 (p.12). The KL term is not penalized below 3 free nats (p.12). CEM uses a horizon of 12, 10 iterations, 1000 candidates, and refits to the best 100 (p.12). Training starts from 5 seed episodes and adds an episode every 100 update steps; the action repeat is between 2 and 8 depending on the task (p.12). Training takes 10 to 20 hours on a single V100 GPU (p.6).

## Key results

- The benchmark is six image-based DeepMind Control Suite tasks: cartpole swingup, reacher easy, cheetah run, finger spin, cup catch and walker walk, all seen as 64x64x3 images (p.6).
- Within 100 episodes, PlaNet outperforms A3C trained from proprioceptive states for 100,000 episodes on all tasks (p.6).
- After 500 episodes, PlaNet performs similarly to D4PG trained from images for 100,000 episodes, except on finger spin (p.6).
- Final scores of PlaNet after 1,000 episodes versus D4PG after 100,000 episodes: cartpole 821 vs 862, reacher 832 vs 967, cheetah 662 vs 524, finger 700 vs 985, cup 930 vs 980, walker 951 vs 968 (p.7, Table 1).
- On cheetah running, PlaNet exceeds the final performance of D4PG by a relative 26% (p.6). The data efficiency gain over D4PG ranges from a factor of 40 to more than 500 depending on the task (p.7, Table 1), about 200 times fewer episodes on average (p.2).
- Model ablation: removing either path hurts on every task; the deterministic part helps the model remember, and without the stochastic part the agent does not learn at all (p.6, Fig. 4).
- Agent ablation: collecting data online by planning helps on all tasks and is necessary for cartpole, finger and walker, and refining plans with CEM beats picking the best of 1000 random sequences (p.6, Fig. 5).
- A single agent trained on all six tasks, without being told which task it faces, solves all of them while learning more slowly (p.6).
- Latent overshooting substantially helps a different model (DRNN) but slightly reduces the performance of the RSSM, so the final agent does not need it (p.14, Fig. 8).
- The RSSM produces pixel-accurate open-loop video predictions for 50 steps into the future on the cheetah task (p.18, Fig. 10).

## Limitations and open questions

- The planner only sees rewards up to its planning horizon; the authors suggest learning a value function to account for rewards beyond it (p.8).
- The action repeat is fixed by hand; learning temporal abstraction, possibly with hierarchical models, is left for future work (p.8).
- Planning evaluates thousands of action sequences at every step, which is why everything has to stay in latent space (p.3). Gradient-based planning could make the agent more efficient (p.8).
- The model is trained by reconstructing images; learning representations without reconstruction could help in visually more diverse tasks (p.8).
- Final performance stays below D4PG on finger spin (700 vs 985) and reacher (832 vs 967) (p.7, Table 1).
- One of the two proposed techniques, latent overshooting, is not needed by the final agent (p.5).

## Related concepts

- [Model-based reinforcement learning](../concepts/model-based-reinforcement-learning.md): PlaNet is a purely model-based agent.
- [World model](../concepts/world-model.md): PlaNet's latent dynamics model.
- [Recurrent state-space model](../concepts/recurrent-state-space-model.md): the model architecture proposed here.
- [Latent overshooting](../concepts/latent-overshooting.md): the multi-step objective proposed here.
- [Latent space planning](../concepts/latent-space-planning.md): how PlaNet chooses actions.
- [Variational autoencoder](../concepts/variational-autoencoder.md): the RSSM is trained like a sequential VAE.

## Relation to other sources

- [World Models](2018-world-models.md): PlaNet reuses the convolutional encoder and deconvolutional decoder of World Models (p.12) and lists World Models among hybrid agents that learn a policy from imagined experience (p.17). Where World Models trains a small controller inside its dream, PlaNet has no policy at all and replans with the model at every step (p.3). David Ha is an author of both papers (p.1).

## Background

- [PlaNet project page](https://danijar.com/planet): code and videos of the trained agents, linked from the paper.

## My notes
