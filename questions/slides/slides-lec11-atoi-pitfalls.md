---
id: slides-lec11-atoi-pitfalls
kind: slides
title: "Τι μπορεί να πάει στραβά με την atoi"
source:
  title: "Διάλεξη 11, διαφάνεια 42"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec11.pdf
  years: [2025]
chapters: [11]
topics: [strings, input-validation, integer-representation]
difficulty: 2
type: debug
---

Τι μπορεί να πάει στραβά με αυτήν τη συνάρτηση;

```c
int atoi(char digits[]) {
  int result = 0;
  for (int i = 0; digits[i]; i++) {
    result = 10 * result + digits[i] - '0';
  }
  return result;
}
```

## Υπόδειξη

Δοκιμάστε νοερά εισόδους που παραβιάζουν τις υποθέσεις της: χαρακτήρες που δεν είναι
ψηφία (π.χ. πρόσημο), έναν πολύ μεγάλο αριθμό, έναν πίνακα χωρίς `'\0'` στο τέλος.
Σκεφτείτε επίσης αν το όνομα της συνάρτησης συγκρούεται με κάτι από την standard
library.
