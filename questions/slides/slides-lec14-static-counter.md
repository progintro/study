---
id: slides-lec14-static-counter
kind: slides
title: "Στατική και τοπική μεταβλητή σε τρεις κλήσεις"
source:
  title: "Διάλεξη 14, διαφάνειες 17–18"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec14.pdf
  years: [2025]
chapters: [14]
topics: [scope, memory-model]
difficulty: 1
type: trace
---

Μια μεταβλητή λέγεται στατική (static), όταν διατηρεί την τιμή της ανάμεσα σε
κλήσεις συναρτήσεων μέχρι το τέλος του προγράμματος. Οι στατικές μεταβλητές
αρχικοποιούνται μόνο στην πρώτη κλήση της συνάρτησης. Τι θα τυπώσει;

```c
#include <stdio.h>
void foo() {
  static int counter = 0; int i = 0;
  counter++; i++;
  printf("%d %d\n", counter, i);
}
int main() {
  foo(); foo(); foo();
  return 0;
}
```

## Υπόδειξη

Κρατήστε δύο στήλες, μία για το `counter` και μία για το `i`, και ενημερώστε τις σε
κάθε κλήση. Ποια από τις δύο αρχικοποιήσεις εκτελείται ξανά σε κάθε κλήση και ποια
μόνο μία φορά;
