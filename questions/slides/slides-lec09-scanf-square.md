---
id: slides-lec09-scanf-square
kind: slides
title: "Τι κάνει το πρόγραμμα με τη scanf;"
source:
  title: "Διάλεξη 9: Δεδομένα Εισόδου, διαφάνεια 32"
  url: https://progintro.github.io/assets/pdf/lec09.pdf
  years: [2025, 2026]
chapters: [9]
topics: [input-output]
difficulty: 1
type: trace
---

Τι κάνει το παρακάτω πρόγραμμα;

```c
#include <stdio.h>
int main() {
  int n;
  printf("Gimme a number: ");
  scanf("%d", &n);
  printf("Square: %d\n", n * n);
  return 0;
}
```

## Υπόδειξη

Τι σημαίνει η προδιαγραφή `%d` στη `scanf`, και γιατί μπροστά από το `n` υπάρχει `&`; Τι γράφεται στο `stdout` αν δώσετε `16`;
