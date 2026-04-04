---
layout: proof
title: "Ratio Test"
chapter: "Sequences and Series"
---

**Theorem:** Let $\sum_{n=1}^{\infty} a_n$ be a series with $a_n \neq 0$ for all $n$, and suppose:

$$L = \lim_{n \to \infty} \left\lvert \frac{a_{n+1}}{a_n} \right\rvert$$

(i) If $L < 1$, the series converges absolutely.

(ii) If $L > 1$, the series diverges.

(iii) If $L = 1$, the test is inconclusive.

**Proof of (i):** Suppose $L < 1$. Choose $r$ with $L < r < 1$. By the [definition of convergence](../D/convergence-sequence), there exists $N$ such that:

$$n > N \implies \left\lvert \frac{a_{n+1}}{a_n} \right\rvert < r$$

Therefore for all $n > N$:

$$\lvert a_{N+k} \rvert \leq \lvert a_{N+1} \rvert r^{k-1}$$

So $\sum \lvert a_n \rvert$ is bounded above by a convergent geometric series, and by the [comparison test](../T/comparison-test), $\sum a_n$ converges absolutely.

**Proof of (ii):** Suppose $L > 1$. Then there exists $N$ such that $n > N \implies \lvert a_{n+1} \rvert > \lvert a_n \rvert$, so $\lvert a_n \rvert$ is eventually increasing and cannot tend to $0$. By the corollary to the [Cauchy criterion for series](../T/series-cauchy), the series diverges.

**Proof of (iii):** Both $\sum \frac{1}{n}$ (diverges) and $\sum \frac{1}{n^2}$ (converges) give $L = 1$, showing the test is inconclusive in this case.