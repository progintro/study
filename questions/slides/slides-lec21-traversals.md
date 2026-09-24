---
id: slides-lec21-traversals
kind: slides
title: "Pre-order, in-order και post-order"
source:
  title: "Διάλεξη 21, διαφάνειες 44–50"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec21.pdf
  years: [2025]
chapters: [21]
topics: [trees, recursion]
difficulty: 1
type: trace
---

Δίνεται το δυαδικό δέντρο:

```text
        5
       / \
      7   1
     / \
    2   9
```

Τι τυπώνει καθεμία από τις τρεις εκδοχές της `print`;

```c
void print(Tree t) {   // Pre-order
  if (t == NULL) return;
  printf("%d ", t->value);
  print(t->left);
  print(t->right);
}
```

```c
void print(Tree t) {   // In-order
  if (t == NULL) return;
  print(t->left);
  printf("%d ", t->value);
  print(t->right);
}
```

```c
void print(Tree t) {   // Post-order
  if (t == NULL) return;
  print(t->left);
  print(t->right);
  printf("%d ", t->value);
}
```

Ποια η πολυπλοκότητά τους ως προς χρόνο και χώρο;

## Υπόδειξη

Οι τρεις εκδοχές διαφέρουν μόνο στο πότε τυπώνεται ο τρέχων κόμβος σε σχέση με τα δύο υποδέντρα. Εφαρμόστε τον κανόνα αναδρομικά: τυπώστε πρώτα ολόκληρο το αριστερό υποδέντρο (7, 2, 9) με την ίδια σειρά, πριν περάσετε στο δεξί.
