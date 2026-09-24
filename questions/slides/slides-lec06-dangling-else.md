---
id: slides-lec06-dangling-else
kind: slides
title: "Το πρόβλημα του dangling else"
source:
  title: "Διάλεξη 6: Εντολές και Ροή Ελέγχου, διαφάνεια 15"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec06.pdf
  years: [2025]
chapters: [6]
topics: [conditionals]
difficulty: 2
type: trace
---

Πολλές εμφωλευμένες εντολές `if` μπορεί να οδηγήσουν σε προβλήματα αμφισημίας (κάτι που δεν μας αρέσει καθόλου στο computer science). Είναι τα δύο προγράμματα ισοδύναμα;

```c
lab = -1;
if (year < 1)
    { /* empty block */ }
else if (year == 1)
    lab = 20;
else
    lab = 0;
```

```c
lab = -1;
if (year <= 1)
    if (year == 1)
        lab = 20;
else
    lab = 0;
```

## Υπόδειξη

Ο μεταγλωττιστής αγνοεί τη στοίχιση. Βρείτε σε ποια `if` ανήκει το `else` του δεύτερου προγράμματος σύμφωνα με τον κανόνα της C, ξαναγράψτε το με αγκύλες και συγκρίνετε τα δύο προγράμματα για `year` ίσο με 0, 1 και 2.
