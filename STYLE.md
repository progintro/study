# Style guide: chapters and the question bank

This is the contract for everything under `chapters/` and `questions/`, whoever writes
it: a person or an agent. `tools/lint.py --strict` enforces the mechanical parts.

## Who we write for

A first-year student who missed the lecture, or who is revising for the exam two
months later. They have the slides, but slides are terse and full of things that were
*said*, not written. A chapter should:

1. teach the lecture's material as **readable prose**, not slide bullets;
2. point precisely to where to read more (the slides, the course notes, the labs);
3. give the questions to practise on: from the slides, the labs, the homework and past
   exams.

It must also work as input to an agent ("make me 5 exercises on chapter 12",
"quiz me on pointers"), so text comes first: no information only in images,
no layout tricks. Everything is plain Markdown that reads well on GitHub, on the site
and in the PDF.

## Language

- **Greek** prose, in second-person plural for instructions ("Παρατηρήστε ότι …"),
  as `lab-material` and `notes` do. The tone is friendly and precise.
- Technical terms: give the Greek term with the English one in parentheses **the first
  time** it appears in a chapter, e.g. "δείκτης (pointer)". After that use whichever the
  course uses (the slides say "pointer" more than "δείκτης": follow the slides).
- Identifiers, commands, keywords, file names and C code stay in English, in backticks.
- Use Greek punctuation properly: the Greek question mark is `;`.

## Chapter file

`chapters/NN-slug/README.md`, where `NN-slug` is the lecture's `slug` in
`sources/manifest.yaml`.

### Front matter

```yaml
---
layout: chapter
chapter: 12
lecture: 12
title: "Δείκτες και Πίνακες"
date: 2025-11-10
part: C
slides: https://github.com/progintro/progintro.github.io/releases/download/2025/lec12.pdf
prev: 11-pointers-recursion
next: 13-memory
topics: [pointers, arrays, pointer-arithmetic]
notes: [05-pointers-arrays]
labs: [lab06]
---
```

- `prev` is omitted on the first chapter and `next` on the last one.
- `topics` are short English kebab-case tags. Reuse the vocabulary in
  `questions/topics.yaml`, and add a topic there if none fits.
- `notes` and `labs` list the related chapters of progintro/notes and the labs of
  progintro/lab-material.

### Body: sections in this order

```markdown
# Κεφάλαιο 12: Δείκτες και Πίνακες

<!-- {% raw %} -->

> **Στόχοι:** μετά από αυτό το κεφάλαιο θα μπορείτε να …
>
> **Προαπαιτούμενα:** [Κεφάλαιο 10](../10-arrays/), [Κεφάλαιο 11](../11-pointers-recursion/)
>
> **Χρόνος μελέτης:** ~2 ώρες

## Σύνοψη
One paragraph (4–6 sentences): what the lecture is about and why it matters.

## Θεωρία
### <one H3 per concept of the lecture, in the lecture's order>
The concepts: definitions in **bold** where they are defined, the rules of the
language, how things work and why. Small illustrative snippets only; diagrams
as mermaid (see below).

## Παραδείγματα
### <one H3 per worked example>
The lecture's worked examples, live-coding sessions, programs with their output,
and tips for the homework or labs that the lecture gave. Each one says which
concepts of «Θεωρία» it applies.

## Κύρια σημεία
1. Numbered list of the key takeaways. Every takeaway the slides state explicitly
   ("Key takeaways", "Τι κρατάμε", summary slides) must be here, plus the ones the
   lecture implies. Each one is a full sentence.

## Ορολογία
| Ελληνικά | English | Σύντομος ορισμός |
| --- | --- | --- |

## Συχνά λάθη
- Mistakes and misconceptions, each with a one-line example or symptom (compiler
  message, crash, wrong output) and the fix.

## Διάβασμα
- **Διαφάνειες:** [Διάλεξη 12](<slides url>), σελ. 1–30. <per-topic page ranges if useful>
- **Σημειώσεις:** [Κεφάλαιο 5: Δείκτες και πίνακες](https://progintro.github.io/notes/chapters/05-pointers-arrays/), ενότητες «Δείκτες», «Πίνακες» (K04, σελ. 78–92)
- **Εργαστήριο:** [Εργαστήριο 6](https://progintro.github.io/lab-material/labs/lab06/): ασκήσεις `pointers.c`, `sieve.c`
- **Βιβλίο:** K&R, κεφ. 5 (only where the slides cite a book)
- **Άλλα:** external links the slides give (Wikipedia, man pages, videos)

## Ασκήσεις
<!-- exercises -->
<!-- /exercises -->

## Ερωτήσεις αυτοαξιολόγησης
1. Short conceptual question.[^q1]
...

[^q1]: Short answer.

<!-- {% endraw %} -->
```

