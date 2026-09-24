---
id: slides-lec15-complexity-malloc
kind: slides
title: "Πολυπλοκότητα δυναμικού πίνακα με malloc"
source:
  title: "Διάλεξη 15, διαφάνεια 19"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec15.pdf
  years: [2025]
chapters: [15, 12]
topics: [complexity, dynamic-memory, arrays]
difficulty: 1
type: short-answer
---

Με την βοήθεια των δεικτών, μπορούμε να χρησιμοποιήσουμε δυναμικούς πίνακες, πίνακες
των οποίων το μέγεθος καθορίζεται δυναμικά, δηλαδή την στιγμή που τρέχει το
πρόγραμμα. Παράδειγμα:

```c
int * array = malloc(N * sizeof(int));
for(int i = 0 ; i < N ; i++)
  array[i] = i * i;
```

Τι χρονική και τι χωρική πολυπλοκότητα έχει ο κώδικας ως προς το `N`;

## Υπόδειξη

Ο χρόνος και ο χώρος δεν έχουν πάντα την ίδια πολυπλοκότητα. Εδώ αναρωτηθείτε πόση
μνήμη ζητά η `malloc` συναρτήσει του `N`.
