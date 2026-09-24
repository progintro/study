---
id: slides-lec06-do-while
kind: slides
title: "Τι τυπώνει η do-while"
source:
  title: "Διάλεξη 6: Εντολές και Ροή Ελέγχου, διαφάνεια 26"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec06.pdf
  years: [2025]
chapters: [6]
topics: [loops]
difficulty: 1
type: trace
---

Τι κάνει το παρακάτω πρόγραμμα;

```c
i = 0;
do
   i++;
while (i < 42);
printf("%d\n", i);
```

## Υπόδειξη

Η `do-while` εκτελεί πρώτα το σώμα και μετά ελέγχει τη συνθήκη. Ποια είναι η πρώτη τιμή του `i` για την οποία ο έλεγχος αποτυγχάνει;
