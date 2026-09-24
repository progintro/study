---
id: slides-lec20-family-tree
kind: slides
title: "Γενεαλογικό δέντρο"
source:
  title: "Διάλεξη 20, διαφάνεια 43"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec20.pdf
  years: [2025]
chapters: [20,22]
topics: [trees, structs]
difficulty: 1
type: short-answer
---

Δίνεται η δομή:

```c
struct person {
  char name[128];
  struct person *parent1;
  struct person *parent2;
};
```

Με αυτήν φτιάχνουμε το γενεαλογικό δέντρο: ο Angel δείχνει στους Logan και River, ο
Logan στους Avery και Andie, ο River στους Hayden και Riley, κ.ο.κ. Μας θυμίζει κάτι;

## Υπόδειξη

Κάθε κόμβος έχει το πολύ δύο δείκτες προς άλλους κόμβους του ίδιου τύπου, και
υπάρχει ένας «πρώτος» κόμβος από τον οποίο ξεκινούν όλα. Ποια δομή δεδομένων έχει
αυτά τα χαρακτηριστικά;
