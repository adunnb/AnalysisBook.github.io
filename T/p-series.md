---
layout: proof
title: "p-Series Test"
chapter: "Sequences and Series"
---

**Theorem:** The **p-series** $\sum_{n=1}^{\infty} \frac{1}{n^p}$ converges if $p > 1$ and diverges if $p \leq 1$.

**Proof:** We use the [integral test](../T/integral-test).

Consider $f(x) = \frac{1}{x^p}$, which is positive, continuous, and decreasing on $[1, \infty)$.

**Case $p \neq 1$:**

$$\int_1^{\infty} \frac{1}{x^p}\, dx = \lim_{b \to \infty} \left[\frac{x^{1-p}}{1-p}\right]_1^b = \lim_{b \to \infty} \frac{b^{1-p} - 1}{1-p}$$

If $p > 1$ then $1 - p < 0$, so $b^{1-p} \to 0$ and the integral converges to $\frac{1}{p-1}$. By the integral test, the series converges.

If $p < 1$ then $1 - p > 0$, so $b^{1-p} \to \infty$ and the integral diverges. By the integral test, the series diverges.

**Case $p = 1$:** This is the harmonic series. Since $\int_1^{\infty} \frac{1}{x}\, dx = \lim_{b \to \infty} \ln b = \infty$, the integral diverges and so does the series.