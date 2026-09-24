---
id: slides-lec12-endianness
kind: slides
title: "Παράδειγμα endianness"
source:
  title: "Διάλεξη 12, διαφάνεια 42"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec12.pdf
  years: [2025]
chapters: [12, 13]
topics: [memory-model, pointers, integer-representation]
difficulty: 2
type: trace
---

Τι θα τυπώσει το παρακάτω;

```c
#include <stdio.h>
int main() {
  int x = 42;
  char * bytes = (char*)&x;
  int i;
  for(i = 0; i < sizeof(int) / sizeof(char); i++)
     printf("%02x\n", bytes[i]);
  return 0;
}
```

## Υπόδειξη

Γράψτε το 42 σε δεκαεξαδικό ως ακέραιο 4 bytes. Ο δείκτης `bytes` διατρέχει τη μνήμη
του `x` ένα byte τη φορά, από τη χαμηλότερη διεύθυνση· η απάντηση εξαρτάται από το αν
ο υπολογιστής σας είναι little ή big endian (οι x86 και οι περισσότεροι ARM είναι
little endian).
