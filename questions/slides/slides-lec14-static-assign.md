---
id: slides-lec14-static-assign
kind: slides
title: "Στατική μεταβλητή με ανάθεση εκτός δήλωσης"
source:
  title: "Διάλεξη 14, διαφάνεια 19"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec14.pdf
  years: [2025]
chapters: [14]
topics: [scope, memory-model]
difficulty: 2
type: trace
---

Τι θα τυπώσει το πρόγραμμα, όπου η `counter` είναι στατική αλλά παίρνει την τιμή 0
με ξεχωριστή εντολή;

```c
#include <stdio.h>
void foo() {
  static int counter; int i = 0; counter = 0;
  counter++; i++;
  printf("%d %d\n", counter, i);
}
int main() {
  foo(); foo(); foo();
  return 0;
}
```

## Υπόδειξη

Συγκρίνετε με την εκδοχή όπου το `= 0` είναι μέρος της δήλωσης
`static int counter = 0;`. Μια αρχικοποίηση στη δήλωση μιας στατικής μεταβλητής
γίνεται μία φορά· μια εντολή ανάθεσης όμως εκτελείται κάθε φορά που τη φτάνει η ροή.
