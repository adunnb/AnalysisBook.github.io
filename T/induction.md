---
layout: proof
title: "Principle of Mathematical Induction"
chapter: "The Natural Numbers"
link_terms: ["mathematical induction", "induction", "induction hypothesis", "inductive hypothesis", "well-ordering principle"]
---

**Theorem:** Let $S \subseteq \mathbb{N}$ be a set of [natural numbers](../D/natural-numbers) such that:

1. $1 \in S$, and
2. for every $k \in \mathbb{N}$, if $k \in S$ then $k + 1 \in S$.

Then $S = \mathbb{N}$.

Equivalently, if $P(n)$ is a statement for each $n \in \mathbb{N}$, and the **base case** $P(1)$ and the **induction step** $P(k) \Rightarrow P(k + 1)$ for every $k \in \mathbb{N}$ both hold, then $P(n)$ is true for every $n \in \mathbb{N}$. More generally, starting from any $n_0 \in \mathbb{Z}$: if $P(n_0)$ holds and $P(k) \Rightarrow P(k+1)$ for every $k \geq n_0$, then $P(n)$ holds for every $n \geq n_0$.

**Remark:** The proof rests on the **well-ordering principle**, which we take as an axiom about $\mathbb{N}$: every nonempty subset of $\mathbb{N}$ has a least element. For example, the least element of $\{5, 6, 7\}$ is $5$.

The **induction hypothesis** $P(k)$ is an assumption made only to prove the implication $P(k) \Rightarrow P(k + 1)$. It is not an assumption that the conclusion already holds for all $n$.

**Example:** For every $n \geq 3$, $2^n > 2n + 1$. The base case is $2^3 = 8 > 7$. If $2^k > 2k + 1$ for some $k \geq 3$, then:

$$2^{k+1} = 2 \cdot 2^k > 4k + 2 > 2k + 3 = 2(k + 1) + 1$$

**Example:** Every induction step must respect the hypotheses of the statement. The false "theorem" *if $p, q \in \mathbb{N}$ and $\max(p, q) = n$, then $p = q$* has a true base case $n = 1$. Its induction step takes $\max(p, q) = k + 1$, notes $\max(p - 1, q - 1) = k$, and concludes $p - 1 = q - 1$. But the induction hypothesis applies only to natural numbers, and if $p = 1$ or $q = 1$ then $p - 1$ or $q - 1$ is $0 \notin \mathbb{N}$. The step from $n = 1$ to $n = 2$ fails at $(p, q) = (1, 2)$.

**Proof:** Suppose instead that $S \neq \mathbb{N}$. Then the [set difference](../D/set-difference) $\mathbb{N} \setminus S$ is a nonempty [subset](../D/subset) of $\mathbb{N}$, so by the well-ordering principle it has a least element $m$. Since $1 \in S$, we have $m > 1$, so $m - 1 \in \mathbb{N}$. By the minimality of $m$, $m - 1 \notin \mathbb{N} \setminus S$, that is, $m - 1 \in S$. Condition 2 then gives $m = (m - 1) + 1 \in S$, a contradiction. Therefore $S = \mathbb{N}$.

For the statement form, apply the theorem to $S = \{n \in \mathbb{N} : P(n) \text{ is true}\}$. For a starting point $n_0$, apply it to $S = \{n \in \mathbb{N} : P(n + n_0 - 1) \text{ is true}\}$.
