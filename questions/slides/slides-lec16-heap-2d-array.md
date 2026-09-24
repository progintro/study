---
id: slides-lec16-heap-2d-array
kind: slides
title: "Δισδιάστατος πίνακας στον σωρό"
source:
  title: "Διάλεξη 16, διαφάνεια 25"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec16.pdf
  years: [2025]
chapters: [16, 13]
topics: [dynamic-memory, multidim-arrays, pointers]
difficulty: 2
type: programming
---

Θέλω να δημιουργήσω έναν δισδιάστατο πίνακα στον σωρό. Πώς μπορώ να το κάνω αυτό;

## Υπόδειξη

Δύο δρόμοι: ένας πίνακας από pointers γραμμών, όπου κάθε γραμμή έχει τη δική της
`malloc`, ή ένα ενιαίο μπλοκ για όλα τα στοιχεία, όπου υπολογίζετε μόνοι σας τη θέση
του στοιχείου `[i][j]`. Μην ξεχάσετε τον έλεγχο για `NULL` και τη σωστή σειρά των
`free`.
