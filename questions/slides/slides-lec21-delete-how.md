---
id: slides-lec21-delete-how
kind: slides
title: "Αφαίρεση στοιχείου από λίστα"
source:
  title: "Διάλεξη 21, διαφάνειες 23–25"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec21.pdf
  years: [2025]
chapters: [21]
topics: [linked-lists, pointers, dynamic-memory]
difficulty: 2
type: short-answer
---

Δίνεται η απλά συνδεδεμένη λίστα:

```text
list -> 5 -> 6 -> 7 -> 8 -> NULL
```

Θέλω να αφαιρέσω ένα στοιχείο (π.χ., το 6). Πως;

## Υπόδειξη

Ποιος δείκτης δείχνει σήμερα στον κόμβο 6, και πού πρέπει να δείχνει μετά την αφαίρεση; Τι γίνεται με τη μνήμη του κόμβου; Σκεφτείτε ξεχωριστά την περίπτωση που το στοιχείο είναι η κεφαλή: γιατί η συνάρτηση χρειάζεται `List *` και όχι `List`;
