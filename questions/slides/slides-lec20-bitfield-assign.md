---
id: slides-lec20-bitfield-assign
kind: slides
title: "Ανάθεση σε πεδία bit"
source:
  title: "Διάλεξη 20, διαφάνεια 12"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec20.pdf
  years: [2025]
chapters: [20]
topics: [structs, unions-enums, integer-representation]
difficulty: 2
type: trace
---

Τι θα τυπώσει το πρόγραμμα;

```c
#include <stdio.h>

typedef struct {
  unsigned char registered : 1;
  unsigned char year : 3;
  unsigned char grade : 4;
} status;

int main() {
  status st = {1, 1, 10};
  printf("Status: %u %u %u\n", st.registered, st.year, st.grade);
  st.year = 2;
  printf("Status: %u %u %u\n", st.registered, st.year, st.grade);
  st.year += 7;
  printf("Status: %u %u %u\n", st.registered, st.year, st.grade);
  return 0;
}
```

## Υπόδειξη

Οι δύο πρώτες γραμμές είναι απλές. Για την τρίτη, σκεφτείτε ποια είναι η μεγαλύτερη
τιμή που χωράει σε 3 bits και τι απομένει όταν κρατήσετε μόνο τα 3 χαμηλά bits
του αποτελέσματος.
