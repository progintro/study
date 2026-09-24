---
id: slides-lec09-charcount
kind: slides
title: "Μετρητής χαρακτήρων με getchar"
source:
  title: "Διάλεξη 9: Δεδομένα Εισόδου, διαφάνεια 20"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec09.pdf
  years: [2025]
chapters: [9]
topics: [input-output, loops]
difficulty: 1
type: trace
---

Διαδοχικές κλήσεις της `getchar()` διαβάζουν διαδοχικούς χαρακτήρες. Τι κάνει το παρακάτω πρόγραμμα;

```c
#include <stdio.h>
int main() {
  int ch, sum = 0;
  printf("Enter characters: ");
  while( (ch = getchar()) != EOF ) {
    printf("%c", ch);
    sum++;
  }
  printf("\nTotal characters: %d\n", sum);
  return 0;
}
```

## Υπόδειξη

Ακολουθήστε τον βρόχο για μια μικρή είσοδο, π.χ. `hi` και Enter, και μετά Ctrl+D. Μην ξεχάσετε ότι και το Enter φτάνει στο πρόγραμμα ως χαρακτήρας.
