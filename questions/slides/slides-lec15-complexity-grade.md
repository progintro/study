---
id: slides-lec15-complexity-grade
kind: slides
title: "Πολυπλοκότητα υπολογισμού βαθμολογίας"
source:
  title: "Διάλεξη 15, διαφάνεια 21"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec15.pdf
  years: [2025]
chapters: [15, 5]
topics: [complexity, functions]
difficulty: 1
type: short-answer
---

Το γνωστό μας παράδειγμα: Υπολογισμός Βαθμολογίας. Τι χρονική και τι χωρική
πολυπλοκότητα έχει η συνάρτηση;

```c
// Compute grades using the class formula
int grade(int final_exam, int homework, int lab, int year) {
  if (year <= 1) {
    return final_exam * 50 / 100 + homework * 30 / 100 + lab * 20 / 100;
  } else {
    return final_exam * 70 / 100 + homework * 30 / 100;
  }
}
```

## Υπόδειξη

Υπάρχει κάποια ποσότητα της εισόδου που κάνει τη συνάρτηση να εκτελεί περισσότερα
βήματα; Αν ο αριθμός των πράξεων δεν εξαρτάται από την είσοδο, ποια κλάση είναι;
