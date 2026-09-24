---
id: exam-2025-sep-q2
kind: exam
title: "Η συνάρτηση transform"
source:
  title: "Εξέταση Σεπτεμβρίου 2025, Θέμα 2"
  url: https://progintro.github.io/exams/2025/progintro-exam-sep-25.pdf
  years: [2025]
chapters: [14, 12]
topics: [strings, pointer-arithmetic, pointers]
difficulty: 1
type: trace
---

**Η συνάρτηση transform (15 Μονάδες)**

```c
char *transform(char * str) {
    int length = strlen(str);
    char * lo = str;
    char * hi = str + length - 1;
    char tmp;
    while (lo < hi) {
      tmp = *lo;
      *lo++ = *hi;
      *hi-- = tmp;
    }
    return str;
}
```

Τι κάνει η συνάρτηση transform (μέχρι 15 λέξεις εξήγηση); Τι θα τυπωθεί κατά την εκτέλεση
των δύο ακόλουθων εντολών;

```c
    char arg[] = {'!', 121, 107, 99, 117, 76, 0};
    printf("%s\n", transform(arg));
```

> Σημείωση: στο τέλος της εξέτασης δίνεται πίνακας ASCII ως βοήθημα.

## Υπόδειξη

Παρακολουθήστε πώς κινούνται οι δείκτες `lo` και `hi` και τι ανταλλάσσουν σε κάθε
επανάληψη, και πότε σταματά ο βρόχος. Για την έξοδο, μετατρέψτε πρώτα κάθε αριθμό του
`arg` σε χαρακτήρα με τον πίνακα ASCII· το `0` στο τέλος είναι ο τερματικός χαρακτήρας.
