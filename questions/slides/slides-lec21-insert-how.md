---
id: slides-lec21-insert-how
kind: slides
title: "Προσθήκη στοιχείου σε λίστα"
source:
  title: "Διάλεξη 21, διαφάνειες 11–12"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec21.pdf
  years: [2025]
chapters: [21]
topics: [linked-lists, pointers, dynamic-memory]
difficulty: 1
type: short-answer
---

Δίνεται η απλά συνδεδεμένη λίστα:

```text
list -> 6 -> 7 -> 8 -> NULL
```

Θέλω να προσθέσω ένα στοιχείο (π.χ., το 5) σε λίστα. Πως;

## Υπόδειξη

Σκεφτείτε πού είναι φθηνότερο να μπει ο νέος κόμβος, ώστε να μη χρειαστεί να διασχίσετε τη λίστα. Ποιοι δείκτες πρέπει να αλλάξουν, και με ποια σειρά, ώστε να μη χαθεί κανένας κόμβος; Από πού θα πάρετε μνήμη για τον νέο κόμβο;
