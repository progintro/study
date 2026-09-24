---
id: slides-lec16-swap
kind: slides
title: "Η συνάρτηση swap"
source:
  title: "Διάλεξη 16, διαφάνειες 22–23"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec16.pdf
  years: [2025]
chapters: [16, 11]
topics: [pointers, functions]
difficulty: 1
type: programming
---

Γράψτε μια συνάρτηση `swap` που ανταλλάζει δύο ακεραίους.

```c
#include <stdio.h>
int main() {
  int a = 100, b = 200;
  printf("%d %d\n", a, b);
  swap( ... );
  printf("%d %d\n", a, b);
  return 0;
}
```

## Υπόδειξη

Τα ορίσματα περνούν κατά τιμή, οπότε μια `swap(a, b)` θα άλλαζε μόνο αντίγραφα. Τι
πρέπει να περάσει η `main` ώστε η `swap` να μπορεί να γράψει στις δικές της `a` και
`b`; Θα χρειαστείτε και μια προσωρινή μεταβλητή.
