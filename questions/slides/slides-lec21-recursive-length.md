---
id: slides-lec21-recursive-length
kind: slides
title: "Αναδρομικό μήκος λίστας"
source:
  title: "Διάλεξη 21, διαφάνεια 18"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec21.pdf
  years: [2025]
chapters: [21]
topics: [linked-lists, recursion]
difficulty: 1
type: programming
---

Η παρακάτω συνάρτηση βρίσκει το μήκος μιας λίστας επαναληπτικά:

```c
int length(List list) {
  int counter = 0;
  while(list) {
    counter++;
    list = list->next;
  }
  return counter;
}
```

Πως θα το κάναμε αναδρομικά;

## Υπόδειξη

Ποιο είναι το μήκος της κενής λίστας (`NULL`); Αν ξέρατε το μήκος της λίστας που ξεκινά από το `list->next`, πώς θα βρίσκατε το μήκος ολόκληρης της λίστας;
