---
id: slides-lec08-digit-names
kind: slides
title: "Το αγγλικό όνομα κάθε ψηφίου"
source:
  title: "Διάλεξη 8: Ροή Ελέγχου #2, διαφάνεια 13"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec08.pdf
  years: [2025]
chapters: [8]
topics: [conditionals, control-flow]
difficulty: 1
type: programming
---

Θέλω να τυπώσω το αγγλικό όνομα κάθε ψηφίου (`zero`, `one`, …, `nine`), και
`unknown` για οποιαδήποτε άλλη τιμή. Πώς;

## Υπόδειξη

Μια αλυσίδα `else if` δουλεύει, αλλά όλες οι συνθήκες συγκρίνουν την ίδια ακέραια
μεταβλητή με σταθερές: αυτή είναι η περίπτωση της `switch`. Μην ξεχάσετε τι
χρειάζεται στο τέλος κάθε `case` και πού πάνε οι τιμές που δεν είναι ψηφία.
