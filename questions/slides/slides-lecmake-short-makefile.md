---
id: slides-lecmake-short-makefile
kind: slides
title: "Ένα Makefile 2-3 γραμμών"
source:
  title: "How to Make? (προσκεκλημένη διάλεξη), διαφάνειες 31-39"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/make.pdf
  years: [2025]
chapters: [26]
topics: [make]
difficulty: 2
type: tooling
---

Το παρακάτω Makefile χτίζει το project `main` (αρχεία `main.c`, `primes.c`,
`primes.h`):

```make
main: main.o primes.o
	gcc -o main main.o primes.o

main.o: main.c primes.h
	gcc -Wall -Wextra -Werror -pedantic -std=c99 -c main.c

primes.o: primes.c primes.h
	gcc -Wall -Wextra -Werror -pedantic -c primes.c
```

Λειτουργεί; Ναι. Είναι καλό; Όχι.

1. Ξαναγράψτε το με macros (`CC`, `CFLAGS`), ώστε κάποιος που χρησιμοποιεί `clang` να
   αλλάζει μία μόνο γραμμή.
2. Χρησιμοποιήστε automatic variables και ένα wildcard rule, ώστε να μην
   επαναλαμβάνονται τα rules των object files.
3. Χρησιμοποιώντας τα built-in rules του Make, κάντε το Makefile 2-3 γραμμές.

Ελέγξτε ότι μετά από `touch main.c` το `make` ξαναφτιάχνει μόνο το `main.o` και
το `main`.

## Υπόδειξη

Τα `$@`, `$^` και `$<` είναι το target, όλα τα prerequisites και το πρώτο
prerequisite. Τα built-in rules χρησιμοποιούν τα macros `CC` και `CFLAGS`· ένα rule
χωρίς recipe απλώς προσθέτει prerequisites. Το `-std=c99` μόνο για το `main.o`
χρειάζεται ανάθεση μέσα σε rule.
