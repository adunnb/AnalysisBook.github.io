---
layout: proof
title: "Infimum Property"
chapter: "Completeness and the Real Numbers"
---

**Theorem:** Every non-empty subset of $\mathbb{R}$ that is bounded below has an [infimum](../D/infimum) in $\mathbb{R}$.

**Remark:** This is the mirror image of the [completeness axiom](../T/completeness-axiom) and follows directly from it. Together they say that $\mathbb{R}$ is complete in both directions.

**Proof:** Let $A \subseteq \mathbb{R}$ be non-empty and bounded below. Define:

$$-A = \{-a : a \in A\}$$

Then $-A$ is non-empty and bounded above -- if $b$ is a lower bound for $A$ then $-b$ is an upper bound for $-A$. By the [completeness axiom](../T/completeness-axiom), $\sup(-A)$ exists. We claim $\inf A = -\sup(-A)$.

Let $s = \sup(-A)$. Then $-a \leq s$ for all $a \in A$, so $-s \leq a$ for all $a \in A$, meaning $-s$ is a lower bound for $A$. If $b$ is any lower bound for $A$, then $-b$ is an upper bound for $-A$, so $s \leq -b$, giving $-s \geq b$. Therefore $-s = \inf A$.