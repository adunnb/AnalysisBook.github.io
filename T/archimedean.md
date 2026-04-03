---
layout: proof
title: "Archimedean Property"
chapter: "Completeness and the Real Numbers"
---

**Theorem:** 

(i) For every real number $x \in \mathbb{R}$, there exists a natural number $n \in \mathbb{N}$ such that $n > x$.

(ii) For every real number $y > 0$, there exists $n \in \mathbb{N}$ such that $\frac{1}{n} < y$.

**Proof of (i):** Suppose for contradiction that no such $n$ exists. Then $x$ is an upper bound for $\mathbb{N}$. Since $\mathbb{N}$ is non-empty and bounded above, the [completeness axiom](../T/completeness-axiom) guarantees that $\alpha = \sup \mathbb{N}$ exists.

Since $\alpha$ is the least upper bound, $\alpha - 1$ is not an upper bound of $\mathbb{N}$. So there exists some $n_0 \in \mathbb{N}$ with $n_0 > \alpha - 1$, which gives:

$$n_0 + 1 > \alpha$$

But $n_0 + 1 \in \mathbb{N}$, so this contradicts $\alpha$ being an upper bound of $\mathbb{N}$. Therefore for every $x \in \mathbb{R}$ there exists $n \in \mathbb{N}$ with $n > x$.

**Proof of (ii):** Let $y > 0$. Then $\frac{1}{y} \in \mathbb{R}$, so by (i) there exists $n \in \mathbb{N}$ such that $n > \frac{1}{y}$. Since $y > 0$ and $n > 0$, we can rearrange to get:

$$\frac{1}{n} < y$$