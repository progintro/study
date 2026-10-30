---
id: slides-lec09-scanf-return
kind: slides
title: "Είναι σωστό αυτό το πρόγραμμα;"
source:
  title: "Διάλεξη 9: Δεδομένα Εισόδου, διαφάνεια 35–37"
  url: https://progintro.github.io/assets/pdf/lec09.pdf
  years: [2025, 2026]
chapters: [9]
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

Τι επιστρέφει η `scanf` όταν πατήσετε Ctrl+D και τι όταν γράψετε `hello`; Ποια τιμή έχει το `n` σε αυτές τις περιπτώσεις, αφού δεν αρχικοποιήθηκε ποτέ;
