---
id: slides-lec15-complexity-perfect-squares
kind: slides
title: "Άθροισμα τέλειων τετραγώνων: δύο εκδοχές"
source:
  title: "Διάλεξη 15, διαφάνεια 33"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec15.pdf
  years: [2025]
chapters: [15]
topics: [complexity, loops, math-algorithms, command-line-args]
difficulty: 2
type: short-answer
---

Άθροισμα τέλειων τετραγώνων. Τι χρονική και τι χωρική πολυπλοκότητα έχει η πρώτη
εκδοχή;

```c
int isPerfectSquare(int num) {
  int root = sqrt(num);
  return root * root == num;
}
int low = atoi(argv[1]);
int high = atoi(argv[2]);
int i, sum = 0;
for(i = low ; i <= high ; i++) {
  if (isPerfectSquare(i))
    sum += i;
}
```

Και η δεύτερη;

```c
int low = atoi(argv[1]);
int high = atoi(argv[2]);
int i, sum = 0;
for(i = sqrt(low) ; i <= sqrt(high) ; i++)
  sum += i*i ;
```

## Υπόδειξη

Και στις δύο, μετρήστε τις επαναλήψεις συναρτήσει του μεγέθους του διαστήματος
(θεωρήστε την `sqrt` ένα βήμα). Η δεύτερη διατρέχει άλλες τιμές από την πρώτη: ποιες;
Δοκιμάστε επίσης τη δεύτερη με `low = 5`, `high = 20` και συγκρίνετε με την πρώτη.
