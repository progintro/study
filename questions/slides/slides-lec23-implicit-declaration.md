---
id: slides-lec23-implicit-declaration
kind: slides
title: "Κλήση πριν από τον ορισμό"
source:
  title: "Διάλεξη 23, διαφάνειες 19-21"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec23.pdf
  years: [2025]
chapters: [23, 3]
topics: [functions, compilation]
difficulty: 1
type: debug
---

Το παρακάτω πρόγραμμα `prototype.c` μεταγλωττίζεται με μήνυμα
`implicit declaration of function ‘print_err’`. Γιατί; Διορθώστε το χωρίς να
μετακινήσετε τον ορισμό της `print_err`.

```c
#include <stdio.h>

int main() {
  print_err("hello");
  return 0;
}
int print_err(char * msg) {
  return fprintf(stderr, "%s\n", msg);
}
```

```text
$ gcc -o prototype prototype.c
prototype.c: In function ‘main’:
prototype.c:4:3: warning: implicit declaration of function ‘print_err’
[-Wimplicit-function-declaration]
    4 |   print_err("hello");
      |   ^~~~~~~~~
```

Μετά τη διόρθωση:

```text
$ gcc -o prototype prototype.c
$ ./prototype
hello
```

## Υπόδειξη

Ο μεταγλωττιστής της C διαβάζει το αρχείο μία φορά, από πάνω προς τα κάτω. Τι
χρειάζεται να ξέρει για την `print_err` όταν φτάσει στη γραμμή 4, και πώς του το
λέτε χωρίς να γράψετε το σώμα της;
