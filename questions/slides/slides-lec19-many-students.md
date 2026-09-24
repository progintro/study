---
id: slides-lec19-many-students
kind: slides
title: "Πώς αναπαριστούμε 100 φοιτητές;"
source:
  title: "Διάλεξη 19, διαφάνειες 6–7"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec19.pdf
  years: [2025]
chapters: [19]
topics: [structs, arrays]
difficulty: 1
type: short-answer
---

Για ένα πρόγραμμα διαχείρισης μιας λίστας φοιτητών θα χρειαστείτε μεταβλητές για τα
ακόλουθα:

```c
char first_name[128];
char last_name[128];
unsigned int year;
double grade;
```

Έστω ότι έχουμε 100 φοιτητές, τι θα κάνουμε για να τους αναπαραστήσουμε στο
πρόγραμμά μας;

## Υπόδειξη

Σκεφτείτε πρώτα τη λύση μόνο με πίνακες: πόσους πίνακες χρειάζεστε και τι πρέπει να
ισχύει για τη θέση `i` σε καθέναν; Μετά σκεφτείτε πώς θα μπορούσαν τα τέσσερα πεδία
ενός φοιτητή να γίνουν ένας τύπος.
