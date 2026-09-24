---
id: slides-lec04-msb
kind: slides
title: "Απομόνωση του πιο σημαντικού bit"
source:
  title: "Διάλεξη 4: Git και Τελεστές, διαφάνεια 29"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec04.pdf
  years: [2025]
chapters: [4]
topics: [bitwise]
difficulty: 1
type: multiple-choice
---

Πως απομονώνουμε το πιο σημαντικό bit σε ένα byte;

- A. `byte & 0xFF`
- B. `byte & 0x80`
- C. `byte | 0xFF`
- D. `byte | 0x80`

## Υπόδειξη

Γράψτε τις σταθερές `0xFF` και `0x80` σε δυαδικό. «Απομονώνω» σημαίνει ότι όλα τα
άλλα bit γίνονται 0 και μένει μόνο το bit που θέλουμε: ποιος τελεστής, `&` ή `|`,
μπορεί να μηδενίσει bit;
