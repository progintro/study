#!/usr/bin/env python3
"""Build everything that derives from the question bank in questions/.

  * three generated blocks in each chapter (only questions whose *primary* chapter is
    this one, except «Σχετικές»):
      - <!-- misconceptions -->, closing «Συχνά λάθη»: the chapter's Kahoot questions
        that have a «Συχνή παρανόηση», hardest first, with the class's % correct;
      - <!-- kahoot -->, closing «Ερωτήσεις κατανόησης»: all the chapter's Kahoot
        questions, easiest first, with the % correct;
      - <!-- exercises -->, the «Ασκήσεις» ladder: slide questions (warm-up), labs,
        homework, exams, each easiest first, then «Σχετικές» from other chapters;
  * labels, so every item can be cited and found (see STYLE.md, «Labels»):
      §N.k  the H3 sections of «Θεωρία» and «Παραδείγματα» (anchor sN-k)
      ΕN.k  the «Ερωτήσεις κατανόησης» items (anchor eN-k)
      ΚN.k  the chapter's Kahoot questions (anchor kN-k)
      ΑN.k  the «Ασκήσεις» ladder, numbered straight through (anchor aN-k)
    numbered from the current order, like an edition of a book; a question's id is
    its permanent reference. _data/refs.yml maps each question id to its label;
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
KINDS = {  # directory -> (front-matter kind, heading in a chapter), in ladder order
    "slides": ("slides", "Ζέσταμα: από τις διαφάνειες"),
    "labs": ("lab", "Εργαστήριο"),
    "homework": ("homework", "Εργασίες"),
    "exams": ("exam", "Θέματα εξετάσεων"),
    "kahoot": ("kahoot", "Kahoot από το αμφιθέατρο"),
}
TYPES = {"programming", "short-answer", "trace", "debug", "multiple-choice", "tooling"}
STARS = {1: "★☆☆", 2: "★★☆", 3: "★★★"}
BEGIN, END = "<!-- exercises -->", "<!-- /exercises -->"
MISC = ("<!-- misconceptions -->", "<!-- /misconceptions -->")
KAHOOT = ("<!-- kahoot -->", "<!-- /kahoot -->")
SITE = "https://progintro.github.io/study"
NOTE_2023 = ("Στα θέματα της online εξέτασης Δεκεμβρίου 2023 (`exam-2023-fall-*`) ισχύει "
             "για όλες τις ασκήσεις: τα προγράμματα πρέπει να είναι ευανάγνωστα, αποδοτικά σε "
             "χώρο και χρόνο και να έχουν έξοδο ίδια με τα παραδείγματα εκτέλεσης. Για είσοδο "
             "εκτός προδιαγραφών το πρόγραμμα τερματίζει με exit code 1 και μήνυμα σφάλματος.")


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
        if m.get("kind") == "kahoot":
            st = m.get("stats") or {}
            if not isinstance(st.get("responses"), int) or not isinstance(st.get("accuracy"), int):
                err("kahoot questions need stats.responses and stats.accuracy (integers)")
            if not m.get("answer"):
                err("kahoot questions need the correct answer in `answer`")
        if "## Υπόδειξη" not in q["body"]:
            err("missing «## Υπόδειξη» section")
        if not q["body"].split("## Υπόδειξη")[0].strip():
            err("empty statement")
    return errors


def accuracy(q):
    return (q["meta"].get("stats") or {}).get("accuracy", 0)


def ladder(qs, n):
    """The chapter's «Ασκήσεις» in order: (heading, [questions]) per group, Kahoot excluded."""
    groups = []
    for d, (kind, heading) in KINDS.items():
        if kind == "kahoot":
            continue
        group = sorted((q for q in qs if q["meta"]["kind"] == kind and q["meta"]["chapters"][0] == n),
                       key=lambda q: (q["meta"]["difficulty"], q["meta"]["id"]))
        if group:
            groups.append((heading, group))
    return groups


def kahoots(qs, n):
    """The chapter's Kahoot questions, easiest first."""
    return sorted((q for q in qs if q["meta"]["kind"] == "kahoot" and q["meta"]["chapters"][0] == n),
                  key=lambda q: (-accuracy(q), q["meta"]["id"]))


