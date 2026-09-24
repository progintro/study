---
id: kahoot-malloc-doubles
kind: kahoot
title: "Δέσμευση 10⁹ double"
source:
  title: "Kahoot «Δείκτες Παντού!» (διάλεξη 12) και «Μνήμη» (διάλεξη 13)"
  years: [2025]
chapters: [13]
topics: [dynamic-memory, types, memory-model]
difficulty: 2
type: multiple-choice
answer: "double * array = malloc(1000000000 * sizeof(double));"
stats: {responses: 215, accuracy: 66}
---

Θέλω να αποθηκεύσω 10⁹ στοιχεία `double`. Τι κάνω;

- `int * array = malloc(1000000000);`
- `double array[1000000000];`
- `double * array = malloc(1000000000);`
- `double * array = malloc(1000000000 * sizeof(double));`

## Υπόδειξη

Η `malloc` μετράει σε bytes, όχι σε στοιχεία· και θυμηθείτε πόσο χωράει η στοίβα.
