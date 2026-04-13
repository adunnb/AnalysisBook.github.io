---
layout: definition
title: "Upper and Lower Sums"
chapter: "Integration"
---

**Definition:** Let $f : [a, b] \to \mathbb{R}$ be bounded and let $P = \{x_0, x_1, \ldots, x_n\}$ be a [partition](../D/partition) of $[a, b]$. For each subinterval $[x_{k-1}, x_k]$, define:

$$M_k = \sup\{f(x) : x \in [x_{k-1}, x_k]\}$$
$$m_k = \inf\{f(x) : x \in [x_{k-1}, x_k]\}$$

The **upper sum** of $f$ with respect to $P$ is:

$$U(f, P) = \sum_{k=1}^{n} M_k (x_k - x_{k-1})$$

The **lower sum** of $f$ with respect to $P$ is:

$$L(f, P) = \sum_{k=1}^{n} m_k (x_k - x_{k-1})$$

**Remark:** For any bounded function and any partition, $L(f, P) \leq U(f, P)$. Moreover, if $P'$ is a refinement of $P$, then:

$$L(f, P) \leq L(f, P') \leq U(f, P') \leq U(f, P)$$

That is, refining a partition brings the upper and lower sums closer together.