---
id: exam-2026-sep-q1
kind: exam
title: "Mystery"
source:
  title: "Εξέταση Σεπτεμβρίου 2026, Θέμα 1"
  url: https://progintro.github.io/exams/2026/progintro-exam-sep-26.pdf
  years: [2026]
chapters: [6, 2]
topics: [loops, operators, undefined-behavior]
difficulty: 1
type: trace
---

**Mystery [10 Μονάδες]**

Η συνάρτηση `mystery` δέχεται ως όρισμα έναν ακέραιο αριθμό που αποτελείται από τα 3
τελευταία ψηφία του sdi σας. Για παράδειγμα, αν ο sdi σας είναι ο sdi2500789 τότε καλούμε
την συνάρτηση ως `mystery(789)`. Τι θα τυπώσει η συνάρτηση για τα ψηφία του δικού σας
sdi; Αιτιολογήστε όπου νομίζετε πως χρειάζεται.

```c
int mystery(int number) {
  int i, total = 0;
  number += 100;
  printf("%s: %d, (%d)\n", "Computing total", total, i);
  for(i = 0 ; number ; i++) {
    total = 10 * total + number % 10;
    number /= 10;
    printf("%d: total: %d\n", i, total);
  }
  printf("%d: total: %d number: %d\n", i, total, number);
  return total;
}
```

## Υπόδειξη

Φτιάξτε έναν πίνακα με τις τιμές των `i`, `number` και `total` σε κάθε επανάληψη,
ξεκινώντας από το `number` *αφού* προστεθεί το 100. Η συνθήκη του `for` είναι απλώς
`number`: σκεφτείτε πότε γίνεται ψευδής. Προσέξτε την πρώτη `printf`: τι τιμή έχει το
`i` εκείνη τη στιγμή; Και σκεφτείτε τι γίνεται με τα μηδενικά όταν τα ψηφία μπαίνουν
στο `total`, π.χ. αν το άθροισμα είναι τετραψήφιο ή τελειώνει σε 0.
