#!/usr/bin/env python3
"""Create a new definition or theorem page and log it in recent.md.

Usage:
    python3 scripts/new_page.py D closed-set "Closed Set" --chapter "Limits and Continuity"
    python3 scripts/new_page.py T rolle "Rolle's Theorem" --chapter "Differentiation"
    python3 scripts/new_page.py D closed-set "Closed Set" --chapter "Limits and Continuity" \\
        --terms "closed set" "closed"

This will:
  1. write D/<slug>.md or T/<slug>.md with front matter and a body template
     (plus a link_terms list if --terms is given, for scripts/autolink.py)
  2. add the page under today's date at the top of recent.md

You still need to add the page to I/ToC.md by hand (its numbering is manual);
scripts/check.py will remind you if you forget, and checks the numbering.
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECENT = ROOT / "recent.md"

KINDS = {
    "D": ("definition", "**Definition:** ", lambda link: f"*{link}*"),
    "T": ("proof", "**Theorem:** \n\n**Proof:** ", lambda link: f"**{link}**"),
}


def existing_chapters():
    chapters = set()
    for d in KINDS:
        for p in (ROOT / d).glob("*.md"):
            m = re.search(r'^chapter:\s*"?(.*?)"?\s*$', p.read_text(), re.MULTILINE)
            if m:
                chapters.add(m.group(1))
    return sorted(chapters)


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def format_date(d):
    return f"{d:%B} {d.day}, {d.year}"


def add_to_recent(entry, date):
    text = RECENT.read_text()
    heading = f"**{format_date(date)}**"
    first = re.search(r"^\*\*[A-Z][a-z]+ \d{1,2}, \d{4}\*\*$", text, re.MULTILINE)

    if first and first.group(0) == heading:
        # Append to the end of today's existing bullet list.
        m = re.compile(r"(?:\n- .*)+").match(text, first.end())
        pos = m.end() if m else first.end()
        text = text[:pos] + f"\n- {entry}" + text[pos:]
    elif first:
        text = text[:first.start()] + f"{heading}\n- {entry}\n\n" + text[first.start():]
    else:
        text = text.rstrip("\n") + f"\n\n{heading}\n- {entry}\n"
    RECENT.write_text(text)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kind", choices=KINDS, help="D for a definition, T for a theorem")
    ap.add_argument("slug", help="file name without .md, e.g. closed-set")
    ap.add_argument("title", help='page title, e.g. "Closed Set"')
    ap.add_argument("--chapter", required=True, help="chapter name as used in other pages")
    ap.add_argument("--new-chapter", action="store_true",
                    help="allow a chapter name no existing page uses")
    ap.add_argument("--terms", nargs="+", metavar="TERM",
                    help="phrases autolink.py should link to this page")
    ap.add_argument("--no-recent", action="store_true", help="don't add to recent.md")
    args = ap.parse_args()

    slug = args.slug.removesuffix(".md")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        sys.exit(f"Slug should be lowercase words joined by hyphens, got: {slug}")
    path = ROOT / args.kind / f"{slug}.md"
    if path.exists():
        sys.exit(f"{args.kind}/{slug}.md already exists.")

    chapters = existing_chapters()
    if args.chapter not in chapters and not args.new_chapter:
        sys.exit(f"Unknown chapter {args.chapter!r}. Existing chapters:\n  "
                 + "\n  ".join(chapters)
                 + "\nUse --new-chapter if this is intentional.")

    layout, body, style = KINDS[args.kind]
    fm = [f"layout: {layout}", f"title: {yaml_str(args.title)}",
          f"chapter: {yaml_str(args.chapter)}"]
    if args.terms:
        fm.append("link_terms: [" + ", ".join(yaml_str(t) for t in args.terms) + "]")
    path.write_text("---\n" + "\n".join(fm) + "\n---\n\n" + body + "\n")
    print(f"Created {args.kind}/{slug}.md")

    if not args.no_recent:
        add_to_recent(style(f"[{args.title}]({args.kind}/{slug})"), datetime.date.today())
        print("Added to recent.md")

    page = f"{args.kind}/{slug}"
    terms = "" if args.terms else f' "{args.title.lower()}"'
    print("\nNext steps (see README, \"Adding a page\"):")
    print(f"  1. write the page, linking what it uses; find missed links with")
    print(f"       python3 scripts/autolink.py --into {page}")
    print(f"  2. add it to I/ToC.md (renumber the entries after it)")
    print(f"  3. link to it from other pages:")
    print(f"       python3 scripts/autolink.py {page}{terms}")
    print(f"  4. python3 scripts/check.py")

if __name__ == "__main__":
    main()
