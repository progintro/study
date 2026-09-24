---
id: slides-lec11-assign-through-pointers
kind: slides
title: "Αναθέσεις μέσω δεικτών"
source:
  title: "Διάλεξη 11, διαφάνεια 24"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec11.pdf
  years: [2025]
chapters: [11]
topics: [pointers]
difficulty: 1
type: trace
---

Τι τυπώνει το παρακάτω πρόγραμμα;

```c
#include <stdio.h>
int main() {
  int a = 100, b = 200, c;
  int *ptr_a = &a, *ptr_b = &b, *ptr_c = &c;
  *ptr_c = a;
  *ptr_a = b;
  *ptr_b = *ptr_c;
  printf("%d %d %d", a, b, c);
  return 0;
}
```

## Υπόδειξη

Αντικαταστήστε κάθε `*ptr_x` με τη μεταβλητή στην οποία δείχνει ο δείκτης και
εκτελέστε τις τρεις αναθέσεις με τη σειρά, κρατώντας έναν πίνακα με τις τιμές των
`a`, `b`, `c` μετά από κάθε γραμμή.
