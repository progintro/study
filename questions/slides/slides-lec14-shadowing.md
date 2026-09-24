---
id: slides-lec14-shadowing
kind: slides
title: "Επισκίαση παγκόσμιας μεταβλητής"
source:
  title: "Διάλεξη 14, διαφάνειες 14–16"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec14.pdf
  years: [2025]
chapters: [14]
topics: [scope]
difficulty: 1
type: trace
---

Όταν μια δήλωση μεταβλητής βρίσκεται εντός εμβέλειας άλλης μεταβλητής με το ίδιο
όνομα, τότε η εσωτερική μεταβλητή επισκιάζει (shadows) την άλλη. Τι θα τυπώσει;

```c
#include <stdio.h>
int baz = 42;
int main() {
  int baz = 43;
  printf("baz: %d\n", baz);
  return 0;
}
```

## Υπόδειξη

Βρείτε την εμβέλεια της παγκόσμιας `baz` και της τοπικής `baz` της `main`. Στο
σημείο της `printf` είναι ορατές και οι δύο· ποια δήλωση είναι η πιο «εσωτερική»;
