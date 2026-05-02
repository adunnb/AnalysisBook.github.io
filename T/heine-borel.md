---
layout: proof
title: "Heine-Borel Theorem"
chapter: "Limits and Continuity"
---

**Theorem:** A set $K \subseteq \mathbb{R}$ is [compact](../D/compact-set) if and only if it is closed and bounded.

**Proof:**

**($\Rightarrow$) Compact implies closed and bounded.**

**Bounded:** Suppose $K$ is not bounded. Then for each $n \in \mathbb{N}$ there exists $a_n \in K$ with $\lvert a_n \rvert > n$. The sequence $(a_n)$ has no convergent subsequence since its terms diverge to infinity, contradicting compactness.

**Closed:** Suppose $(a_n)$ is a sequence in $K$ converging to some $L \in \mathbb{R}$. Since $K$ is compact, $(a_n)$ has a subsequence converging to some $x \in K$. By [uniqueness of limits](../T/limit-uniqueness), $x = L$. Therefore $L \in K$, so $K$ is closed.

**($\Leftarrow$) Closed and bounded implies compact.**

Let $K$ be closed and bounded, and let $(a_n)$ be a sequence in $K$. Since $K$ is bounded, $(a_n)$ is a bounded sequence. By [Bolzano-Weierstrass](../T/bolzano-weierstrass), $(a_n)$ has a convergent subsequence $a_{n_k} \to L$. Since $K$ is closed and $a_{n_k} \in K$ for all $k$, we have $L \in K$. Therefore every sequence in $K$ has a subsequence converging to a limit in $K$, so $K$ is compact.