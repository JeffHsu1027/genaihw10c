---
title: "Latent overshooting"
aliases: [overshooting, multi-step latent objective]
updated: 2026-11-24
areas: [world-model]
sources: [2019-planet]
---

## One-line definition

A training objective for latent sequence models that, besides one-step predictions, also trains multi-step predictions by pulling them toward the states inferred from real observations, entirely in latent space.

## Explanation

Standard variational training only teaches the transition model to predict one step ahead. With limited capacity, the best one-step model is not necessarily the best multi-step model, yet planning needs accurate predictions far ahead. Overshooting rolls the transition model forward several steps from an earlier state and pulls each predicted state toward the state inferred from the actual observations. Doing this in latent space avoids decoding extra images, which would be expensive.

## What each source says

### Learning Latent Dynamics for Planning from Pixels (2019)

[PlaNet](../sources/2019-planet.md) proposes latent overshooting as a generalization of the standard variational bound that trains predictions of every distance up to a maximum, with a weight for each distance (pp.5-6, Eq. 7). It contrasts this with observation overshooting, which decodes every multi-step prediction into an image and is usually too expensive in image domains (p.5, Fig. 3). Gradients are stopped at the posterior for longer distances, so the predictions move toward the informed posteriors but not the other way around (p.6). In the experiments, latent overshooting substantially improves a model called DRNN but slightly reduces the performance of the RSSM (p.14, Fig. 8). The final PlaNet agent therefore does not use it (p.12).

## Related concepts

- [Recurrent state-space model](recurrent-state-space-model.md): the model that turned out not to need overshooting.
- [Latent space planning](latent-space-planning.md): the reason multi-step predictions matter.

## Background

(None yet)

## My notes
