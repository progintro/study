---
id: kahoot-struct-uninitialized
kind: kahoot
title: "Δομή χωρίς αρχικοποίηση"
source:
  title: "Kahoot «Δομές + Αρχεία», «Ταξινόμηση και Δομές»"
  years: [2025]
chapters: [19, 13]
topics: [structs, memory-model, undefined-behavior]
difficulty: 1
type: multiple-choice
answer: "Ότι έτυχε να έχει η μνήμη σε εκείνη την θέση"
stats: {responses: 151, accuracy: 74}
---

Έστω `struct {int x; int y;} point;` (τοπική μεταβλητή). Ποια είναι η τιμή του `point.y`;

- 0xFFFFFFFF
- 0
- 1
- Ότι έτυχε να έχει η μνήμη σε εκείνη την θέση

## Υπόδειξη

Μια τοπική μεταβλητή χωρίς αρχικοποιητή δεν παίρνει καμία τιμή αυτόματα, είτε είναι `int` είτε δομή.
