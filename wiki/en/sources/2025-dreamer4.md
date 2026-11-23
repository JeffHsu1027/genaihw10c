---
title: "Training Agents Inside of Scalable World Models"
authors: "Danijar Hafner, Wilson Yan, Timothy Lillicrap"
year: 2025
venue: "arXiv:2509.24527"
url: "https://arxiv.org/abs/2509.24527"
raw: "raw/(dreamerv4)Training Agents Inside of Scalable World Modelsv1.pdf"
pages: 32
added: 2026-11-24
updated: 2026-11-24
areas: [world-model, reinforcement-learning]
status: to-read
concepts: [shortcut-forcing, offline-reinforcement-learning, action-conditioning, world-model, learning-in-imagination, actor-critic, recurrent-state-space-model, symlog-predictions, return-normalization, model-based-reinforcement-learning]
topics: [world-models]
---

## One-line summary

Dreamer 4 replaces the recurrent world model of earlier Dreamers with a scalable transformer world model trained by [shortcut forcing](../concepts/shortcut-forcing.md), and becomes the first agent to obtain diamonds in Minecraft purely from offline data, by [reinforcement learning inside the world model](../concepts/learning-in-imagination.md) without any environment interaction (p.1).

## Research question

Earlier world-model agents such as DreamerV3 are fast and accurate in narrow environments but cannot fit complex, diverse data, while large controllable video models handle diverse scenes but still miss precise object interactions and need many GPUs to run in real time (p.2). Can one world model be both accurate enough and fast enough to train a capable agent purely in imagination, from a fixed [offline](../concepts/offline-reinforcement-learning.md) dataset (p.2)?

## Method

- **Three phases**: first pretrain a tokenizer and a dynamics model on videos and, optionally, actions; then finetune the world model with task inputs to predict actions and rewards; finally improve the policy by imagination training (p.4).
- **Causal tokenizer**: a transformer encoder and decoder compress each frame into continuous representations through a low-dimensional bottleneck with a tanh activation, trained by masked autoencoding with a mean squared error plus perceptual loss (p.5).
- **Interactive dynamics**: a transformer predicts the next representations from interleaved actions and noisy representations, using [shortcut forcing](../concepts/shortcut-forcing.md) so that each frame needs only 4 forward passes (p.5). The network predicts clean representations instead of velocities, which avoids error accumulation over long rollouts, and the loss is weighted by a ramp that favors signal levels with more learning signal (p.6).
- **[Action conditioning](../concepts/action-conditioning.md)**: each action component, such as mouse and keyboard, is encoded into tokens; for unlabeled videos only a learned placeholder embedding is used, so the model can train on videos without actions (p.5).
- **Agent finetuning**: agent tokens with task embeddings are inserted into the transformer to predict the policy and the reward; other tokens cannot attend to the agent tokens, which prevents the world model from being influenced by the current task (pp.6-7). The reward head uses a [symexp twohot](../concepts/symlog-predictions.md) output, following DreamerV3 (p.7).
- **Imagination training**: the transformer is frozen, and a policy head and a value head are trained on rollouts that the world model generates from dataset contexts, with one rollout per context (p.7). The value head learns λ-returns with a discount of 0.997 (p.7). The policy is trained with PMPO, which averages separate likelihood losses over states with positive and negative advantages and adds a KL term toward the behavior-cloned policy, so no return normalization is needed (pp.7-8). See [actor-critic](../concepts/actor-critic.md).
- **Efficient transformer**: separate space and time attention, temporal attention only every 4 layers, grouped-query attention, and alternating short and long training batches make inference fast (p.8).

> **Explainer:** First the agent watches thousands of hours of other people playing and learns how the game reacts to mouse and keyboard; then it copies what players do; finally it practises on its own inside its learned copy of the game, where mistakes cost nothing.

Implementation details: the model has 2B parameters, 400M for the tokenizer and 1.6B for the dynamics, trained on 256 to 1024 TPU-v5p chips (p.9). Minecraft uses 256 spatial tokens and a context of 192 frames (p.9). The main dataset is the VPT contractor dataset with 2541 hours of gameplay recorded at 20 FPS (p.9). Past inputs are slightly corrupted to a signal level of 0.1 during generation so the model tolerates its own small errors (p.6).

