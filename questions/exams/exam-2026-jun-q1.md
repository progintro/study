---
id: exam-2026-jun-q1
kind: exam
title: "Η συνάρτηση mystery"
source:
  title: "Εξέταση Ιουνίου 2026, Θέμα 1"
  url: https://progintro.github.io/exams/2026/progintro-exam-jun-26.pdf
  years: [2026]
chapters: [5, 6]
topics: [bitwise, loops, types]
difficulty: 1
type: trace
---

**Η Συνάρτηση mystery (15 Μονάδες)**

Η συνάρτηση `mystery` δέχεται ως όρισμα έναν ακέραιο αριθμό που αποτελείται από τα 3
τελευταία ψηφία του sdi σας. Για παράδειγμα, αν ο sdi σας είναι ο sdi2500789 τότε καλούμε
την συνάρτηση ως `mystery(789)`. Τι θα τυπώσει η συνάρτηση για τα ψηφία του δικού σας sdi;
Αν δεν έχετε sdi, επιλέξτε έναν τυχαίο τριψήφιο. Αιτιολογήστε όπου νομίζετε πως χρειάζεται.

```c
int mystery(int number) {
  int i = 0;
  while(number > 4) {
    printf("Loop %d: %d\n", i++, number);
    number >>= 2;
  }
  printf("Result: %c\n", '0' + number);
  return number;
}
```

## Υπόδειξη

Το `number >>= 2` για θετικό ακέραιο ισοδυναμεί με ακέραια διαίρεση με το 4. Κρατήστε
έναν πίνακα με τις τιμές των `i` και `number` σε κάθε επανάληψη, προσέχοντας ότι το
`i++` τυπώνει την τιμή *πριν* την αύξηση. Στο τέλος, σκεφτείτε ποιος χαρακτήρας
αντιστοιχεί στον κωδικό ASCII `'0' + number` όταν το `number` είναι μεταξύ 0 και 4.
