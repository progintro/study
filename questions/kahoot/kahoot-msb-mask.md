---
id: kahoot-msb-mask
kind: kahoot
title: "Απομόνωση του πιο σημαντικού bit"
source:
  title: "Kahoot «Git και Τελεστές» (διάλεξη 4)"
  years: [2025]
chapters: [4, 5]
topics: [bitwise]
difficulty: 3
type: multiple-choice
answer: "byte & 0x80"
stats: {responses: 318, accuracy: 14}
---

Google backend engineer interview question: πώς απομονώνουμε το πιο σημαντικό bit (το 8ο) σε ένα byte;

- `byte & 0xFF`
- `byte & 0x80`
- `byte | 0xFF`
- `byte | 0x80`

## Συχνή παρανόηση

Το 29% διάλεξε `byte & 0xFF`: η μάσκα `0xFF` έχει και τα 8 bits στο 1, άρα κρατάει ολόκληρο το byte αντί να απομονώνει μόνο το πιο σημαντικό.

## Υπόδειξη

Γράψτε κάθε μάσκα στο δυαδικό. Για να κρατήσουμε ένα bit και να μηδενίσουμε τα υπόλοιπα, χρειαζόμαστε τον τελεστή που δίνει 1 μόνο όπου *και τα δύο* bits είναι 1, και μια μάσκα με ένα μόνο 1.
