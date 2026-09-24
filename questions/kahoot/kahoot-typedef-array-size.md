---
id: kahoot-typedef-array-size
kind: kahoot
title: "sizeof ενός typedef πίνακα"
source:
  title: "Kahoot «Δομές + Αρχεία», «Ταξινόμηση και Δομές»"
  years: [2025]
chapters: [19, 10]
topics: [structs, types, arrays]
difficulty: 2
type: multiple-choice
answer: "8192"
stats: {responses: 151, accuracy: 66}
---

Έστω `typedef double trouble[1024];` και `sizeof(double) == 8`. Ποιο είναι το `sizeof(trouble)`;

- 1024
- 4096
- 8192
- Εξαρτάται

## Συχνή παρανόηση

Το 24% επέλεξε «Εξαρτάται», ενώ το `typedef` απλώς δίνει όνομα στον τύπο «πίνακας 1024 `double`», που έχει σταθερό μέγεθος.

## Υπόδειξη

Το `typedef` δεν φτιάχνει μεταβλητή, μόνο ένα συνώνυμο για τον τύπο· ποιος είναι αυτός ο τύπος και πόσα bytes πιάνει;
