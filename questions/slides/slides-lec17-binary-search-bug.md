---
id: slides-lec17-binary-search-bug
kind: slides
title: "Το σφάλμα της δυαδικής αναζήτησης"
source:
  title: "Διάλεξη 17: Δυαδική Αναζήτηση και Ταξινόμηση, διαφάνεια 16"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec17.pdf
  years: [2025]
chapters: [17]
topics: [searching, integer-representation, undefined-behavior]
difficulty: 2
type: debug
---

Αυτός ο αλγόριθμος έχει σφάλμα, μπορούμε να το βρούμε και να το διορθώσουμε;

```c
int binary_search(int elem, int *array, int n) {
  int mid, low = 0, high = n - 1;
  while (low <= high) {
    mid = (low + high) / 2;
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

Η λογική του αλγορίθμου είναι σωστή για μικρούς πίνακες. Σκεφτείτε έναν πίνακα με δύο δισεκατομμύρια στοιχεία: ποιες τιμές μπορούν να πάρουν τα `low` και `high`, και χωράει πάντα το άθροισμά τους σε `int`; Βρείτε μια έκφραση για το μέσο που δεν αθροίζει δύο μεγάλες θέσεις.
