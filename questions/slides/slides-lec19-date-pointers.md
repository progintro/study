---
id: slides-lec19-date-pointers
kind: slides
title: "Δείκτες σε δομές: διαφορά ημερομηνιών"
source:
  title: "Διάλεξη 19, διαφάνειες 42–43"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec19.pdf
  years: [2025]
chapters: [19]
topics: [structs, pointers, dynamic-memory]
difficulty: 2
type: trace
---

Οι δείκτες μπορούν να συνδυαστούν με δομές όπως όλοι οι άλλοι τύποι. Τι θα τυπώσει το
παρακάτω πρόγραμμα;

```c
#include <stdio.h>
#include <stdlib.h>
typedef struct { int day; int month; int year; } Date;
int main() {
  Date d1 = {1, 10, 2023};
  Date * d2 = &d1;
  (*d2).day = 2;
  Date * d3 = malloc(sizeof(Date));
  *d3 = *d2;
  (*d3).month = 12; (*d3).day = 11;
  printf("Diff: %d/%d/%d\n", (*d3).day - d1.day, (*d3).month - d1.month, (*d3).year - d1.year);
  return 0;
}
```

## Υπόδειξη

Ξεχωρίστε πού δείχνει κάθε δείκτης: το `d2` σε υπάρχουσα μεταβλητή, το `d3` σε νέα
μνήμη. Αλλάζει το `d1` όταν γράφετε μέσω του `d2`; Τι αντιγράφει το `*d3 = *d2`;
