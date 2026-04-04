---
layout: proof
title: "Existence of Square Roots"
chapter: "Completeness and the Real Numbers"
---

**Theorem:** For every real number $x \geq 0$, there exists a unique real number $y \geq 0$ such that $y^2 = x$. We write $y = \sqrt{x}$.

**Remark:** This theorem shows how fundamental the [completeness axiom](../T/completeness-axiom) is for the real number system, as it guarantees the existence of numbers like $\sqrt{2}$ which do not exist in $\mathbb{Q}$.

**Proof:** Let $x \geq 0$ and define the set:

$$A = \{t \in \mathbb{R} : t \geq 0 \text{ and } t^2 \leq x\}$$

**Non-emptiness:** $0 \in A$ since $0^2 = 0 \leq x$.

**Bounded above:** If $t \in A$ then $t^2 \leq x$, so $t \leq x + 1$ is an upper bound for $A$.

By the [completeness axiom](../T/completeness-axiom), $y = \sup A$ exists. We claim $y^2 = x$ by ruling out $y^2 < x$ and $y^2 > x$.

**Case 1: $y^2 < x$.** Let $\varepsilon = \frac{x - y^2}{2y + 1} > 0$. Then:

$$(y + \varepsilon)^2 = y^2 + 2y\varepsilon + \varepsilon^2 \leq y^2 + (2y + 1)\varepsilon = y^2 + (x - y^2) = x$$

So $y + \varepsilon \in A$, contradicting $y = \sup A$.

**Case 2: $y^2 > x$.** Let $\varepsilon = \frac{y^2 - x}{2y} > 0$. Then:

$$(y - \varepsilon)^2 = y^2 - 2y\varepsilon + \varepsilon^2 \geq y^2 - 2y\varepsilon = y^2 - (y^2 - x) = x$$

So $y - \varepsilon$ is an upper bound for $A$, contradicting $y = \sup A$.

Therefore $y^2 = x$.

**Uniqueness:** If $y_1, y_2 \geq 0$ both satisfy $y_1^2 = y_2^2 = x$, then $y_1^2 - y_2^2 = 0$, so $(y_1 - y_2)(y_1 + y_2) = 0$. Since $y_1, y_2 \geq 0$ we have $y_1 + y_2 \geq 0$, so $y_1 = y_2$.