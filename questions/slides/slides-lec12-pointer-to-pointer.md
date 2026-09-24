---
id: slides-lec12-pointer-to-pointer
kind: slides
title: "Δείκτης σε δείκτη"
source:
  title: "Διάλεξη 12, διαφάνεια 27"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec12.pdf
  years: [2025]
chapters: [12]
topics: [pointers, memory-model]
difficulty: 1
type: trace
---

Τι θα τυπώσει το παρακάτω;

```c
int x = 42;
int * ptr = &x;
int ** ptr2 = &ptr;
printf("%p %d", *ptr2, **ptr2);
```

Στη διαφάνεια η μνήμη σχεδιάζεται ως εξής: το `x` βρίσκεται στη διεύθυνση 100 με
τιμή 42, ο `ptr` στη διεύθυνση 200 με τιμή 100, και ο `ptr2` στη διεύθυνση 400 με
τιμή 200.

## Υπόδειξη

Κάθε `*` «ακολουθεί ένα βέλος»: ξεκινήστε από την τιμή του `ptr2` και βρείτε τι
υπάρχει στη διεύθυνση όπου δείχνει, μία φορά για το `*ptr2` και δύο φορές για το
`**ptr2`. Σκεφτείτε επίσης σε τι μορφή τυπώνει το `%p`.
