---
id: kahoot-sizeof-row
kind: kahoot
title: "sizeof μιας γραμμής"
source:
  title: "Kahoot «Πίνακες και Δείκτες» (διάλεξη 12)"
  years: [2025]
chapters: [12]
topics: [multidim-arrays, types]
difficulty: 2
type: multiple-choice
answer: "10"
stats: {responses: 141, accuracy: 42}
---

Έστω `sizeof(char) == 1` και πίνακας `char map[10][10]`. Πόσο είναι το `sizeof(map[5])`;

- `1`
- `10`
- `100`
- Εξαρτάται

## Συχνή παρανόηση

Το 26% επέλεξε `1`, θεωρώντας ότι το `map[5]` είναι ένας χαρακτήρας. Στην πραγματικότητα το `map[5]` είναι ολόκληρη η 6η γραμμή, ένας πίνακας 10 `char`.

## Υπόδειξη

Με έναν μόνο δείκτη σε δισδιάστατο πίνακα, τι παίρνουμε: ένα στοιχείο ή μια ολόκληρη γραμμή;
