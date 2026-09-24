---
id: slides-lec15-getchar-count
kind: slides
title: "Τι κάνει το πρόγραμμα με την getchar"
source:
  title: "Διάλεξη 15, διαφάνεια 17"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec15.pdf
  years: [2025]
chapters: [15, 9]
topics: [complexity, input-output, loops]
difficulty: 1
type: trace
---

Διαδοχικές κλήσεις της `getchar()` διαβάζουν διαδοχικούς χαρακτήρες. Τι κάνει το
παρακάτω πρόγραμμα; Τι χρονική και τι χωρική πολυπλοκότητα έχει;

```c
#include <stdio.h>

int main() {
  int ch, sum = 0;
  printf("Enter characters: ");
  while( (ch = getchar()) != '\n' && ch != EOF ) {
    printf("%c", ch);
    sum++;
  }
  printf("\nTotal characters: %d\n", sum);
  return 0;
}
```

## Υπόδειξη

Ακολουθήστε τον βρόχο για την είσοδο `hello` και Enter: πότε σταματά και τι τυπώνεται
σε κάθε επανάληψη; Για τον χώρο, ρωτήστε αν το πρόγραμμα κρατά κάπου όλη τη γραμμή.
