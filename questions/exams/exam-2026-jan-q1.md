---
id: exam-2026-jan-q1
kind: exam
title: "Mystery"
source:
  title: "Εξέταση Ιανουαρίου 2026, Θέμα 1"
  url: https://progintro.github.io/exams/2026/progintro-exam-jan-26.pdf
  years: [2026]
chapters: [5, 6]
topics: [bitwise, operators, loops]
difficulty: 1
type: trace
---

**Mystery [10 Μονάδες]**

Η συνάρτηση `mystery` δέχεται ως όρισμα έναν ακέραιο αριθμό που αποτελείται από τα 3
τελευταία ψηφία του sdi σας. Για παράδειγμα, αν ο sdi σας είναι ο sdi2500789 τότε καλούμε
την συνάρτηση ως `mystery(789)`. Τι θα τυπώσει η συνάρτηση για τα ψηφία του δικού σας sdi;
Αν δεν έχετε sdi, επιλέξτε έναν τυχαίο τριψήφιο. Αιτιολογήστε όπου νομίζετε πως χρειάζεται.

```c
int mystery(int number) {
  int seed = number % 10;
  int count = (seed == 0 || seed > 4) ? 2 : seed;
  printf("Seed %d, count: %d\n", seed, count);
  for(int i = 0; i < count; ++i) {
    printf("Loop %d: %d\n", i, ++seed);
    seed &= 0xF;
  }
  printf("Result: %d\n", seed);
  return seed;
}
```

## Υπόδειξη

Μόνο το τελευταίο ψηφίο μετράει· βρείτε πρώτα τι κάνει ο τελεστής συνθήκης `?:` για
το `count`. Προσέξτε ότι το `++seed` αυξάνει την τιμή *πριν* τυπωθεί, και ότι το
`& 0xF` κρατά μόνο τα 4 χαμηλότερα bit: τι γίνεται όταν το `seed` φτάσει το 16;
