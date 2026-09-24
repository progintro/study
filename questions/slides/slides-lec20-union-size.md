---
id: slides-lec20-union-size
kind: slides
title: "Χρήση ένωσης και μέγεθος"
source:
  title: "Διάλεξη 20, διαφάνεια 19"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec20.pdf
  years: [2025]
chapters: [20]
topics: [unions-enums, memory-model]
difficulty: 2
type: trace
---

Τι θα τυπώσει το πρόγραμμα;

```c
#include <stdio.h>

union anything {
  char c;  int i;  float f;  double d;
};

int main() {
  union anything a1;
  a1.i = 0x42;
  printf("%d %c\n", a1.i, a1.c);
  a1.c = 'C';
  printf("%d %c\n", a1.i, a1.c);
  printf("%zu\n", sizeof(a1));
  return 0;
}
```

## Υπόδειξη

Όλα τα μέλη της ένωσης ξεκινούν από το ίδιο byte, οπότε το `c` είναι το πρώτο byte
του `i`. Σκεφτείτε ποιο byte ενός ακεραίου είναι πρώτο σε ένα little-endian
μηχάνημα, και ότι το μέγεθος της ένωσης καθορίζεται από το μεγαλύτερο μέλος.