## Key results

- On the offline diamond challenge, evaluated over 1000 episodes of 60 minutes each, Dreamer 4 reaches success rates above 90% up to the stone pickaxe, 29% for the iron pickaxe, and obtains diamonds in 0.7% of episodes (p.12).
- The finetuned VPT agent progresses only up to sticks, which it reaches 53% of the time, and the VLA agent built on Gemma 3 reaches the iron pickaxe in 11% of episodes (p.12).
- Dreamer 4 outperforms the VPT offline agent while using 100 times less data (p.9, Fig. 3).
- Imagination training improves both success rates and the time needed to reach milestones, and helps more the harder the milestone is (p.12).
- Behavior cloning on top of the world model's representations outperforms behavior cloning on Gemma 3 or from scratch (p.12).
- In human interaction tests, players complete 14 of 16 Minecraft tasks inside the Dreamer 4 world model, compared with 5 of 16 for the large Oasis model (p.13).
- The world model runs faster than 20 FPS on a single H100 GPU, with a context of 9.6 seconds compared with 0.8 to 1.6 seconds for earlier Minecraft world models (p.13).
- With actions for only 100 of the 2541 hours of video, action-conditioned generation reaches 85% of the PSNR and 100% of the SSIM of training with all actions (p.14).
- When actions are given only for the Overworld, action conditioning still transfers to the Nether and End, reaching 76% of the PSNR and 80% of the SSIM of the fully labeled model (p.15).
- Shortcut forcing with 4 sampling steps approaches the quality of diffusion forcing with 64 steps, 16 times faster (p.16, Fig. 8); the full design reaches an FVD of 57, compared with 306 for a naive diffusion forcing transformer (p.16).

## Limitations and open questions

- The world model is far from a full clone of the game: its memory is short and its inventory predictions are imprecise (p.18).
- Temporal consistency is limited to the 9.6-second context, and inventory items are sometimes unclear or change over time (p.13).
- Diamonds are obtained in under 1% of evaluation episodes (p.12).
- Only the policy and value heads are trained during imagination training; finetuning the whole transformer helps slightly but costs more (p.7).
- Future directions named by the authors include pretraining on general internet videos, long-term memory, language understanding, small amounts of corrective online data, and automatic goal discovery (p.18).

## Related concepts

- [Shortcut forcing](../concepts/shortcut-forcing.md): the training objective of the dynamics model.
- [Offline reinforcement learning](../concepts/offline-reinforcement-learning.md): the setting of the diamond challenge.
- [Action conditioning](../concepts/action-conditioning.md): learned from a small amount of labeled video.
- [World model](../concepts/world-model.md): now a scalable transformer.
- [Learning in imagination](../concepts/learning-in-imagination.md): the final training phase.
- [Actor-critic](../concepts/actor-critic.md): policy and value heads trained with PMPO and λ-returns.
- [Recurrent state-space model](../concepts/recurrent-state-space-model.md): the earlier architecture that this paper replaces.
- [Symlog predictions](../concepts/symlog-predictions.md): used for the reward and value heads.
- [Return normalization](../concepts/return-normalization.md): no longer needed with PMPO.
- [Model-based reinforcement learning](../concepts/model-based-reinforcement-learning.md): compared with VPT and VLA agents.

## Relation to other sources

- [Mastering Diverse Domains through World Models](2023-dreamerv3.md): DreamerV3 collected diamonds online from scratch with low-resolution inputs and abstract crafting actions; Dreamer 4 does it offline from high-resolution images with low-level mouse and keyboard actions (p.29). It keeps the symexp twohot heads but replaces the RSSM, return normalization and entropy regularizer (p.29).
- [Learning Latent Dynamics for Planning from Pixels](2019-planet.md) and [World Models](2018-world-models.md): Dreamer 4 cites both as early world models accurate enough for planning from pixels (p.17).

## Background

- [Dreamer 4 project page](https://danijar.com/dreamer4): linked from the paper.

## My notes
