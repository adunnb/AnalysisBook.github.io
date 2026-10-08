---
layout: proof
title: "Images of Unions and Intersections"
chapter: "Sets and Functions"
link_terms: ["images of unions and intersections"]
---

**Theorem:** Let $f : X \to Y$ be a [function](../D/function) and $A, B \subseteq X$. Then for [images](../D/image):

1. If $A \subseteq B$, then $f(A) \subseteq f(B)$.
2. $f(A \cup B) = f(A) \cup f(B)$.
3. $f(A \cap B) \subseteq f(A) \cap f(B)$.

**Remark:** The inclusion in (3) can be strict. For $f(x) = x^2$ with $A = \{-1\}$ and $B = \{1\}$:

$$f(A \cap B) = \varnothing, \qquad f(A) \cap f(B) = \{1\}$$

Equality in (3) holds for all $A, B$ exactly when $f$ is [injective](../D/injective). In contrast, [preimages](../T/preimage-operations) respect every set operation.

**Proof of (1):** If $y \in f(A)$, then $y = f(x)$ for some $x \in A \subseteq B$, so $y \in f(B)$.

**Proof of (2):** $y \in f(A \cup B)$ if and only if $y = f(x)$ for some $x$ in the [union](../D/union-intersection) $A \cup B$. That holds if and only if $y = f(x)$ for some $x \in A$ or some $x \in B$, which means $y \in f(A) \cup f(B)$.

**Proof of (3):** Since $A \cap B \subseteq A$ and $A \cap B \subseteq B$, part (1) gives $f(A \cap B) \subseteq f(A)$ and $f(A \cap B) \subseteq f(B)$.
