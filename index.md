---
layout: page
title: "AnalysisGraph"
---

<!-- Style -->
<style type="text/css" media="screen">
.container {
  text-align: center;
}
.list {
  text-align: left;
}
h1 {
  font-size: 4em;
  line-height: 1;
  letter-spacing: -1px;
}
</style>

Welcome to **AnalysisGraph** -- *a graph of real analysis*!
Every definition and theorem, with full proofs, linked by what
depends on what.

[Table of Contents](I/ToC) · [Dependency Graph](graph)

---

## Explore logical dependencies

<div class="book-graph home-graph" data-book-graph="feature"
     data-graph-url="{{ '/graph.json' | relative_url }}" data-focus="T/bolzano-weierstrass">
  <p>The <b><a href="T/bolzano-weierstrass">Bolzano&ndash;Weierstrass Theorem</a></b>
  says that every bounded sequence has a convergent subsequence. Above it are
  the results it builds on; below it, the theorems it makes possible. Click any
  page to open it.</p>
  <div class="book-graph-controls"><span data-graph-legend></span></div>
  <div class="book-graph-canvas"></div>
  <p class="home-graph-cta">
    <a href="graph">Explore the full dependency graph &rarr;</a>
    <span>Every definition and theorem, and how they connect.</span>
  </p>
</div>

<script src="{{ '/assets/js/graph.js' | relative_url }}" defer></script>

---

*AnalysisGraph is a work in progress! New content is added regularly.*