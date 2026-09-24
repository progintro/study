---
id: slides-lec21-find-output
kind: slides
title: "Τι τυπώνει η find σε λίστα;"
source:
  title: "Διάλεξη 21, διαφάνειες 21–22"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec21.pdf
  years: [2025]
chapters: [21]
topics: [linked-lists, pointers, complexity]
difficulty: 2
type: trace
---

Τι θα τυπώσει το πρόγραμμα; (Η `insert` είναι η εισαγωγή στην αρχή της λίστας της διάλεξης.)

```c
#include <stdio.h>
#include <stdlib.h>
typedef struct listnode {int value; struct listnode * next;} * List;
List find(List list, int value) {
  while(list && list->value != value) {
    list = list->next;
  }
  return list;
}
int main() {
  List list = NULL;
  insert(&list, 42); insert(&list, 43); insert(&list, 44);
  printf("Found 43: %x\n", find(list, 43));
  printf("Found 34: %x\n", find(list, 34));
  return 0;
}
```

Ποια η πολυπλοκότητα της `find` ως προς χρόνο και χώρο;

## Υπόδειξη

Τι επιστρέφει η `find` όταν βρει την τιμή και τι όταν φτάσει στο τέλος της λίστας; Η μία από τις δύο γραμμές δεν μπορεί να προβλεφθεί ακριβώς: γιατί; Σκεφτείτε επίσης αν το `%x` είναι ο σωστός προσδιοριστής για δείκτη.
