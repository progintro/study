---
id: slides-lec09-cat-char
kind: slides
title: "Μια cat με char"
source:
  title: "Διάλεξη 9: Δεδομένα Εισόδου, διαφάνεια 24"
  url: https://progintro.github.io/assets/pdf/lec09.pdf
  years: [2025, 2026]
chapters: [9]
topics: [input-output, types]
difficulty: 2
type: debug
---

Τι πρόβλημα έχει η παρακάτω υλοποίηση της `cat`;

```c
#include <stdio.h>

int main() {
  char c;
  while((c = getchar()) != EOF)
    putchar(c);
  return 0;
}
```

## Υπόδειξη

Πόσες διαφορετικές τιμές μπορεί να επιστρέψει η `getchar` και πόσες χωράει ένα `char`; Δοκιμάστε την είσοδο `echo -e "hello\xffworld" | ./cat` και σκεφτείτε ποια τιμή παίρνει το `c` για το byte `0xff`.