def labels(qs, lectures):
    """id -> {"label", "anchor", "n"} for every question, from the current order."""
    refs = {}
    for l in lectures:
        n = l["n"]
        i = 0
        for _, group in ladder(qs, n):
            for q in group:
                i += 1
                refs[q["meta"]["id"]] = {"label": f"Α{n}.{i}", "anchor": f"a{n}-{i}", "n": n}
        for i, q in enumerate(kahoots(qs, n), 1):
            refs[q["meta"]["id"]] = {"label": f"Κ{n}.{i}", "anchor": f"k{n}-{i}", "n": n}
    return refs


def entry(q, rel, refs, anchor=True):
    """One list line: the label (linking to the question's page), title and metadata."""
    m, r = q["meta"], refs[q["meta"]["id"]]
    stats = m.get("stats") or {}
    acc = f" · {stats['accuracy']}% σωστές απαντήσεις" if "accuracy" in stats else ""
    a = f'<a id="{r["anchor"]}"></a>' if anchor else ""
    return (f"- {a}**[{r['label']}]({rel}{q['path']})** {m['title']}: {m['source']['title']} · "
            f"{STARS[m['difficulty']]} · {m['type']}{acc} · `{m['id']}`")


def span(group, refs):
    first, last = refs[group[0]["meta"]["id"]]["label"], refs[group[-1]["meta"]["id"]]["label"]
    return first if first == last else f"{first}–{last}"


def chapter_block(n, qs, refs):
    """«Ασκήσεις»: everything but Kahoot, from warm-up to exam level."""
    related = sorted((q for q in qs if q["meta"]["kind"] != "kahoot" and n in q["meta"]["chapters"][1:]),
                     key=lambda q: (q["meta"]["chapters"][0], q["meta"]["id"]))
    groups = ladder(qs, n)
    out = [BEGIN, ""]
    if not groups and not related:
        out += ["Δεν υπάρχουν ακόμα ασκήσεις για αυτό το κεφάλαιο.", ""]
    for heading, group in groups:
        out += [f"### {heading} ({span(group, refs)})", ""] + [entry(q, "../../", refs) for q in group] + [""]
    if related:
        out += ["### Σχετικές ασκήσεις από άλλα κεφάλαια", ""]
        out += [entry(q, "../../", refs, anchor=False) for q in related] + [""]
    out.append(END)
    return "\n".join(out)


def kahoot_block(n, qs, refs):
    """«Ερωτήσεις κατανόησης»: the chapter's Kahoot questions, easiest first."""
    group = kahoots(qs, n)
    out = [KAHOOT[0], ""]
    if group:
        out += [f"### Kahoot από το αμφιθέατρο ({span(group, refs)})", "",
                "Ερωτήσεις που παίχτηκαν στις διαλέξεις, με το ποσοστό των φοιτητών που "
                "απάντησαν σωστά.", ""]
        for q in group:
            r = refs[q["meta"]["id"]]
            out.append(f'- <a id="{r["anchor"]}"></a>**[{r["label"]}](../../{q["path"]})** '
                       f'{q["meta"]["title"]}: {accuracy(q)}% σωστές απαντήσεις')
        out.append("")
    out.append(KAHOOT[1])
    return "\n".join(out)


def misconception(q):
    """The first paragraph of a question's «Συχνή παρανόηση» section, or None."""
    m = re.search(r"^## Συχνή παρανόηση\n+(.+?)(?:\n\n|\n## |\Z)", q["body"], re.M | re.S)
    return " ".join(m.group(1).split()) if m else None


def misconceptions_block(n, qs, refs):
    """«Συχνά λάθη»: what the class actually got wrong, hardest first."""
    group = sorted((q for q in kahoots(qs, n) if misconception(q)),
                   key=lambda q: (accuracy(q), q["meta"]["id"]))
    out = [MISC[0], ""]
    if group:
        out += ["### Τι δυσκόλεψε την τάξη", "",
                "Από τα Kahoot των διαλέξεων: οι ερωτήσεις όπου μια λάθος απάντηση "
                "μάζεψε πολλές ψήφους, με το ποσοστό σωστών απαντήσεων.", ""]
        out += [f"- **[{refs[q['meta']['id']]['label']}](../../{q['path']})** {q['meta']['title']} "
                f"({accuracy(q)}% σωστές): {misconception(q)}" for q in group] + [""]
    out.append(MISC[1])
    return "\n".join(out)


