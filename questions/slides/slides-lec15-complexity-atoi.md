---
id: slides-lec15-complexity-atoi
kind: slides
title: "Πολυπλοκότητα της atoi"
source:
  title: "Διάλεξη 15, διαφάνεια 15"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec15.pdf
  years: [2025]
chapters: [15, 10]
topics: [complexity, strings, loops]
difficulty: 1
type: short-answer
---

Θέλω μια συνάρτηση `atoi` που να παίρνει ένα πίνακα χαρακτήρων (μόνο ψηφία) και να
επιστρέφει έναν ακέραιο. Πώς;

```c
int atoi(char digits[]) {
  int result = 0;
  for(int i = 0; digits[i]; i++) {
    result = 10 * result + digits[i] - '0';
  }
  return result;
}
```

Τι χρονική και τι χωρική πολυπλοκότητα έχει η συνάρτηση;

## Υπόδειξη

Ορίστε πρώτα τι είναι το μέγεθος $N$ της εισόδου εδώ (τι ακριβώς διατρέχει ο βρόχος;).
Μετά μετρήστε τις επαναλήψεις και τις μεταβλητές που χρειάζονται.
