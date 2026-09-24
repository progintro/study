---
id: slides-lec21-length-complexity
kind: slides
title: "Πολυπλοκότητα του μήκους λίστας"
source:
  title: "Διάλεξη 21, διαφάνειες 19–20"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec21.pdf
  years: [2025]
chapters: [21]
topics: [complexity, linked-lists, recursion]
difficulty: 2
type: short-answer
---

Δίνονται δύο υλοποιήσεις της `length`:

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

```c
int length(List list) {
  if (!list) return 0;
  return 1 + length(list->next);
}
```

Ποια η πολυπλοκότητα των παραπάνω ως προς χρόνο και χώρο;

## Υπόδειξη

Για τον χρόνο, μετρήστε πόσες φορές επισκέπτεται κάθε εκδοχή κάθε κόμβο. Για τον χώρο, σκεφτείτε πόσες κλήσεις της συνάρτησης είναι ταυτόχρονα ενεργές στη στοίβα όταν φτάνουμε στο τέλος της λίστας.
