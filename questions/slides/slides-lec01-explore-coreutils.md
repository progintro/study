---
id: slides-lec01-explore-coreutils
kind: slides
title: "Εξερευνήστε κι άλλα βασικά προγράμματα"
source:
  title: "Διάλεξη 1: Η Γραμμή Εντολών, διαφάνεια 31"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec01.pdf
  years: [2025]
chapters: [1]
topics: [shell, unix]
difficulty: 2
type: tooling
---

Υπάρχουν και άλλα βασικά προγράμματα που δεν κοιτάξαμε (στα coreutils ή εκτός) τα οποία προτείνουμε να εξερευνήσετε:

```text
find, grep, sort, df -h, du -sh, wc -l, file, which, basename, dirname, ping, curl
```

Για καθένα, βρείτε τι κάνει και τρέξτε το τουλάχιστον μία φορά σε κάποιο αρχείο ή κατάλογο του λογαριασμού σας.

## Υπόδειξη

Ξεκινήστε από το `man` κάθε εντολής (π.χ. `man wc`) και διαβάστε τις πρώτες γραμμές της περιγραφής και τις επιλογές που αναφέρει η διαφάνεια (`-h`, `-sh`, `-l`). Δοκιμάστε τις σε αρχεία που ήδη έχετε, όπως το `hello.c`.
