---
layout: proof
title: "Russell's Paradox"
chapter: "Set Theory and Functions"
link_terms: ["Russell's paradox", "set of all sets"]
---

**Theorem:** There is no set $U$ that contains every set as an element, assuming that for any set $U$ and any property $P$ we may form the subset $\{S \in U : P(S)\}$.

**Remark:** The theorem shows that "the collection of all sets" cannot be treated as an ordinary [set](../D/set). In axiomatic set theory, collections that are too large to be sets are called **proper classes**. They cannot be elements of sets, and the usual set operations do not apply to them freely.

**Proof:** Suppose for contradiction that such a set $U$ exists. Using [set-builder notation](../D/set), form the [subset](../D/subset):

$$R = \{S \in U : S \notin S\}$$

Since $R$ is a set, $R \in U$. We ask whether $R \in R$.

If $R \in R$, then $R$ satisfies the defining condition of $R$, so $R \notin R$.

If $R \notin R$, then $R$ satisfies the condition $S \notin S$, so $R \in R$.

Either way we reach a contradiction, so no such $U$ exists.
