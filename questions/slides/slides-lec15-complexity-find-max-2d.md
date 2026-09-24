---
id: slides-lec15-complexity-find-max-2d
kind: slides
title: "Πολυπλοκότητα εύρεσης μέγιστου σε πίνακα N x N"
source:
  title: "Διάλεξη 15, διαφάνεια 23"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec15.pdf
  years: [2025]
chapters: [15, 12]
topics: [complexity, multidim-arrays, loops]
difficulty: 1
type: short-answer
---

Εύρεση Μέγιστου Στοιχείου σε Πίνακα N x N. Τι χρονική και τι χωρική πολυπλοκότητα
έχει η συνάρτηση;

```c
int find_max(int **matrix, size_t n) {
  int i, j, max = -1;
  for(i = 0; i < n; i++) {
    for(j = 0; j < n; j++) {
      if (matrix[i][j] > max) max = matrix[i][j];
    }
  }
  return max;
}
```

## Υπόδειξη

Πόσες φορές τρέχει ο εσωτερικός βρόχος για *κάθε* επανάληψη του εξωτερικού; Μετά
σκεφτείτε αν η αρχική τιμή `max = -1` είναι σωστή για κάθε πίνακα.
