---
id: slides-lec13-after-free
kind: slides
title: "Τι γίνεται μετά την free;"
source:
  title: "Διάλεξη 13, διαφάνειες 47–51"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec13.pdf
  years: [2025]
chapters: [13]
topics: [dynamic-memory, undefined-behavior]
difficulty: 1
type: short-answer
---

Μάθαμε να δεσμεύουμε μνήμη με την `malloc`: μας λείπει κάτι;

```c
int * array = malloc(4 * sizeof(int));
if (!array) {
  // fail gracefully
}
free(array);
```

1. Τι θα συμβεί στη μνήμη (στη στοίβα και στον σωρό) μετά την `free`;
2. Τι θα συμβεί αν προσπαθήσουμε να προσπελάσουμε μνήμη που έχουμε αποδεσμεύσει,
   π.χ. με `array[0] = 4;` μετά την `free`;
3. Τι θα συμβεί αν προσπαθήσουμε να αποδεσμεύσουμε μνήμη που έχουμε ήδη αποδεσμεύσει,
   δηλαδή με δεύτερο `free(array);`;

## Υπόδειξη

Ξεχωρίστε τον pointer `array` (που ζει στη στοίβα) από το μπλοκ στο οποίο δείχνει
(στον σωρό): ποιο από τα δύο αλλάζει η `free`; Για τα 2 και 3, σκεφτείτε τι
σημαίνει να χρησιμοποιούμε μνήμη που δεν μας ανήκει πια, στην καλύτερη και στη
χειρότερη περίπτωση.
