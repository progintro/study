---
id: kahoot-2d-element-address
kind: kahoot
title: "Διεύθυνση στοιχείου δισδιάστατου πίνακα"
source:
  title: "Kahoot «Πίνακες και Δείκτες» (διάλεξη 12)"
  years: [2025]
chapters: [12]
topics: [multidim-arrays, memory-model]
difficulty: 3
type: multiple-choice
answer: "320"
stats: {responses: 141, accuracy: 33}
---

Έστω ότι η διεύθυνση του `int array[10][10]` είναι 100 και `sizeof(int) == 4`. Η διεύθυνση του `array[5][5]` είναι:

- `320`
- `145`
- `155`
- Εξαρτάται

## Συχνή παρανόηση

Το 29% επέλεξε `155`: μέτρησαν σωστά ότι προηγούνται 55 στοιχεία, αλλά ξέχασαν να τα πολλαπλασιάσουν με `sizeof(int)` για να τα κάνουν bytes.

## Υπόδειξη

Ο πίνακας αποθηκεύεται κατά γραμμές: πόσα στοιχεία προηγούνται του `array[5][5]`, και πόσα bytes είναι το καθένα;
