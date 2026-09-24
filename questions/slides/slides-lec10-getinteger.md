---
id: slides-lec10-getinteger
kind: slides
title: "Τι κάνει η getinteger;"
source:
  title: "Διάλεξη 10, διαφάνεια 17"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec10.pdf
  years: [2025]
chapters: [10, 9]
topics: [input-output, functions]
difficulty: 2
type: trace
---

Τι κάνει το παρακάτω πρόγραμμα;

```c
#define ERROR -1

int getinteger(int base) {
  int ch;
  int val = 0;
  while ((ch = getchar()) != '\n')
    if (ch >= '0' && ch <= '0' + base - 1)
      val = base * val + (ch - '0');
    else
      return ERROR;
  return val;
}
```

## Υπόδειξη

Εκτελέστε τη με το χέρι για `base = 10` και είσοδο `472`, και μετά για `base = 2`
και είσοδο `101`. Ποιοι χαρακτήρες θεωρούνται νόμιμοι για κάθε βάση;
