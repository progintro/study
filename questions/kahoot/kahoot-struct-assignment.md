---
id: kahoot-struct-assignment
kind: kahoot
title: "Ανάθεση δομών"
source:
  title: "Kahoot «Δομές + Αρχεία», «Ταξινόμηση και Δομές»"
  years: [2025]
chapters: [19]
topics: [structs, operators]
difficulty: 2
type: multiple-choice
answer: "1"
stats: {responses: 151, accuracy: 49}
---

Έστω `struct {int x;} cafe = {1}, bar = {2}; bar = cafe;`. Η παράσταση `bar.x` αποτιμάται σε:

- 1
- 2
- Δεν αποτιμάται
- 42

## Συχνή παρανόηση

Το 28% επέλεξε `2`, σαν η ανάθεση `bar = cafe` να μην άλλαζε τα πεδία της `bar`· στην πραγματικότητα η ανάθεση δομών αντιγράφει όλα τα πεδία.

## Υπόδειξη

Αναρωτηθείτε αν ο τελεστής `=` επιτρέπεται ανάμεσα σε δύο δομές του ίδιου τύπου και τι αντιγράφει.
