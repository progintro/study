---
id: slides-lec18-fopen-fail
kind: slides
title: "Γιατί μπορεί να αποτύχει η fopen;"
source:
  title: "Διάλεξη 18, διαφάνειες 43–44"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec18.pdf
  years: [2025]
chapters: [18]
topics: [files]
difficulty: 1
type: short-answer
---

Ελέγχουμε πάντα το αποτέλεσμα της `fopen` αν είναι `NULL`. Για ποιο λόγο μπορεί να
αποτύχει;

```c
#include <stdio.h>
int main() {
  FILE *fileToRead, *fileToWrite;
  fileToRead = fopen("input.txt", "r");
  if (!fileToRead) {
    return 1;
  }
  fileToWrite = fopen("output.txt", "w");
  if (!fileToWrite) {
    return 1;
  }
  return 0;
}
```

## Υπόδειξη

Σκεφτείτε ξεχωριστά το άνοιγμα για διάβασμα και για γράψιμο: τι πρέπει να υπάρχει
ήδη, τι πρέπει να επιτρέπεται στον χρήστη και ποιους πόρους του συστήματος
καταναλώνει ένα ανοιχτό αρχείο.
