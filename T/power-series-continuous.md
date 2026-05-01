---
layout: proof
title: "Continuity of Power Series"
chapter: "Sequences of Functions"
---

**Theorem:** Let $\sum_{n=0}^{\infty} c_n(x-a)^n$ be a [power series](../D/power-series) with [radius of convergence](../D/radius-convergence) $R > 0$. Then the function:

$$f(x) = \sum_{n=0}^{\infty} c_n(x-a)^n$$

is [continuous](../D/continuity) on the interval $(a-R, a+R)$.

**Proof:** Let $c \in (a-R, a+R)$. Choose $r$ with $\lvert c - a \rvert < r < R$. By [convergence of power series](../T/power-series-convergence), the series converges uniformly on $[a-r, a+r]$.

Each partial sum $f_N(x) = \sum_{n=0}^{N} c_n(x-a)^n$ is a polynomial and therefore [continuous](../D/continuity). By [continuity of uniform limits](../T/uniform-limit-continuous), the uniform limit $f$ is continuous on $[a-r, a+r]$. Since $c \in [a-r, a+r]$, $f$ is continuous at $c$.