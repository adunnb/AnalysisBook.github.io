---
layout: definition
title: "Limit of a Function"
chapter: "Limits and Continuity"
---

**Definition:** Let $f : A \to \mathbb{R}$ and let $c$ be a [limit point](../D/limit-point) of $A$. We say $\lim_{x \to c} f(x) = L$ if for every $\varepsilon > 0$ there exists $\delta > 0$ such that:

$$0 < \lvert x - c \rvert < \delta \text{ and } x \in A \implies \lvert f(x) - L \rvert < \varepsilon$$

**Remark:** The condition $0 < \lvert x - c \rvert$ ensures that we never evaluate $f$ at $c$ itself. The limit describes the behavior of $f$ near $c$, not at $c$. In particular, $f$ need not even be defined at $c$.

**Intuition:** For any tolerance $\varepsilon > 0$ around $L$, we can find a radius $\delta > 0$ around $c$ such that $f$ maps every point within $\delta$ of $c$ (other than $c$ itself) to within $\varepsilon$ of $L$.