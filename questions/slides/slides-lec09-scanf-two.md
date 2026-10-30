---
id: slides-lec09-scanf-two
kind: slides
title: "scanf με πολλά ορίσματα"
source:
  title: "Διάλεξη 9: Δεδομένα Εισόδου, διαφάνεια 38–39"
  url: https://progintro.github.io/assets/pdf/lec09.pdf
  years: [2025, 2026]
chapters: [9]
topics: [input-output]
difficulty: 1
type: trace
---

Τι κάνει το παρακάτω πρόγραμμα; Τι τυπώνει με είσοδο `   2   4` (με επιπλέον κενά);

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

Τι κάνει η `%d` με τους κενούς χαρακτήρες και τις αλλαγές γραμμής που συναντά πριν από το πρώτο ψηφίο;
