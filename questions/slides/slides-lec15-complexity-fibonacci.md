---
id: slides-lec15-complexity-fibonacci
kind: slides
title: "Πολυπλοκότητα του αναδρομικού Fibonacci"
source:
  title: "Διάλεξη 15, διαφάνεια 27"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec15.pdf
  years: [2025]
chapters: [15, 11]
topics: [complexity, recursion]
difficulty: 2
type: short-answer
---

Η συνάρτηση fibonacci. Τι χρονική και τι χωρική πολυπλοκότητα έχει;

```c
int fib(int n) {
  if (n == 0 || n == 1) return 1;
  return fib(n - 1) + fib(n - 2);
}
```

## Υπόδειξη

Σχεδιάστε το δέντρο κλήσεων του `fib(4)` ή του `fib(5)`: πόσα παιδιά έχει κάθε κόμβος
και πόσο βαθύ είναι το δέντρο; Ο χρόνος εξαρτάται από το πλήθος των κόμβων, ο χώρος από
το μακρύτερο μονοπάτι.
