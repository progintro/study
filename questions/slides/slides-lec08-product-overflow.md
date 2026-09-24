---
id: slides-lec08-product-overflow
kind: slides
title: "Αρνητικό γινόμενο σε βρόχο"
source:
  title: "Διάλεξη 8: Ροή Ελέγχου #2, διαφάνεια 2"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec08.pdf
  years: [2025]
chapters: [8, 2]
topics: [integer-representation, loops]
difficulty: 1
type: debug
---

Έτρεξα τον παρακάτω πολλαπλασιασμό:

```c
for(prod = 1, i = 105 ; i <= 999 ; i += 14) {
    prod *= i;
}
```

και μου τύπωσε το παρακάτω. Τι συμβαίνει;

```text
$ ./prod
-1187656959
```

## Υπόδειξη

Πόσους παράγοντες πολλαπλασιάζει ο βρόχος και πόσο μεγάλο είναι περίπου το σωστό
γινόμενο; Συγκρίνετέ το με τη μέγιστη τιμή που χωράει σε έναν `int` των 32 bit.
