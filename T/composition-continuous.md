---
layout: proof
title: "Composition of Continuous Functions"
chapter: "Limits and Continuity"
---

**Theorem:** Let $f : A \to \mathbb{R}$ and $g : B \to \mathbb{R}$ where $f(A) \subseteq B$. If $f$ is [continuous at](../D/continuity) $c \in A$ and $g$ is continuous at $f(c) \in B$, then the composition $g \circ f : A \to \mathbb{R}$ is continuous at $c$.

**Proof:** Let $(x_n)$ be a sequence in $A$ with $x_n \to c$. Since $f$ is continuous at $c$:

$$f(x_n) \to f(c)$$

Since $g$ is continuous at $f(c)$:

$$g(f(x_n)) \to g(f(c))$$

Therefore $(g \circ f)(x_n) \to (g \circ f)(c)$, and since $(x_n)$ was arbitrary, $g \circ f$ is continuous at $c$.