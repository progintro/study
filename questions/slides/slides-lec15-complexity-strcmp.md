---
id: slides-lec15-complexity-strcmp
kind: slides
title: "Πολυπλοκότητα της strcmp"
source:
  title: "Διάλεξη 15, διαφάνεια 31"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec15.pdf
  years: [2025]
chapters: [15, 14]
topics: [complexity, strings, pointers]
difficulty: 2
type: short-answer
---

Η συνάρτηση strcmp. Μια πιθανή υλοποίηση:

```c
int strcmp(char * str1, char * str2) {
  while(*str1 && (*str1 == *str2)) {
    str1++;
    str2++;
  }
  return *str1 - *str2;
}
```

Τι πολυπλοκότητας είναι η συνάρτηση strcmp ως προς το μέγεθος των συμβολοσειρών
(έστω n και m);

## Υπόδειξη

Βρείτε όλους τους λόγους για τους οποίους σταματά ο βρόχος. Ποια είναι η χειρότερη
περίπτωση, και ποιο από τα δύο μήκη την περιορίζει;
