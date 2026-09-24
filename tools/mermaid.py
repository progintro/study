#!/usr/bin/env python3
"""Render every ```mermaid block in the chapters and questions to build/mermaid/<hash>.pdf.

The site draws mermaid diagrams in the browser (see _includes/head-custom.html) and
the Markdown keeps them as text, which is what agents read. Only the PDF needs them
as pictures: tools/pdf-prep.py swaps each block for the PDF this script rendered,
found by the hash of the block's source.

Rendering uses minlag/mermaid-cli, as lab-material does, in a single container run
over all diagrams that are not already in build/mermaid/ (Chromium's start-up is most
of the cost of each run).

Usage: tools/mermaid.py [--docker CMD]
"""

import glob
import hashlib
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "build", "mermaid")
FENCE = re.compile(r"^([ \t]*)```mermaid\n(.*?)^\1```[ \t]*$", re.M | re.S)
IMAGE = os.environ.get("MERMAID_IMAGE", "minlag/mermaid-cli")


def blocks(text):
    """(match, source, hash) for every mermaid block, source de-indented."""
    for m in FENCE.finditer(text):
        indent = m.group(1)
        src = "\n".join(l[len(indent):] if l.startswith(indent) else l
                        for l in m.group(2).rstrip("\n").split("\n")) + "\n"
        yield m, src, hashlib.sha1(src.encode("utf-8")).hexdigest()[:16]


def main(argv):
    os.makedirs(OUT, exist_ok=True)
    todo = {}
    paths = glob.glob(os.path.join(ROOT, "chapters", "*", "README.md")) + \
        glob.glob(os.path.join(ROOT, "questions", "*", "*.md"))
    for path in sorted(paths):
        for _, src, h in blocks(open(path, encoding="utf-8").read()):
            if not os.path.exists(os.path.join(OUT, h + ".pdf")):
                todo[h] = src
    if not todo:
        print("mermaid: all diagrams up to date")
        return 0
    for h, src in todo.items():
        open(os.path.join(OUT, h + ".mmd"), "w", encoding="utf-8").write(src)
    # one container, one Chromium, a shell loop over the diagrams
    script = " && ".join(f"/home/mermaidcli/node_modules/.bin/mmdc -p /puppeteer-config.json -i {h}.mmd -o {h}.pdf --pdfFit -q"
                         for h in todo)
    cmd = ["docker", "run", "--rm", "--tmpfs", "/tmp:size=1g,mode=1777,exec",
           "-u", f"{os.getuid()}:{os.getgid()}", "-e", "HOME=/tmp",
           "-v", f"{OUT}:/data", "-w", "/data", "--entrypoint", "sh", IMAGE, "-c", script]
    r = subprocess.run(cmd)
    missing = [h for h in todo if not os.path.exists(os.path.join(OUT, h + ".pdf"))]
    if r.returncode or missing:
        print(f"mermaid: failed to render {missing}", file=sys.stderr)
        return 1
    print(f"mermaid: rendered {len(todo)} diagrams")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
