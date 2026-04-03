---
layout: proof
title: "Archimedean Property"
chapter: "Completeness and the Real Numbers"
---

**Theorem:** For every real number $x \in \mathbb{R}$, there exists a natural number $n \in \mathbb{N}$ such that $n > x$.

**Proof:** Suppose for contradiction that no such $n$ exists. Then $x$ is an upper bound for $\mathbb{N}$. Since $\mathbb{N}$ is non-empty and bounded above, the [completeness axiom](../T/completeness-axiom) guarantees that $\alpha = \sup \mathbb{N}$ exists.

Since $\alpha$ is the least upper bound, $\alpha - 1$ is not an upper bound of $\mathbb{N}$. So there exists some $n_0 \in \mathbb{N}$ with $n_0 > \alpha - 1$, which gives:

$$n_0 + 1 > \alpha$$

But $n_0 + 1 \in \mathbb{N}$, so this contradicts $\alpha$ being an upper bound of $\mathbb{N}$. Therefore no such upper bound $x$ exists, and for every $x \in \mathbb{R}$ there exists $n \in \mathbb{N}$ with $n > x$.