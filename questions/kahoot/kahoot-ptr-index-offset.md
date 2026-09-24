---
id: kahoot-ptr-index-offset
kind: kahoot
title: "Δείκτης στη μέση πίνακα"
source:
  title: "Kahoot «Δείκτες και Αναδρομή» (διάλεξη 11) και «Δείκτες Παντού!» (διάλεξη 12)"
  years: [2025]
chapters: [11, 10]
topics: [pointers, pointer-arithmetic, arrays]
difficulty: 3
type: short-answer
answer: "30"
stats: {responses: 232, accuracy: 12}
---

Τι θα τυπώσει ο παρακάτω κώδικας;

```c
int a[] = {10, 20, 30, 40};
int *ptr = &a[1];
printf("%d", ptr[1]);
```

Γράψτε την απάντηση.

## Υπόδειξη

Το `ptr[n]` σημαίνει `*(ptr + n)`, και μετράει από εκεί που δείχνει ο `ptr`, όχι από την αρχή του πίνακα.
