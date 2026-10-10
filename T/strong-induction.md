---
layout: proof
title: "Strong Induction"
chapter: "The Natural Numbers"
link_terms: ["strong induction"]
---

**Theorem:** Let $P(n)$ be a statement for each integer $n \geq n_0$. Suppose that $P(n_0)$ is true and that, for every $k \geq n_0$:

$$P(n_0),\ P(n_0 + 1),\ \ldots,\ P(k) \text{ all true} \implies P(k + 1) \text{ true}$$

Then $P(n)$ is true for every $n \geq n_0$.

**Remark:** Strong induction allows the induction step to use *every* earlier case, not just the previous one. It is no stronger than ordinary [mathematical induction](../T/induction): the proof below derives it from ordinary induction. When the step reaches back more than one case, as in the example below, several base cases are needed.

**Example:** Every integer $n \geq 18$ can be written as $n = 4a + 7b$ with $a, b \in \mathbb{N}_0$. The base cases are:

$$18 = 4 \cdot 1 + 7 \cdot 2, \quad 19 = 4 \cdot 3 + 7 \cdot 1, \quad 20 = 4 \cdot 5 + 7 \cdot 0, \quad 21 = 4 \cdot 0 + 7 \cdot 3$$

For $k \geq 21$, suppose every integer from $18$ through $k$ has such a representation. Then $18 \leq k - 3 \leq k$, so $k - 3 = 4a + 7b$, and $k + 1 = 4(a + 1) + 7b$. Four base cases are needed because the step reaches back four places, from $k + 1$ to $k - 3$.

**Proof:** For $k \geq n_0$, let $Q(k)$ be the statement "$P(j)$ is true for every integer $n_0 \leq j \leq k$." Then $Q(n_0)$ is the statement $P(n_0)$, which is true. If $Q(k)$ is true, then $P(n_0), \ldots, P(k)$ are all true, so the hypothesis gives $P(k + 1)$, and therefore $Q(k + 1)$ is true. By the [principle of mathematical induction](../T/induction) starting at $n_0$, $Q(k)$ holds for every $k \geq n_0$. In particular $P(n)$ holds for every $n \geq n_0$.
