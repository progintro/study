---
id: kahoot-string-array-element
kind: kahoot
title: "Χαρακτήρας από πίνακα συμβολοσειρών"
source:
  title: "Kahoot «Δείκτες Παντού!» (διάλεξη 12) και «Πίνακες και Δείκτες» (διάλεξη 12)"
  years: [2025]
chapters: [12, 14]
topics: [pointers, strings, multidim-arrays]
difficulty: 3
type: multiple-choice
answer: "'n'"
stats: {responses: 221, accuracy: 38}
---

Έστω ότι

```c
char *strings[] = { "Hello", "fine", "world", NULL };
```

Το στοιχείο `strings[1][2]` είναι:

- `'e'`
- `NULL`
- `"fine"`
- `'n'`

## Συχνή παρανόηση

Το 23% επέλεξε `"fine"` και άλλο 22% `'e'`: οι πρώτοι σταμάτησαν στο `strings[1]` αγνοώντας τον δεύτερο δείκτη, οι δεύτεροι μέτρησαν τις θέσεις από το 1.

## Υπόδειξη

Ο πρώτος δείκτης διαλέγει συμβολοσειρά και ο δεύτερος χαρακτήρα μέσα σε αυτή· και οι δύο μετράνε από το 0.
