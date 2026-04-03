---
layout: definition
title: "Ordered Field"
chapter: "Completeness and the Real Numbers"
---

**Definition:** A **field** is a set $F$ equipped with two operations, addition and multiplication, satisfying the following axioms for all $a, b, c \in F$:

*Addition:*

1. $a + b = b + a$ (commutativity)
2. $(a + b) + c = a + (b + c)$ (associativity)
3. There exists $0 \in F$ such that $a + 0 = a$ (additive identity)
4. There exists $-a \in F$ such that $a + (-a) = 0$ (additive inverse)

*Multiplication:*

5. $ab = ba$ (commutativity)
6. $(ab)c = a(bc)$ (associativity)
7. There exists $1 \in F$ with $1 \neq 0$ such that $a \cdot 1 = a$ (multiplicative identity)
8. For each $a \neq 0$, there exists $a^{-1} \in F$ such that $a \cdot a^{-1} = 1$ (multiplicative inverse)

*Distributivity:*

9. $a(b + c) = ab + ac$

An **ordered field** is a field $F$ together with a relation $<$ satisfying for all $a, b, c \in F$:

1. Exactly one of $a < b$, $a = b$, $b < a$ holds (trichotomy)
2. If $a < b$ and $b < c$, then $a < c$ (transitivity)
3. If $a < b$, then $a + c < b + c$
4. If $a < b$ and $c > 0$, then $ac < bc$

The real numbers $\mathbb{R}$ form an ordered field. The rational numbers $\mathbb{Q}$ also form an ordered field, and are actually the *smallest* ordered field.