# Prompt: turn one lecture's slides into a study chapter

(Used by the maintainers to run one extraction agent per lecture. Placeholders in
{{BRACES}} are filled from `sources/manifest.yaml`.)

---

You are writing one chapter of the study guide in `/Users/ethan/github/progintro/study`
for the C course "Εισαγωγή στον Προγραμματισμό" (ΕΚΠΑ / DIT).

**Your lecture:** Διάλεξη {{N}}: «{{TITLE}}» ({{DATE}}), chapter slug `{{SLUG}}`, part {{PART}}.
- Slides: `/Users/ethan/github/progintro/study/sources/slides/{{PDF}}`
  (published at {{RELEASE}}/{{PDF}}).
- Starting guess for related material: notes chapters {{NOTES}}; labs {{LABS}}.
- Previous chapter slug: {{PREV}}. Next chapter slug: {{NEXT}}.

## Read first
1. `/Users/ethan/github/progintro/study/STYLE.md`: the contract for your output. Follow it exactly.
2. `/Users/ethan/github/progintro/study/sources/manifest.yaml`: all lectures, so you
   know what comes before and after yours and can cross-link.
3. `/Users/ethan/github/progintro/study/questions/topics.yaml`: the topic vocabulary.

## Steps
1. **Read every page of the slides**, using the Read tool on the PDF with the
   `pages` parameter, at most 20 pages per call, until you reach the last page. Text
   extraction tools garble this PDF's Greek fonts, so read the pages visually.
   Note for each page what it teaches, every definition, every code example and its
   output, every question posed to the audience, exercises, key-takeaway slides, and
   every pointer the slides give (K04 / notes pages, K&R, Wikipedia, man pages, labs,
   homework).
2. **Read the related course material** so that your reading list is precise:
   - The notes chapters: `/Users/ethan/github/progintro/notes/chapters/<slug>/README.md`.
     Pick the exact sections («heading text») that match your lecture. Look for other
     notes chapters too if the lecture covers them.
   - `/Users/ethan/github/progintro/study/sources/k04-map.tsv` gives the K04.pdf
     page numbers for those sections.
   - The labs: `/Users/ethan/github/progintro/lab-material/labs/labNN/README.md`. Pick
     the lab and the exercises (file names) that practise this lecture.
   - Optional context on where students struggle:
     `/Users/ethan/github/progintro/faq/faq.md`, `faq2.md` (a Piazza FAQ) and
     `/Users/ethan/github/progintro/lab-material/field.md` (TA field notes). Use them
     for «Συχνά λάθη» where relevant.
3. **Write `chapters/{{SLUG}}/README.md`**, following STYLE.md: front matter, Στόχοι,
   Σύνοψη, Θεωρία, Κύρια σημεία, Ορολογία, Συχνά λάθη, Διάβασμα, the empty exercises
   markers, and Ερωτήσεις αυτοαξιολόγησης. The theory must be real explanatory Greek
   prose that a student can learn from without the slides, covering *everything* in the
   lecture. Chapters are typically 250–600 lines.
4. **Write one question file per question or exercise found in the slides** in
   `questions/slides/slides-lec{{NN}}-<short-slug>.md`, following STYLE.md (hints only).
   This covers questions posed to the audience, "try it yourself" exercises and quizzes.
   Their primary chapter is {{N}}. If the slides contain none, write none. Do **not**
   write lab, homework or exam questions: other agents do that.
5. **Write `sources/extract/lec{{NN}}.yaml`:**
   ```yaml
   lecture: {{N}}
   pages: 42                       # page count of the PDF
   outline:                        # slide pages -> the H3 of Θεωρία that covers them
     - {pages: "1-3", section: "Τι είναι ένα πρόγραμμα"}
   pointers:                       # every external reference the slides make
     - {page: 12, text: "K04 σελ. 40-45"}
   takeaways_slide: 41             # page with explicit key takeaways, if any
   issues:                         # anything unreadable, ambiguous or suspect
     - "p. 17: code screenshot partly cut off; reconstructed the loop body"
   ```
6. **Self-check before you finish:**
   - `python3 tools/lint.py --strict chapters/{{SLUG}}/README.md` passes.
   - `python3 tools/check-code.py chapters/{{SLUG}}/README.md` passes.
   - `python3 tools/gen-exercises.py --lint` passes on your question files.

   Fix anything they report.

## Rules
- Write only these files: `chapters/{{SLUG}}/`, `questions/slides/slides-lec{{NN}}-*`
  and `sources/extract/lec{{NN}}.yaml`. If you need a new topic tag, do not edit
  `topics.yaml`; list the tag under `new_topics:` in your extract yaml.
- Do not edit any other repository. Do not run git.
- Do not invent facts that are not supported by the slides or the course material.
  When unsure, say so in `issues`.

Finish with a short report (≤ 15 lines): the page count, the chapter length, the number
of questions written, and the most important issues.
