---
layout: proof
title: "Differentiability of Power Series"
chapter: "Sequences of Functions"
---

**Theorem:** Let $f(x) = \sum_{n=0}^{\infty} c_n(x-a)^n$ be a [power series](../D/power-series) with [radius of convergence](../D/radius-convergence) $R > 0$. Then $f$ is [differentiable](../D/derivative) on $(a-R, a+R)$ and:

$$f'(x) = \sum_{n=1}^{\infty} n c_n(x-a)^{n-1}$$

Moreover the differentiated series has the same radius of convergence $R$.

**Remark:** This theorem says that power series can be differentiated term by term inside the interval of convergence. Combined with [continuity of power series](../T/power-series-continuous), it follows that power series are infinitely differentiable on their interval of convergence.

**Proof:** Let $g(x) = \sum_{n=1}^{\infty} nc_n(x-a)^{n-1}$ be the formally differentiated series. We first show it has radius of convergence $R$. Since $\lim_{n \to \infty} n^{1/n} = 1$:

$$\limsup_{n \to \infty} \lvert nc_n \rvert^{1/n} = \limsup_{n \to \infty} \lvert c_n \rvert^{1/n}$$

so the radius of convergence of $g$ is also $R$.

Let $c \in (a-R, a+R)$ and choose $r$ with $\lvert c-a \rvert < r < R$. By [convergence of power series](../T/power-series-convergence), $g$ converges uniformly on $[a-r, a+r]$. The partial sums of $f$ converge at $x = a$ (to $c_0$), and the partial sums of $f$ are polynomials whose derivatives are the partial sums of $g$. By [differentiability of uniform limits](../T/uniform-limit-differentiable), $f$ is differentiable on $[a-r, a+r]$ and $f' = g$. Since $c$ was arbitrary, $f' = g$ on all of $(a-R, a+R)$.