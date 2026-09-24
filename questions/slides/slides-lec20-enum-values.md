---
id: slides-lec20-enum-values
kind: slides
title: "Τιμές απαρίθμησης"
source:
  title: "Διάλεξη 20, διαφάνεια 25"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec20.pdf
  years: [2025]
chapters: [20]
topics: [unions-enums]
difficulty: 1
type: trace
---

Τι θα τυπώσει το ακόλουθο πρόγραμμα;

```c
#include <stdio.h>

enum weekday {Mon, Tue, Wed, Thu, Fri, Sat, Sun};

int main() {
  enum weekday day1 = Mon, day2;
  day2 = Fri;
  printf("%d %d\n", day1, day2);
  return 0;
}
```

## Υπόδειξη

Θυμηθείτε από ποια τιμή ξεκινά η πρώτη σταθερά μιας απαρίθμησης όταν δεν της δίνουμε
τιμή, και πόσο αυξάνεται κάθε επόμενη.
