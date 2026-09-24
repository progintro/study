---
id: slides-lec14-str-plus-plus
kind: slides
title: "Η έκφραση *str++"
source:
  title: "Διάλεξη 14, διαφάνεια 34"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec14.pdf
  years: [2025]
chapters: [14, 5]
topics: [pointers, pointer-arithmetic, precedence]
difficulty: 2
type: short-answer
---

Η υλοποίηση της `strlen` στις διαφάνειες είναι:

```c
size_t strlen(char * str) {
  size_t length = 0;
  while(*str++) length++;
  return length;
}
```

Πώς αποτιμάται η έκφραση `*str++`;

- Έχει διαφορά από την έκφραση `(*str)++`;
- Έχει διαφορά από την έκφραση `*(str++)`;
- Τελικά έχει σημασία η προτεραιότητα τελεστών / χρήση παρενθέσεων;

## Υπόδειξη

Βρείτε στον πίνακα προτεραιότητας ποιος τελεστής δένει πιο σφιχτά, ο μεταθεματικός
`++` ή το μοναδιαίο `*`. Για κάθε έκφραση απαντήστε σε δύο ερωτήσεις: ποια τιμή
δίνει, και τι αλλάζει στη μνήμη, ο δείκτης ή ο χαρακτήρας όπου δείχνει;
