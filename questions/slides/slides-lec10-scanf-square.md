---
id: slides-lec10-scanf-square
kind: slides
title: "Τι κάνει το πρόγραμμα με τη scanf;"
source:
  title: "Διάλεξη 10, διαφάνειες 9-10"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec10.pdf
  years: [2025]
chapters: [10]
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

Διαβάστε τη `scanf` ως την «αντίστροφη» της `printf`. Τι ρόλο παίζει το `&` μπροστά
από το `n`;
