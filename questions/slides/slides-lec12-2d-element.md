---
id: slides-lec12-2d-element
kind: slides
title: "Στοιχείο δισδιάστατου πίνακα"
source:
  title: "Διάλεξη 12, διαφάνεια 14"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec12.pdf
  years: [2025]
chapters: [12]
topics: [multidim-arrays, arrays]
difficulty: 1
type: trace
---

Δίνεται ο πίνακας:

```c
int array[2][4] = {
    {1, 4, 7, 10},
    {3, 6, 9, 12},
};
```

Ποιο είναι το στοιχείο `a[1][1]` (δηλαδή `array[1][1]`);

## Υπόδειξη

Ο πρώτος δείκτης επιλέγει τη γραμμή και ο δεύτερος τη στήλη, και οι δύο μετρούν από
το 0. Γράψτε τον πίνακα σε μορφή γραμμών και στηλών και βρείτε το κελί.
