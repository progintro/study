---
id: slides-lec09-letter-frequencies
kind: slides
title: "Μέτρηση γραμμάτων στην είσοδο"
source:
  title: "Διάλεξη 9: Δεδομένα Εισόδου, διαφάνεια 41"
  url: https://progintro.github.io/assets/pdf/lec09.pdf
  years: [2025, 2026]
chapters: [9]
topics: [input-output, arrays]
difficulty: 2
type: trace
---

Τι κάνει το παρακάτω πρόγραμμα;

```c
int i, ch, total = 0;
int letfr[26];  // Letter occurrences and frequencies array
for (i=0 ; i < 26 ; i++)
  letfr[i] = 0;
while ((ch = getchar()) != EOF) {
  if (ch >= 'A' && ch <= 'Z') {
    letfr[ch-'A']++;            // Found upper case letter
    total++;
  }
  if (ch >= 'a' && ch <= 'z') {
    letfr[ch-'a']++;            // Found lower case letter
    total++;
  }
}
```

## Υπόδειξη

Ποια θέση του πίνακα `letfr` αυξάνεται όταν διαβαστεί το `'C'` και ποια όταν διαβαστεί το `'c'`; Τι μετρά το `total` και τι γίνεται με τα ψηφία και τα κενά;
