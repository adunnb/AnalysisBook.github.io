---
layout: proof
title: "Rolle's Theorem"
chapter: "Differentiation"
---

**Theorem:** Let $f : [a, b] \to \mathbb{R}$ be [continuous](../D/continuity) on $[a, b]$ and [differentiable](../D/derivative) on $(a, b)$. If $f(a) = f(b)$, then there exists $c \in (a, b)$ such that $f'(c) = 0$.

**Remark:** Rolle's theorem says that if a differentiable function starts and ends at the same value, it must have a horizontal tangent somewhere in between. It is the key lemma used to prove the [mean value theorem](../T/mean-value).

**Proof:** By the [extreme value theorem](../T/extreme-value), $f$ attains both a maximum and minimum on $[a, b]$.

**Case 1:** Both the maximum and minimum are attained at the endpoints. Since $f(a) = f(b)$, this means $f$ is constant on $[a, b]$, so $f'(c) = 0$ for every $c \in (a, b)$.

**Case 2:** At least one of the maximum or minimum is attained at an interior point $c \in (a, b)$. Then $c$ is a local extremum of $f$ in the interior of $[a, b]$, and by the [interior extremum theorem](../T/interior-extremum), $f'(c) = 0$.