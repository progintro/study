---
id: kahoot-variable-increment-via-ptr
kind: kahoot
title: "Αλλαγή μεταβλητής και δείκτης"
source:
  title: "Kahoot «Δείκτες και Αναδρομή» (διάλεξη 11)"
  years: [2025]
chapters: [11]
topics: [pointers, variables]
difficulty: 2
type: multiple-choice
answer: "42"
stats: {responses: 152, accuracy: 48}
---

Τι θα τυπώσει ο παρακάτω κώδικας;

```c
int x = 41;
int *ptr = &x;
x++;
printf("%d", *ptr);
```

- `41`
- `42`
- `43`
- Που να ξέρω

## Υπόδειξη

Ο δείκτης δεν κρατά αντίγραφο της τιμής του `x` αλλά τη διεύθυνσή του.
