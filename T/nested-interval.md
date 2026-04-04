---
layout: proof
title: "Nested Interval Property"
chapter: "Completeness and the Real Numbers"
---

**Theorem:** For each $n \in \mathbb{N}$, let $I_n = [a_n, b_n]$ be a closed bounded interval. Suppose the intervals are nested, meaning:

$$I_1 \supseteq I_2 \supseteq I_3 \supseteq \cdots$$

Then the intersection $\bigcap_{n=1}^{\infty} I_n$ is non-empty.

**Remark:** This theorem is a direct consequence of the [completeness axiom](../T/completeness-axiom) and fails for open intervals. For example, the open intervals $\left(0, \frac{1}{n}\right)$ are nested but their intersection is empty.

**Proof:** Since the intervals are nested, we have $a_n \leq a_{n+1}$ and $b_{n+1} \leq b_n$ for all $n$. In particular $a_n \leq b_n$ for all $n$, so every $b_n$ is an upper bound for the set $A = \{a_n : n \in \mathbb{N}\}$.

Since $A$ is non-empty and bounded above, the [completeness axiom](../T/completeness-axiom) guarantees $x = \sup A$ exists. We claim $x \in I_n$ for all $n$, i.e. $a_n \leq x \leq b_n$.

- $a_n \leq x$: This holds since $x = \sup A \geq a_n$ for all $n$.
- $x \leq b_n$: Since $b_n$ is an upper bound for $A$ and $x$ is the least upper bound, $x \leq b_n$.

Therefore $x \in \bigcap_{n=1}^{\infty} I_n$, which is thus non-empty.