---
id: slides-lec21-expression-traversal
kind: slides
title: "Διάσχιση για αποτιμητή εκφράσεων"
source:
  title: "Διάλεξη 21, διαφάνεια 51"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec21.pdf
  years: [2025]
chapters: [21]
topics: [trees, recursion]
difficulty: 2
type: short-answer
---

Θέλω να γράψω έναν αποτιμητή εκφράσεων (calculator / evaluator / interpreter). Ποια διάσχιση θα χρησιμοποιήσω;

```text
        +
       / \
      *   1
     / \
    2   9
```

## Υπόδειξη

Για να εφαρμόσει τον τελεστή ενός κόμβου (π.χ. το `*`), τι πρέπει να ξέρει ήδη ο αποτιμητής; Ποια από τις τρεις διασχίσεις (pre-order, in-order, post-order) εγγυάται ότι έχουν επεξεργαστεί πρώτα τα παιδιά;
