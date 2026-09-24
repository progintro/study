---
id: slides-lec15-complexity-factorial
kind: slides
title: "Πολυπλοκότητα του αναδρομικού παραγοντικού"
source:
  title: "Διάλεξη 15, διαφάνεια 25"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec15.pdf
  years: [2025]
chapters: [15, 11]
topics: [complexity, recursion]
difficulty: 2
type: short-answer
---

Η συνάρτηση παραγοντικό (factorial). Τι χρονική και τι χωρική πολυπλοκότητα έχει;

```c
int factorial(int n) {
  if (n == 0) return 1;
  return n * factorial(n - 1);
}
```

## Υπόδειξη

Για τον χρόνο, μετρήστε τις κλήσεις. Για τον χώρο, μην κοιτάξετε μόνο τις μεταβλητές
μιας κλήσης: πόσες κλήσεις είναι ενεργές ταυτόχρονα στη στοίβα;
