# A First Course in Real Analysis

An open, rigorous, and readable introduction to real analysis for 
undergraduate mathematics students, presented as a Jekyll site 
hosted on GitHub Pages.

The book covers the real number system, sequences and series, 
continuity, differentiation, and integration, loosely following 
the structure of Abbott's *Understanding Analysis* (2nd ed., 
Springer, 2015).

**Live site:** https://adunnb.github.io/AnalysisBook.github.io

**Dependency graph:** https://adunnb.github.io/AnalysisBook.github.io/graph,
an interactive map of every definition and theorem and which results
each one builds on.

## Structure

Content is organized into two folders:

- `D/` — Definitions
- `T/` — Theorems (each file contains the statement and proof)

The table of contents is in `I/ToC.md`, and `recent.md` is a dated feed
of new pages. `graph.md` is the interactive dependency graph.

## Adding a page

1. **Create it.** This writes the front matter and adds the page to
   `recent.md` under today's date:

   ```sh
   python3 scripts/new_page.py D closed-set "Closed Set" \
       --chapter "Limits and Continuity" --terms "closed set" "closed sets"
   ```

   `--chapter` must be a name other pages already use (the script lists
   them if it isn't); for the first page of a new section add
   `--new-chapter`. `--terms` are the phrases that should link to this
   page from elsewhere.

2. **Write it**, and link the pages it uses where the statement or proof
   uses them (see [Writing a page](#writing-a-page)). These links are the
   page's prerequisites in the dependency graph. To find the ones you
   missed:

   ```sh
   python3 scripts/autolink.py --into D/closed-set
   ```

   Review the suggestions, then re-run with `--write`, using `--exclude`
   for any wrong ones.

3. **Add it to `I/ToC.md`** at its place in reading order. If it goes in
   the middle of a subsection, renumber the entries after it.

4. **Link to it from existing pages:**

   ```sh
   python3 scripts/autolink.py D/closed-set
   ```

   Again a dry run first; then `--write`, with `--exclude` as needed.

5. **Check:** `python3 scripts/check.py` must pass. It catches a page
   missing from the ToC, ToC numbering mistakes, broken links and
   dependency cycles.

6. **Commit and push.** The dependency graph, `graph.json` and each
   page's "Uses / Used in" lists are rebuilt from the links on every
   site build; there is nothing to update by hand.

## Writing a page

Each page starts with front matter:

```yaml
---
layout: definition            # "definition" in D/, "proof" in T/
title: "Closed Set"
chapter: "Limits and Continuity"   # must match the name other pages use
link_terms: ["closed set"]          # optional, for scripts/autolink.py
ignore_edges: ["T/heine-borel"]     # optional, see below
---
```

Link to other pages as `[text](../D/slug)` or `[text](../T/slug)`, with no
`.md` extension. The dependency graph and the "Uses / Used in" lists are
built from these links, and a link written any other way is invisible to
them.

**Dependencies vs. "see also" links.** Only links in the main text (the
definition, statement and proof) count as dependencies. Links in
paragraphs that start with `**Remark:**`, `**Example:**`, `**Examples:**`
or `**Intuition:**` are "see also" links: readers can follow them, but
they are left out of the graph and the "Uses / Used in" lists. So put
asides, generalizations and forward references ("the same proof works for
any indexed family") in a Remark, and link a concept
the result actually needs where the statement or proof uses it. An
unlabeled paragraph (a list, display math) belongs to the labeled
paragraph before it.

**`ignore_edges`** lists pages this page links to in its main text without
depending on them. The link stays in the text but is left out of the
graph. It is rarely needed; `scripts/check.py` reports a dependency cycle
when one is, since one side of the cycle is usually a forward reference.

## Scripts

Three Python scripts in `scripts/` (no dependencies; run `--help` on any
of them for details):

1. **`new_page.py`** creates a page with the right front matter and adds
   it to `recent.md`:

   ```sh
   python3 scripts/new_page.py D closed-set "Closed Set" \
       --chapter "Limits and Continuity" --terms "closed set"
   ```

   Add the page to `I/ToC.md` by hand; the numbering there is manual
   (`check.py` verifies it). Use `--new-chapter` for a chapter name no
   page uses yet.

2. **`autolink.py`** links mentions of a page across `D/` and `T/`. It is a
   dry run by default: review the proposed links, leave out wrong ones
   with `--exclude`, then apply with `--write`.

   ```sh
   python3 scripts/autolink.py D/closed-set
   python3 scripts/autolink.py D/closed-set --exclude T/heine-borel --write
   ```

   It only links the first mention per file, and never touches math,
   existing links, headings or bold text.

   `--into PAGE` works the other way round: it looks for every other
   page's terms in PAGE alone, to link a new page to what it uses.

   ```sh
   python3 scripts/autolink.py --into D/closed-set
   ```

   Terms come from each page's `link_terms`, or else its title. A page
   without `link_terms` is only found where its full title appears, so
   give pages `link_terms` when the title isn't how the text names them
   ("Upper Bound and Supremum" -> `["supremum", "upper bound"]`).

3. **`check.py`** should pass before every push. It reports broken links,
   pages missing from the ToC, ToC numbering out of sequence (gaps,
   duplicates), front matter and math-delimiter problems,
   links not in the `../D/slug` form, stale `ignore_edges` entries and
   dependency cycles. `python3 scripts/check.py --aside-links` lists the
   links that appear only in Remarks, Examples and Intuitions, to check
   that no real dependency is linked only there.

`autolink.py` links the first mention in the main text, and only falls
back to a Remark, Example or Intuition when the term appears nowhere else
(the dry run marks those "(see also)").

## Dependency graph

Every build regenerates the graph from the links in `D/` and `T/`:

- `_includes/out-links.html` extracts a page's links. Everything else uses
  it, so the lists, the data and the drawings always agree.
- `_includes/connections.html` adds the "Uses", "Used in" and
  "Prerequisite graph" sections to the bottom of each page (included by
  `_layouts/definition.html` and `_layouts/proof.html`).
- `graph.json` is the graph as data: every page, and an edge for every
  link.
- `assets/js/graph.js` draws the per-page graphs, the full graph on
  `graph.md` and the featured graph on the home page, using Cytoscape.js
  and dagre from a CDN. To feature a different page on the home page,
  change `data-focus` (and the sentence about it) in `index.md`.

In the drawings, a direct link that a longer chain already implies (A uses
B, B uses C, and A also uses C) is hidden; selecting a page in the full
graph shows its hidden links as dashed lines. The lists and `graph.json`
keep every link.

The rule for which links count as dependencies (main text vs. Remark,
Example and Intuition paragraphs, minus `ignore_edges`) is implemented
twice: in `_includes/out-links.html` for the site and in `scripts/check.py`
(`paragraphs()` and `check_graph()`) for the checks. Change both together.

Liquid includes share variables with whatever includes them, so the
include files prefix their internal variables (`_ol_` in
`out-links.html`). Keep doing this when editing them.

## Styles

The site loads `assets/main.css`, built from `assets/main.scss`, which
imports the minima theme and then the partials in `_sass/`. Add styles
there. `assets/css/style.scss` is **not** loaded by any page, so changes
to it have no effect.

## Status

This book is a work in progress. New pages are added regularly:
Chapter 0 covers set theory and functions, and Chapter I is being
expanded into a full chapter on number systems (induction,
cardinality and the rationals); see
[Recently Added](https://adunnb.github.io/AnalysisBook.github.io/recent).

## Attribution

This site was built using the Jekyll setup from the
[StatProofBook](https://github.com/StatProofBook/StatProofBook.github.io),
used under CC-BY-SA 4.0.

## License

The content of this book is licensed under
[CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); the full
text is in [LICENSE](LICENSE).
