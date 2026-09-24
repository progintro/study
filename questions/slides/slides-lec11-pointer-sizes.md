---
id: slides-lec11-pointer-sizes
kind: slides
title: "Το μέγεθος δεικτών διαφορετικών τύπων"
source:
  title: "Διάλεξη 11, διαφάνεια 18"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec11.pdf
  years: [2025]
chapters: [11]
topics: [pointers, types]
difficulty: 1
type: trace
---

Τι θα τυπώσει το παρακάτω πρόγραμμα;

```c
#include <stdio.h>

int main() {
  int * ipointer;
  char * cpointer;
  double * dpointer;
  printf("%d %d %d\n", sizeof(ipointer), sizeof(cpointer), sizeof(dpointer));
  return 0;
}
```

## Υπόδειξη

Τι ακριβώς αποθηκεύει μια μεταβλητή τύπου δείκτη; Εξαρτάται το μέγεθος αυτού που
αποθηκεύει από τον τύπο των δεδομένων στα οποία δείχνει ή από το σύστημα (32 ή 64 bit)
για το οποίο μεταγλωττίζεται το πρόγραμμα;
