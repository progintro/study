---
id: kahoot-char-array-address
kind: kahoot
title: "Διεύθυνση στοιχείου πίνακα char"
source:
  title: "Kahoot «Πίνακες» (διάλεξη 10)"
  years: [2025]
chapters: [10]
topics: [arrays, memory-model]
difficulty: 3
type: multiple-choice
answer: "1042"
stats: {responses: 249, accuracy: 19}
---

Αν ο πίνακας `char array[100];` ξεκινάει στη διεύθυνση 1000, σε ποια διεύθυνση βρίσκεται το στοιχείο `array[42]`;

- `1000`
- `1042`
- `1041`
- `1043`

## Συχνή παρανόηση

Το 52% επέλεξε `1041`, μετρώντας τις θέσεις σαν να ξεκινούσαν από το 1. Αφού το `array[0]` είναι στο 1000 και κάθε `char` πιάνει 1 byte, το `array[i]` είναι στο 1000 + i.

## Υπόδειξη

Ποια είναι η διεύθυνση του `array[0]`, και πόσα bytes πιάνει κάθε `char`;
