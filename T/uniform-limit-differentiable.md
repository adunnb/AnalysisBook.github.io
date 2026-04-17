---
layout: proof
title: "Differentiability of Uniform Limits"
chapter: "Sequences of Functions"
---

**Theorem:** Let $(f_n)$ be a sequence of [differentiable](../D/derivative) functions on $[a, b]$ with $f_n' : [a,b] \to \mathbb{R}$ [continuous](../D/continuity). Suppose:

1. $(f_n)$ converges [pointwise](../D/pointwise-convergence) at some point $x_0 \in [a,b]$
2. $(f_n')$ converges [uniformly](../D/uniform-convergence) to some function $g$ on $[a,b]$

Then $(f_n)$ converges uniformly to a differentiable function $f$ on $[a,b]$, and $f' = g$.

**Remark:** Notice the asymmetry: we need uniform convergence of the derivatives, not of the functions themselves. Pointwise convergence of the functions at just one point, combined with uniform convergence of the derivatives, is enough to guarantee uniform convergence of the functions everywhere.

**Proof:** By [FTC I](../T/ftc-1), for each $n$ and all $x \in [a,b]$:

$$f_n(x) = f_n(x_0) + \int_{x_0}^x f_n'$$

Since $f_n(x_0)$ converges by assumption and $f_n' \to g$ uniformly, by [integrability of uniform limits](../T/uniform-limit-integrable):

$$\int_{x_0}^x f_n' \to \int_{x_0}^x g$$

Therefore $(f_n(x))$ converges for all $x \in [a,b]$. Define:

$$f(x) = \lim_{n \to \infty} f_n(x_0) + \int_{x_0}^x g$$

The convergence is uniform since $f_n' \to g$ uniformly and $f_n(x_0)$ converges. By [FTC I](../T/ftc-1), $f$ is differentiable and $f' = g$.