---
layout: definition
title: "Uniform Continuity"
chapter: "Limits and Continuity"
---

**Definition:** A function $f : A \to \mathbb{R}$ is **uniformly continuous on $A$** if for every $\varepsilon > 0$ there exists $\delta > 0$ such that for all $x, y \in A$:

$$\lvert x - y \rvert < \delta \implies \lvert f(x) - f(y) \rvert < \varepsilon$$

**Remark:** The crucial difference from [continuity at a point](../D/continuity) is the order of quantifiers. In ordinary continuity, $\delta$ may depend on both $\varepsilon$ and the point $c$. In uniform continuity, a single $\delta$ works for all points in $A$ simultaneously.

Every uniformly continuous function is continuous, but the converse is false. The function $f(x) = x^2$ is continuous on $\mathbb{R}$ but not uniformly continuous, since points far from the origin require increasingly small $\delta$ for a given $\varepsilon$. Uniform continuity is a more restrictive condition than general continuity.