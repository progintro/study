---
id: kahoot-pointer-plus-int-hex
kind: kahoot
title: "Δείκτης συν 4 σε δεκαεξαδικό"
source:
  title: "Kahoot «Δείκτες και Αναδρομή» (διάλεξη 11)"
  years: [2025]
chapters: [11, 2]
topics: [pointer-arithmetic, pointers]
difficulty: 3
type: multiple-choice
answer: "0x52"
stats: {responses: 152, accuracy: 31}
---

Έστω ότι `sizeof(int) == 4` και η τιμή του `int *ptr` είναι `0x42`. Ποια η τιμή της έκφρασης `ptr + 4`;

- `0x46`
- `42`
- `0x52`
- `0x4C`

## Συχνή παρανόηση

Το 32% επέλεξε `0x4C` και το 22% `0x46`. Οι δεύτεροι ξέχασαν ότι το `+ 4` σημαίνει 4 × `sizeof(int)` bytes, ενώ οι πρώτοι πρόσθεσαν σωστά 16 bytes, αλλά μπέρδεψαν τη δεκαεξαδική πρόσθεση (16 = `0x10`).

## Υπόδειξη

Η αριθμητική δεικτών μετράει σε στοιχεία, όχι σε bytes· προσέξτε και σε ποια βάση κάνετε την πρόσθεση.
