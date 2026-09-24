#!/usr/bin/env python3
"""Build everything that derives from the question bank in questions/.

  * each chapter's «Ασκήσεις» list, between <!-- exercises --> and <!-- /exercises -->
    (only the questions whose *primary* chapter is this one get a full entry; the
    ones that merely also need it are listed under «Σχετικές»);
  * questions/README.md, the index by chapter and by source;
  * the chapter table on the home page, README.md, between <!-- chapters --> markers;
  * with --build DIR: DIR/questions.md (every statement, grouped by chapter, for the
    book appendix and llms-full.txt) and DIR/questions.json.

Usage:
  tools/gen-exercises.py              rewrite the chapter lists and questions/README.md
  tools/gen-exercises.py --check      fail if any of them is out of date (CI)
  tools/gen-exercises.py --lint [f…]  validate question files (all, or the given ones)
  tools/gen-exercises.py --build DIR  also write DIR/questions.md and DIR/questions.json
"""

import glob
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KINDS = {  # directory -> (front-matter kind, heading in a chapter)
    "slides": ("slides", "Από τις διαφάνειες"),
    "labs": ("lab", "Από τα εργαστήρια"),
    "homework": ("homework", "Από τις εργασίες"),
    "exams": ("exam", "Από τα θέματα εξετάσεων"),
}
TYPES = {"programming", "short-answer", "trace", "debug", "multiple-choice", "tooling"}
STARS = {1: "★☆☆", 2: "★★☆", 3: "★★★"}
BEGIN, END = "<!-- exercises -->", "<!-- /exercises -->"
SITE = "https://progintro.github.io/study"


def manifest():
    return yaml.safe_load(open(os.path.join(ROOT, "sources", "manifest.yaml"), encoding="utf-8"))


