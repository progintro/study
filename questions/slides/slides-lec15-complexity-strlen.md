---
id: slides-lec15-complexity-strlen
kind: slides
title: "Πολυπλοκότητα της strlen"
source:
  title: "Διάλεξη 15, διαφάνεια 29"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec15.pdf
  years: [2025]
chapters: [15, 14]
topics: [complexity, strings, pointers]
difficulty: 1
type: short-answer
---

Η συνάρτηση strlen. Μια πιθανή υλοποίηση:

```c
size_t strlen(char * str) {
  size_t length = 0;
  while(*str++) length++;
  return length;
}
```

Τι πολυπλοκότητας είναι η συνάρτηση strlen ως προς το μέγεθος της συμβολοσειράς;

## Υπόδειξη

Πότε σταματά ο βρόχος και πόσους χαρακτήρες έχει περάσει μέχρι τότε; Υπάρχει τρόπος
να βρεθεί το μήκος χωρίς να διατρέξουμε τη συμβολοσειρά;
