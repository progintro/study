---
id: kahoot-deref-increment
kind: kahoot
title: "Αύξηση μέσω δείκτη"
source:
  title: "Kahoot «Δείκτες και Αναδρομή» (διάλεξη 11) και «Δείκτες Παντού!» (διάλεξη 12)"
  years: [2025]
chapters: [11]
topics: [pointers, precedence]
difficulty: 3
type: multiple-choice
answer: "42"
stats: {responses: 232, accuracy: 34}
---

Τι θα τυπώσει ο παρακάτω κώδικας;

```c
int x = 41;
int *ptr = &x;
(*ptr)++;
printf("%d", *ptr);
```

- `41`
- `42`
- `43`
- Που να ξέρω

## Υπόδειξη

Οι παρενθέσεις ορίζουν σε τι εφαρμόζεται το `++`: στον ίδιο τον δείκτη ή σε αυτό που δείχνει;
