---
id: kahoot-qsort-compare-ascending
kind: kahoot
title: "Συνάρτηση σύγκρισης για αύξουσα ταξινόμηση"
source:
  title: "Kahoot «Ταξινόμηση και Δομές»"
  years: [2025]
chapters: [18, 17, 19]
topics: [sorting, structs, function-pointers]
difficulty: 3
type: multiple-choice
answer: "int comp(... s1, ... s2) { return s1.grade - s2.grade; }"
stats: {responses: 127, accuracy: 12}
---

Θέλω να ταξινομήσω σε αύξουσα σειρά βαθμολογίας τον πίνακα `struct student[1024]`. Χρησιμοποιώ τη συνάρτηση σύγκρισης:

- `int comp(... s1, ... s2) { return s1.grade - s2.grade; }`
- `int comp(... s1, ... s2) { return s2.grade - s1.grade; }`
- `int comp(... s1, ... s2) { return s1.grade == s2.grade; }`
- `int comp(... s1, ... s2) { return s1.grade ^ s2.grade; }`

## Συχνή παρανόηση

Το 43% επέλεξε `s2.grade - s1.grade`, αντιστρέφοντας τη σύμβαση: αρνητική τιμή σημαίνει ότι το `s1` μπαίνει πρώτο, οπότε η αφαίρεση `s2 - s1` δίνει φθίνουσα σειρά. Οι επιλογές με `==` και `^` (20% η καθεμία) δεν δίνουν καν πρόσημο που να λέει ποιο στοιχείο προηγείται.

## Υπόδειξη

Η συνάρτηση σύγκρισης της `qsort` επιστρέφει αρνητικό, μηδέν ή θετικό· σκεφτείτε ποιο πρόσημο σημαίνει «το πρώτο όρισμα πάει πριν από το δεύτερο» και δοκιμάστε με δύο βαθμούς, π.χ. 5 και 8.
