---
id: slides-lec20-enum-loop
kind: slides
title: "Βρόχος με απαρίθμηση"
source:
  title: "Διάλεξη 20, διαφάνεια 27"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec20.pdf
  years: [2025]
chapters: [20]
topics: [unions-enums, loops]
difficulty: 1
type: trace
---

Τι θα τυπώσει το ακόλουθο πρόγραμμα;

```c
#include <stdio.h>

enum weekday {Mon = 1, Tue, Wed, Thu, Fri, Sat, Sun};

int main() {
  for (enum weekday day = Mon; day <= Sun; day++) {
    if (day == Mon || day == Fri)
      printf("We have class on day # %d of the week\n", day);
  }
  return 0;
}
```

## Υπόδειξη

Βρείτε πρώτα την ακέραια τιμή κάθε σταθεράς, αφού τώρα η `Mon` έχει ρητή τιμή. Μετά
τρέξτε τον βρόχο σαν να ήταν ένας απλός ακέραιος μετρητής.
