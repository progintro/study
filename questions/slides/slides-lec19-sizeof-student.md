---
id: slides-lec19-sizeof-student
kind: slides
title: "Το μέγεθος του struct student"
source:
  title: "Διάλεξη 19, διαφάνειες 20–21, 28"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec19.pdf
  years: [2025]
chapters: [19]
topics: [structs, memory-model, types]
difficulty: 2
type: trace
---

```c
struct student {
  char first_name[128];
  char last_name[128];
  unsigned int year;
  double grade;
};
```

Τι θα τυπώσει το ακόλουθο, όταν το πρόγραμμα μεταγλωττιστεί με `gcc -m32`;

```c
printf("%zu\n", sizeof(struct student));
```

Ποιο είναι, γενικά, το μέγεθος του `struct student`;

## Υπόδειξη

Αθροίστε τα μεγέθη των πεδίων με τη σειρά της δήλωσης. Για το γενικό ερώτημα,
σκεφτείτε αν ο μεταγλωττιστής είναι υποχρεωμένος να τα τοποθετήσει κολλητά (τι
αλλάζει για ένα `double` σε σύστημα 64 bit;).
