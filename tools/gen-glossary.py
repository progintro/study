#!/usr/bin/env python3
"""Merge every chapter's «Ορολογία» table into one glossary, glossary.md.

Each chapter defines its terms in a three-column table (Ελληνικά | English | Σύντομος
ορισμός). The glossary lists every term once, sorted by its Greek name, with the
first definition given and links to every chapter that defines it. The site serves
it as /glossary.html; the book prints it as an appendix; agents get it inside
llms-full.txt.

A term is the same term in two chapters when its English name matches (ignoring
case and anything in parentheses), or, lacking an English name, its Greek one.

Usage: tools/gen-glossary.py [--check]
"""

import glob
import os
import re
import sys
import unicodedata

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "glossary.md")


def key(s):
    s = re.sub(r"\([^)]*\)|`", "", s).strip().lower()
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def cells(line):
    line = line.strip().strip("|")
    return [c.strip() for c in re.split(r"(?<!\\)\|", line)]


def main(argv):
    m = yaml.safe_load(open(os.path.join(ROOT, "sources", "manifest.yaml"), encoding="utf-8"))
    terms = {}
    for l in m["lectures"]:
        path = os.path.join(ROOT, "chapters", l["slug"], "README.md")
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        sec = re.search(r"^## Ορολογία\n(.*?)(?=^## )", text, re.M | re.S)
        if not sec:
            continue
        rows = [r for r in sec.group(1).split("\n") if r.strip().startswith("|")]
        for r in rows[2:]:  # skip header and separator
            c = cells(r)
            if len(c) < 3 or not c[0]:
                continue
            el, en, definition = c[0], c[1], c[2]
            k = key(en) or key(el)
            t = terms.setdefault(k, {"el": el, "en": en, "def": definition, "chapters": []})
            if l["n"] not in t["chapters"]:
                t["chapters"].append(l["n"])
    slugs = {l["n"]: l["slug"] for l in m["lectures"]}
    out = ["# Γλωσσάριο", "", "<!-- {% raw %} -->", "",
           "Όλοι οι όροι του οδηγού, από τους πίνακες «Ορολογία» των κεφαλαίων, με τον αγγλικό",
           "όρο, σύντομο ορισμό και τα κεφάλαια όπου εμφανίζονται.", "",
           "| Ελληνικά | English | Ορισμός | Κεφάλαια |", "| --- | --- | --- | --- |"]
    for t in sorted(terms.values(), key=lambda t: key(t["el"])):
        chs = ", ".join(f"[{n}](chapters/{slugs[n]}/)" for n in sorted(t["chapters"]))
        out.append(f"| {t['el']} | {t['en']} | {t['def']} | {chs} |")
    out += ["", "<!-- {% endraw %} -->"]
    new = "\n".join(out) + "\n"
    old = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else None
    if "--check" in argv:
        if old != new:
            print("glossary.md is out of date (run tools/gen-glossary.py)")
            return 1
        return 0
    if old != new:
        open(OUT, "w", encoding="utf-8").write(new)
    print(f"gen-glossary: {len(terms)} terms")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
