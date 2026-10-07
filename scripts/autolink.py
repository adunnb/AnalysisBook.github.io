#!/usr/bin/env python3
"""Link mentions of a definition/theorem page across D/ and T/.

Usage:
    python3 scripts/autolink.py D/open-set "open set" "closed set"
    python3 scripts/autolink.py D/neighborhood            # uses link_terms or title
    python3 scripts/autolink.py D/open-set "open set" --write
    python3 scripts/autolink.py D/supremum "bounded above" --exclude D/bounded-sequence
    python3 scripts/autolink.py --into D/closed-set     # links *from* a new page

By default, mentions of the target page are linked in every other page.
With --into PAGE it works the other way round: every other page's terms
are looked for in PAGE alone, which is how a new page gets links to what
it uses (its prerequisites in the dependency graph). --exclude then names
pages not to link to.

Terms come from the command line; if none are given, from a `link_terms:`
list in the target page's front matter; failing that, from its title.
Matching is case-insensitive, whole-word, and also accepts plurals
("open sets" matches "open set").

Dry run by default: prints each proposed change. Pass --write to apply.

Never touched: front matter, math ($...$, $$...$$, \\(...\\), \\[...\\]),
inline code, existing links, **bold text** (where pages define their own
terms), HTML tags, headings, and the target page itself.
Files that already link to the target are skipped, and only the first
mention in each file is linked unless --all is given.

The first mention in the main text (definition, statement, proof) is
preferred. Links in **Remark:**, **Example(s):** and **Intuition:**
paragraphs are "see also" links that don't count as dependencies (see
scripts/check.py), so a Remark is linked only when the term appears
nowhere else; the dry run marks those "(see also)".
"""
import argparse
import re
import sys
from pathlib import Path

from check import paragraphs

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
    | \*\*[^*\n]+\*\*             # bold: where a page defines its own terms
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


def link_file(text, pattern, url, link_all, main_only=False):
    """Return (new_text, [(position_in_new_text, in_aside), ...])."""
    fm = read_front_matter(text)
    body = text[len(fm):]

    asides, pos = [], 0
    for para, aside in paragraphs(body):
        if aside:
            asides.append((pos, pos + len(para)))
        pos += len(para)

    def in_aside(i):
        return any(a <= i < b for a, b in asides)

    editable, pos = [], 0
    for m in PROTECTED.finditer(body):
        editable.append((pos, m.start()))
        pos = m.end()
    editable.append((pos, len(body)))
    matches = [m for a, b in editable for m in pattern.finditer(body, a, b)]

    if link_all:
        chosen = matches
    else:
        main = [m for m in matches if not in_aside(m.start())]
        chosen = (main if main_only else main or matches)[:1]

    out, last, hits, size = [], 0, [], len(fm)
    for m in chosen:
        out.append(body[last:m.start()])
        size += m.start() - last
        hits.append((size, in_aside(m.start())))
        link = f"[{m.group(0)}]({url})"
        out.append(link)
        size += len(link)
        last = m.end()
    out.append(body[last:])
    return fm + "".join(out), hits


def context(text, i, width=60):
    """The new link at position i, with some text either side."""
    end = text.index(")", i) + 1
    return text[max(0, i - width): end + width].replace("\n", " ")


def page_path(name):
    """D/open-set or D/open-set.md -> (Path of the file, "D/open-set")."""
    p = Path(name)
    p = p.with_suffix("") if p.suffix == ".md" else p
    f = ROOT / p.with_suffix(".md")
    if not f.exists():
        sys.exit(f"No such page: {f.relative_to(ROOT)}")
    return f, p.as_posix()


def linked_from(text, url):
    """{False} if text links url in its main text, {True} if only in asides."""
    already = re.compile(rf"\]\({re.escape(url)}(?:\.md)?(?:#[^)]*)?\)")
    return {aside for para, aside in paragraphs(text) if already.search(para)}


def link_into(page_file, excluded, write):
    """Link mentions of every other page inside page_file."""
    targets = []
    for d in SEARCH_DIRS:
        for p in sorted((ROOT / d).glob("*.md")):
            if p == page_file or p.resolve() in excluded:
                continue
            terms = terms_from_page(p)
            if terms:
                targets.append((p.relative_to(ROOT).with_suffix("").as_posix(), terms))
    # Longest terms first, so "uniform convergence" claims its text before
    # "convergence" can.
    targets.sort(key=lambda t: -max(len(x) for x in t[1]))

    rel = page_file.relative_to(ROOT)
    print(f"Linking other pages into {rel}" + ("" if write else "   (dry run)"))
    text, count = page_file.read_text(), 0
    for target, terms in targets:
        url = f"../{target}"
        linked_in = linked_from(text, url)
        if False in linked_in:
            continue
        new_text, hits = link_file(text, term_pattern(terms), url, False,
                                   main_only=True in linked_in)
        for i, aside in hits:
            note = "  (see also)" if aside else ""
            print(f"  -> {target}: ...{context(new_text, i)}...{note}")
            count += 1
        text = new_text
    if write and count:
        page_file.write_text(text)
    verb = "Added" if write else "Would add"
    print(f"{verb} {count} link(s).")
    if count and not write:
        print("Re-run with --write to apply, adding --exclude for any wrong ones.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", nargs="?", help="page to link to, e.g. D/open-set or D/open-set.md")
    ap.add_argument("terms", nargs="*", help="phrases to link (default: link_terms or title)")
    ap.add_argument("--write", action="store_true", help="apply changes (default: dry run)")
    ap.add_argument("--all", action="store_true", help="link every mention, not just the first per file")
    ap.add_argument("--exclude", nargs="+", default=[], metavar="PAGE",
                    help="pages to leave alone, e.g. --exclude D/bounded-sequence T/archimedean")
    ap.add_argument("--into", metavar="PAGE",
                    help="link mentions of all other pages inside PAGE instead")
    args = ap.parse_args()

    excluded = {(ROOT / Path(e).with_suffix(".md")).resolve() for e in args.exclude}
    if args.into:
        if args.target or args.terms or args.all:
            ap.error("--into takes no target, terms or --all")
        link_into(page_path(args.into)[0], excluded, args.write)
        return
    if not args.target:
        ap.error("give a target page, or --into PAGE")

    target_file, target = page_path(args.target)
    target = Path(target)

    terms = args.terms or terms_from_page(target_file)
    if not terms:
        sys.exit("No terms given and none found in the page's front matter.")

    url = f"../{target.as_posix()}"
    pattern = term_pattern(terms)

    print(f"Linking {terms} -> {url}" + ("" if args.write else "   (dry run)"))
    changed = 0
    for d in SEARCH_DIRS:
        for path in sorted((ROOT / d).glob("*.md")):
            if path == target_file or path.resolve() in excluded:
                continue
            text = path.read_text()
            # Skip files that already depend on the target. A file that only
            # links it from a Remark/Example/Intuition still gets a main-text
            # link if the term appears there, but no second see-also link.
            linked_in = linked_from(text, url)
            if False in linked_in and not args.all:
                continue
            new_text, hits = link_file(text, pattern, url, args.all,
                                       main_only=True in linked_in)
            if not hits:
                continue
            changed += 1
            rel = path.relative_to(ROOT)
            for i, aside in hits:
                note = "  (see also)" if aside else ""
                print(f"  {rel}: ...{context(new_text, i)}...{note}")
            if args.write:
                path.write_text(new_text)

    verb = "Updated" if args.write else "Would update"
    print(f"{verb} {changed} file(s).")
    if changed and not args.write:
        print("Re-run with --write to apply.")


if __name__ == "__main__":
    main()
