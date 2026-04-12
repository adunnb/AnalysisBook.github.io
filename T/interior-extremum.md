---
layout: proof
title: "Interior Extremum Theorem"
chapter: "Differentiation"
---

**Theorem:** Let $f : [a, b] \to \mathbb{R}$. If $f$ has a [local extremum](../D/interior-extremum) at $c \in (a, b)$ and $f$ is [differentiable](../D/derivative) at $c$, then $f'(c) = 0$.

**Remark:** The converse is false — $f'(c) = 0$ does not guarantee a local extremum. For example $f(x) = x^3$ has $f'(0) = 0$ but no local extremum at $0$.

**Proof:** Suppose $f$ has a local maximum at $c$ — the case of a local minimum is analogous. Then there exists $\delta > 0$ such that $f(c) \geq f(x)$ for all $x \in (c - \delta, c + \delta)$.

Consider the difference quotient from the right. For $0 < h < \delta$:

$$\frac{f(c + h) - f(c)}{h} \leq 0$$

since $f(c+h) \leq f(c)$ and $h > 0$. Taking the limit as $h \to 0^+$:

$$f'(c) = \lim_{h \to 0^+} \frac{f(c+h) - f(c)}{h} \leq 0$$

Similarly, from the left, for $-\delta < h < 0$:

$$\frac{f(c+h) - f(c)}{h} \geq 0$$

since $f(c+h) \leq f(c)$ and $h < 0$. Taking the limit as $h \to 0^-$:

$$f'(c) = \lim_{h \to 0^-} \frac{f(c+h) - f(c)}{h} \geq 0$$

Since $f'(c) \leq 0$ and $f'(c) \geq 0$, we conclude $f'(c) = 0$.