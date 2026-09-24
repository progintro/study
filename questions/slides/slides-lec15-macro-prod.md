---
id: slides-lec15-macro-prod
kind: slides
title: "Τι επιστρέφει το πρόγραμμα με τη μακροεντολή PROD"
source:
  title: "Διάλεξη 15, διαφάνεια 47"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec15.pdf
  years: [2025]
chapters: [15]
topics: [preprocessor, precedence]
difficulty: 1
type: trace
---

Η μακροεντολή αντικαθίσταται στον κώδικα πριν την μεταγλώττιση. Τι θα επιστρέψει το
παρακάτω πρόγραμμα;

```c
#define PROD 2*5
int main() {
  return 20 / PROD;
}
```

## Υπόδειξη

Γράψτε τη γραμμή `return` όπως θα τη δει ο μεταγλωττιστής μετά την αντικατάσταση
(ή τρέξτε `cpp` στο αρχείο), και υπολογίστε την παράσταση με τους κανόνες
προτεραιότητας και προσεταιριστικότητας. Την τιμή επιστροφής τη βλέπετε με `echo $?`.