SEC_ANCHOR = re.compile(r'^<a id="s\d+-\d+"></a>(?:<a id="[^"]*"></a>)?\n\n?', re.M)
SEC_LABEL = re.compile(r"^(### )§\d+\.\d+ ", re.M)
SELF_ITEM = re.compile(r'^(?:\d+\.|- <a id="e\d+-\d+"></a>\*\*\[Ε\d+\.\d+\]\(#e\d+-\d+\)\*\*) +(.*)$')


def slug(heading):
    """The id GitHub, kramdown and pandoc give a heading: lower case, punctuation
    dropped, spaces to hyphens."""
    return re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")


def number_chapter(text, n):
    """Label the H3 sections of «Θεωρία»/«Παραδείγματα» (§) and the «Ερωτήσεις
    κατανόησης» items (Ε). Idempotent: old labels and anchors are stripped first.

    The label changes the heading's own id, so each labelled heading also gets an
    anchor named after its unlabelled slug: links such as (#η-συνάρτηση-getchar) keep
    working. tools/pdf-prep.py maps them to the § anchor for the PDF."""
    a = text.index("\n## Θεωρία\n")
    b = text.index("\n## Κύρια σημεία\n")
    body = SEC_LABEL.sub(r"\1", SEC_ANCHOR.sub("", text[a:b]))
    out, k, fenced = [], 0, False
    for line in body.split("\n"):
        if re.match(r"\s*```", line):
            fenced = not fenced
        if not fenced and line.startswith("### "):
            k += 1
            out += [f'<a id="s{n}-{k}"></a><a id="{slug(line[4:])}"></a>', "", f"### §{n}.{k} {line[4:]}"]
        else:
            out.append(line)
    text = text[:a] + "\n".join(out) + text[b:]

    a = text.index("\n## Ερωτήσεις κατανόησης\n")
    b = text.index(KAHOOT[0], a)
    out, k = [], 0
    for line in text[a:b].split("\n"):
        m = SELF_ITEM.match(line)
        if m:
            k += 1
            line = f'- <a id="e{n}-{k}"></a>**[Ε{n}.{k}](#e{n}-{k})** {m.group(1)}'
        out.append(line)
    return text[:a] + "\n".join(out) + text[b:]


def chapter_groups(qs, n):
    """Everything numbered in a chapter, in label order: Kahoot first, then the ladder."""
    group = kahoots(qs, n)
    out = [("Kahoot από το αμφιθέατρο", group)] if group else []
    return out + ladder(qs, n)


def index(qs, lectures, refs):
    out = ["# Τράπεζα ασκήσεων", "",
           "Όλες οι ασκήσεις του οδηγού μελέτης, από τις διαφάνειες, τα εργαστήρια, τις",
           "εργασίες και τα θέματα εξετάσεων, ανά κεφάλαιο. Κάθε άσκηση έχει υπόδειξη,",
           "όχι λύση. Δυσκολία: ★☆☆ άμεση εφαρμογή, ★★☆ συνδυασμός ιδεών, ★★★ επιπέδου εξέτασης.",
           "",
           "Κάθε άσκηση έχει έναν αριθμό, π.χ. **Α12.16** (άσκηση 16 του Κεφαλαίου 12) ή **Κ12.2**",
           "(Kahoot), και ένα μόνιμο αναγνωριστικό, π.χ. `exam-2025-jan-q2`. Ο αριθμός",
           "ακολουθεί την τρέχουσα έκδοση του οδηγού· το αναγνωριστικό δεν αλλάζει ποτέ.",
           "",
           f"Σε μορφή για εργαλεία: [`questions.json`]({SITE}/downloads/questions.json).", "",
           NOTE_2023, ""]
    for l in lectures:
        groups = chapter_groups(qs, l["n"])
        if not groups:
            continue
        label = "Παράρτημα Α" if l.get("appendix") else f"Κεφάλαιο {l['n']}"
        out += [f"## [{label}: {l['title']}](../chapters/{l['slug']}/)", ""]
        for heading, group in groups:
            out += [f"### {heading} ({span(group, refs)})", ""]
            out += [entry(q, "../", refs, anchor=False) for q in group] + [""]
    return "\n".join(out).rstrip() + "\n"


