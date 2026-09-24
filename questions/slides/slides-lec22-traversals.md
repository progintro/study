---
id: slides-lec22-traversals
kind: slides
title: "Διασχίσεις pre-order, in-order, post-order"
source:
  title: "Διαλέξεις 21–22: Δέντρα, διαφάνειες 22–28 (διάλεξη 21: διαφάνειες 44–50)"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec22.pdf
  years: [2025]
chapters: [22, 21]
topics: [trees, recursion]
difficulty: 1
type: trace
---

Δίνεται το δέντρο με ρίζα το 5· τα παιδιά του 5 είναι το 7 (αριστερά) και το 1 (δεξιά),
και τα παιδιά του 7 είναι το 2 (αριστερά) και το 9 (δεξιά).

```mermaid
flowchart TD
  N5(("5")) --> N7(("7"))
  N5 --> N1(("1"))
  N7 --> N2(("2"))
  N7 --> N9(("9"))
```

Τι τυπώνει καθεμία από τις παρακάτω εκδοχές της `print` όταν καλείται με τη ρίζα;

```c
void print(Tree t) {       /* Pre-order */
  if (t == NULL) return;
  printf("%d ", t->value);
  print(t->left);
  print(t->right);
}
```

```c
void print(Tree t) {       /* In-order */
  if (t == NULL) return;
  print(t->left);
  printf("%d ", t->value);
  print(t->right);
}
```

```c
void print(Tree t) {       /* Post-order */
  if (t == NULL) return;
  print(t->left);
  print(t->right);
  printf("%d ", t->value);
}
```

## Υπόδειξη

Εφαρμόστε τον ορισμό αναδρομικά, ξεκινώντας από τη ρίζα: η διάσχιση του 5 αποτελείται από τη διάσχιση του υποδέντρου του 7, τη διάσχιση του υποδέντρου του 1 και το ίδιο το 5, με τη σειρά που ορίζει η θέση του `printf`.
