#!/usr/bin/env python3
"""Map every page of K04.pdf to the notes chapter and section that carries it.

K04.pdf is the seminar-class build of notes/original/K04.tex, one slide per page
(184 of each), so page N is the N-th \\begin{slide}. Each slide is assigned to the
notes chapter whose first slide it follows (the table notes/tools/convert.py used
for the conversion) and to the notes section whose heading best matches the last
{\\bfseries ...} heading seen, since the converted headings went through pandoc and
no longer match the LaTeX text exactly.

Page numbers are the ones *printed* on K04's pages, which is what the lecture slides
cite ("σημειώσεις μέχρι τη σελίδα 62"): the unnumbered title page is PDF page 1, so
printed page N is PDF page N+1. The title page itself is page 0.

Writes sources/k04-map.tsv: printed page, notes chapter slug, section heading.

Usage: tools/k04map.py [path/to/notes]   (default: ../notes)
"""

import difflib
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (slug, line of the first slide heading in K04.tex), from notes/tools/convert.py
CHAPTERS = [
    ("00-intro", 83), ("01-first-programs", 567), ("02-types-operators", 1008),
    ("03-control-flow", 1545), ("04-functions", 1948), ("05-pointers-arrays", 2450),
    ("06-memory-strings", 3018), ("07-structs", 3785), ("08-lists-trees", 4518),
    ("09-io", 4859), ("10-preprocessor", 5588), ("11-sorting-searching", 5811),
    ("12-good-practice", 6531),
]


def norm(s):
    s = re.sub(r"\\[a-zA-Z]+|[{}$`*]", " ", s)
    s = "".join(c for c in unicodedata.normalize("NFD", s.lower())
                if unicodedata.category(c) != "Mn")
    return re.sub(r"\W+", " ", s).strip()


def main(argv):
    notes = argv[0] if argv else os.path.join(ROOT, "..", "notes")
    lines = open(os.path.join(notes, "original", "K04.tex"), encoding="iso-8859-7").read().split("\n")
    sections = {}
    for slug, _ in CHAPTERS:
        text = open(os.path.join(notes, "chapters", slug, "README.md"), encoding="utf-8").read()
        sections[slug] = re.findall(r"^## (.+)$", text, re.M)

    rows, page, heading = [], 0, None
    for i, line in enumerate(lines, 1):
        if r"\begin{slide" in line:
            page += 1
            chap = None
            for slug, start in CHAPTERS:
                if i + 1 >= start:
                    chap = slug
            # the slide's heading, if any: the first {\bfseries ...} line before \end{slide}
            for nxt in lines[i:]:
                if r"\end{slide" in nxt:
                    break
                m = re.match(r"\s*\{\\bfseries (.+)\}\s*$", nxt)
                if m and chap:
                    heading = m.group(1)
                    break
            title = ""
            if chap and heading:
                cands = sections[chap]
                scores = [difflib.SequenceMatcher(None, norm(heading), norm(c)).ratio() for c in cands]
                if scores and max(scores) > 0.5:
                    title = cands[scores.index(max(scores))]
            if chap and not title and rows and rows[-1][1] == chap:
                title = rows[-1][2]
            if chap and not title and sections[chap]:
                title = sections[chap][0]
            rows.append((page, chap or "-", title or "-"))

    out = os.path.join(ROOT, "sources", "k04-map.tsv")
    with open(out, "w", encoding="utf-8") as f:
        f.write("k04_page\tnotes_chapter\tnotes_section\n")
        for page, chap, title in rows:
            f.write("%d\t%s\t%s\n" % (page - 1, chap, title))
    print(f"k04map: {len(rows)} pages -> {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
