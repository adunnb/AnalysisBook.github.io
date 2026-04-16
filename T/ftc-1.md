---
layout: proof
title: "Fundamental Theorem of Calculus I"
chapter: "Integration"
---

**Theorem:** Let $f \in \mathcal{R}[a,b]$ and define $F : [a,b] \to \mathbb{R}$ by:

$$F(x) = \int_a^x f$$

Then $F$ is [continuous](../D/continuity) on $[a,b]$. Moreover if $f$ is continuous at $c \in [a,b]$, then $F$ is [differentiable](../D/derivative) at $c$ and $F'(c) = f(c)$.

**Remark:** This theorem says that every continuous function has an antiderivative. It connects the two main operations of calculus by showing that differentiation undoes integration.

**Proof:**

**Continuity of $F$:** Since $f \in \mathcal{R}[a,b]$, $f$ is bounded — say $\lvert f \rvert \leq M$. For $x, y \in [a,b]$ with $x < y$, by [additivity](../T/integral-additivity) and the [integral inequality](../T/integral-inequality):

$$\lvert F(y) - F(x) \rvert = \left\lvert \int_x^y f \right\rvert \leq \int_x^y \lvert f \rvert \leq M(y - x)$$

Given $\varepsilon > 0$, take $\delta = \frac{\varepsilon}{M}$. Then $\lvert y - x \rvert < \delta \implies \lvert F(y) - F(x) \rvert < \varepsilon$, so $F$ is [uniformly continuous](../D/uniform-continuity) on $[a,b]$.

**Differentiability at $c$:** Suppose $f$ is continuous at $c$. Let $\varepsilon > 0$. There exists $\delta > 0$ such that $\lvert x - c \rvert < \delta \implies \lvert f(x) - f(c) \rvert < \varepsilon$. For $0 < \lvert h \rvert < \delta$:

$$\frac{F(c+h) - F(c)}{h} - f(c) = \frac{1}{h}\int_c^{c+h} f - f(c) = \frac{1}{h}\int_c^{c+h} (f(t) - f(c))\, dt$$

By the [integral inequality](../T/integral-inequality):

$$\left\lvert \frac{F(c+h) - F(c)}{h} - f(c) \right\rvert \leq \frac{1}{\lvert h \rvert} \int_c^{c+h} \lvert f(t) - f(c) \rvert\, dt < \frac{1}{\lvert h \rvert} \cdot \varepsilon \lvert h \rvert = \varepsilon$$

Therefore $F'(c) = f(c)$.