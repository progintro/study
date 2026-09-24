---
id: slides-lecmake-per-file-flags
kind: slides
title: "Διαφορετικά flags ανά αρχείο"
source:
  title: "How to Make? (προσκεκλημένη διάλεξη), διαφάνειες 10-14"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/make.pdf
  years: [2025]
chapters: [26]
topics: [compilation, code-organization]
difficulty: 1
type: tooling
---

Ένα project έχει δύο αρχεία, το `main.c` και το `primes.c`, και μέχρι τώρα χτίζεται
με

```text
$ gcc -Wall -Wextra -Werror -std=c99 -pedantic -o main main.c primes.c
```

Θέλω το `primes.c` translation unit να μην έχει το standard enforcement
(`-std=c99`), επειδή θέλω να χρησιμοποιήσω την `reallocarray`, που είναι
non-standard. Το `main.c` πρέπει να κρατήσει όλα τα flags. Πώς θα το κάνω αυτό;
Γράψτε τις εντολές.

## Υπόδειξη

Με μία εντολή `gcc` όλα τα αρχεία παίρνουν τα ίδια flags. Σπάστε το compilation σε
βήματα: θυμηθείτε ποιο flag του `gcc` σταματά πριν από τη σύνδεση και τι αρχείο
παράγει.
