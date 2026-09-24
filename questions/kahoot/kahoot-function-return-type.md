---
id: kahoot-function-return-type
kind: kahoot
title: "Ο τύπος επιστροφής μιας συνάρτησης"
source:
  title: "Kahoot «Τύπωμα και Συναρτήσεις» (διάλεξη 3)"
  years: [2025]
chapters: [3]
topics: [functions, types]
difficulty: 3
type: multiple-choice
answer: "double"
stats: {responses: 190, accuracy: 28}
---

Ποιος ο τύπος επιστροφής της συνάρτησης:

```c
double square(int x) { return x * x; }
```

- square
- double
- int
- x

## Συχνή παρανόηση

Το 25% επέλεξε `int`, μπερδεύοντας τον τύπο της παραμέτρου `x` με τον τύπο επιστροφής· η τιμή του `x * x` μετατρέπεται σε `double` κατά την επιστροφή.

## Υπόδειξη

Ο τύπος επιστροφής γράφεται πριν από το όνομα της συνάρτησης· ό,τι βρίσκεται μέσα στις παρενθέσεις αφορά τις παραμέτρους.
