---
id: slides-lec20-bitfield-sizeof
kind: slides
title: "Μέγεθος δομής με πεδία bit"
source:
  title: "Διάλεξη 20, διαφάνεια 7"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec20.pdf
  years: [2025]
chapters: [20]
topics: [structs, unions-enums]
difficulty: 1
type: trace
---

Τι τυπώνει το παρακάτω κομμάτι κώδικα; Τι θα τύπωνε αν οι τρεις τύποι `int` γίνονταν
`char`; Και αν, επιπλέον, αφαιρούσαμε τα `: 1`, `: 3`, `: 4`;

```c
struct student_status {
  int registered : 1;
  int year : 3;
  int grade : 4;
};
printf("%zu\n", sizeof(struct student_status));
```

## Υπόδειξη

Μετρήστε πόσα bits χρειάζονται συνολικά τα τρία πεδία και σκεφτείτε σε πόσες
«μονάδες» του τύπου τους χωράνε. Χωρίς πεδία bit, κάθε μέλος πιάνει ολόκληρο τον
τύπο του.
