---
layout: definition
title: "Limit Point"
chapter: "Limits and Continuity"
---

**Definition:** Let $A \subseteq \mathbb{R}$. A point $c \in \mathbb{R}$ is a **limit point** (or **accumulation point**) of $A$ if for every $\varepsilon > 0$ there exists a point $x \in A$ with $x \neq c$ such that:

$$\lvert x - c \rvert < \varepsilon$$

Equivalently, $c$ is a limit point of $A$ if every $\varepsilon$-neighborhood $(c - \varepsilon, c + \varepsilon)$ contains a point of $A$ other than $c$ itself.

**Remark:** A limit point of $A$ need not belong to $A$. For example, $0$ is a limit point of the open interval $(0, 1)$ even though $0 \notin (0,1)$. The concept is important because the limit of a function $f$ at a point $c$ is only meaningful when $c$ is a limit point of the domain of $f$ — otherwise there are no nearby points to approach $c$ from.