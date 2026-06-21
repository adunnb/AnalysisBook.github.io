---
layout: proof
title: "Taylor's Theorem"
chapter: "Differentiation"
---

**Theorem:** Let $f : [a, b] \to \mathbb{R}$ be [$n$ times differentiable](../D/higher-derivatives) on $[a, b]$ with $f^{(n)}$ [continuous](../D/continuity) on $[a, b]$ and $(n+1)$ times differentiable on $(a, b)$. Then for any $x, c \in [a, b]$ there exists a point $\xi$ strictly between $x$ and $c$ such that:

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(c)}{k!}(x-c)^k + \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-c)^{n+1}$$

The sum $\displaystyle P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(c)}{k!}(x-c)^k$ is called the **$n$-th order Taylor polynomial** of $f$ centered at $c$, and the remaining term $\displaystyle R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-c)^{n+1}$ is called the **Lagrange remainder**.

**Remark:** Taylor's theorem generalizes the [mean value theorem](../T/mean-value), which is the case $n = 0$. It says that a smooth function can be approximated by a polynomial, with the remainder controlled by a higher derivative.

**Proof:** Fix $x$ and $c$ and define the constant $K$ by:

$$f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(c)}{k!}(x-c)^k + K(x-c)^{n+1}$$

Define $g : [a,b] \to \mathbb{R}$ by:

$$g(t) = f(x) - \sum_{k=0}^{n} \frac{f^{(k)}(t)}{k!}(x-t)^k - K(x-t)^{n+1}$$

Then $g(x) = 0$ and $g(c) = 0$ by the choice of $K$. By [Rolle's theorem](../T/rolles-theorem), there exists $\xi$ strictly between $x$ and $c$ with $g'(\xi) = 0$. Computing $g'$, all terms telescope except the last:

$$g'(t) = -\frac{f^{(n+1)}(t)}{n!}(x-t)^n + K(n+1)(x-t)^n$$

Setting $g'(\xi) = 0$ and solving for $K$:

$$K = \frac{f^{(n+1)}(\xi)}{(n+1)!}$$

Substituting back gives the result.