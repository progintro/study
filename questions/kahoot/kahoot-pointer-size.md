---
id: kahoot-pointer-size
kind: kahoot
title: "Μέγεθος δεικτών"
source:
  title: "Kahoot «Δείκτες και Αναδρομή» (διάλεξη 11)"
  years: [2025]
chapters: [11]
topics: [pointers, types, memory-model]
difficulty: 2
type: multiple-choice
answer: "True"
stats: {responses: 152, accuracy: 46}
---

Οι μεταβλητές `double *x;` και `char *c;` καταλαμβάνουν τον ίδιο χώρο στη μνήμη.

- True
- False

## Συχνή παρανόηση

Το 49% απάντησε False, μπερδεύοντας το μέγεθος του δείκτη με το μέγεθος του τύπου στον οποίο δείχνει. Κάθε δείκτης κρατά μια διεύθυνση, άρα όλοι έχουν το ίδιο μέγεθος (8 bytes σε 64-bit συστήματα).

## Υπόδειξη

Τι αποθηκεύει μια μεταβλητή δείκτη, και εξαρτάται το μέγεθος αυτού που αποθηκεύει από τον τύπο στον οποίο δείχνει;
