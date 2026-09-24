---
id: slides-lecmake-sqrt-errors
kind: slides
title: "Compiler error ή linking error; (math.h και libm.so)"
source:
  title: "How to Make? (προσκεκλημένη διάλεξη), διαφάνειες 6-8"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/make.pdf
  years: [2025]
chapters: [26, 3]
topics: [compilation]
difficulty: 1
type: debug
---

Το πρόγραμμα:

```c
#include <stdio.h>
// does-not-compile
int main(void) {
    printf("%.2f\n", sqrt(3));
    return 0;
}
```

```text
$ gcc -o main main.c
main.c: In function 'main':
main.c:4:20: error: implicit declaration of function 'sqrt'
[-Wimplicit-function-declaration]
main.c:2:1: note: include '<math.h>' or provide a declaration of 'sqrt'
```

1. Τι έγινε εδώ; Τι είδους error είναι αυτό;
2. Προσθέτουμε `#include <math.h>` και ξανατρέχουμε:

   ```text
   $ gcc -o main main.c
   /usr/bin/ld: /tmp/ccaw9D8e.o: in function `main':
   main.c:(.text+0x1f): undefined reference to `sqrt'
   collect2: error: ld returned 1 exit status
   ```

   Τι είδους error είναι αυτό τώρα; Παρατηρήστε ότι, σε αντίθεση με τον compiler, το
   μήνυμα δεν είναι και πολύ βοηθητικό. Έχει κανείς ιδέα γιατί;
3. Πώς το διορθώνουμε ώστε το `./main` να τυπώσει `1.73`;

## Υπόδειξη

Ποιο πρόγραμμα βγάζει κάθε μήνυμα (δείτε τη λέξη `ld`); Ένα αρχείο `.h` δίνει
δηλώσεις, όχι υλοποιήσεις: σκεφτείτε σε ποιο object file ή βιβλιοθήκη βρίσκεται η
`sqrt` και πώς το λέτε στον linker.
