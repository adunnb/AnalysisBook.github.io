---
layout: definition
title: "Subset and Set Equality"
chapter: "Sets and Functions"
link_terms: ["subset", "proper subset"]
---

**Definition:** For [sets](../D/set) $A$ and $B$, we say $A$ is a **subset** of $B$, written $A \subseteq B$, if every element of $A$ is an element of $B$. If $A \subseteq B$ and $A \neq B$, then $A$ is a **proper subset** of $B$, written $A \subsetneq B$.

Two sets are **equal** exactly when they have the same elements:

$$A = B \iff A \subseteq B \text{ and } B \subseteq A$$

**Example:** $\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R}$, and each of these inclusions is proper.

**Remark:** Membership and inclusion are different relations: $1 \in \{1, 2\}$ and $\{1\} \subseteq \{1, 2\}$, but $\{1\} \notin \{1, 2\}$. The empty set is a subset of every set $A$, since $\varnothing$ has no element that could fail to lie in $A$.

The equality criterion is the standard way to prove two sets are equal: show each is a subset of the other. This is called a proof by **two inclusions** (see [De Morgan's laws](../T/de-morgan)).
