---
id: slides-lec11-factorial-calls
kind: slides
title: "Πόσες αναδρομικές κλήσεις κάνει το factorial"
source:
  title: "Διάλεξη 11, διαφάνεια 46"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec11.pdf
  years: [2025]
chapters: [11]
topics: [recursion]
difficulty: 1
type: short-answer
---

Με τη συνάρτηση

```c
int factorial(int number) {
  if (number == 0) return 1;
  else return number * factorial(number - 1);
}
```

πόσες αναδρομικές (στον εαυτό της) κλήσεις κάνει η κλήση `factorial(5)`; Πόσες η κλήση
`factorial(N)`;

## Υπόδειξη

Γράψτε την αλυσίδα κλήσεων που ξεκινά από το `factorial(5)` μέχρι τη βάση τερματισμού
και μετρήστε τους κρίκους της, προσέχοντας αν μετράτε και την αρχική κλήση. Μετά
γενικεύστε για `N`.
