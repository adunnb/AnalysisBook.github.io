---
layout: definition
title: "Function"
chapter: "Sets and Functions"
link_terms: ["function", "domain", "codomain", "restriction", "graph of a function"]
---

**Definition:** A **function** $f : A \to B$ assigns to every $a \in A$ exactly one element $f(a) \in B$. The [set](../D/set) $A$ is the **domain** of $f$, and $B$ is its **codomain**.

The **graph** of $f$ is the set:

$$\{(a, f(a)) : a \in A\} \subseteq A \times B$$

Equivalently, a [subset](../D/subset) $G$ of the [Cartesian product](../D/cartesian-product) $A \times B$ is the graph of a function exactly when for every $a \in A$ there is exactly one $b \in B$ with $(a, b) \in G$.

For $E \subseteq A$, the **restriction** of $f$ to $E$ is the function $f\vert_E : E \to B$ given by $f\vert_E(x) = f(x)$. The rule is unchanged; only the domain is smaller.

**Example:** Let $f : \mathbb{R} \to \mathbb{R}$, $f(x) = x^2$. Both $2$ and $-2$ map to $4$, while no real number maps to $-1$.

**Remark:** Every element of the domain must have exactly one value. An element of the codomain, however, may have no [preimage](../D/preimage), one, or several. For a graph in the plane, this is the **vertical line test**: every vertical line above a point of the domain meets the graph exactly once. Two functions are equal when they have the same domain, the same codomain, and the same value at every point.
