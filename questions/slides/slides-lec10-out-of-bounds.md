---
id: slides-lec10-out-of-bounds
kind: slides
title: "Πρόσβαση εκτός ορίων πίνακα"
source:
  title: "Διάλεξη 10, διαφάνεια 44"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec10.pdf
  years: [2025]
chapters: [10]
topics: [arrays, undefined-behavior]
difficulty: 1
type: short-answer
---

Για τον πίνακα `int bears[100];`, τι θα συμβεί αν προσπελάσω εκτός ορίων, π.χ.
`bears[100]` ή `bears[-1]`;

## Υπόδειξη

Ποιες είναι οι έγκυρες θέσεις; Σκεφτείτε αν η C ελέγχει τα όρια και πώς
κατατάσσει το standard αυτή τη χρήση.
