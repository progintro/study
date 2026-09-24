---
id: kahoot-little-endian-read
kind: kahoot
title: "Ανάγνωση int σε little endian"
source:
  title: "Kahoot «Δομές + Αρχεία»"
  years: [2025]
chapters: [18, 2]
topics: [files, integer-representation]
difficulty: 2
type: multiple-choice
answer: "0xbeefcafe"
stats: {responses: 24, accuracy: 62}
---

Το αρχείο `input.txt` περιέχει τα bytes `0xfe 0xca 0xef 0xbe`. Αν διαβάσουμε έναν `int` σε μορφή little endian, θα πάρουμε:

- 0xfecaefbe
- 0xefbefeca
- 0xbeefcafe
- 0xcafebeef

## Υπόδειξη

Στο little endian το πρώτο byte στη μνήμη (ή στο αρχείο) είναι το λιγότερο σημαντικό byte του αριθμού.
