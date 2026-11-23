---
title: "World Models"
authors: "David Ha, Jürgen Schmidhuber"
year: 2018
venue: "arXiv:1803.10122"
url: "https://arxiv.org/abs/1803.10122"
raw: "raw/world modelv4.pdf"
pages: 22
added: 2026-11-24
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
status: read
concepts: [world-model, variational-autoencoder, mixture-density-rnn, evolution-strategies, learning-in-imagination]
topics: [world-models]
---

## One-line summary

The agent is split into a large [world model](../concepts/world-model.md) that learns, without rewards, to compress and predict what it sees, and a tiny controller that acts on the world model's features; the agent can even be trained entirely inside the world model's own *dream* and then moved back to the real environment (p.1).

## Research question

Can a reinforcement learning agent put most of its capacity into a large, unsupervised world model and keep only a very small policy, so that the hard credit assignment problem is solved in a small search space (p.2)? And if the world model is accurate enough, can it replace the real environment during training (p.6)?

## Method

The agent has three components, loosely inspired by human perception and memory (p.2, Fig. 4):

- **V (vision)**: a [variational autoencoder](../concepts/variational-autoencoder.md) compresses each frame into a small latent vector z (p.3). Frames are resized to 64x64 RGB images and encoded by four convolutional layers; z has 32 dimensions for Car Racing and 64 for Doom (p.13).
- **M (memory)**: an LSTM with a mixture density output layer, the [MDN-RNN](../concepts/mixture-density-rnn.md), predicts a probability distribution over the next latent vector, `P(z[t+1] | a[t], z[t], h[t])`, as a mixture of Gaussians (p.3). A temperature parameter τ controls how random the sampled future is (p.3).
- **C (controller)**: a single linear layer maps the latent vector z and the RNN hidden state h to an action, `a = Wc [z h] + bc` (p.3, Eq. 1). It is kept deliberately small so that almost all of the agent's complexity lives in V and M (p.3).

V and M are trained first, without any reward signal, on rollouts collected by a random policy; only C sees the reward (p.5). C is then optimized with CMA-ES, an [evolution strategy](../concepts/evolution-strategies.md) that works well for solution spaces of up to a few thousand parameters (p.4). Training V and M separately was more practical than end-to-end training, and each took less than an hour on a single GPU (p.4).

For Car Racing, the procedure is to collect 10,000 random rollouts, train V, train M, define C, and solve for C's weights with CMA-ES (p.5). For VizDoom: Take Cover, M also predicts whether the agent dies in the next frame, which turns M into a complete virtual environment with the same interface as the real game (p.7). C is trained only inside this virtual environment and then deployed in the actual game (p.7); the real VizDoom environment is used only to collect random-policy data (p.15).

> **Explainer:** V is the agent's eyes, M is a memory that guesses what comes next, and C is a reflex that acts on what the eyes see and what the memory expects. Training C inside M is like rehearsing a sport only in your head and then playing the real match.

Training details from the appendix: the VAE is trained for one epoch with an L2 reconstruction loss plus a KL loss (p.13); the MDN-RNN uses 5 Gaussian mixtures, 256 hidden units for Car Racing and 512 for Doom, and is trained for 20 epochs (p.14); CMA-ES uses a population of 64, and each candidate's fitness is its average reward over 16 rollouts (p.14).

## Key results

- CarRacing-v0 counts as solved when the average reward over 100 consecutive trials reaches 900 (p.4).
- With both V and M, the agent scores 906 ± 21 over 100 random trials, the first reported solution; earlier deep RL methods scored between 591 and 652, and the best leaderboard entry scored 838 ± 11 (p.6, Table 1).
- With V alone, the agent wobbles on sharp corners and scores 632 ± 251; adding a hidden layer to C raises this to 788 ± 141, still short of solving the task (p.5).
- The controller has only 867 parameters, compared with 4,348,547 in the VAE and 422,368 in the MDN-RNN (p.5).
- VizDoom: Take Cover counts as solved when the agent survives more than 750 time steps on average over 100 rollouts (p.7).
- An agent trained only inside the dream survives about 900 time steps there (p.7) and about 1100 time steps when moved to the real game (p.8).
- Temperature matters: at τ = 0.1 the dream is almost deterministic, the monsters stop shooting, and the policy scores 2086 ± 140 in the dream but only 193 ± 58 in reality; the best transfer, 1092 ± 556, comes at τ = 1.15 (p.10, Table 2).
- The best Take Cover score on the Gym leaderboard at the time was 820 ± 58 (p.10).

## Limitations and open questions

- The controller can *cheat* the world model: in early experiments it found a way of moving that made the dream's monsters never shoot fireballs, an exploit that does not exist in the real game (p.8). The authors describe the weakness this way: "it'll find a policy that looks good under our dynamics model, but will fail in the actual environment" (p.9).
- A stochastic M and a higher temperature τ make such exploits harder, but too much randomness makes the dream too difficult to learn anything, so τ has to be tuned (p.10).
- V is trained separately and without rewards, so it can spend capacity on irrelevant details: it reproduced brick patterns on the Doom walls but missed task-relevant road tiles in Car Racing (p.12).
- The LSTM world model has limited capacity and may suffer catastrophic forgetting as more data is collected (p.12).
- The model simulates the future one time step at a time, without hierarchical planning or abstract reasoning (p.13).
- Both tasks were simple enough for a world model trained on random-policy data; harder environments would need an iterative procedure that alternates exploration and model training, possibly driven by curiosity, which the paper proposes but does not test (pp.10-11).

## Related concepts

- [World model](../concepts/world-model.md): the paper's V and M together.
- [Variational autoencoder](../concepts/variational-autoencoder.md): the V component.
- [Mixture density RNN](../concepts/mixture-density-rnn.md): the M component.
- [Evolution strategies](../concepts/evolution-strategies.md): how C is trained (CMA-ES).
- [Learning in imagination](../concepts/learning-in-imagination.md): training C inside the dream.

## Relation to other sources

No directly related sources yet.

## Background

- [Interactive version of the paper](https://worldmodels.github.io): the authors' web version, with live demos of the VAE and of the dream environments.

## My notes
