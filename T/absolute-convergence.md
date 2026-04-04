---
layout: proof
title: "Absolute Convergence"
chapter: "Sequences and Series"
---

**Definition:** A series $\sum_{n=1}^{\infty} a_n$ **converges absolutely** if $\sum_{n=1}^{\infty} \lvert a_n \rvert$ converges.

**Theorem:** If a series converges absolutely, then it converges.

**Proof:** Suppose $\sum \lvert a_n \rvert$ converges. Let $\varepsilon > 0$. By the [Cauchy criterion for series](../T/series-cauchy), there exists $N \in \mathbb{N}$ such that for all $m > n > N$:

$$\lvert a_{n+1} \rvert + \lvert a_{n+2} \rvert + \cdots + \lvert a_m \rvert < \varepsilon$$

By the [triangle inequality](../D/absolute-value):

$$\lvert a_{n+1} + a_{n+2} + \cdots + a_m \rvert \leq \lvert a_{n+1} \rvert + \lvert a_{n+2} \rvert + \cdots + \lvert a_m \rvert < \varepsilon$$

So $\sum a_n$ satisfies the Cauchy criterion and therefore converges.

**Remark:** The converse is false. The alternating harmonic series $\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}$ converges but does not converge absolutely. Such series are called **conditionally convergent**.