---
id: slides-lec06-while-sum
kind: slides
title: "Άθροισμα με while"
source:
  title: "Διάλεξη 6: Εντολές και Ροή Ελέγχου, διαφάνεια 19"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec06.pdf
  years: [2025]
chapters: [6]
topics: [loops]
difficulty: 1
type: trace
---

Τι κάνει το παρακάτω πρόγραμμα;

```c
int i = 0;
int sum = 0;
while (i < 42) {
  sum += i;
  i++;
}
printf("%d %d\n", i, sum);
```

## Υπόδειξη

Ποια είναι η πρώτη τιμή του `i` για την οποία η συνθήκη είναι ψευδής; Ποιες τιμές έχουν προστεθεί στο `sum` μέχρι τότε; Ο τύπος για το άθροισμα $1 + 2 + \dots + n$ θα σας γλιτώσει από τις πράξεις.
