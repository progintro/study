---
id: slides-lec19-padding-interleaved
kind: slides
title: "Padding: η σειρά των πεδίων μετράει"
source:
  title: "Διάλεξη 19, διαφάνειες 25–27"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec19.pdf
  years: [2025]
chapters: [19]
topics: [structs, memory-model]
difficulty: 2
type: trace
---

Τι θα τυπώσει αυτό το πρόγραμμα (μεταγλώττιση με `gcc -m32 -o struct3 struct3.c`);

```c
#include <stdio.h>
int main() {
  struct pixel_tag {
     char red; int alpha;
     char green; int beta;
     char blue; int gamma;
  } pixel;
  printf("%zu\n", sizeof(pixel));
  return 0;
}
```

## Υπόδειξη

Ζωγραφίστε τη δομή byte-byte με τη σειρά της δήλωσης και βάλτε κάθε `int` σε
διεύθυνση πολλαπλάσιο του 4. Πόσα από τα bytes χρησιμοποιούνται στην πραγματικότητα;
