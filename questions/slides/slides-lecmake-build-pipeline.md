---
id: slides-lecmake-build-pipeline
kind: slides
title: "Τα στάδια του C build process"
source:
  title: "How to Make? (προσκεκλημένη διάλεξη), διαφάνεια 5"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/make.pdf
  years: [2025]
chapters: [26, 0]
topics: [compilation]
difficulty: 1
type: short-answer
---

«Say 'Aye' if you know what this is!» Η διαφάνεια δείχνει το παρακάτω διάγραμμα:

```text
Translation Unit (.c) -> Preprocessor (cpp) -> Preprocessed Translation Unit (.c)
  -> Compiler (gcc) -> Object File (.o) -> Linker (ld) -> Executable
                        Object File (.o) -----^
                   Dynamic Library (.so) -----^
```

Εξηγήστε τι κάνει το καθένα από τα τρία στάδια (preprocessor, compiler, linker) και τι
παράγει. Γιατί ο linker δέχεται και άλλα object files και δυναμικές βιβλιοθήκες;

## Υπόδειξη

Σκεφτείτε τι απογίνονται οι οδηγίες `#include` και `#define`, σε ποιο στάδιο ο κώδικας
γίνεται γλώσσα μηχανής, και πού βρίσκεται η υλοποίηση της `printf` που καλεί το
πρόγραμμά σας.
