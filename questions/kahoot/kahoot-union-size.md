---
id: kahoot-union-size
kind: kahoot
title: "Μέγεθος ένωσης"
source:
  title: "Kahoot «Προχωρημένες Δομές» (διάλεξη 20), «Προχωρημένες Δομές #2»"
  years: [2025]
chapters: [20]
topics: [unions-enums, memory-model]
difficulty: 3
type: multiple-choice
answer: "max(sizeof(x), sizeof(name), sizeof(double))"
stats: {responses: 164, accuracy: 36}
---

Έστω `union station {int x; char name[20]; double d;};`. Ποιο είναι το `sizeof(union station)`;

- sizeof(double)
- sizeof(int) + sizeof(name) + sizeof(double)
- max(sizeof(x), sizeof(name), sizeof(double))
- 42

## Συχνή παρανόηση

Το 22% επέλεξε `sizeof(double)`, θεωρώντας τον `double` το μεγαλύτερο πεδίο, ενώ ο πίνακας `name` πιάνει 20 bytes· και το 18% πρόσθεσε τα μεγέθη, όπως σε μια δομή.

## Υπόδειξη

Σε μια ένωση όλα τα πεδία ξεκινούν από την ίδια διεύθυνση· πόσος χώρος χρειάζεται ώστε να χωράει οποιοδήποτε από αυτά;
