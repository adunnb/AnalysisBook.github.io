---
layout: proof
title: "Integral Test"
chapter: "Sequences and Series"
---

**Theorem:** Let $f : [1, \infty) \to \mathbb{R}$ be a positive, continuous, and decreasing function with $f(n) = a_n$ for all $n \in \mathbb{N}$. Then:

$$\sum_{n=1}^{\infty} a_n \text{ converges} \iff \int_1^{\infty} f(x)\, dx \text{ converges}$$

**Proof:** Since $f$ is decreasing, for each $n \in \mathbb{N}$ and $x \in [n, n+1]$:

$$f(n+1) \leq f(x) \leq f(n)$$

Integrating over $[n, n+1]$:

$$a_{n+1} = f(n+1) \leq \int_n^{n+1} f(x)\, dx \leq f(n) = a_n$$

Summing from $n = 1$ to $N$:

$$\sum_{n=2}^{N+1} a_n \leq \int_1^{N+1} f(x)\, dx \leq \sum_{n=1}^{N} a_n$$

**($\Rightarrow$)** If $\sum a_n$ converges, the right inequality shows $\int_1^{N+1} f \leq \sum_{n=1}^{\infty} a_n < \infty$ for all $N$, so the integral converges.

**($\Leftarrow$)** If $\int_1^{\infty} f$ converges, the left inequality shows $\sum_{n=2}^{N+1} a_n \leq \int_1^{\infty} f < \infty$ for all $N$, so the [partial sums](../D/partial-sums) are bounded. Since $a_n > 0$, the series converges by the [monotone convergence theorem](../T/monotone-convergence).