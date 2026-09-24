---
id: slides-lec09-getinteger
kind: slides
title: "Η συνάρτηση getinteger"
source:
  title: "Διάλεξη 9: Δεδομένα Εισόδου, διαφάνεια 26, 38"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec09.pdf
  years: [2025]
chapters: [9]
topics: [input-output, functions, input-validation]
difficulty: 2
type: trace
---

Τι κάνει το παρακάτω πρόγραμμα;

```c
#define ERROR -1          // Return value for illegal character

int getinteger(int base) {
  int ch;                 // No need to declare ch as int - no EOF handling
  int val = 0;                               // Initialize return value
  while ((ch = getchar()) != '\n')           // Read up to new line
    if (ch >= '0' && ch <= '0' + base - 1)   // Legal character?
      val = base * val + (ch - '0');         // Update return value
    else
      return ERROR;                          // Illegal character read
  return val;   // Everything OK - Return value of number read
}
```

## Υπόδειξη

Ιχνηλατήστε το `val` για την κλήση `getinteger(10)` με είσοδο `42` και για την `getinteger(2)` με είσοδο `101`. Τι τιμή έχει το `ch - '0'` για έναν χαρακτήρα-ψηφίο; Τι γίνεται αν εμφανιστεί γράμμα;
