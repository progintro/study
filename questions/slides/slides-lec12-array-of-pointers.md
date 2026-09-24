---
id: slides-lec12-array-of-pointers
kind: slides
title: "Πίνακας από δείκτες"
source:
  title: "Διάλεξη 12, διαφάνεια 29"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec12.pdf
  years: [2025]
chapters: [12]
topics: [pointers, arrays]
difficulty: 1
type: trace
---

Οι δείκτες είναι μεταβλητές και μπορούν να μπουν σε πίνακες. Για παράδειγμα, τι θα
τυπώσει το ακόλουθο;

```c
#include <stdio.h>
int main() {
  int *ptr[3], a = 100, b = 200, c = 300;
  ptr[0] = &a;
  ptr[1] = &b;
  ptr[2] = &c;
  printf("%d %d %d\n", *ptr[2], *ptr[1], *ptr[0]);
  return 0;
}
```

## Υπόδειξη

Το `*ptr[2]` διαβάζεται ως `*(ptr[2])`: πρώτα παίρνουμε το στοιχείο του πίνακα
(έναν δείκτη) και μετά την τιμή όπου αυτός δείχνει. Προσέξτε τη σειρά των ορισμάτων
στο `printf`.
