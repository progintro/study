---
id: slides-lec06-expression-statements
kind: slides
title: "Τιμές μετά από εντολές έκφρασης"
source:
  title: "Διάλεξη 6: Εντολές και Ροή Ελέγχου, διαφάνεια 7"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec06.pdf
  years: [2025]
chapters: [6, 5]
topics: [statements, operators]
difficulty: 1
type: trace
---

Ποια η τιμή των `x`, `y`, `z` μετά την εκτέλεση αυτών των εντολών έκφρασης;

```c
x = 4;
y = 7;
z = ++y;
y = z - (x++);
z = x - (--y);
```

## Υπόδειξη

Φτιάξτε έναν πίνακα με μία στήλη για κάθε μεταβλητή και μία γραμμή για κάθε εντολή. Θυμηθείτε ότι το `++y` αλλάζει πρώτα τη μεταβλητή και δίνει τη νέα τιμή, ενώ το `x++` δίνει την παλιά τιμή και αλλάζει τη μεταβλητή μετά.
