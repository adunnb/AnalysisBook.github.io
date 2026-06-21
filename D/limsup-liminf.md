---
layout: definition
title: "Limsup and Liminf"
chapter: "Sequences and Series"
---

**Definition:** Let $(a_n)$ be a [bounded sequence](../D/bounded-sequence). For each $n \in \mathbb{N}$, define:

$$y_n = \sup\{a_k : k \geq n\}, \qquad z_n = \inf\{a_k : k \geq n\}$$

The sequence $(y_n)$ is decreasing and bounded below, and $(z_n)$ is increasing and bounded above. By the [monotone convergence theorem](../T/monotone-convergence), both converge. The **limit superior** and **limit inferior** of $(a_n)$ are defined as:

$$\limsup_{n \to \infty} a_n = \lim_{n \to \infty} y_n = \lim_{n \to \infty} \sup\{a_k : k \geq n\}$$

$$\liminf_{n \to \infty} a_n = \lim_{n \to \infty} z_n = \lim_{n \to \infty} \inf\{a_k : k \geq n\}$$

**Properties:** For any bounded sequence $(a_n)$:

1. $\liminf_{n \to \infty} a_n \leq \limsup_{n \to \infty} a_n$
2. $(a_n)$ converges if and only if $\liminf_{n \to \infty} a_n = \limsup_{n \to \infty} a_n$, in which case all three are equal
3. $\limsup_{n \to \infty} (-a_n) = -\liminf_{n \to \infty} a_n$