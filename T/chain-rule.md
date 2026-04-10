---
layout: proof
title: "Chain Rule"
chapter: "Differentiation"
---

**Theorem:** Let $f : A \to \mathbb{R}$ and $g : B \to \mathbb{R}$ with $f(A) \subseteq B$. If $f$ is [differentiable](../D/derivative) at $c \in A$ and $g$ is differentiable at $f(c) \in B$, then $g \circ f$ is differentiable at $c$ and:

$$(g \circ f)'(c) = g'(f(c)) \cdot f'(c)$$

**Proof:** Define the auxiliary function:

$$d(y) = \begin{cases} \dfrac{g(y) - g(f(c))}{y - f(c)} & \text{if } y \neq f(c) \\ g'(f(c)) & \text{if } y = f(c) \end{cases}$$

Since $g$ is differentiable at $f(c)$, we have $\lim_{y \to f(c)} d(y) = g'(f(c))$, so $d$ is [continuous](../D/continuity) at $f(c)$.

For all $x \in A$ with $x \neq c$, regardless of whether $f(x) = f(c)$ or not:

$$g(f(x)) - g(f(c)) = d(f(x)) \cdot (f(x) - f(c))$$

Dividing by $x - c$:

$$\frac{(g \circ f)(x) - (g \circ f)(c)}{x - c} = d(f(x)) \cdot \frac{f(x) - f(c)}{x - c}$$

Taking the limit as $x \to c$, since $f$ is continuous at $c$ and $d$ is continuous at $f(c)$, we have $d(f(x)) \to d(f(c)) = g'(f(c))$. Therefore:

$$(g \circ f)'(c) = g'(f(c)) \cdot f'(c)$$