- **One H1**, `# Κεφάλαιο N: <title>`. The appendix chapter is `# Παράρτημα Α: <title>`.
- The body sits between `<!-- {% raw %} -->` and `<!-- {% endraw %} -->`. C code such as
  `{{1, 2}}` is Liquid syntax and would otherwise break the site build.
- **Never edit between the `<!-- exercises -->` markers by hand.**
  `tools/gen-exercises.py` fills them from `questions/`.
- Self-assessment answers go in footnotes named `[^q1]`, `[^q2]`, … .
- K04 page numbers come from `sources/k04-map.tsv` (printed K04 page → notes chapter and section).
  Give notes sections by their exact heading text in «».

### Writing the theory and examples

- **Concepts first, examples after.** «Θεωρία» teaches the concepts; complete
  programs, walkthroughs, live coding and homework/lab tips go in «Παραδείγματα».
  A concept may show a 2–6 line snippet inline; anything longer is an example.
- **Concise.** Say each thing once, in plain sentences; no filler ("Όπως είναι
  γνωστό…", "Ας δούμε τώρα…"), no repeating the slide text and then paraphrasing
  it. A typical chapter is 350–550 lines.
- **Transform, don't transcribe.** Slides are bullets plus the lecturer's voice; the
  chapter supplies the missing sentences that connect them. Explain *why*, not only
  *what*. Keep every fact, example and program from the slides. Drop nothing that
  would be on an exam.
- Do not invent course policy, deadlines or grading. When the slides show something
  that you cannot read reliably, write what you can and record the gap in
  `sources/extract/lecNN.yaml` under `issues`.
- Where the slides show live-coding output (terminal screenshots), transcribe it as a
  ```text block with the `$` prompt.
- Where the slides use an image to make a point (a meme), keep the point in words.
  Do not describe the meme itself unless it teaches something.
- Cross-reference earlier chapters by link: `[Κεφάλαιο 6](../06-control-flow/)`.

### Code

- Fence every block with a language: `c`, `text`, `sh`, `make`, `diff`, `yaml`, `mermaid`.
- A ```c block that defines `main` must compile: `tools/check-code.py` runs
  `gcc -fsyntax-only` on it (with `-std=gnu11`). If a program is deliberately
  incomplete or wrong (for example "find the bug"), put a line containing only `....`
  or the comment `// does-not-compile` in it so the check skips it.
- Write code the way the slides do (modern C, `int main(int argc, char **argv)` where
  the slides use it). Keep lines ≤ 80 characters so the PDF does not wrap.

### Diagrams: mermaid

Draw flowcharts, control flow, call trees, recursion trees, linked lists, trees,
graphs, pointer diagrams, state machines and processes (compile → link → run) as
```mermaid blocks. The site renders them, the PDF build renders them to images,
and agents read the source. Memory layouts (addresses and contents) stay tables.

- Use `flowchart TD` / `flowchart LR` for almost everything. `sequenceDiagram`
  and `stateDiagram-v2` are fine when they fit. Avoid experimental diagram types.
- Quote every label that has punctuation, operators or Greek: `A["i < 42"]`,
  `B{"x > 0;"}`. Use `#quot;` for a double quote inside a label, and `#lt;` / `#gt;`
  if a label has `<` or `>` next to letters.
- Keep a diagram to roughly 15 nodes, and give it a one-line caption in italics
  underneath (`*Σχήμα: …*`).

### Math, HTML and figures

- Math: `$x$` inline, `$$x$$` display on its own line. No spaces just inside the
  delimiters. Write `\lbrace`/`\rbrace` rather than `\{`/`\}`.
- No raw HTML except `<a id="..."></a>` anchors (the PDF drops HTML).
- Image figures are a last resort, when neither mermaid nor a table can carry the
  point. Put them in `figures/` as SVG plus PDF (the build needs both) and reference the `.svg`.

## The question bank: `questions/`

One question per file, `questions/<kind>/<id>.md`, where kind is `slides`, `labs`,
`homework`, `exams` or `kahoot`.

```markdown
---
id: exam-2025-jan-q2
kind: exam
title: "Αντιστροφή λέξεων"
source:
  title: "Εξέταση Ιανουαρίου 2025, Θέμα 2"
  url: https://github.com/progintro/progintro.github.io/blob/main/exams/2025/progintro-exam-jan-25.pdf
  years: [2025]
chapters: [14, 12]
topics: [strings, pointers]
difficulty: 2
type: programming
---

<statement, faithful to the original, in Markdown; sample runs as ```text blocks>

## Υπόδειξη

<1-4 sentences that start the student on the right track, without giving the solution>
```

- `id` equals the file name without `.md`. Conventions:
  - `slides-lecNN-<slug>`
  - `lab-labNN-<file>`
  - `hw-<year>-hwN-<slug>`
  - `exam-<exam-id>-qN`, with a letter suffix for sub-parts if they are separate problems.
  - `kahoot-<short-slug>`
- `chapters`: the chapter numbers where the question belongs. **The first one is the
  primary chapter**, where most of the needed material is taught. List others only if
  the question genuinely needs them.
- `difficulty`: 1 (direct application), 2 (combines ideas), 3 (exam-hard or longer).
- `type` is one of:
  - `programming`: write a program or function
  - `short-answer`: explain or define
  - `trace`: what does this print?
  - `debug`: find the bug
  - `multiple-choice`
  - `tooling`: shell, git, gcc, make
- **Hints only, never full solutions.** A hint may name the technique ("use two
  indices that move towards each other"), but must not contain the code.
- Transcribe statements faithfully (Greek as written). Include the input/output
  examples, which are often the precise spec. Long input files are linked, not
  pasted.
- If the same problem appeared in more than one year, keep one file and list every
  year in `source.years`, adding the other sources in the body under
  `## Εμφανίσεις`.

### Kahoot questions

`questions/kahoot/` holds the quiz questions played in lectures, with how the class
did on them. They carry two extra front-matter fields:

```yaml
kind: kahoot
type: multiple-choice
answer: "(*robin).hood"          # the correct option(s), for tools and agents
stats: {responses: 212, accuracy: 43}   # all plays, % answered correctly
```

- The statement gives the question and **all the options** as a list. It does
  **not** say which option is correct. The page shows only the question, the options
  and the hint; `answer` is machine-readable, for agents that quiz students.
- Add `## Συχνή παρανόηση` before the hint when one wrong option drew a large share of
  the answers. Say which misconception it reveals, e.g. "Το 38% επέλεξε `*robin.hood`,
  ξεχνώντας ότι η `.` έχει μεγαλύτερη προτεραιότητα από το `*`." This is allowed
  even though it names a wrong option, because it is the point of the data.
- Leave out questions that depend on a figure or code the export does not include.
- Keep no player names or per-player data. The stats are aggregates only.
