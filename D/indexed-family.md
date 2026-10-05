---
layout: definition
title: "Indexed Family of Sets"
chapter: "Sets and Functions"
link_terms: ["indexed family", "indexed families"]
---

**Definition:** An **indexed family** of sets $\{A_\alpha : \alpha \in \Omega\}$ is a collection of sets labeled by a nonempty **index set** $\Omega$. Its [union](../D/union-intersection) and intersection are:

$$\bigcup_{\alpha \in \Omega} A_\alpha = \{x : x \in A_\alpha \text{ for some } \alpha \in \Omega\}$$

$$\bigcap_{\alpha \in \Omega} A_\alpha = \{x : x \in A_\alpha \text{ for every } \alpha \in \Omega\}$$

For a finite family indexed by $\{1, \ldots, N\}$, these are written $\bigcup_{i=1}^N A_i$ and $\bigcap_{i=1}^N A_i$.

**Example:** For each $x \in [0, 1]$, let $A_x = \{(x, t) : t \in \mathbb{R}\}$ be the vertical line through $x$. Then:

$$\bigcup_{x \in [0,1]} A_x = [0, 1] \times \mathbb{R}, \qquad \bigcap_{x \in [0,1]} A_x = \varnothing$$

The intersection is empty because already $A_0 \cap A_1 = \varnothing$.

**Example:** $\bigcap_{n \in \mathbb{N}} \left(0, \tfrac{1}{n}\right) = \varnothing$, by the [Archimedean property](../T/archimedean).

**Remark:** The index set may be infinite, even uncountable. The quantifiers $\exists$ ("there exists") and $\forall$ ("for every") correspond exactly to unions and intersections over indexed families.
