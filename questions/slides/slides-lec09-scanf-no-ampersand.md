---
id: slides-lec09-scanf-no-ampersand
kind: slides
title: "scanf χωρίς &"
source:
  title: "Διάλεξη 9: Δεδομένα Εισόδου, διαφάνεια 34"
  url: https://progintro.github.io/assets/pdf/lec09.pdf
  years: [2025, 2026]
chapters: [9]
topics: [input-output, pointers]
difficulty: 2
type: short-answer
---

Στο πρόγραμμα

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

τι θα γινόταν αν γράφαμε `scanf("%d", n);`; Γιατί;

```text
$ ./scanf
Gimme a number: 3
Segmentation fault
```

## Υπόδειξη

Η C περνάει τα ορίσματα με τιμή. Τι παίρνει η `scanf` στη μία και τι στην άλλη περίπτωση, και πού προσπαθεί να γράψει τον αριθμό που διάβασε;
