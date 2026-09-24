---
id: slides-lec16-atoi
kind: slides
title: "Η atoi και τι μπορεί να πάει στραβά"
source:
  title: "Διάλεξη 16, διαφάνειες 16–17"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec16.pdf
  years: [2025]
chapters: [16, 11]
topics: [strings, input-validation, functions]
difficulty: 2
type: programming
---

Θέλω μια συνάρτηση `atoi` που να παίρνει ένα πίνακα χαρακτήρων (μόνο ψηφία) και να
επιστρέφει έναν ακέραιο. Πώς;

Η λύση των διαφανειών είναι η εξής. Τι μπορεί να πάει στραβά με αυτήν τη συνάρτηση;

```c
int atoi(char digits[]) {
  int result = 0;
  for(int i = 0; digits[i]; i++) {
    result = 10 * result + digits[i] - '0';
  }
  return result;
}
```

## Υπόδειξη

Γράψτε τις υποθέσεις που κάνει η συνάρτηση για την είσοδό της και δοκιμάστε νοερά
εισόδους που τις παραβιάζουν: πρόσημο ή γράμματα, έναν πολύ μεγάλο αριθμό, έναν
πίνακα χωρίς `'\0'`. Σκεφτείτε και το όνομά της.
