---
id: slides-lec05-cast-division
kind: slides
title: "Cast και διαίρεση: (double)3/4"
source:
  title: "Διάλεξη 5: Τελεστές και Εντολές, διαφάνεια 14"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec05.pdf
  years: [2025]
chapters: [5]
topics: [operators, types, precedence]
difficulty: 1
type: trace
---

Ο τελεστής μετατροπής αλλάζει τον τύπο ενός τελεστέου, με γενική μορφή
`(τύπος)τελεστέος`. Για παράδειγμα:

```text
(int)42.67   επιστρέφει 42
(char)67.8   επιστρέφει 'C'
(double)3    επιστρέφει 3.0
(double)3/4  επιστρέφει ??
```

Τι επιστρέφει το `(double)3/4`;

## Υπόδειξη

Αποφασίστε πρώτα τι εφαρμόζεται πρώτο, το cast ή η διαίρεση (δείτε τον πίνακα
προτεραιότητας). Μετά σκεφτείτε τι γίνεται σε μια διαίρεση όπου ο ένας τελεστέος είναι
`double` και ο άλλος `int`. Συγκρίνετε με το `(double)(3/4)`.
