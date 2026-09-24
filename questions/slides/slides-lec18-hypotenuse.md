---
id: slides-lec18-hypotenuse
kind: slides
title: "Υποτείνουσα με scanf"
source:
  title: "Διάλεξη 18, διαφάνειες 29–30"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec18.pdf
  years: [2025]
chapters: [18, 9]
topics: [input-output, floating-point]
difficulty: 1
type: trace
---

Τι κάνει το παρακάτω πρόγραμμα; Τι τυπώνει αν ο χρήστης δώσει `3.0 4.0`;

```c
#include <stdio.h>
#include <math.h>
int main() {
  double d1, d2;
  printf("Gimme two doubles: ");
  scanf("%lf %lf", &d1, &d2);
  printf("Hypotenuse: %.1f\n", sqrt(d1 * d1 + d2 * d2));
  return 0;
}
```

## Υπόδειξη

Το `%lf` διαβάζει `double` και το `%.1f` τυπώνει με ένα δεκαδικό. Αναγνωρίστε
τον τύπο που υπολογίζεται μέσα στη `sqrt` (Πυθαγόρειο θεώρημα).
