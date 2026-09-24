---
id: kahoot-pointer-increment-scalar
kind: kahoot
title: "Αύξηση του ίδιου του δείκτη"
source:
  title: "Kahoot «Δείκτες και Αναδρομή» (διάλεξη 11) και «Δείκτες Παντού!» (διάλεξη 12)"
  years: [2025]
chapters: [11]
topics: [pointers, pointer-arithmetic, undefined-behavior]
difficulty: 3
type: multiple-choice
answer: "Που να ξέρω"
stats: {responses: 232, accuracy: 37}
---

Τι θα τυπώσει ο παρακάτω κώδικας;

```c
int x = 41;
int *ptr = &x;
ptr++;
printf("%d", *ptr);
```

- `41`
- `42`
- `43`
- Που να ξέρω

## Συχνή παρανόηση

Το 25% επέλεξε `42`, θεωρώντας ότι το `ptr++` αυξάνει την τιμή του `x`. Στην πραγματικότητα αλλάζει τη διεύθυνση που κρατά ο δείκτης, όχι την τιμή στην οποία δείχνει.

## Υπόδειξη

Μετά το `ptr++` πού δείχνει ο `ptr`; Υπάρχει εκεί κάποια μεταβλητή που ξέρουμε;
