---
layout: proof
title: "Convergence of Power Series"
chapter: "Sequences of Functions"
---

**Theorem:** Let $\sum_{n=0}^{\infty} c_n(x-a)^n$ be a [power series](../D/power-series) with [radius of convergence](../D/radius-convergence) $R > 0$. Then the series converges [uniformly](../D/uniform-convergence) on every closed interval $[a-r, a+r]$ with $0 < r < R$.

**Remark:** The convergence is uniform on compact subsets of the interval of convergence, but need not be uniform on the full open interval $(a-R, a+R)$.

**Proof:** Without loss of generality take $a = 0$. Let $0 < r < R$ and choose $s$ with $r < s < R$. Since the series converges absolutely at $x = s$, the terms $c_n s^n \to 0$ and in particular are bounded: there exists $M > 0$ with $\lvert c_n \rvert s^n \leq M$ for all $n$.

For $\lvert x \rvert \leq r$ and all $n$:

$$\lvert c_n x^n \rvert = \lvert c_n \rvert s^n \cdot \left(\frac{\lvert x \rvert}{s}\right)^n \leq M \left(\frac{r}{s}\right)^n$$

Since $\frac{r}{s} < 1$, the geometric series $\sum M\left(\frac{r}{s}\right)^n$ converges. By the [comparison test](../T/comparison-test), $\sum \lvert c_n x^n \rvert$ converges uniformly on $[-r, r]$ by the Weierstrass M-test, and therefore $\sum c_n x^n$ converges uniformly on $[-r, r]$.