---
layout: proof
title: "Finite Geometric Sum"
chapter: "The Natural Numbers"
link_terms: ["finite geometric sum", "geometric sum"]
---

**Theorem:** For every real number $z \neq 1$ and every $n \in \mathbb{N}_0$:

$$1 + z + z^2 + \cdots + z^n = \frac{1 - z^{n+1}}{1 - z}$$

**Remark:** For $z = 1$ the sum is $n + 1$, while the quotient on the right is undefined. Letting $n \to \infty$ when $\lvert z \rvert < 1$ gives the [geometric series test](../T/geometric-series).

**Proof:** We use [mathematical induction](../T/induction) starting at $n = 0$. For $n = 0$, both sides equal $1$, since $\frac{1 - z}{1 - z} = 1$. If the formula holds for $n = k$, then:

$$\sum_{j=0}^{k+1} z^j = \frac{1 - z^{k+1}}{1 - z} + z^{k+1} = \frac{1 - z^{k+1} + z^{k+1} - z^{k+2}}{1 - z} = \frac{1 - z^{k+2}}{1 - z}$$

which is the formula for $n = k + 1$.

Alternatively, multiplying the sum by $1 - z$ makes the intermediate terms cancel:

$$(1 - z)(1 + z + \cdots + z^n) = 1 - z^{n+1}$$
