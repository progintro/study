---
id: slides-lec00-hello-world
kind: slides
title: "Hello World σε online compiler"
source:
  title: "Διάλεξη 0: Καλημέρα Κόσμε!, διαφάνεια 32"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec00.pdf
  years: [2025]
chapters: [0]
topics: [compilation, input-output]
difficulty: 1
type: tooling
---

Ας τρέξουμε το παρακάτω πρόγραμμα με έναν [online compiler](https://www.programiz.com/c-programming/online-compiler/):

```c
/* File: helloworld.c */
#include <stdio.h>

int main() {
  printf("Hello world\n");
}
```

Τι τυπώνει; Στη συνέχεια αλλάξτε το ώστε να τυπώνει δύο γραμμές, και δοκιμάστε τι συμβαίνει αν αφαιρέσετε το `\n`.

## Υπόδειξη

Κάθε κλήση της `printf` τυπώνει ακριβώς ό,τι βρίσκεται ανάμεσα στα διπλά εισαγωγικά· η αλλαγή γραμμής γίνεται μόνο όπου υπάρχει `\n`.
