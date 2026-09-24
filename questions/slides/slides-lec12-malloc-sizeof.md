---
id: slides-lec12-malloc-sizeof
kind: slides
title: "Πόση μνήμη δεσμεύει η malloc και τι λέει το sizeof"
source:
  title: "Διάλεξη 12, διαφάνειες 39–40"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec12.pdf
  years: [2025]
chapters: [12, 13]
topics: [dynamic-memory, pointers, types]
difficulty: 2
type: short-answer
---

```c
int * nums = malloc(100 * sizeof(int));
double * coeffs = malloc(100 * sizeof(double));
char * str = malloc(100 * sizeof(char));
```

1. Πόση μνήμη δεσμεύεται με καθεμιά από τις παραπάνω κλήσεις;
2. Τι θα τυπώσει το ακόλουθο;

```c
printf("%d %d %d\n", sizeof(nums), sizeof(coeffs), sizeof(str));
```

## Υπόδειξη

Για το (1), η `malloc` μετρά bytes: υπολογίστε `100 * sizeof(τύπος)` με τα
συνηθισμένα μεγέθη των τύπων. Για το (2), αναρωτηθείτε ποιος είναι ο τύπος των
`nums`, `coeffs` και `str`: πίνακες ή δείκτες; Και τι μέγεθος έχει μια διεύθυνση
σε ένα σύστημα 64 bit;
