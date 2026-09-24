---
id: slides-lec03-function-call
kind: slides
title: "Τιμή μετά από κλήση συνάρτησης"
source:
  title: "Διάλεξη 3: Συναρτήσεις, διαφάνεια 37"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec03.pdf
  years: [2025]
chapters: [3]
topics: [functions]
difficulty: 1
type: trace
---

Ποια η τιμή του `x` μετά την εκτέλεση της ανάθεσης στη `main`;

```c
int g(int x, int y, int z) {
  return x * x + y * y + z * z + 42;
}

int main(int argc, char **argv) {
  ....
  int x = g(1, 2, 3);
  ....
}
```

## Υπόδειξη

Κατά την κλήση, οι παράμετροι `x`, `y`, `z` της `g` παίρνουν με τη σειρά τις τιμές των
ορισμάτων. Αντικαταστήστε τις στην παράσταση του `return`.
