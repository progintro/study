---
id: slides-lec24-dependencies
kind: slides
title: "Εξαρτήσεις ανάμεσα σε αρχεία"
source:
  title: "Διάλεξη 24: Προχωρημένα Θέματα, διαφάνεια 16"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec24.pdf
  years: [2025]
chapters: [24, 23]
topics: [code-organization, compilation]
difficulty: 2
type: short-answer
---

Δίνονται τρία αρχεία:

```c
// err.c
int print_err(
  char *msg
) {
...
}
```

```c
// err.h
int print_err(
  char *
);
```

```c
// init.c
#include "err.h"

...
print_err("hi");
```

Το `err.c` *υλοποιεί* τη διεπαφή (interface) `err.h`, και το `init.c` τη
*χρησιμοποιεί*.

- Αν αλλάξω ένα αρχείο, τι επηρεάζεται;
- Με τι μοιάζουν αυτές οι εξαρτήσεις;

## Υπόδειξη

Εξετάστε χωριστά τις τρεις περιπτώσεις: αλλαγή μόνο στο σώμα της συνάρτησης στο
`err.c`, αλλαγή στο `init.c`, αλλαγή στη δήλωση του `err.h`. Για καθεμία,
σκεφτείτε ποια αντικειμενικά αρχεία (`.o`) πρέπει να ξαναφτιαχτούν. Για το δεύτερο
ερώτημα, σχεδιάστε τα αρχεία ως κόμβους και τις σχέσεις ως βέλη: ποια δομή του
μαθήματος θυμίζει;