def split_front(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    return yaml.safe_load(m.group(1)), text[m.end():]


def load_questions():
    qs = []
    for path in sorted(glob.glob(os.path.join(ROOT, "questions", "*", "*.md"))):
        meta, body = split_front(open(path, encoding="utf-8").read())
        qs.append({"path": os.path.relpath(path, ROOT), "meta": meta or {}, "body": body.strip()})
    return qs


def lint(qs, only=None):
    topics = yaml.safe_load(open(os.path.join(ROOT, "questions", "topics.yaml"), encoding="utf-8"))
    chapters = {l["n"] for l in manifest()["lectures"]}
    seen, errors = {}, []
    for q in qs:
        m, p = q["meta"], q["path"]
        if only and os.path.abspath(os.path.join(ROOT, p)) not in only:
            continue
        err = lambda msg: errors.append(f"{p}: {msg}")
        if not m:
            err("missing front matter")
            continue
        d = p.split(os.sep)[1]
        if m.get("id") != os.path.splitext(os.path.basename(p))[0]:
            err(f"id {m.get('id')!r} does not match the file name")
        if m.get("id") in seen:
            err(f"duplicate id, also in {seen[m['id']]}")
        seen[m.get("id")] = p
        if d not in KINDS or m.get("kind") != KINDS[d][0]:
            err(f"kind {m.get('kind')!r} does not match directory {d!r}")
        if not m.get("title"):
            err("missing title")
        src = m.get("source") or {}
        if not src.get("title"):
            err("missing source.title")
        ch = m.get("chapters")
        if not ch or not isinstance(ch, list) or any(c not in chapters for c in ch):
            err(f"chapters must be a non-empty list of chapter numbers, found {ch!r}")
        for t in m.get("topics") or []:
            if t not in topics:
                err(f"unknown topic {t!r} (add it to questions/topics.yaml)")
        if not m.get("topics"):
            err("missing topics")
        if m.get("difficulty") not in STARS:
            err(f"difficulty must be 1, 2 or 3, found {m.get('difficulty')!r}")
        if m.get("type") not in TYPES:
            err(f"type must be one of {sorted(TYPES)}, found {m.get('type')!r}")
        if "## Υπόδειξη" not in q["body"]:
            err("missing «## Υπόδειξη» section")
        if not q["body"].split("## Υπόδειξη")[0].strip():
            err("empty statement")
    return errors


def entry(q, rel):
    m = q["meta"]
    link = f"{rel}{q['path']}"
    years = (m.get("source") or {}).get("years")
    src = m["source"]["title"]
    return f"- [{m['title']}]({link}): {src} · {STARS[m['difficulty']]} · {m['type']}"


def chapter_block(n, qs):
    primary = [q for q in qs if q["meta"]["chapters"][0] == n]
    related = [q for q in qs if n in q["meta"]["chapters"][1:]]
    out = [BEGIN, ""]
    if not primary and not related:
        out += ["Δεν υπάρχουν ακόμα ασκήσεις για αυτό το κεφάλαιο.", ""]
    for d, (kind, heading) in KINDS.items():
        group = sorted((q for q in primary if q["meta"]["kind"] == kind),
                       key=lambda q: (q["meta"]["difficulty"], q["meta"]["id"]))
        if group:
            out += [f"### {heading}", ""] + [entry(q, "../../") for q in group] + [""]
    if related:
        out += ["### Σχετικές ασκήσεις από άλλα κεφάλαια", ""]
        out += [entry(q, "../../") + f" (κεφ. {q['meta']['chapters'][0]})"
                for q in sorted(related, key=lambda q: (q["meta"]["chapters"][0], q["meta"]["id"]))]
        out += [""]
    out.append(END)
    return "\n".join(out)


def index(qs, lectures):
    out = ["# Τράπεζα ασκήσεων", "",
           "Όλες οι ασκήσεις του οδηγού μελέτης, από τις διαφάνειες, τα εργαστήρια, τις",
           "εργασίες και τα θέματα εξετάσεων, ανά κεφάλαιο. Κάθε άσκηση έχει υπόδειξη,",
           "όχι λύση. Δυσκολία: ★☆☆ άμεση εφαρμογή, ★★☆ συνδυασμός ιδεών, ★★★ επιπέδου εξέτασης.",
           "",
           f"Σε μορφή για εργαλεία: [`questions.json`]({SITE}/downloads/questions.json).", ""]
    for l in lectures:
        group = sorted((q for q in qs if q["meta"]["chapters"][0] == l["n"]),
                       key=lambda q: (list(KINDS).index(q["path"].split(os.sep)[1]),
                                      q["meta"]["difficulty"], q["meta"]["id"]))
        if not group:
            continue
        label = "Παράρτημα Α" if l.get("appendix") else f"Κεφάλαιο {l['n']}"
        out += [f"## [{label}: {l['title']}](../chapters/{l['slug']}/)", ""]
        out += [entry(q, "../") for q in group] + [""]
    return "\n".join(out).rstrip() + "\n"


def fill(text, block, begin=BEGIN, end=END):
    if begin not in text or end not in text:
        return None
    a, b = text.index(begin), text.index(end) + len(end)
    return text[:a] + block + text[b:]


def home_table(m, qs):
    """The chapter table of README.md: one row per chapter that exists, by part."""
    topics = yaml.safe_load(open(os.path.join(ROOT, "questions", "topics.yaml"), encoding="utf-8"))
    out, part = ["<!-- chapters -->"], None
    for l in m["lectures"]:
        path = os.path.join(ROOT, "chapters", l["slug"], "README.md")
        if not os.path.exists(path):
            continue
        meta, _ = split_front(open(path, encoding="utf-8").read())
        if l["part"] != part:
            if part:
                out += ["  </tbody>", "</table>"]
            part = l["part"]
            name = m["parts"][part]
            label = name if part == "X" else f"Μέρος {'ΑΒΓΔΕ'['ABCDE'.index(part)]}: {name}"
            out += ["", f"### {label}", "", '<table class="lab-index">', "  <thead>",
                    "    <tr><th>#</th><th>Κεφάλαιο</th><th>Θέματα</th><th>Ασκήσεις</th><th>PDF</th></tr>",
                    "  </thead>", "  <tbody>"]
        n = sum(1 for q in qs if q["meta"]["chapters"][0] == l["n"])
        tags = ", ".join(topics.get(t, t) for t in (meta or {}).get("topics") or [])
        num = "Α" if l.get("appendix") else str(l["n"])
        out += ["    <tr>", f"      <td>{num}</td>",
                f'      <td><a href="chapters/{l["slug"]}/">{l["title"]}</a></td>',
                f"      <td>{tags}</td>", f"      <td>{n}</td>",
                f'      <td><a href="downloads/{l["slug"]}.pdf">PDF</a></td>', "    </tr>"]
    if part:
        out += ["  </tbody>", "</table>"]
    out += ["", "<!-- /chapters -->"]
    return "\n".join(out)


def build(qs, lectures, outdir):
    os.makedirs(outdir, exist_ok=True)
    md = ["# Τράπεζα ασκήσεων", ""]
    for l in lectures:
        group = sorted((q for q in qs if q["meta"]["chapters"][0] == l["n"]),
                       key=lambda q: (list(KINDS).index(q["path"].split(os.sep)[1]),
                                      q["meta"]["difficulty"], q["meta"]["id"]))
        if not group:
            continue
        label = "Παράρτημα Α" if l.get("appendix") else f"Κεφάλαιο {l['n']}"
        md += [f"## {label}: {l['title']}", ""]
        for q in group:
            m = q["meta"]
            md += [f"### {m['title']}", "",
                   f"*{m['source']['title']}* · {STARS[m['difficulty']]} · {m['type']} · `{m['id']}`", ""]
            # demote the question's own headings below the ### title
            md += [re.sub(r"^(#+) ", lambda h: "#" * max(4, len(h.group(1)) + 2) + " ", q["body"], flags=re.M), ""]
    open(os.path.join(outdir, "questions.md"), "w", encoding="utf-8").write("\n".join(md))
    data = [dict(q["meta"], path=q["path"], url=f"{SITE}/{os.path.splitext(q['path'])[0]}.html",
                 statement=q["body"].split("## Υπόδειξη")[0].strip(),
                 hint=q["body"].split("## Υπόδειξη", 1)[-1].strip()) for q in qs]
    json.dump(data, open(os.path.join(outdir, "questions.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, default=str)


def main(argv):
    known = {"--lint", "--check", "--build"}
    if any(a.startswith("-") and a not in known for a in argv):
        print(__doc__)
        return 2
    qs = load_questions()
    if argv and argv[0] == "--lint":
        only = {os.path.abspath(a) for a in argv[1:]} or None
        errors = lint(qs, only)
        print("\n".join(errors) if errors else f"gen-exercises: {len(qs)} questions valid")
        return 1 if errors else 0
    errors = lint(qs)
    if errors:
        print("\n".join(errors))
        return 1
    check = "--check" in argv
    lectures = manifest()["lectures"]
    stale = []
    for l in lectures:
        path = os.path.join(ROOT, "chapters", l["slug"], "README.md")
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        new = fill(text, chapter_block(l["n"], qs))
        if new is None:
            stale.append(f"{os.path.relpath(path, ROOT)}: no {BEGIN} markers")
        elif new != text:
            stale.append(os.path.relpath(path, ROOT))
            if not check:
                open(path, "w", encoding="utf-8").write(new)
    ipath = os.path.join(ROOT, "questions", "README.md")
    new = index(qs, lectures)
    if not os.path.exists(ipath) or open(ipath, encoding="utf-8").read() != new:
        stale.append("questions/README.md")
        if not check:
            open(ipath, "w", encoding="utf-8").write(new)
    hpath = os.path.join(ROOT, "README.md")
    home = open(hpath, encoding="utf-8").read()
    new = fill(home, home_table(manifest(), qs), "<!-- chapters -->", "<!-- /chapters -->")
    if new is not None and new != home:
        stale.append("README.md")
        if not check:
            open(hpath, "w", encoding="utf-8").write(new)
    if "--build" in argv:
        build(qs, lectures, argv[argv.index("--build") + 1])
    if check and stale:
        print("out of date (run tools/gen-exercises.py):\n  " + "\n  ".join(stale))
        return 1
    print(f"gen-exercises: {len(qs)} questions, {len(stale)} files updated")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
