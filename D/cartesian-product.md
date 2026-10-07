---
layout: definition
title: "Cartesian Product"
chapter: "Sets and Functions"
link_terms: ["Cartesian product", "ordered pair", "direct product"]
---

**Definition:** The **Cartesian product** (or **direct product**) of [sets](../D/set) $A$ and $B$ is the set of all ordered pairs:

$$A \times B = \{(a, b) : a \in A,\ b \in B\}$$

Two **ordered pairs** are equal, $(a, b) = (c, d)$, exactly when $a = c$ and $b = d$. More generally, for sets $A_1, \ldots, A_N$:

$$A_1 \times \cdots \times A_N = \{(a_1, \ldots, a_N) : a_i \in A_i \text{ for every } i\}$$

**Example:** For $A = \{1, 2, 3\}$ and $B = \{1, 2, 4\}$, the product $A \times B$ has nine elements:

$$(1,1),\ (1,2),\ (1,4),\ (2,1),\ (2,2),\ (2,4),\ (3,1),\ (3,2),\ (3,4)$$

**Example:** $\mathbb{R}^2 = \mathbb{R} \times \mathbb{R}$ is the plane and $\mathbb{R}^3 = \mathbb{R} \times \mathbb{R} \times \mathbb{R}$ is three-dimensional space. The set $\{(x_1, x_2) \in \mathbb{R}^2 : x_1 + x_2 = 1\}$ is a line containing $(0, 1)$, $(1, 0)$, and $(3, -2)$.

**Remark:** Order matters: $(1, 2) \neq (2, 1)$, and $A \times B \neq B \times A$ in general. Pairs and triples are different objects, so $\mathbb{R}^2$ is not literally a [subset](../D/subset) of $\mathbb{R}^3$. It is usually identified with the plane $\{(x_1, x_2, 0)\}$ through the embedding $(x_1, x_2) \mapsto (x_1, x_2, 0)$.
