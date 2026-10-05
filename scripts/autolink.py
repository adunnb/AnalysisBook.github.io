#!/usr/bin/env python3
"""Link mentions of a definition/theorem page across D/ and T/.

Usage:
    python3 scripts/autolink.py D/open-set "open set" "closed set"
    python3 scripts/autolink.py D/neighborhood            # uses link_terms or title
    python3 scripts/autolink.py D/open-set "open set" --write
    python3 scripts/autolink.py D/supremum "bounded above" --exclude D/bounded-sequence

Terms come from the command line; if none are given, from a `link_terms:`
list in the target page's front matter; failing that, from its title.
Matching is case-insensitive, whole-word, and also accepts plurals
("open sets" matches "open set").

Dry run by default: prints each proposed change. Pass --write to apply.

Never touched: front matter, math ($...$, $$...$$, \\(...\\), \\[...\\]),
inline code, existing links, HTML tags, headings, and the target page itself.
Files that already link to the target are skipped, and only the first
mention in each file is linked unless --all is given.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEARCH_DIRS = ["D", "T"]

# Spans that must never be rewritten. Order matters: longer delimiters first.
PROTECTED = re.compile(
    r"""
      \$\$.*?\$\$                 # display math
    | (?<!\\)\$.*?(?<!\\)\$       # inline math
    | \\\(.*?\\\)                 # \( ... \)
    | \\\[.*?\\\]                 # \[ ... \]
    | `[^`]*`                     # inline code
    | !?\[[^\]]*\]\([^)]*\)       # markdown links / images
    | <a\b.*?</a>                 # html anchors
    | <[^>]+>                     # any other html tag
    | ^\#.*$                      # headings
    """,
    re.DOTALL | re.MULTILINE | re.VERBOSE,
)

FRONT_MATTER = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)


def read_front_matter(text):
    m = FRONT_MATTER.match(text)
    return m.group(0) if m else ""


def terms_from_page(path):
    fm = read_front_matter(path.read_text())
    m = re.search(r"^link_terms:\s*\[(.*?)\]", fm, re.MULTILINE)
    if m:
        return [t.strip().strip("\"'") for t in m.group(1).split(",") if t.strip()]
    m = re.search(r"^link_terms:\s*\n((?:\s*-\s*.+\n)+)", fm, re.MULTILINE)
    if m:
        return [re.sub(r"^\s*-\s*", "", l).strip().strip("\"'")
                for l in m.group(1).splitlines()]
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', fm, re.MULTILINE)
    return [m.group(1).lower()] if m else []


def term_pattern(terms):
    # Longest first so "uniform convergence" wins over "convergence".
    alts = sorted(set(terms), key=len, reverse=True)
    body = "|".join(re.escape(t).replace(r"\ ", r"\s+") for t in alts)
    return re.compile(rf"(?<![\w-])(?:{body})(?:s|es)?(?![\w-])", re.IGNORECASE)


def link_file(text, pattern, url, link_all):
    """Return (new_text, list_of_matched_strings)."""
    fm = read_front_matter(text)
    body = text[len(fm):]

    out, hits, pos = [], [], 0
    segments = []
    for m in PROTECTED.finditer(body):
        segments.append((body[pos:m.start()], True))
        segments.append((m.group(0), False))
        pos = m.end()
    segments.append((body[pos:], True))

    for seg, editable in segments:
        if not editable or (hits and not link_all):
            out.append(seg)
            continue

        def repl(m):
            if hits and not link_all:
                return m.group(0)
            hits.append(m.group(0))
            return f"[{m.group(0)}]({url})"

        out.append(pattern.sub(repl, seg))

    return fm + "".join(out), hits


def context(text, needle, width=60):
    i = text.find(needle)
    s = text[max(0, i - width): i + len(needle) + width].replace("\n", " ")
    return s


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", help="page to link to, e.g. D/open-set or D/open-set.md")
    ap.add_argument("terms", nargs="*", help="phrases to link (default: link_terms or title)")
    ap.add_argument("--write", action="store_true", help="apply changes (default: dry run)")
    ap.add_argument("--all", action="store_true", help="link every mention, not just the first per file")
    ap.add_argument("--exclude", nargs="+", default=[], metavar="PAGE",
                    help="pages to leave alone, e.g. --exclude D/bounded-sequence T/archimedean")
    args = ap.parse_args()

    target = Path(args.target)
    target = target.with_suffix("") if target.suffix == ".md" else target
    target_file = ROOT / target.with_suffix(".md")
    if not target_file.exists():
        sys.exit(f"No such page: {target_file.relative_to(ROOT)}")

    terms = args.terms or terms_from_page(target_file)
    if not terms:
        sys.exit("No terms given and none found in the page's front matter.")

    url = f"../{target.as_posix()}"
    pattern = term_pattern(terms)
    excluded = {(ROOT / Path(e).with_suffix(".md")).resolve() for e in args.exclude}
    already_linked = re.compile(rf"\]\({re.escape(url)}(?:\.md)?(?:#[^)]*)?\)")

    print(f"Linking {terms} -> {url}" + ("" if args.write else "   (dry run)"))
    changed = 0
    for d in SEARCH_DIRS:
        for path in sorted((ROOT / d).glob("*.md")):
            if path == target_file or path.resolve() in excluded:
                continue
            text = path.read_text()
            if already_linked.search(text) and not args.all:
                continue
            new_text, hits = link_file(text, pattern, url, args.all)
            if not hits:
                continue
            changed += 1
            rel = path.relative_to(ROOT)
            for h in hits:
                print(f"  {rel}: ...{context(new_text, f'[{h}]({url})')}...")
            if args.write:
                path.write_text(new_text)

    verb = "Updated" if args.write else "Would update"
    print(f"{verb} {changed} file(s).")
    if changed and not args.write:
        print("Re-run with --write to apply.")


if __name__ == "__main__":
    main()
