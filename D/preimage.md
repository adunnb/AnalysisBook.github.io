---
layout: definition
title: "Preimage"
chapter: "Sets and Functions"
link_terms: ["preimage", "inverse image", "fiber"]
---

**Definition:** Let $f : A \to B$ be a [function](../D/function). For $H \subseteq B$, the **preimage** (or **inverse image**) of $H$ under $f$ is:

$$f^{-1}(H) = \{x \in A : f(x) \in H\} \subseteq A$$

For $b \in B$, the set $f^{-1}(\{b\})$ is called the **fiber** of $f$ over $b$.

**Example:** Let $f : \mathbb{R} \to \mathbb{R}$, $f(x) = x^2 + 5$. For $H = (21, 41)$:

$$f^{-1}(H) = \{x : 21 < x^2 + 5 < 41\} = \{x : 16 < x^2 < 36\} = (-6, -4) \cup (4, 6)$$

The fibers include $f^{-1}(\{21\}) = \{-4, 4\}$, $f^{-1}(\{41\}) = \{-6, 6\}$, and $f^{-1}(\{2\}) = \varnothing$.

**Remark:** The notation $f^{-1}(H)$ does **not** require $f$ to have an [inverse function](../D/inverse-function). The preimage is defined for every function and every $H \subseteq B$, including [subsets](../D/subset) of $B$ outside the [image](../D/image). It may be empty, and an empty preimage is not "undefined." The fibers over the points of $f(A)$ partition $A$: each $x \in A$ lies in exactly one fiber, namely $f^{-1}(\{f(x)\})$.
