---
id: slides-lec11-print-world
kind: slides
title: "Πώς τυπώνω μόνο το World"
source:
  title: "Διάλεξη 11, διαφάνειες 34–35"
  url: https://progintro.github.io/assets/pdf/lec11.pdf
  years: [2025, 2026]
chapters: [11]
topics: [pointers, strings, arrays]
difficulty: 1
type: programming
---

Από την προηγούμενη φορά, πώς μπορώ να τυπώσω `"World\n"`; Συμπληρώστε το `...`:

```c
char hello[] = "Hello World\n";
char *world = ...;
printf("%s", world);
```

## Υπόδειξη

Το `%s` τυπώνει χαρακτήρες ξεκινώντας από τη διεύθυνση που του δίνετε, μέχρι το
`'\0'`. Μετρήστε σε ποια θέση του πίνακα βρίσκεται το `'W'` και σκεφτείτε πώς
παίρνετε τη διεύθυνση αυτού του στοιχείου.
