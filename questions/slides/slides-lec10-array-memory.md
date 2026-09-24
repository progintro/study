---
id: slides-lec10-array-memory
kind: slides
title: "Ποιος πίνακας πιάνει περισσότερη μνήμη;"
source:
  title: "Διάλεξη 10, διαφάνεια 40"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec10.pdf
  years: [2025]
chapters: [10]
topics: [arrays, types, memory-model]
difficulty: 1
type: short-answer
---

Πίνακες μπορούν να οριστούν για όλους τους τύπους της C. Παράδειγμα:

```c
int a[1024];
char b[2048];
double c[512];
```

Ποιος από τους παραπάνω πίνακες καταλαμβάνει περισσότερη μνήμη;

## Υπόδειξη

Ένας πίνακας πιάνει «πλήθος στοιχείων × μέγεθος τύπου» bytes. Θυμηθείτε τα
συνηθισμένα `sizeof` των `int`, `char` και `double`.
