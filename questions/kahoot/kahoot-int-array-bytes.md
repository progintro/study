---
id: kahoot-int-array-bytes
kind: kahoot
title: "Μέγεθος πίνακα int"
source:
  title: "Kahoot «Πίνακες» (διάλεξη 10)"
  years: [2025]
chapters: [10, 2]
topics: [arrays, types, memory-model]
difficulty: 2
type: multiple-choice
answer: "Εξαρτάται"
stats: {responses: 249, accuracy: 49}
---

Ένας πίνακας `int numbers[1024];` πόσα bytes καταλαμβάνει στη μνήμη;

- `1024`
- `4096`
- `8192`
- Εξαρτάται

## Συχνή παρανόηση

Το 35% επέλεξε `4096`, θεωρώντας ότι ένας `int` είναι πάντα 4 bytes. Το πρότυπο της C δεν ορίζει το ακριβές μέγεθος του `int`· εξαρτάται από το σύστημα.

## Υπόδειξη

Το μέγεθος του πίνακα είναι πλήθος στοιχείων × μέγεθος στοιχείου· είναι το μέγεθος του `int` ίδιο παντού;
