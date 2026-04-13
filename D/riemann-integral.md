---
layout: definition
title: "Riemann Integrability"
chapter: "Integration"
---

**Definition:** Let $f : [a, b] \to \mathbb{R}$ be bounded. The **upper integral** of $f$ is:

$$U(f) = \inf\{U(f, P) : P \text{ is a partition of } [a,b]\}$$

The **lower integral** of $f$ is:

$$L(f) = \sup\{L(f, P) : P \text{ is a partition of } [a,b]\}$$

We always have $L(f) \leq U(f)$. The function $f$ is **Riemann integrable** on $[a, b]$ if:

$$L(f) = U(f)$$

in which case the common value is the **Riemann integral** of $f$:

$$\int_a^b f = L(f) = U(f)$$

The collection of all Riemann integrable functions on $[a,b]$ is denoted $\mathcal{R}[a,b]$.