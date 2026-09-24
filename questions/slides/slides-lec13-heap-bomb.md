---
id: slides-lec13-heap-bomb
kind: slides
title: "Ένας τεράστιος πίνακας στον σωρό"
source:
  title: "Διάλεξη 13, διαφάνειες 43–46"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec13.pdf
  years: [2025]
chapters: [13]
topics: [dynamic-memory, memory-model]
difficulty: 2
type: trace
---

Τι θα κάνει το ακόλουθο πρόγραμμα;

```c
#include <stdio.h>
#include <stdlib.h>
int main() {
  char *bomb = malloc(sizeof(char) * 9000000);
  printf("Hello World\n");
  return 0;
}
```

Τι θα κάνει αν η `malloc` ζητήσει `sizeof(char) * 900000000000L` bytes; Και τι αν
μετά από αυτή την κλήση προσθέσουμε τη γραμμή `bomb[0] = 'A';` πριν το `printf`;
Πώς πρέπει να διορθωθεί το πρόγραμμα;

## Υπόδειξη

Συγκρίνετε κάθε μέγεθος με τη μνήμη του υπολογιστή σας. Τι επιστρέφει η `malloc`
όταν δεν υπάρχει αρκετή μνήμη, και τι γίνεται όταν γράφουμε σε αυτή τη διεύθυνση;
