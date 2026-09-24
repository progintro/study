---
id: slides-lec06-for-count
kind: slides
title: "Πόσες φορές εκτελείται μια for"
source:
  title: "Διάλεξη 6: Εντολές και Ροή Ελέγχου, διαφάνεια 24"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec06.pdf
  years: [2025]
chapters: [6]
topics: [loops]
difficulty: 1
type: short-answer
---

Γενικό παράδειγμα:

```c
int i;
for ( i = 0 ; i < N ; i++ ) {
    printf("%d\n", i);
}
```

Πόσες φορές θα εκτελεστεί το block εντολών μέσα στην `for`; Θα τυπωθεί το `N`; Τι θα συμβεί αν αλλάξω την αρχικοποίηση ή το βήμα;

## Υπόδειξη

Γράψτε τις τιμές του `i` για τις οποίες η συνθήκη είναι αληθής, για ένα μικρό `N` (π.χ. 3). Τι τιμή έχει το `i` τη στιγμή που ο βρόχος σταματάει; Δοκιμάστε μετά με `i = 1` ή με βήμα `i += 2`.
