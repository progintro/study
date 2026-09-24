---
id: slides-lec17-binary-search-complexity
kind: slides
title: "Πολυπλοκότητα της δυαδικής αναζήτησης"
source:
  title: "Διάλεξη 17: Δυαδική Αναζήτηση και Ταξινόμηση, διαφάνεια 18"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec17.pdf
  years: [2025]
chapters: [17]
topics: [searching, complexity]
difficulty: 1
type: short-answer
---

Τι πολυπλοκότητα (χρόνου και χώρου) έχει αυτός ο αλγόριθμος;

```c
int binary_search(int elem, int *array, int n) {
  int mid, low = 0, high = n - 1;
  while (low <= high) {
    mid = low + (high - low) / 2;
    if (array[mid] == elem)
      return 1;
    else if (array[mid] < elem)
      low = mid + 1;
    else
      high = mid - 1;
  }
  return 0;
}
```

## Υπόδειξη

Πόσα στοιχεία μένουν στο διάστημα `[low, high]` μετά από κάθε γύρο του βρόχου; Μετρήστε πόσες φορές μπορείτε να διαιρέσετε το $n$ με το 2 μέχρι να φτάσετε στο 1. Για τον χώρο, μετρήστε τις μεταβλητές που χρησιμοποιεί η συνάρτηση.
