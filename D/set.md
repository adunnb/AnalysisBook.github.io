---
layout: definition
title: "Sets"
chapter: "Set Theory and Functions"
link_terms: ["empty set", "set-builder notation"]
---

**Definition:** A **set** is a collection of objects, called its **elements**. We write $a \in A$ if $a$ is an element of $A$, and $a \notin A$ otherwise. The order in which elements are listed does not matter, and repeating an element does not produce a new one:

$$\{1, 2, 3\} = \{3, 1, 2\} = \{1, 1, 2, 3\}$$

The **empty set** $\varnothing$ is the set with no elements.

A set may be described by a condition on its elements using **set-builder notation**:

$$\{x \in A : P(x)\}$$

read "the set of all $x$ in $A$ such that $P(x)$."

**Example:** $\{a \in \mathbb{Z} : 2 \nmid a\}$ is the set of odd [integers](../D/natural-numbers), and $\{x \in \mathbb{R} : x^2 < 4\} = (-2, 2)$.

**Remark:** In this book a set is treated as a basic, undefined notion. Some care is needed, however: not every collection of objects can be a set. In particular, there is no "[set of all sets](../T/russell-paradox)."
