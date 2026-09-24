---
id: kahoot-stderr-fd
kind: kahoot
title: "Ο file descriptor του stderr"
source:
  title: "Kahoot «Δομές + Αρχεία», «Δυαδική Αναζήτηση και Ταξινόμηση» (διάλεξη 17)"
  years: [2025]
chapters: [18]
topics: [files, redirection, input-output]
difficulty: 2
type: multiple-choice
answer: "2"
stats: {responses: 95, accuracy: 51}
---

Το `stderr` έχει συνήθως file descriptor με αριθμό:

- 0
- 1
- 2
- 3

## Συχνή παρανόηση

Το 29% επέλεξε `1`, που είναι ο αριθμός του `stdout`· τα τρία πρότυπα ρεύματα έχουν τους πρώτους αριθμούς με τη σειρά `stdin`, `stdout`, `stderr`.

## Υπόδειξη

Θυμηθείτε τη σειρά των τριών ρευμάτων που ανοίγουν αυτόματα και ότι η αρίθμηση ξεκινάει από το 0 (σκεφτείτε και το `2>` του shell).
