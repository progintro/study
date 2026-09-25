#!/usr/bin/env python3
"""Defect linter for chapters/*/README.md.

Catches what the LaTeX conversion tends to leave behind and what breaks one of the
three renderers (GitHub, the Jekyll site, the xelatex PDF):

  latex      a \\command outside code and math - a macro pandoc did not know
  bullet     an empty list item ("- - x"), the remains of seminar's blank-bullet trick
  math-space a $...$ span with whitespace just inside a delimiter, which pandoc's
             gfm reader then does not treat as math
  math-brace \\{ or \\} inside math, which kramdown turns into a bare brace
  html       raw HTML, which the LaTeX writer drops from the PDF
  image      an image whose file does not exist
  front      missing or inconsistent front matter (layout / chapter / prev / next and
             the study-guide keys: lecture, title, date, part, slides, topics, notes, labs)
  topic      a topics: tag that is not in questions/topics.yaml
  section    the H1 or the H2 sections are missing or out of order (see STYLE.md)
  fence      a code fence followed by text on the same line (``` Για …), which
             never closes the block and swallows the rest of the chapter
  anchor     a link to #x within the chapter where no <a id="x"> or heading has that id
  liquid     body not wrapped in <!-- {% raw %} --> ... <!-- {% endraw %} -->, so C code
             such as {{'a','b'}} would break the Jekyll build

Usage: tools/lint.py [--strict] [files...]   (--strict: exit 1 on any finding)
"""

import glob
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECTIONS = ["Σύνοψη", "Θεωρία", "Παραδείγματα", "Κύρια σημεία", "Ορολογία", "Διάβασμα",
            "Συχνά λάθη", "Ερωτήσεις κατανόησης", "Ασκήσεις"]
REQUIRED = ["lecture", "title", "date", "part", "slides", "topics", "notes", "labs"]


def strip_code(text):
    """Blank out fenced blocks and code spans, keeping line numbers intact."""
    text = re.sub(r"^[ \t]*```.*?^[ \t]*```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.M | re.S)
    return re.sub(r"`[^`\n]+`", "``", text)


def check(path, chapters):
    findings = []
    raw = open(path, encoding="utf-8").read()
    text = strip_code(raw)
    lines = text.split("\n")

    def add(kind, lineno, msg):
        findings.append(f"{os.path.relpath(path, ROOT)}:{lineno}: [{kind}] {msg}")

    for i, line in enumerate(lines, 1):
        nomath = re.sub(r"\$\$.+?\$\$|\$[^$]+\$", "", line)
        for m in re.finditer(r"\\[a-zA-Z]+", nomath):
            add("latex", i, m.group(0))
        if re.match(r"\s*[-*] [-*] ", line):
            add("bullet", i, line.strip()[:60])
        for m in re.finditer(r"(?<!\$)\$(?!\$)([^$]+)\$(?!\$)", line):
            if m.group(1) != m.group(1).strip():
                add("math-space", i, m.group(0)[:60])
        for m in re.finditer(r"\$[^$]+\$", line):
            if re.search(r"\\[{}]", m.group(0)):
                add("math-brace", i, m.group(0)[:60])
        if re.search(r"<(?!!--)[a-zA-Z/][^>]*>", nomath) and "<a id=" not in nomath:
            add("html", i, line.strip()[:60])
        for m in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", line):
            if not os.path.exists(os.path.join(os.path.dirname(path), m.group(1))):
                add("image", i, m.group(1))

    for i, line in enumerate(raw.split("\n"), 1):
        if re.match(r"\s*```[^`\s]* +\S", line):
            add("fence", i, line.strip()[:60])

    ids = set(re.findall(r'<a id="([^"]+)"></a>', raw))
    ids |= {re.sub(r"[^\w\- ]", "", h.strip().lower()).replace(" ", "-")
            for h in re.findall(r"^#{1,6} (.+)$", text, re.M)}
    for i, line in enumerate(raw.split("\n"), 1):
        for target in re.findall(r"\]\(#([^)\s]+)\)", line):
            if target not in ids:
                add("anchor", i, f"#{target} matches no anchor or heading in this file")

    if "chapters" in path and not ("<!-- {% raw %} -->" in raw and raw.rstrip().endswith("<!-- {% endraw %} -->")):
        add("liquid", 1, "chapter body is not wrapped in raw tags")

    slug = os.path.basename(os.path.dirname(path))
    if slug in chapters:
        n = chapters.index(slug)
        fm = re.match(r"---\n(.*?)\n---\n", raw, re.S)
        try:
            meta = (yaml.safe_load(fm.group(1)) if fm else None) or {}
        except yaml.YAMLError as e:
            meta = {}
            add("front", 1, f"front matter is not valid YAML: {e}")
        want = {"layout": "chapter", "chapter": n,
                "prev": chapters[n - 1] if n else None,
                "next": chapters[n + 1] if n + 1 < len(chapters) else None}
        for k, v in want.items():
            if meta.get(k) != v:
                add("front", 1, f"{k}: expected {v!r}, found {meta.get(k)!r}")
        for k in REQUIRED:
            if k not in meta:
                add("front", 1, f"missing {k}")
        for t in meta.get("topics") or []:
            if t not in TOPICS:
                add("topic", 1, f"unknown topic {t!r} (add it to questions/topics.yaml)")

        h1 = re.findall(r"^# (.+)$", text, re.M)
        if len(h1) != 1 or not re.match(r"(Κεφάλαιο \d+|Παράρτημα [Α-Ω]): ", h1[0]):
            add("section", 1, f"expected one H1 «Κεφάλαιο N: …», found {h1!r}")
        h2 = [h.strip() for h in re.findall(r"^## (.+)$", text, re.M)]
        if h2 != SECTIONS:
            add("section", 1, f"H2 sections should be {SECTIONS}, found {h2}")
        for marker in ("exercises", "kahoot", "misconceptions"):
            if f"<!-- {marker} -->" not in raw or f"<!-- /{marker} -->" not in raw:
                add("section", 1, f"missing <!-- {marker} --> ... <!-- /{marker} --> markers")
    return findings


TOPICS = yaml.safe_load(open(os.path.join(ROOT, "questions", "topics.yaml"), encoding="utf-8"))


def main(argv):
    strict = "--strict" in argv
    files = [a for a in argv if not a.startswith("--")]
    # chapter order comes from the manifest, so a chapter lints correctly on its own,
    # before its neighbours exist
    manifest = yaml.safe_load(open(os.path.join(ROOT, "sources", "manifest.yaml"), encoding="utf-8"))
    chapters = [l["slug"] for l in manifest["lectures"]]
    if not files:
        files = sorted(glob.glob(os.path.join(ROOT, "chapters", "*", "README.md")))
    findings = [f for p in files for f in check(p, chapters)]
    print("\n".join(findings) if findings else f"lint: {len(files)} files clean")
    return 1 if strict and findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
