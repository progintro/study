# CLAUDE.md

Guidance for Claude Code (and other agents) working in this repository.

## What this repository is

The study guide for "Introduction to Programming" (C, K04) at the University of
Athens, in Greek, published at https://progintro.github.io/study/. It is **content,
not software**. It has one chapter per 2025-26 lecture, plus a question bank:

- `chapters/NN-slug/README.md`: one chapter per lecture. The order, titles, dates and
  parts come from `sources/manifest.yaml`.
- `questions/<kind>/<id>.md`: one exercise per file (slides, labs, homework, exams),
  with a hint but no solution.
- `STYLE.md`: **the contract for both**. Read it before writing any content.

Sources, all in sibling checkouts, are read-only from here. Do not edit or open PRs
against them.

- `../progintro.github.io`: the course site. It has the exams in `exams/`, the
  schedule in `past/2025/README.md` and the sample submissions in `samples/`.
  Slides and homework PDFs are release assets: `make fetch` downloads them to
  `sources/slides/` and `sources/hw/` (gitignored).
- `../notes`: the K04 notes as Markdown. `sources/k04-map.tsv` (from
  `tools/k04map.py`) maps K04.pdf pages to notes chapters and sections.
- `../lab-material`: the labs. `../faq`: the curated Piazza FAQ.

The slide PDFs' Greek fonts do not survive text extraction. Read them visually (the
Read tool with `pages`, at most 20 per call).

## Commands

```sh
make fetch          # download slides + homework PDFs (needs gh)
make lint           # chapters (tools/lint.py --strict) + questions (gen-exercises --lint)
make check-code     # every complete C program in the chapters compiles
make exercises      # regenerate the chapters' generated blocks, questions/README.md, home table, glossary
make check          # all of the above in check mode, as CI runs it
make                # PDFs, study.pdf, study-md.zip, questions.json, llms*.txt (Docker)
```

Do not use `make -j`: parallel pandoc containers have produced truncated PDFs.

## Rules

- The content between the `<!-- exercises -->`, `<!-- kahoot -->` and
  `<!-- misconceptions -->` markers, in `questions/README.md`, `glossary.md`, and
  between `<!-- chapters -->` markers in `README.md` is **generated**. Edit
  `questions/` and run `make exercises`.
- Keep the chapter front matter and the `<!-- {% raw %} -->` wrapper (see STYLE.md).
- Math: `$x$` inline, `$$x$$` display. `tools/site-prep.py` converts it for kramdown
  in CI only. Never run it in a working tree.
- Hints, never full solutions, in `questions/`.
- `tools/prompts/extract-lecture.md` is the prompt the chapters were extracted with,
  one agent per lecture.
- Commit and push straight to `main`: this repo has no PR workflow.
