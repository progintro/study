---
id: slides-lec10-scanf-correct
kind: slides
title: "Είναι σωστό αυτό το πρόγραμμα;"
source:
  title: "Διάλεξη 10, διαφάνειες 12-14"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec10.pdf
  years: [2025]
chapters: [10]
topics: [input-output, input-validation]
difficulty: 2
type: debug
---

Είναι σωστό αυτό το πρόγραμμα;

```c
#include <stdio.h>

int main() {
  int n;
  printf("Gimme a number: ");
  scanf("%d", &n);
  printf("Square: %d\n", n * n);
  return 0;
}
```

Μερικές εκτελέσεις:

```text
$ ./scanf
Gimme a number: 16
Square: 256
$ ./scanf
Gimme a number: Square:
1068701481
$ ./scanf
Gimme a number: hello
Square: 1072038564
```

## Υπόδειξη

Η `scanf` επιστρέφει κάτι. Τι επιστρέφει όταν τελειώσει η είσοδος και τι όταν η
είσοδος δεν είναι αριθμός; Τι τιμή έχει η `n` σε αυτές τις περιπτώσεις;
