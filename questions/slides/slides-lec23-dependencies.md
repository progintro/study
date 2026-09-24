---
id: slides-lec23-dependencies
kind: slides
title: "Εξαρτήσεις ανάμεσα σε αρχεία"
source:
  title: "Διάλεξη 23, διαφάνεια 15"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec23.pdf
  years: [2025]
chapters: [23]
topics: [code-organization, compilation, make]
difficulty: 2
type: short-answer
---

Ένα πρόγραμμα έχει τρία αρχεία:

```c
/* err.c */
int print_err(char *msg) {
  ...
}
```

```c
/* err.h */
int print_err(char *);
```

```c
/* init.c */
#include "err.h"
...
print_err("hi");
```

Το `err.c` υλοποιεί τη διεπαφή `err.h` και το `init.c` τη χρησιμοποιεί.

1. Αν αλλάξω ένα αρχείο, τι επηρεάζεται; Απαντήστε για καθένα από τα τρία αρχεία.
2. Με τι μοιάζουν αυτές οι εξαρτήσεις;

## Υπόδειξη

Για κάθε αρχείο, αναρωτηθείτε ποια άλλα αρχεία «βλέπουν» το περιεχόμενό του κατά τη
μεταγλώττιση. Σχεδιάστε τα αρχεία ως κόμβους και τις σχέσεις «υλοποιεί» και
«χρησιμοποιεί» ως βέλη: ποια δομή δεδομένων από τις προηγούμενες διαλέξεις
σχηματίζεται;