def refs_yaml(refs, lectures):
    slugs = {l["n"]: l["slug"] for l in lectures}
    lines = ["# Generated by tools/gen-exercises.py: question id -> label, anchor, chapter."]
    for qid in sorted(refs):
        r = refs[qid]
        lines.append(f'{qid}: {{label: "{r["label"]}", anchor: {r["anchor"]}, chapter: {slugs[r["n"]]}}}')
    return "\n".join(lines) + "\n"


def chapters_yaml(lectures):
    return "".join(f"{l['n']}: {l['slug']}\n" for l in lectures)


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


def build(qs, lectures, refs, outdir):
    os.makedirs(outdir, exist_ok=True)
    md = ["# Τράπεζα ασκήσεων", "", NOTE_2023, ""]
    for l in lectures:
        groups = chapter_groups(qs, l["n"])
        if not groups:
            continue
        label = "Παράρτημα Α" if l.get("appendix") else f"Κεφάλαιο {l['n']}"
        md += [f"## {label}: {l['title']}", ""]
        for heading, group in groups:
            md += [f"### {heading} ({span(group, refs)})", ""]
            for q in group:
                m, r = q["meta"], refs[q["meta"]["id"]]
                url = f"{SITE}/{os.path.splitext(q['path'])[0]}.html"
                acc = f" · {m['stats']['accuracy']}% σωστές" if m.get("stats") else ""
                md += [f'<a id="{r["anchor"]}-full"></a>', "",
                       f"#### {r['label']} · {m['title']}", "",
                       f"[{r['label']}]({url}) · *{m['source']['title']}* · {STARS[m['difficulty']]} · "
                       f"{m['type']}{acc} · `{m['id']}`", ""]
                # demote the question's own headings below the #### title
                md += [re.sub(r"^(#+) ", lambda h: "#" * max(5, len(h.group(1)) + 3) + " ",
                              q["body"], flags=re.M), "", "---", ""]
    open(os.path.join(outdir, "questions.md"), "w", encoding="utf-8").write("\n".join(md))
    data = [dict(q["meta"], label=refs[q["meta"]["id"]]["label"], path=q["path"],
                 url=f"{SITE}/{os.path.splitext(q['path'])[0]}.html",
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
    refs = labels(qs, lectures)
    stale = []

    def write(path, new):
        old = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        if old != new:
            stale.append(os.path.relpath(path, ROOT))
            if not check:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                open(path, "w", encoding="utf-8").write(new)

    for l in lectures:
        path = os.path.join(ROOT, "chapters", l["slug"], "README.md")
        if not os.path.exists(path):
            continue
        new = open(path, encoding="utf-8").read()
        for markers, block in ((MISC, misconceptions_block(l["n"], qs, refs)),
                               (KAHOOT, kahoot_block(l["n"], qs, refs)),
                               ((BEGIN, END), chapter_block(l["n"], qs, refs))):
            filled = fill(new, block, *markers)
            if filled is None:
                stale.append(f"{os.path.relpath(path, ROOT)}: no {markers[0]} markers")
            else:
                new = filled
        write(path, number_chapter(new, l["n"]))
    write(os.path.join(ROOT, "questions", "README.md"), index(qs, lectures, refs))
    write(os.path.join(ROOT, "_data", "refs.yml"), refs_yaml(refs, lectures))
    write(os.path.join(ROOT, "_data", "chapters.yml"), chapters_yaml(lectures))
    hpath = os.path.join(ROOT, "README.md")
    home = open(hpath, encoding="utf-8").read()
    new = fill(home, home_table(manifest(), qs), "<!-- chapters -->", "<!-- /chapters -->")
    if new is not None and new != home:
        stale.append("README.md")
        if not check:
            open(hpath, "w", encoding="utf-8").write(new)
    if "--build" in argv:
        build(qs, lectures, refs, argv[argv.index("--build") + 1])
    if check and stale:
        print("out of date (run tools/gen-exercises.py):\n  " + "\n  ".join(stale))
        return 1
    print(f"gen-exercises: {len(qs)} questions, {len(stale)} files updated")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
