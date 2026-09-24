---
id: slides-lec10-letter-frequency
kind: slides
title: "Τι κάνει ο πίνακας letfr;"
source:
  title: "Διάλεξη 10, διαφάνεια 18"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec10.pdf
  years: [2025]
chapters: [10]
topics: [arrays, input-output]
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

Υπολογίστε τι τιμή έχει η έκφραση `ch - 'A'` για `ch = 'A'`, `'B'` και `'Z'`. Τι
μετράει λοιπόν το `letfr[i]` και τι το `total`;
