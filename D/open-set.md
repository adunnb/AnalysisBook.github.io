---
layout: definition
title: "Open and Closed Sets"
chapter: "Limits and Continuity"
---

**Definition:** A set $O \subseteq \mathbb{R}$ is **open** if for every $x \in O$ there exists $\varepsilon > 0$ such that $V_\varepsilon(x) \subseteq O$, i.e. every point of $O$ has a [neighborhood](../D/neighborhood) contained entirely in $O$.

A set $C \subseteq \mathbb{R}$ is **closed** if its complement $\mathbb{R} \setminus C$ is open.

**Examples:**

- Every open interval $(a, b)$ is open
- Every closed interval $[a, b]$ is closed
- The set $\mathbb{R}$ and the empty set $\emptyset$ are both open and closed
- The half-open interval $[a, b)$ is neither open nor closed

**Properties:** Open and closed sets satisfy:

1. Arbitrary unions of open sets are open
2. Finite intersections of open sets are open
3. Arbitrary intersections of closed sets are closed
4. Finite unions of closed sets are closed

**Remark:** A set being "not open" does not mean it is closed, and vice versa. The terms are not opposites.