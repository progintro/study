---
id: slides-lec20-folder-parent
kind: slides
title: "Γονικοί φάκελοι"
source:
  title: "Διάλεξη 20, διαφάνεια 33"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec20.pdf
  years: [2025]
chapters: [20]
topics: [structs, pointers]
difficulty: 1
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
  printf("%s -> %s -> %s\n", newton.name, newton.parent->name,
         newton.parent->parent->name);
  return 0;
}
```

## Υπόδειξη

Ακολουθήστε τους δείκτες `parent` ένα βήμα κάθε φορά, ξεκινώντας από τον `newton`.
Γράψτε δίπλα σε κάθε φάκελο σε ποια μεταβλητή δείχνει.
