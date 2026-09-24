---
id: kahoot-struct-padding-size
kind: kahoot
title: "Μέγεθος δομής και padding"
source:
  title: "Kahoot «Δομές + Αρχεία», «Ταξινόμηση και Δομές»"
  years: [2025]
chapters: [19]
topics: [structs, memory-model, types]
difficulty: 2
type: multiple-choice
answer: "Εξαρτάται"
stats: {responses: 151, accuracy: 52}
---

Ποιο είναι το μέγεθος του `struct {char c; int x; double d;}`;

- 1 + 4 + 8 = 13
- 1 + 8 + 8 = 17
- 4 + 4 + 8 = 16
- Εξαρτάται

## Συχνή παρανόηση

Το 24% επέλεξε `4 + 4 + 8 = 16`, την τιμή που δίνει συνήθως ένας 64-bit υπολογιστής· όμως το padding ανάμεσα στα πεδία και τα μεγέθη των τύπων δεν ορίζονται από το πρότυπο.

## Υπόδειξη

Θυμηθείτε ότι ο μεταγλωττιστής μπορεί να προσθέσει padding για τη στοίχιση των πεδίων, και ότι ούτε το `sizeof(int)` είναι ίδιο παντού.
