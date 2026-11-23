---
title: "Creativity support"
aliases: [creativity support tools, creative ideation, consistency diversity persistency]
updated: 2026-11-24
areas: [game-ai]
sources: [2025-wham]
---

## One-line definition

Designing and evaluating AI systems by how well they help people come up with and refine ideas, rather than by how well they complete a task on their own.

## Explanation

Creative work usually alternates between opening up many options and narrowing them down through many small adjustments. A tool that supports this must offer varied suggestions, keep them coherent with the work's rules and style, and let the person steer the result directly. Generative models trained to produce one good answer from a prompt often miss these needs. Evaluating models against what creatives actually do can therefore point model development in a different direction than task-completion benchmarks.

> **Explainer:** A good creative assistant is less like a vending machine that hands out one finished product and more like a sketching partner who offers rough variations and keeps your corrections.

## What each source says

### World and Human Action Models towards gameplay ideation (2025)

[WHAM](../sources/2025-wham.md) interviews 27 game-development creatives and finds two needs: divergent thinking that stays consistent with the game world, and control over an iterative process (p.2). From these it derives three capabilities for generative models: consistency, diversity and persistency (p.3). It turns each into a measurable criterion, using Fréchet Video Distance for consistency, the Wasserstein distance to human actions for diversity, and human labelling of whether inserted elements survive for persistency (pp.4-5). The authors argue that model evaluation should be informed by the requirements of creatives, in contrast with the usual focus on measuring task completion (p.7).

## Related concepts

- [World model](world-model.md): WHAM is the generative model evaluated against these criteria.
- [Autoregressive transformer](autoregressive-transformer.md): token-by-token generation is what makes edits possible.

## Background

(None yet)

## My notes
