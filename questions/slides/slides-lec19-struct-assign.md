---
id: slides-lec19-struct-assign
kind: slides
title: "Ανάθεση με δομές"
source:
  title: "Διάλεξη 19, διαφάνειες 29–30"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec19.pdf
  years: [2025]
chapters: [19]
topics: [structs, variables]
difficulty: 1
type: trace
---

Για να αντιγραφούν τα περιεχόμενα μιας δομής σε μια άλλη, χρησιμοποιούμε τον τελεστή
ανάθεσης. Τι θα τυπώσει αυτό το πρόγραμμα;

```c
#include <stdio.h>
struct point { int x;  int y; };
int main() {
  struct point pt1 = { 3, 4 };
  struct point pt2;
  printf("%d %d\n", pt2.x, pt2.y);
  pt2 = pt1;
  printf("%d %d\n", pt2.x, pt2.y);
  return 0;
}
```

## Υπόδειξη

Εξετάστε χωριστά τα δύο `printf`: τι περιέχει το `pt2` πριν από την ανάθεση, αφού
δεν αρχικοποιήθηκε; Και τι αντιγράφει η ανάθεση ανάμεσα σε δύο δομές ίδιου τύπου;
