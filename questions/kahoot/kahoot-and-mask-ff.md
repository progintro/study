---
id: kahoot-and-mask-ff
kind: kahoot
title: "0x42 & 0xFF"
source:
  title: "Kahoot «Git και Τελεστές» (διάλεξη 4)"
  years: [2025]
chapters: [4]
topics: [bitwise]
difficulty: 3
type: multiple-choice
answer: "0x42"
stats: {responses: 318, accuracy: 18}
---

Ποια η τιμή της παράστασης `0x42 & 0xFF`;

- `0xFF`
- `42`
- `0x42`
- `0`

## Συχνή παρανόηση

Το 30% απάντησε `0`, πιθανότατα επειδή μπέρδεψε το bitwise `&` με το λογικό `&&` ή υπέθεσε ότι το AND «σβήνει» τα bits· στην πραγματικότητα το AND με `0xFF` αφήνει το byte ανέπαφο.

## Υπόδειξη

Το `0xFF` είναι οκτώ άσοι στο δυαδικό. Τι αφήνει το bitwise AND με 1 σε κάθε bit του άλλου τελεστέου;
