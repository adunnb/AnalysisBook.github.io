---
layout: definition
title: "Set Difference and Complement"
chapter: "Set Theory and Functions"
link_terms: ["complement", "set difference", "symmetric difference"]
---

**Definition:** The **difference** of sets $A$ and $B$ is:

$$A \setminus B = \{x : x \in A \text{ and } x \notin B\}$$

The **symmetric difference** is the set of elements in exactly one of $A$ and $B$:

$$A \,\triangle\, B = (A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B)$$

If all sets under consideration lie inside a fixed **ambient set** $U$, the **complement** of $A \subseteq U$ is:

$$A^c = U \setminus A$$

**Example:** For $A = \{1, 2, 3\}$ and $B = \{1, 2, 4\}$: $A \setminus B = \{3\}$, $B \setminus A = \{4\}$, and $A \,\triangle\, B = \{3, 4\}$.

**Remark:** A complement depends on the ambient set. The complement of $[0, 1]$ in $\mathbb{R}$ is $(-\infty, 0) \cup (1, \infty)$, but its complement in $[0, 2]$ is $(1, 2]$. Note also that $A \setminus \varnothing = A$ and $\varnothing \setminus A = \varnothing$.
