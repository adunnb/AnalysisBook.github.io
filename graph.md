---
layout: page
title: "Dependency Graph"
---

Every definition and theorem in AnalysisGraph, each drawn below the pages it builds
on. Use it to see what a result needs, or what it leads to. The
[Table of Contents](I/ToC) lists the same pages in reading order.

<div class="book-graph book-graph-full" data-book-graph="full"
     data-graph-url="{{ '/graph.json' | relative_url }}">
  <div class="book-graph-panel">
    <div class="book-graph-fields">
      <label class="book-graph-field">
        <span>Find a page</span>
        <input type="search" list="book-graph-titles" placeholder="e.g. Mean Value Theorem"
               data-graph-search>
      </label>
      <datalist id="book-graph-titles"></datalist>
      <label class="book-graph-field">
        <span>Show one chapter</span>
        <select data-graph-chapter>
          <option value="">All chapters</option>
        </select>
      </label>
      <button type="button" class="book-graph-reset" data-graph-reset>Reset view</button>
    </div>
    <div class="book-graph-try">
      <span>Try:</span>
      <button type="button" data-graph-try="page:T/mean-value">Mean Value Theorem</button>
      <button type="button" data-graph-try="page:T/bolzano-weierstrass">Bolzano&ndash;Weierstrass Theorem</button>
      <button type="button" data-graph-try="chapter:Differentiation">The Differentiation chapter</button>
    </div>
    <ul class="book-graph-tips">
      <li><b>Click</b> a page to highlight everything it depends on and everything that builds on it.</li>
      <li><b>Double-click</b> a page to open it.</li>
      <li><b>Scroll</b> to zoom and <b>drag</b> to move around.</li>
    </ul>
  </div>
  <div class="book-graph-status">
    <div class="book-graph-info" data-graph-info aria-live="polite"></div>
    <span data-graph-legend></span>
  </div>
  <div class="book-graph-canvas book-graph-canvas-full"></div>
</div>

When a page cites another both directly and through a longer chain, only the
chain is drawn; select the page to see its direct links as dashed lines.

<script src="{{ '/assets/js/graph.js' | relative_url }}" defer></script>
