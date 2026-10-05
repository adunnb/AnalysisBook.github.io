---
layout: definition
title: "Union and Intersection"
chapter: "Sets and Functions"
link_terms: ["union", "intersection", "disjoint"]
---

**Definition:** The **union** and **intersection** of sets $A$ and $B$ are:

$$A \cup B = \{x : x \in A \text{ or } x \in B\}$$

$$A \cap B = \{x : x \in A \text{ and } x \in B\}$$

Sets $A$ and $B$ are **disjoint** if $A \cap B = \varnothing$.

**Example:** For $A = \{1, 2, 3\}$ and $B = \{1, 2, 4\}$:

$$A \cup B = \{1, 2, 3, 4\}, \qquad A \cap B = \{1, 2\}$$

**Remark:** The word "or" in a union is inclusive, so elements in both sets are allowed. Directly from the definitions, $A \cup \varnothing = A$, $A \cap \varnothing = \varnothing$, and $A \cap B \subseteq A \subseteq A \cup B$. Unions and intersections of more than two sets are described by [indexed families](../D/indexed-family).
