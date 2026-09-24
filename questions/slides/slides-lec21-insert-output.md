---
id: slides-lec21-insert-output
kind: slides
title: "Τι τυπώνει η εισαγωγή σε λίστα;"
source:
  title: "Διάλεξη 21, διαφάνειες 13–16"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec21.pdf
  years: [2025]
chapters: [21]
topics: [linked-lists, dynamic-memory, pointers]
difficulty: 1
type: trace
---

Τι θα τυπώσει το πρόγραμμα;

```c
#include <stdio.h>
#include <stdlib.h>
typedef struct listnode {int value; struct listnode * next;} * List;
void insert(List * list, int value) {
  List current_head = *list;
  List new_head = malloc(sizeof(struct listnode));
  new_head->value = value;
  new_head->next = current_head;
  *list = new_head;
}
void print(List list) {
  printf("list: ");
  while(list) {
    printf(" -> %d", list->value);
    list = list->next;
  }
  printf(" -> NULL\n");
}
int main() {
  List list = NULL;
  insert(&list, 42); insert(&list, 43); insert(&list, 44);
  print(list);
  return 0;
}
```

## Υπόδειξη

Ζωγραφίστε τη λίστα μετά από κάθε κλήση της `insert`: σε ποια θέση μπαίνει κάθε νέος κόμβος; Προσέξτε και τα κενά που τυπώνουν τα δύο πρώτα `printf`.
