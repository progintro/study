---
id: exam-2025-jan-q1
kind: exam
title: "Mystery"
source:
  title: "Εξέταση Ιανουαρίου 2025, Θέμα 1"
  url: https://progintro.github.io/exams/2025/progintro-exam-jan-25.pdf
  years: [2025]
chapters: [5, 6]
topics: [bitwise, loops, undefined-behavior]
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
  int i;
  int step = 2;
  printf("%s %d\n", "Starting loop", i);
  for(i = 0; i < 3; i++) {
    printf("step %d %d\n", i, number + step);
    step = (step << 2) + 2;
  }
  printf("Ending loop %d\n", i);
  return number + step;
}
```

## Υπόδειξη

Κοιτάξτε προσεκτικά την πρώτη `printf`: τι τιμή έχει το `i` εκείνη τη στιγμή; Για
το `step`, θυμηθείτε ότι το `<< 2` πολλαπλασιάζει επί 4, και φτιάξτε έναν πίνακα με
τις τιμές του `i` και του `step` σε κάθε επανάληψη. Προσέξτε και την τιμή του `i`
μετά το τέλος του βρόχου.
