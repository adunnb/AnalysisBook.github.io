---
layout: definition
title: "Neighborhood"
chapter: "Completeness and the Real Numbers"
---

**Definition:** Let $c \in \mathbb{R}$ and $\varepsilon > 0$. The **$\varepsilon$-neighborhood** of $c$ is the open interval:

$$V_\varepsilon(c) = (c - \varepsilon, c + \varepsilon) = \{x \in \mathbb{R} : \lvert x - c \rvert < \varepsilon\}$$

A **neighborhood** of $c$ is any set containing a $\varepsilon$-neighborhood of $c$ for some $\varepsilon > 0$.

**Remark:** Neighborhoods provide a convenient language for describing closeness. For example, the [definition of convergence](../D/convergence-sequence) can be restated as: $a_n \to L$ if for every $\varepsilon > 0$, all but finitely many terms of $(a_n)$ lie in $V_\varepsilon(L)$. Similarly, the [definition of a limit of a function](../D/limit-function) says that $f(x)$ eventually lies in any neighborhood of $L$ as $x$ approaches $c$.