---
id: slides-lec08-print-all-issue
kind: slides
title: "Υπάρχει θέμα με αυτή την υλοποίηση;"
source:
  title: "Διάλεξη 8: Ροή Ελέγχου #2, διαφάνεια 7"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec08.pdf
  years: [2025]
chapters: [8]
topics: [loops, control-flow]
difficulty: 1
type: debug
---

Θέλω να τυπώσω (αν υπάρχει) τον μικρότερο τριψήφιο που είναι πολλαπλάσιο του 2 και
του 5 αλλά όχι του 4. Πώς;

```c
for(i = 100 ; i < 1000 ; i++) {
  if (i % 2 == 0 && i % 5 == 0 && i % 4 != 0) {
      printf("%d\n", i);
  }
}
```

Υπάρχει κάποιο θέμα με αυτήν την υλοποίηση;

## Υπόδειξη

Τι γίνεται αφού ο βρόχος βρει και τυπώσει τον πρώτο κατάλληλο αριθμό; Μετρήστε πόσες
γραμμές θα τυπωθούν και σκεφτείτε πώς σταματάμε έναν βρόχο νωρίς.
