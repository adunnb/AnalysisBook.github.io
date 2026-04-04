---
layout: definition
title: "Subsequence"
chapter: "Sequences and Series"
---

**Definition:** Let $(a_n)$ be a sequence. A **subsequence** of $(a_n)$ is a sequence of the form $(a_{n_k})$ where $n_1 < n_2 < n_3 < \cdots$ is a strictly increasing sequence of natural numbers.

**Intuition:** A subsequence is obtained by selecting an infinite collection of terms from the original sequence, in order, and discarding the rest.

**Example:** If $a_n = \frac{1}{n}$, then $a_{2k} = \frac{1}{2k}$ is the subsequence of even-indexed terms:

$$\frac{1}{2}, \frac{1}{4}, \frac{1}{6}, \frac{1}{8}, \ldots$$

**Remark:** If $(a_n) \to L$, then every subsequence $(a_{n_k}) \to L$ as well. This fact is often used contrapositively: if two subsequences converge to different limits, the original sequence diverges.