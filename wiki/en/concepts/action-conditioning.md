---
title: "Action conditioning"
aliases: [action-conditioned video prediction, action grounding, learning from unlabeled videos]
updated: 2026-11-24
areas: [world-model]
sources: [2025-dreamer4]
---

## One-line definition

Making a world model's predictions depend on the actions taken, so that different actions from the same situation lead to correspondingly different predicted futures.

## Explanation

A video model without actions can only predict what usually happens next. To serve as a world model for an agent, it must also predict how the future changes with the agent's choices. Learning this requires videos paired with the actions that produced them, which are scarce compared with the huge amount of unlabeled video available. A useful property is therefore to learn most of the world's appearance and physics from unlabeled video and only the link between actions and outcomes from a small labeled set.

> **Explainer:** It is like learning a game mostly by watching others play, and then needing only a short session with the controller to figure out which button does what.

## What each source says

### Training Agents Inside of Scalable World Models (2025)

[Dreamer 4](../sources/2025-dreamer4.md) encodes each action component, such as mouse and keyboard, into tokens, and uses only a learned embedding when a video has no actions, so labeled and unlabeled videos can be mixed (p.5). Trained on all 2541 hours of VPT videos but with actions for only 100 hours, it reaches 85% of the PSNR and 100% of the SSIM of a model trained with all actions (p.14). When actions are given only for the Overworld, the action conditioning transfers to the Nether and End, which appear only in unlabeled videos, reaching 76% of the PSNR and 80% of the SSIM (p.15). The authors conclude that world models can absorb most of their knowledge from unlabeled videos, which points toward learning from web videos (p.14).

## Related concepts

- [World model](world-model.md): action conditioning is what turns a video model into a world model.
- [Shortcut forcing](shortcut-forcing.md): the objective of the action-conditioned dynamics model in Dreamer 4.
- [Offline reinforcement learning](offline-reinforcement-learning.md): the world model is trained on logged actions only.

## Background

(None yet)

## My notes
