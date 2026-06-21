---
layout: definition
title: "Compact Set"
chapter: "Limits and Continuity"
---

**Definition:** A set $K \subseteq \mathbb{R}$ is **compact** if every sequence $(a_n)$ in $K$ has a [subsequence](../D/subsequence) that [converges](../D/convergence-sequence) to a limit in $K$.

This is called the **sequential compactness** definition of compactness.

**Examples:**

- Every closed bounded interval $[a, b]$ is compact
- The open interval $(0, 1)$ is not compact -- the sequence $a_n = \frac{1}{n}$ has no subsequence converging to a limit in $(0,1)$
- The real line $\mathbb{R}$ is not compact -- the sequence $a_n = n$ has no convergent subsequence

**Remark:** Compactness is the precise condition underlying the [extreme value theorem](../T/extreme-value) and the [uniform continuity theorem](../T/uniform-continuity-theorem), both of which require a closed bounded interval. The [Heine-Borel theorem](../T/heine-borel) characterizes compact subsets of $\mathbb{R}$ as exactly the closed and bounded sets.