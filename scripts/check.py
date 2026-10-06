#!/usr/bin/env python3
"""Sanity checks for the book. Run before pushing:

    python3 scripts/check.py

Reports:
  - broken internal links (in D/, T/, I/ and the top-level pages)
  - D/ and T/ pages missing from the table of contents
  - front matter problems (missing title/chapter, wrong layout for the folder)
  - math delimiter problems ($ / $$ unbalanced, \\left without \\right)
  - links between D/ and T/ pages not written as ../D/slug or ../T/slug
    (the form the dependency graph and autolink.py expect)
  - bad ignore_edges entries (unknown page, a page that isn't linked, or
    one only linked from a Remark/Example/Intuition, which never counts)
  - cycles in the dependency graph; break each one by adding the
    forward-reference side to that page's ignore_edges, e.g.
        ignore_edges: ["T/mean-value"]

Exits with status 1 if anything is found.

Links in **Remark:**, **Example(s):** and **Intuition:** paragraphs are
"see also" links: readers can follow them, but they are not dependencies.
To review them (some may be real dependencies that should also be linked
in the statement or proof):

    python3 scripts/check.py --aside-links
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOC = ROOT / "I" / "ToC.md"
BASEURL = "/AnalysisBook.github.io"
LAYOUTS = {"D": "definition", "T": "proof"}

GRAPH_LINK = re.compile(r"^\.\./([DT]/[a-z0-9]+(?:-[a-z0-9]+)*)(?:#[\w-]*)?$")
LINK = re.compile(r"\]\(([^)\s]+)\)|href=\"([^\"]+)\"")
FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
CODE = re.compile(r"```.*?```|`[^`]*`", re.DOTALL)


def rel(p):
    return p.relative_to(ROOT).as_posix()


def content_files():
    files = [p for d in ("D", "T", "I") for p in sorted((ROOT / d).glob("*.md"))]
    files += sorted(ROOT.glob("*.md"))
    return [p for p in files if p.name != "README.md"]


def resolve(src, target):
    """Return True if an internal link target exists on disk."""
    target = target.split("#")[0].split("?")[0]
    if not target:
        return True
    if target.startswith(BASEURL):
        target = target[len(BASEURL):]
    base = ROOT if target.startswith("/") else src.parent
    p = (base / target.lstrip("/")).resolve()
    if p.suffix == ".html":
        p = p.with_suffix("")
    candidates = [p, p.with_suffix(".md"), p.with_suffix(".html"),
                  p / "index.md", p / "index.html"]
    return any(c.is_file() for c in candidates)


def check_links(files, problems):
    for f in files:
        text = CODE.sub("", f.read_text())
        for m in LINK.finditer(text):
            target = m.group(1) or m.group(2)
            if re.match(r"[a-z]+:|#|\{\{", target):  # external, anchor, liquid
                continue
            if not resolve(f, target):
                line = text.count("\n", 0, m.start()) + 1
                problems.append(f"{rel(f)}:{line}: broken link -> {target}")


def check_toc(problems):
    toc = TOC.read_text()
    linked = set()
    for m in LINK.finditer(toc):
        target = (m.group(1) or m.group(2)).split("#")[0]
        linked.add((TOC.parent / target).resolve().with_suffix(""))
    for d in LAYOUTS:
        for p in sorted((ROOT / d).glob("*.md")):
            if p.resolve().with_suffix("") not in linked:
                problems.append(f"{rel(p)}: not linked from I/ToC.md")


def check_front_matter(problems):
    for d, layout in LAYOUTS.items():
        for p in sorted((ROOT / d).glob("*.md")):
            m = FRONT_MATTER.match(p.read_text())
            if not m:
                problems.append(f"{rel(p)}: missing front matter")
                continue
            fm = m.group(1)
            got = re.search(r"^layout:\s*(\S+)", fm, re.MULTILINE)
            if not got or got.group(1) != layout:
                problems.append(f"{rel(p)}: layout should be '{layout}'")
            for key in ("title", "chapter"):
                if not re.search(rf"^{key}:\s*\S", fm, re.MULTILINE):
                    problems.append(f"{rel(p)}: missing '{key}' in front matter")


def check_math(problems):
    for d in LAYOUTS:
        for p in sorted((ROOT / d).glob("*.md")):
            text = FRONT_MATTER.sub("", p.read_text())
            text = CODE.sub("", text).replace(r"\$", "")
            if text.count("$$") % 2:
                problems.append(f"{rel(p)}: odd number of $$ delimiters")
                continue
            inline = re.sub(r"\$\$.*?\$\$", "", text, flags=re.DOTALL)
            for para in re.split(r"\n\s*\n", inline):
                if para.count("$") % 2:
                    snippet = " ".join(para.split())[:70]
                    problems.append(f"{rel(p)}: unbalanced $ in paragraph: {snippet}")
            lefts = len(re.findall(r"\\left\b", text))
            rights = len(re.findall(r"\\right\b", text))
            if lefts != rights:
                problems.append(f"{rel(p)}: {lefts} \\left vs {rights} \\right")


def fm_list(text, key):
    """Read a YAML list (inline [..] or block - ..) from front matter."""
    m = FRONT_MATTER.match(text)
    fm = m.group(1) if m else ""
    inline = re.search(rf"^{key}:\s*\[(.*?)\]", fm, re.MULTILINE)
    if inline:
        items = inline.group(1).split(",")
    else:
        block = re.search(rf"^{key}:\s*\n((?:\s*-\s*.+\n?)+)", fm, re.MULTILINE)
        items = re.findall(r"-\s*(.+)", block.group(1)) if block else []
    return [i.strip().strip("\"'") for i in items if i.strip()]


# A paragraph opening with one of these bold labels starts a "see also"
# stretch; any other bold label ends it, and unlabeled paragraphs (lists,
# display math) continue whichever is current. Mirrors out-links.html.
ASIDE_LABELS = ("Remark", "Example", "Intuition")


def is_aside_label(paragraph, current):
    head = paragraph.lstrip().replace("<p>", "", 1).replace("<strong>", "**", 1)
    if not head.startswith("**"):
        return current
    return any(head[2:2 + len(label)] == label for label in ASIDE_LABELS)


def paragraphs(body):
    """Split a page body into [(text, is_aside)], keeping the separators so
    the pieces join back into the original text."""
    out, aside = [], False
    for i, piece in enumerate(body.split("\n\n")):
        if i:
            out.append(("\n\n", aside))
        aside = is_aside_label(piece, aside)
        out.append((piece, aside))
    return out


def graph_pages():
    return {p.relative_to(ROOT).with_suffix("").as_posix(): p
            for d in LAYOUTS for p in sorted((ROOT / d).glob("*.md"))}


def check_graph(problems):
    """Link format, ignore_edges and cycles; mirrors _includes/out-links.html."""
    pages = graph_pages()
    edges, asides = {}, {}
    for node, path in pages.items():
        text = path.read_text()
        body = CODE.sub("", FRONT_MATTER.sub("", text))
        linked, main = [], []
        for para, aside in paragraphs(body):
            for m in LINK.finditer(para):
                target = m.group(1) or m.group(2)
                if re.match(r"[a-z]+:|#|\{\{", target):
                    continue
                g = GRAPH_LINK.match(target)
                if g:
                    linked.append(g.group(1))
                    if not aside:
                        main.append(g.group(1))
                elif re.search(r"(?:^|/)[DT]/", target):
                    line = text.count("\n", 0, text.find(target)) + 1
                    problems.append(f"{rel(path)}:{line}: write links between pages as "
                                    f"../D/slug or ../T/slug -> {target}")
        ignore = fm_list(text, "ignore_edges")
        for t in ignore:
            if t not in pages:
                problems.append(f"{rel(path)}: ignore_edges names unknown page {t}")
            elif t not in linked:
                problems.append(f"{rel(path)}: ignore_edges lists {t}, which the page doesn't link to")
            elif t not in main:
                problems.append(f"{rel(path)}: ignore_edges entry {t} is not needed; it is only "
                                f"linked from a Remark/Example/Intuition, which never counts")
        edges[node] = [t for t in dict.fromkeys(main)
                       if t != node and t in pages and t not in ignore]
        asides[node] = [t for t in dict.fromkeys(linked)
                        if t not in main and t != node and t in pages]

    for cycle in find_cycles(edges):
        problems.append("dependency cycle: " + " -> ".join(cycle))
    return asides


def find_cycles(edges):
    """One shortest cycle per strongly connected component (Tarjan)."""
    index, low, stack, on_stack, sccs = {}, {}, [], set(), []

    def visit(v):
        index[v] = low[v] = len(index)
        stack.append(v)
        on_stack.add(v)
        for w in edges[v]:
            if w not in index:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = set()
            while True:
                w = stack.pop()
                on_stack.discard(w)
                comp.add(w)
                if w == v:
                    break
            if len(comp) > 1:
                sccs.append(comp)

    for v in sorted(edges):
        if v not in index:
            visit(v)

    cycles = []
    for comp in sccs:
        start = min(comp)
        prev, queue = {start: None}, [start]
        while queue:
            v = queue.pop(0)
            nxt = [w for w in edges[v] if w in comp]
            if start in nxt:
                path = [v]
                while prev[path[-1]] is not None:
                    path.append(prev[path[-1]])
                cycles.append(path[::-1] + [start])
                break
            for w in nxt:
                if w not in prev:
                    prev[w] = v
                    queue.append(w)
    return sorted(cycles)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--aside-links", action="store_true",
                    help="also list links that appear only in Remark/Example/Intuition paragraphs")
    args = ap.parse_args()

    problems = []
    check_links(content_files(), problems)
    check_toc(problems)
    check_front_matter(problems)
    check_math(problems)
    asides = check_graph(problems)
    if args.aside_links:
        print("Links only in Remark/Example/Intuition paragraphs (not dependencies):")
        for node, targets in asides.items():
            for t in targets:
                print(f"  {node} -> {t}")
        print()
    for p in problems:
        print(p)
    print(f"\n{len(problems)} problem(s) found." if problems else "All checks passed.")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
