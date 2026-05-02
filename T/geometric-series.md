---
layout: proof
title: "Geometric Series Test"
chapter: "Sequences and Series"
---

**Theorem:** The geometric series $\sum_{n=0}^{\infty} r^n$ converges if and only if $\lvert r \rvert < 1$, in which case:

$$\sum_{n=0}^{\infty} r^n = \frac{1}{1-r}$$

If $\lvert r \rvert \geq 1$, the series diverges.

**Proof:** The $n$-th partial sum is:

$$s_n = \sum_{k=0}^{n} r^k = 1 + r + r^2 + \cdots + r^n$$

For $r \neq 1$, multiplying by $r$ and subtracting:

$$s_n(1 - r) = 1 - r^{n+1} \implies s_n = \frac{1 - r^{n+1}}{1 - r}$$

If $\lvert r \rvert < 1$, then $r^{n+1} \to 0$, so $s_n \to \frac{1}{1-r}$.

If $\lvert r \rvert > 1$, then $\lvert r^{n+1} \rvert \to \infty$, so $(s_n)$ diverges.

If $r = 1$, then $s_n = n+1 \to \infty$, so the series diverges.

If $r = -1$, then $s_n$ alternates between $1$ and $0$ and does not converge.