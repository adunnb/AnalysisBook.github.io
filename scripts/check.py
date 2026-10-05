#!/usr/bin/env python3
"""Sanity checks for the book. Run before pushing:

    python3 scripts/check.py

Reports:
  - broken internal links (in D/, T/, I/ and the top-level pages)
  - D/ and T/ pages missing from the table of contents
  - front matter problems (missing title/chapter, wrong layout for the folder)
  - math delimiter problems ($ / $$ unbalanced, \\left without \\right)

Exits with status 1 if anything is found.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOC = ROOT / "I" / "ToC.md"
BASEURL = "/AnalysisBook.github.io"
LAYOUTS = {"D": "definition", "T": "proof"}

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


def main():
    problems = []
    check_links(content_files(), problems)
    check_toc(problems)
    check_front_matter(problems)
    check_math(problems)
    for p in problems:
        print(p)
    print(f"\n{len(problems)} problem(s) found." if problems else "All checks passed.")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
