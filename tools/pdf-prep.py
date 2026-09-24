#!/usr/bin/env python3
"""Turn chapter Markdown into the Markdown the pandoc/xelatex pass reads.

The PDF is a different renderer from GitHub and the Pages site, and needs:

  * no Jekyll front matter - pandoc's gfm reader would print it as text;
  * figures as PDF rather than SVG (xelatex cannot include SVG), with paths relative
    to the repository root, which is where pandoc runs;
  * footnote labels unique across chapters, because the book concatenates them all
    and every chapter numbers its notes from 1;
  * mermaid diagrams as the PDFs tools/mermaid.py rendered (the plain Markdown for
    agents keeps the mermaid source, which is the more useful form for them);
  * links that work outside the site: links to other chapters and to questions are
    relative on GitHub and the site, and become absolute site URLs here.

The book (--all) also gets its structure from sources/manifest.yaml: a \\part before
the first chapter of each part, \\appendix before the appendix chapters, and the whole
question bank (build/questions.md, from tools/gen-exercises.py --build) at the end.

Usage:
  tools/pdf-prep.py chapters/NN-slug/README.md > build/NN-slug.md    one chapter
  tools/pdf-prep.py --all > build/study.md                            the whole book
  tools/pdf-prep.py --all --plain > build/study-plain.md              the book as plain
                                                                      Markdown (llms-full)
"""

import io
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mermaid  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://progintro.github.io/study"


def links(text):
    # remote images (exam screenshots, asciinema casts) become links: xelatex cannot
    # include them, and a PDF reader can follow the link
    text = re.sub(r"!\[([^\]]*)\]\((https?://[^)\s]+)\)",
                  lambda m: "[Εικόνα: %s](%s)" % (m.group(1) or "σύνδεσμος", m.group(2)), text)
    text = re.sub(r"\]\((?:\.\./)+questions/(\w+)/([\w.-]+)\.md\)", "](" + SITE + r"/questions/\1/\2.html)", text)
    text = re.sub(r"\]\((?:\.\./)+questions/(?:README\.md)?\)", "](" + SITE + "/questions/)", text)
    text = re.sub(r"\]\(\.\./([\w-]+)/?\)", "](" + SITE + r"/chapters/\1/)", text)
    return text


def diagrams(text):
    out, last = [], 0
    for m, _, h in mermaid.blocks(text):
        pdf = os.path.join("build", "mermaid", h + ".pdf")
        if not os.path.exists(os.path.join(ROOT, pdf)):
            sys.exit(f"missing {pdf}: run tools/mermaid.py")
        # capped so a tall flowchart does not take a whole page; never scaled up
        out += [text[last:m.start()],
                "```{=latex}\n\\begin{center}\\includegraphics[max width=0.9\\linewidth,"
                f"max height=0.6\\textheight]{{{pdf}}}\\end{{center}}\n```"]
        last = m.end()
    return "".join(out) + text[last:]


def prepare(path, plain=False):
    text = io.open(path, encoding="utf-8").read()
    if text.startswith("---\n"):
        text = text[text.index("\n---\n", 3) + 5:]
    if not plain:
        text = diagrams(text)
    text = re.sub(r"\]\((?:\.\./)+figures/(\w+)\.svg\)", r"](figures/\1.pdf)", text)
    slug = os.path.basename(os.path.dirname(path))[:2]
    text = re.sub(r"\[\^(\w+)\]", lambda m: "[^c%s-%s]" % (slug, m.group(1)), text)
    missing = [f for f in re.findall(r"\]\((figures/[^)]+)\)", text)
               if not os.path.exists(os.path.join(ROOT, f))]
    if missing:
        sys.exit(f"{path}: missing figures {missing}")
    return links(text).strip() + "\n"


def latex(s):
    return "```{=latex}\n" + s + "\n```\n"


def book(plain):
    m = yaml.safe_load(open(os.path.join(ROOT, "sources", "manifest.yaml"), encoding="utf-8"))
    out, part, appendix = [], None, False
    for l in m["lectures"]:
        path = os.path.join(ROOT, "chapters", l["slug"], "README.md")
        if not os.path.exists(path):
            continue
        if not plain and l.get("appendix") and not appendix:
            out.append(latex("\\appendix"))
            appendix = True
        if not plain and l["part"] != part:
            part = l["part"]
            title = m["parts"][part]
            label = "Παραρτήματα" if part == "X" else f"Μέρος {'ΑΒΓΔΕ'['ABCDE'.index(part)]}: {title}"
            out.append(latex("\\part*{%s}\n\\addcontentsline{toc}{part}{%s}" % (label, label)))
        text = prepare(path, plain)
        if plain:
            meta = f"> Διάλεξη {l['n']} · {l['date']} · [διαφάνειες]({m['release']}/{l['slides']})"
            text = re.sub(r"^(# .+\n)", lambda h: h.group(1) + "\n" + meta + "\n", text, count=1, flags=re.M)
        out.append(text)
    gpath = os.path.join(ROOT, "glossary.md")
    if os.path.exists(gpath):
        if not plain and not appendix:
            out.append(latex("\\appendix"))
            appendix = True
        g = open(gpath, encoding="utf-8").read()
        g = re.sub(r"\]\(chapters/([\w-]+)/\)", "](" + SITE + r"/chapters/\1/)", g)
        out.append(g)
    qpath = os.path.join(ROOT, "build", "questions.md")
    if os.path.exists(qpath):
        if not plain and not appendix:
            out.append(latex("\\appendix"))
            appendix = True
        # the bank's H1 is a chapter of its own; its per-chapter H2s stay sections
        qtext = links(open(qpath, encoding="utf-8").read())
        out.append(qtext if plain else diagrams(qtext))
    return "\n\n".join(out)


def main(argv):
    if argv and argv[0] == "--all":
        sys.stdout.write(book("--plain" in argv))
    elif len(argv) == 1:
        sys.stdout.write(prepare(argv[0]))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
