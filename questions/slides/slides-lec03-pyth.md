---
id: slides-lec03-pyth
kind: slides
title: "Πυθαγόρειο θεώρημα (pyth.c)"
source:
  title: "Διάλεξη 3: Συναρτήσεις, διαφάνεια 40"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec03.pdf
  years: [2025]
chapters: [3]
topics: [functions, floating-point, compilation]
difficulty: 1
type: programming
---

Challenge #1: Χρειαζόμαστε ένα πρόγραμμα `pyth.c` το οποίο **με δεδομένα τα μήκη των
καθέτων πλευρών ενός ορθογωνίου τριγώνου** να τυπώνει τα ακόλουθα:

1. Το εμβαδόν του τριγώνου.
2. Την περίμετρο του τριγώνου.

## Υπόδειξη

Γράψτε μία συνάρτηση για κάθε υπολογισμό, με δύο ορίσματα `double`. Για την περίμετρο
χρειάζεστε πρώτα την υποτείνουσα από το Πυθαγόρειο θεώρημα, με την `sqrt` του
`math.h`· θυμηθείτε τι χρειάζεται στη γραμμή του `gcc` για να συνδεθεί η μαθηματική
βιβλιοθήκη.
