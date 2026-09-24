---
id: slides-lec04-cast-division
kind: slides
title: "Τι επιστρέφει το (double)3/4;"
source:
  title: "Διάλεξη 4: Git και Τελεστές, διαφάνεια 32"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec04.pdf
  years: [2025]
chapters: [4]
topics: [operators, types, precedence]
difficulty: 2
type: trace
---

Ο τελεστής μετατροπής αλλάζει τον τύπο ενός τελεστέου. Γενική μορφή: `(τύπος)τελεστέος`.

Παραδείγματα:

- `(int)42.67` επιστρέφει `42`
- `(char)67.8` επιστρέφει `'C'`
- `(double)3` επιστρέφει `3.0`
- `(double)3/4` επιστρέφει ??

## Υπόδειξη

Βρείτε στον πίνακα προτεραιότητας ποιος εφαρμόζεται πρώτα, το cast ή η διαίρεση. Μετά
σκεφτείτε τι τύπου είναι οι δύο τελεστέοι της διαίρεσης και τι κάνει η σιωπηρή
μετατροπή τύπων. Συγκρίνετε με το `(double)(3/4)`.
