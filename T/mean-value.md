---
layout: proof
title: "Mean Value Theorem"
chapter: "Differentiation"
---

**Theorem:** Let $f : [a, b] \to \mathbb{R}$ be [continuous](../D/continuity) on $[a, b]$ and [differentiable](../D/derivative) on $(a, b)$. Then there exists $c \in (a, b)$ such that:

$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

**Remark:** The mean value theorem says that for a differentiable function, there is always some point where the instantaneous rate of change equals the average rate of change over the interval. Geometrically, there is a point where the tangent line is parallel to the secant line through $(a, f(a))$ and $(b, f(b))$.

**Proof:** Define the auxiliary function:

$$g(x) = f(x) - \frac{f(b) - f(a)}{b - a}(x - a)$$

Then $g$ is continuous on $[a, b]$ and differentiable on $(a, b)$, and:

$$g(a) = f(a), \qquad g(b) = f(b) - (f(b) - f(a)) = f(a)$$

So $g(a) = g(b)$. By [Rolle's theorem](../T/rolles-theorem), there exists $c \in (a, b)$ with $g'(c) = 0$. Since:

$$g'(x) = f'(x) - \frac{f(b) - f(a)}{b - a}$$

we get $f'(c) = \dfrac{f(b) - f(a)}{b - a}$.