---
id: slides-lec13-quiz-5x5
kind: slides
title: "Κουίζ: πίνακας 5x5 σε συνάρτηση"
source:
  title: "Διάλεξη 13, διαφάνειες 61–63"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec13.pdf
  years: [2025]
chapters: [13]
topics: [dynamic-memory, multidim-arrays, good-practice]
difficulty: 2
type: debug
---

Θέλω να δημιουργήσω έναν πίνακα 5x5. Για καθεμία από τις τρεις υλοποιήσεις, είναι
σωστή; Αν όχι, τι πρόβλημα έχει;

**Υλοποίηση 1**

```c
void bar() {
  int ** array = malloc(5 * sizeof(int*));
  int i;
  for(i = 0 ; i < 5 ; i++)
    array[i] = malloc(5 * sizeof(int));
  // process loop here
}
```

**Υλοποίηση 2**

```c
void bar() {
  int ** array = malloc(5 * sizeof(int*));
  if (!array) {
    return;
  }
  int i;
  for(i = 0 ; i < 5 ; i++) {
    array[i] = malloc(5 * sizeof(int));
    if (!array[i]) {
      return;
    }
  }
  // process loop here
}
```

**Υλοποίηση 3**

```c
void bar() {
  int ** array = malloc(5 * sizeof(int*));
  if (!array) {
    return;
  }
  int i;
  for(i = 0 ; i < 5 ; i++) {
    array[i] = malloc(5 * sizeof(int));
    if (!array[i]) {
      return;
    }
  }
  // process loop here
  for(i = 0 ; i < 5 ; i++) {
    free(array[i]);
  }
  free(array);
}
```

## Υπόδειξη

Για κάθε `malloc` ρωτήστε: ελέγχεται για `NULL`; Αποδεσμεύεται με `free` σε
**κάθε** δρόμο εξόδου από τη συνάρτηση, και στον κανονικό και σε αυτόν μιας
αποτυχίας στη μέση του βρόχου;
