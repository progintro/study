---
id: kahoot-for-n-times-trap
kind: kahoot
title: "Πόσες φορές εκτελείται ένα for μέχρι N"
source:
  title: "Kahoot «Επίλυση Προβλημάτων» (διάλεξη 7), δύο εκδοχές"
  years: [2025]
chapters: [6]
topics: [loops]
difficulty: 3
type: multiple-choice
answer: "Εξαρτάται"
stats: {responses: 192, accuracy: 23}
---

Πόσες φορές θα τυπώσει `hello` αυτό το loop;

```c
for (int i = 0; i < N; i++)
    printf("hello\n");
```

- N
- N-1
- N+1
- Εξαρτάται

## Συχνή παρανόηση

Το 34% απάντησε N, υποθέτοντας σιωπηρά ότι το `N` είναι θετικό· αν το `N` είναι 0 ή αρνητικό, το σώμα δεν εκτελείται καθόλου.

## Υπόδειξη

Δεν ξέρουμε τίποτα για το `N`: δοκιμάστε νοερά τιμές όπως 5, 0 ή -3.
