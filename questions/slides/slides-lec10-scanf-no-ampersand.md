---
id: slides-lec10-scanf-no-ampersand
kind: slides
title: "scanf χωρίς &"
source:
  title: "Διάλεξη 10, διαφάνεια 11"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec10.pdf
  years: [2025]
chapters: [10, 11]
topics: [input-output, pointers]
difficulty: 2
type: debug
---

Στο πρόγραμμα:

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

Τι θα γινόταν αν γράφαμε `scanf("%d", n);`; Γιατί;

```text
$ ./scanf
Gimme a number: 3
Segmentation fault
```

## Υπόδειξη

Σκεφτείτε τι παίρνει μια συνάρτηση όταν της περνάμε μια μεταβλητή με τιμή, και τι
τιμή έχει η `n` τη στιγμή της κλήσης. Πού θα προσπαθήσει να γράψει η `scanf`;
