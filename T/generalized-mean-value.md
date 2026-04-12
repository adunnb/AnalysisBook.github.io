---
layout: proof
title: "Generalized Mean Value Theorem"
chapter: "Differentiation"
---

**Theorem:** Let $f, g : [a, b] \to \mathbb{R}$ be [continuous](../D/continuity) on $[a, b]$ and [differentiable](../D/derivative) on $(a, b)$. Then there exists $c \in (a, b)$ such that:

$$f'(c)(g(b) - g(a)) = g'(c)(f(b) - f(a))$$

**Remark:** This is also called **Cauchy's mean value theorem**. When $g(x) = x$, this reduces to the ordinary [mean value theorem](../T/mean-value). The generalized version is needed for the proof of [L'Hôpital's rule](../T/lhopital).

**Proof:** Define the auxiliary function:

$$h(x) = f(x)(g(b) - g(a)) - g(x)(f(b) - f(a))$$

Then $h$ is continuous on $[a, b]$ and differentiable on $(a, b)$. Computing:

$$h(a) = f(a)g(b) - f(a)g(a) - g(a)f(b) + g(a)f(a) = f(a)g(b) - g(a)f(b)$$

$$h(b) = f(b)g(b) - f(b)g(a) - g(b)f(b) + g(b)f(a) = f(a)g(b) - g(a)f(b)$$

So $h(a) = h(b)$. By [Rolle's theorem](../T/rolles-theorem), there exists $c \in (a, b)$ with $h'(c) = 0$:

$$h'(c) = f'(c)(g(b) - g(a)) - g'(c)(f(b) - f(a)) = 0$$

which gives the result.