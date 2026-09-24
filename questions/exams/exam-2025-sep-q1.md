---
id: exam-2025-sep-q1
kind: exam
title: "Mystery"
source:
  title: "Εξέταση Σεπτεμβρίου 2025, Θέμα 1"
  url: https://progintro.github.io/exams/2025/progintro-exam-sep-25.pdf
  years: [2025]
chapters: [6, 2]
topics: [loops, variables, undefined-behavior]
difficulty: 1
type: trace
---

**Mystery [10 Μονάδες]**

Η συνάρτηση `mystery` δέχεται ως όρισμα έναν ακέραιο αριθμό που αποτελείται από τα 3
τελευταία ψηφία του sdi σας. Για παράδειγμα, αν ο sdi σας είναι ο sdi2400789 τότε καλούμε
την συνάρτηση ως `mystery(789)`. Τι θα τυπώσει η συνάρτηση για τα ψηφία του δικού σας sdi;
Αν δεν έχετε sdi, επιλέξτε έναν τυχαίο τριψήφιο. Αιτιολογήστε όπου νομίζετε πως χρειάζεται.

```c
int mystery(int number) {
  int s = 0, rem;
  printf("%s %d %d\n", "Starting loop", s, rem);
  do {
    rem = number % 10;
    printf("Inner: %d\n", rem);
    number /= 10;
    s += rem;
  } while (number);
  printf("Loop ended %d\n", s);
  return s;
}
```

## Υπόδειξη

Κρατήστε έναν πίνακα με τις τιμές των `number`, `rem` και `s` σε κάθε επανάληψη
και θυμηθείτε ότι το σώμα της `do-while` εκτελείται τουλάχιστον μία φορά. Προσέξτε
ιδιαίτερα την πρώτη `printf`: ποια τιμή έχει το `rem` εκείνη τη στιγμή; Σκεφτείτε
επίσης τι γίνεται αν το τριψήφιό σας ξεκινά με 0 (π.χ. 042).
