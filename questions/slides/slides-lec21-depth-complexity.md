---
id: slides-lec21-depth-complexity
kind: slides
title: "Βάθος δέντρου και πολυπλοκότητα"
source:
  title: "Διάλεξη 21, διαφάνειες 41–42"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec21.pdf
  years: [2025]
chapters: [21]
topics: [trees, recursion, complexity]
difficulty: 2
type: short-answer
---

Τι θα τυπώσει το πρόγραμμα; Ποια η πολυπλοκότητα για ένα τέλειο δυαδικό δέντρο;

```c
#include <stdio.h>
#include <stdlib.h>
typedef struct treenode {
  int value; struct treenode * left; struct treenode * right;
} * Tree;
int depth(Tree t) {
  if (t == NULL) return -1;
  int left_depth = depth(t->left);
  int right_depth = depth(t->right);
  return 1 + ((left_depth > right_depth) ? left_depth : right_depth);
}
int main() {
  struct treenode t2 = {2, NULL, NULL}, t9 = {9, NULL, NULL};
  struct treenode t1 = {1, NULL, NULL};
  struct treenode t7 = {7, &t2, &t9}, t5 = {5, &t7, &t1};
  Tree t = &t5;
  printf("Depth: %d\n", depth(t));
  return 0;
}
```

## Υπόδειξη

Ζωγραφίστε το δέντρο που φτιάχνει η `main`. Για τον χρόνο, πόσες φορές καλείται η `depth` για κάθε κόμβο; Για τον χώρο, πόσες κλήσεις είναι το πολύ ταυτόχρονα στη στοίβα, και πώς σχετίζεται αυτό με το βάθος ενός τέλειου δέντρου με n κόμβους;
