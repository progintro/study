---
id: slides-lec17-swap
kind: slides
title: "Η συνάρτηση swap"
source:
  title: "Διάλεξη 17: Δυαδική Αναζήτηση και Ταξινόμηση, διαφάνεια 21"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec17.pdf
  years: [2025]
chapters: [17, 18]
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

Τα ορίσματα στη C περνούν με τιμή, άρα μια συνάρτηση που παίρνει δύο `int` αλλάζει μόνο τα δικά της αντίγραφα. Περάστε στη `swap` τις διευθύνσεις των `a` και `b` και χρησιμοποιήστε μια βοηθητική μεταβλητή.
