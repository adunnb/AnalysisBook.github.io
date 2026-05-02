---
layout: proof
title: "Integration by Substitution"
chapter: "Integration"
---

**Theorem:** Let $g : [a, b] \to \mathbb{R}$ be [differentiable](../D/derivative) with $g'$ [continuous](../D/continuity) on $[a,b]$, and let $f : g([a,b]) \to \mathbb{R}$ be continuous. Then:

$$\int_a^b f(g(x)) g'(x)\, dx = \int_{g(a)}^{g(b)} f(u)\, du$$

**Remark:** This theorem formalizes the substitution $u = g(x)$, $du = g'(x)\, dx$. It is a direct consequence of the [chain rule](../T/chain-rule) and the [fundamental theorem of calculus](../T/ftc-2).

**Proof:** Since $f$ is continuous, by [FTC I](../T/ftc-1) it has an antiderivative $F$ with $F' = f$. By the [chain rule](../T/chain-rule):

$$(F \circ g)'(x) = F'(g(x)) \cdot g'(x) = f(g(x)) \cdot g'(x)$$

Since $f \circ g$ and $g'$ are both continuous, $f(g(x))g'(x)$ is continuous on $[a,b]$ and therefore [integrable](../D/riemann-integral). By [FTC II](../T/ftc-2):

$$\int_a^b f(g(x))g'(x)\, dx = F(g(b)) - F(g(a)) = \int_{g(a)}^{g(b)} f(u)\, du$$