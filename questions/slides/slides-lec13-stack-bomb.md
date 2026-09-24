---
id: slides-lec13-stack-bomb
kind: slides
title: "Ένας τεράστιος πίνακας στη στοίβα"
source:
  title: "Διάλεξη 13, διαφάνειες 28–31"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec13.pdf
  years: [2025]
chapters: [13]
topics: [memory-model, arrays, dynamic-memory]
difficulty: 2
type: trace
---

Τι θα κάνει το ακόλουθο πρόγραμμα;

```c
#include <stdio.h>

int main() {
  char bomb[9000000];
  printf("Hello World\n");
  return 0;
}
```

```text
$ ulimit -s
8192
```

Τι αλλάζει αν πρώτα εκτελέσουμε `ulimit -s unlimited`; Και τι κάνουμε όταν η στοίβα
δεν είναι αρκετή και χρειάζεται να χρησιμοποιήσουμε πίνακες μεγάλου μεγέθους;

## Υπόδειξη

Η τιμή του `ulimit -s` είναι σε KB. Συγκρίνετε τη με το μέγεθος του τοπικού πίνακα
και θυμηθείτε πού αποθηκεύονται οι τοπικές μεταβλητές. Για το τελευταίο ερώτημα,
σκεφτείτε ποια άλλη κατηγορία μνήμης μπορεί να δεσμεύσει όλη τη διαθέσιμη μνήμη.
