---
id: slides-lec12-pointer-copy-loop
kind: slides
title: "Περιεχόμενα του x μετά από βρόχο με δείκτη"
source:
  title: "Διάλεξη 12, διαφάνεια 25"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec12.pdf
  years: [2025]
chapters: [12, 11]
topics: [pointer-arithmetic, pointers, arrays]
difficulty: 2
type: trace
---

Ποια είναι τα περιεχόμενα του `x` μετά την εκτέλεση;

```c
int * p;
int x[] = {5, 7, 2, 3, 6, 0, 1, 4};
p = x;
while (*p = *(p+2))
  p++;
```

## Υπόδειξη

Η συνθήκη του `while` είναι ανάθεση, όχι σύγκριση: αντιγράφει στο `*p` την τιμή
δύο θέσεις πιο μετά, και ο βρόχος σταματά όταν η τιμή που αντιγράφηκε είναι 0.
Ιχνηλατήστε βήμα-βήμα σε πίνακα τη θέση του `p` και τα περιεχόμενα του `x`,
θυμίζοντας στον εαυτό σας ότι ο πίνακας αλλάζει καθώς προχωρά ο βρόχος.
