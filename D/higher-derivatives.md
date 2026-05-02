---
layout: definition
title: "Higher Order Derivatives"
chapter: "Differentiation"
---

**Definition:** Let $f : A \to \mathbb{R}$ be [differentiable](../D/derivative) on $A$. If the derivative $f' : A \to \mathbb{R}$ is itself differentiable at $c \in A$, we call the result the **second derivative** of $f$ at $c$:

$$f''(c) = (f')'(c)$$

More generally, the **$n$-th derivative** $f^{(n)}$ is defined inductively by $f^{(0)} = f$ and:

$$f^{(n)}(c) = \left(f^{(n-1)}\right)'(c)$$

provided the derivative exists. We say $f$ is **$n$ times differentiable** at $c$ if $f^{(n)}(c)$ exists.

A function is **infinitely differentiable** (or **smooth**) on $A$ if $f^{(n)}$ exists on $A$ for every $n \in \mathbb{N}$. The class of infinitely differentiable functions on $A$ is denoted $C^{\infty}(A)$.

**Remark:** A function can be $n$ times differentiable without being $(n+1)$ times differentiable. For example $f(x) = \lvert x \rvert^3$ is twice differentiable at $0$ but not three times differentiable there.