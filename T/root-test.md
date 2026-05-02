---
layout: proof
title: "Root Test"
chapter: "Sequences and Series"
---

**Theorem:** Let $\sum_{n=1}^{\infty} a_n$ be a series and suppose:

$$L = \limsup_{n \to \infty} \lvert a_n \rvert^{1/n}$$

(i) If $L < 1$, the series converges absolutely.

(ii) If $L > 1$, the series diverges.

(iii) If $L = 1$, the test is inconclusive.

**Proof of (i):** Suppose $L < 1$. Choose $r$ with $L < r < 1$. By the definition of [limsup](../D/limsup-liminf), there exists $N$ such that $\lvert a_n \rvert^{1/n} < r$ for all $n > N$, so $\lvert a_n \rvert < r^n$. Since $\sum r^n$ converges by the [geometric series test](../T/geometric-series), the [comparison test](../T/comparison-test) gives absolute convergence.

**Proof of (ii):** Suppose $L > 1$. Then $\lvert a_n \rvert^{1/n} > 1$ for infinitely many $n$, meaning $\lvert a_n \rvert > 1$ for infinitely many $n$. Therefore $a_n \not\to 0$, and by the corollary to the [Cauchy criterion for series](../T/series-cauchy), the series diverges.

**Proof of (iii):** Both $\sum \frac{1}{n}$ (diverges) and $\sum \frac{1}{n^2}$ (converges) give $L = 1$.