---
layout: definition
title: "Continuity at a Point"
chapter: "Limits and Continuity"
---

**Definition:** Let $f : A \to \mathbb{R}$ and let $c \in A$. We say $f$ is **continuous at $c$** if for every $\varepsilon > 0$ there exists $\delta > 0$ such that:

$$\lvert x - c \rvert < \delta \text{ and } x \in A \implies \lvert f(x) - f(c) \rvert < \varepsilon$$

We say $f$ is **continuous on $A$** if it is continuous at every point $c \in A$.

**Remark:** Compare this to the [definition of a functional limit](../D/limit-function). The key differences are:

1. We require $c \in A$ — continuity is defined at points in the domain
2. We use $\lvert x - c \rvert < \delta$ rather than $0 < \lvert x - c \rvert < \delta$, so we include $x = c$ itself
3. The target value is $f(c)$ rather than an arbitrary $L$

**Sequential characterization:** By the [sequential characterization of functional limits](../T/sequential-limits), $f$ is continuous at $c$ if and only if for every sequence $(x_n) \subseteq A$ with $x_n \to c$, we have $f(x_n) \to f(c)$.