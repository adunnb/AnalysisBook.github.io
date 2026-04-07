---
layout: proof
title: "Intermediate Value Theorem"
chapter: "Limits and Continuity"
---

**Theorem:** Let $f : [a, b] \to \mathbb{R}$ be [continuous](../D/continuity) on $[a, b]$. If $L$ is any real number with $f(a) < L < f(b)$ (or $f(b) < L < f(a)$), then there exists $c \in (a, b)$ such that $f(c) = L$.

**Remark:** Intuitively, a continuous function cannot jump over a value, it must pass through every intermediate value. This theorem formalizes that intuition and relies essentially on the [completeness axiom](../T/completeness-axiom).

**Proof:** Without loss of generality assume $f(a) < L < f(b)$. Define:

$$A = \{x \in [a, b] : f(x) < L\}$$

Then $A$ is non-empty since $a \in A$, and bounded above by $b$. By the [completeness axiom](../T/completeness-axiom), $c = \sup A$ exists.

We claim $f(c) = L$ by ruling out $f(c) < L$ and $f(c) > L$.

**Case 1: $f(c) < L$.** Since $f$ is continuous at $c$, there exists $\delta > 0$ such that $f(x) < L$ for all $x \in (c - \delta, c + \delta)$. In particular $c + \frac{\delta}{2} \in A$, contradicting $c = \sup A$.

**Case 2: $f(c) > L$.** Since $f$ is continuous at $c$, there exists $\delta > 0$ such that $f(x) > L$ for all $x \in (c - \delta, c + \delta)$. Then $c - \frac{\delta}{2}$ is an upper bound for $A$, contradicting $c = \sup A$.

Therefore $f(c) = L$.