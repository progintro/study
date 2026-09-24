---
id: kahoot-count-set-bits
kind: kahoot
title: "Πολυπλοκότητα μέτρησης bit"
source:
  title: "Kahoot «Πολυπλοκότητα και άλλα» (διάλεξη 15)"
  years: [2025]
chapters: [15, 5]
topics: [complexity, bitwise]
difficulty: 2
type: multiple-choice
answer: "O(log n)"
stats: {responses: 124, accuracy: 43}
---

Μια συνάρτηση παίρνει έναν αριθμό n και επιστρέφει πόσα bit είναι 1. Πόσο γρήγορη μπορώ να κάνω αυτήν τη συνάρτηση;

- O(n³)
- O(n²)
- O(n)
- O(f(x))
- O(log n)

## Συχνή παρανόηση

Το 32% επέλεξε O(n), μπερδεύοντας την τιμή του n με το πλήθος των bit του, που είναι περίπου $\log_2 n$.

## Υπόδειξη

Πόσα bit χρειάζονται για να γράψετε τον αριθμό n στο δυαδικό;
