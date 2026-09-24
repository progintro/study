---
id: slides-lec09-float-equality
kind: slides
title: "OK ή Not OK;"
source:
  title: "Διάλεξη 9: Δεδομένα Εισόδου, διαφάνεια 3"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec09.pdf
  years: [2025]
chapters: [9]
topics: [floating-point, operators]
difficulty: 2
type: trace
---

Τι θα τυπώσει το παρακάτω πρόγραμμα; Υπάρχει κάποια εξήγηση;

```c
#include <stdio.h>
int main() {
    float a = 3.1;

    if(a == 3.1)
       printf("OK\n");
    else
       printf("Not OK\n");
    return 0;
}
```

## Υπόδειξη

Ποιος είναι ο τύπος της σταθεράς `3.1` και ποιος του `a`; Αναπαρίσταται το `3.1` ακριβώς σε δυαδική μορφή, και πόσα ψηφία ακρίβειας κρατά ένα `float` σε σχέση με ένα `double`;
