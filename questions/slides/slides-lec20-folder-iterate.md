---
id: slides-lec20-folder-iterate
kind: slides
title: "Διάσχιση φακέλων"
source:
  title: "Διάλεξη 20, διαφάνεια 35"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec20.pdf
  years: [2025]
chapters: [20]
topics: [structs, pointers, loops]
difficulty: 2
type: trace
---

Τι θα τυπώσει το πρόγραμμα;

```c
#include <stdio.h>

typedef struct folder {
  char name[128];
  struct folder *parent;
} Folder;

int main() {
  Folder root = {"/", NULL};
  Folder home = {"home/", &root};
  Folder user = {"thanos/", &home};
  Folder hw0 = {"hw0/", &user}, hw1 = {"hw1/", &user};
  Folder newton = {"newton/", &hw0};
  for (Folder *iterator = &newton; iterator; iterator = iterator->parent)
    printf("folder: %s\n", iterator->name);
  return 0;
}
```

## Υπόδειξη

Ο βρόχος ξεκινά με δείκτη στον `newton` και σε κάθε βήμα μετακινείται στον γονέα.
Ρωτήστε: πότε γίνεται ψευδής η συνθήκη `iterator`; Τυπώνεται ποτέ ο `hw1`;
