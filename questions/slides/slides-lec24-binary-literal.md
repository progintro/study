---
id: slides-lec24-binary-literal
kind: slides
title: "Ο τυχερός αριθμός σε δυαδικό"
source:
  title: "Διάλεξη 24: Προχωρημένα Θέματα, διαφάνεια 32"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec24.pdf
  years: [2025]
chapters: [24, 2]
topics: [integer-representation, types]
difficulty: 1
type: trace
---

Τι θα τυπώσει αυτό το πρόγραμμα;

```c
#include <stdio.h>

int main() {
  int i = 0b101010;
  printf("My lucky number is: %d\n", i);
  return 0;
}
```

## Υπόδειξη

Το πρόθεμα `0b` (C2X) σημαίνει ότι τα ψηφία που ακολουθούν είναι δυαδικά. Γράψτε
τη θέση κάθε bit από δεξιά (θέση 0) και αθροίστε τις δυνάμεις του 2 για όσα bit είναι 1.
