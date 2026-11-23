---
id: slides-lec15-complexity-mirror
kind: slides
title: "Πολυπλοκότητα εύρεσης κατόπτρου ακεραίου"
source:
  title: "Διάλεξη 15, διαφάνεια 40"
  url: https://progintro.github.io/assets/pdf/lec15.pdf
  years: [2025, 2026]
chapters: [15]
topics: [complexity, loops, math-algorithms]
difficulty: 2
type: short-answer
---

Εύρεση του κατόπτρου ενός ακεραίου. Τι χρονική και τι χωρική πολυπλοκότητα έχει η
συνάρτηση ως προς την τιμή του `n`;

```c
int mirror(int n) {
  int result = 0, tmp;
  while(n > 0) {
    tmp = n % 10;
    result = 10 * result + tmp;
    n /= 10;
  }
  return result;
}
```

## Υπόδειξη

Τι παθαίνει το `n` σε κάθε επανάληψη; Πόσες επαναλήψεις γίνονται για `n = 9`, `99`,
`999`; Ποια συνάρτηση του `n` μετρά αυτό το πλήθος;
