---
layout: definition
title: "Partition of an Interval"
chapter: "Integration"
---

**Definition:** A **partition** of a closed interval $[a, b]$ is a finite ordered set:

$$P = \{x_0, x_1, x_2, \ldots, x_n\}$$

where $a = x_0 < x_1 < x_2 < \cdots < x_n = b$. The partition divides $[a, b]$ into $n$ subintervals $[x_{k-1}, x_k]$ for $k = 1, 2, \ldots, n$.

The **mesh** (or **norm**) of a partition is the length of the largest subinterval:

$$\lVert P \rVert = \max_{1 \leq k \leq n} (x_k - x_{k-1})$$

A partition $P'$ is a **refinement** of $P$ if $P \subseteq P'$, i.e. $P'$ is obtained by adding more points to $P$.