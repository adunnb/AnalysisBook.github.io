---
layout: proof
title: "L'Hôpital's Rule"
chapter: "Differentiation"
---

**Theorem:** Let $f, g : (a, b) \to \mathbb{R}$ be [differentiable](../D/derivative) on $(a, b)$ with $g'(x) \neq 0$ for all $x \in (a, b)$. Suppose:

$$\lim_{x \to a^+} f(x) = 0 \quad \text{and} \quad \lim_{x \to a^+} g(x) = 0$$

If $\displaystyle\lim_{x \to a^+} \frac{f'(x)}{g'(x)} = L$, then $\displaystyle\lim_{x \to a^+} \frac{f(x)}{g(x)} = L$.

**Remark:** The theorem also holds for the $\frac{\infty}{\infty}$ indeterminate form, for two-sided limits, and as $x \to \infty$. We state and prove only the $\frac{0}{0}$ one-sided case here.

**Proof:** Extend $f$ and $g$ to $[a, b)$ by setting $f(a) = g(a) = 0$. Then $f$ and $g$ are continuous on $[a, x]$ and differentiable on $(a, x)$ for any $x \in (a, b)$.

By the [generalized mean value theorem](../T/generalized-mean-value), there exists $c \in (a, x)$ such that:

$$f'(c)(g(x) - g(a)) = g'(c)(f(x) - f(a))$$

Since $f(a) = g(a) = 0$:

$$f'(c) \cdot g(x) = g'(c) \cdot f(x)$$

Since $g'(c) \neq 0$ and $g(x) \neq 0$ (as $g'$ is nonzero on $(a,b)$, $g$ is injective near $a$):

$$\frac{f(x)}{g(x)} = \frac{f'(c)}{g'(c)}$$

As $x \to a^+$, we have $c \to a^+$ since $c \in (a, x)$. Therefore:

$$\lim_{x \to a^+} \frac{f(x)}{g(x)} = \lim_{c \to a^+} \frac{f'(c)}{g'(c)} = L$$