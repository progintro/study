---
id: slides-lec10-scanf-two-numbers
kind: slides
title: "scanf με πολλά ορίσματα"
source:
  title: "Διάλεξη 10, διαφάνειες 15-16"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec10.pdf
  years: [2025]
chapters: [10]
topics: [input-output]
difficulty: 1
type: trace
---

Τι κάνει το παρακάτω πρόγραμμα; Τι θα τυπώσει αν δώσουμε ως είσοδο `   2   4`
(με επιπλέον κενά);

```c
#include <stdio.h>

int main() {
  int n1, n2;
  printf("Gimme two numbers: ");
  scanf("%d %d", &n1, &n2);
  printf("Result: %d\n", n1 * n2);
  return 0;
}
```

## Υπόδειξη

Τι κάνει η `scanf` με τους κενούς χαρακτήρες όταν ψάχνει για δεκαδικό ψηφίο;
