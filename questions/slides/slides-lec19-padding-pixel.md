---
id: slides-lec19-padding-pixel
kind: slides
title: "Padding: το μέγεθος ενός pixel"
source:
  title: "Διάλεξη 19, διαφάνειες 22–24"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec19.pdf
  years: [2025]
chapters: [19]
topics: [structs, memory-model]
difficulty: 2
type: trace
---

Τι θα τυπώσει αυτό το πρόγραμμα (μεταγλώττιση με `gcc -m32 -o struct2 struct2.c`);

```c
#include <stdio.h>
int main() {
  struct pixel_tag {
      char red;
      char green;
      char blue;
      int alpha;
  } pixel = {0xFF, 0xFF, 0xFF, 42};
  printf("%zu\n", sizeof(pixel));
  return 0;
}
```

## Υπόδειξη

Τα πεδία πιάνουν 7 bytes, αλλά η απάντηση δεν είναι 7. Σκεφτείτε σε ποια διεύθυνση
προτιμά ο επεξεργαστής να ξεκινά ένα `int` (memory alignment).
