---
id: slides-lec03-overflow
kind: slides
title: "Υπερχείλιση ακεραίων"
source:
  title: "Διάλεξη 3: Συναρτήσεις, διαφάνεια 8"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec03.pdf
  years: [2025]
chapters: [3]
topics: [integer-representation, types, input-output]
difficulty: 2
type: trace
---

Τι θα τυπώσει το παρακάτω πρόγραμμα;

```c
#include <stdio.h>

int main() {
  printf("%d\n", 2000000000 + 2000000000);
  return 0;
}
```

Όταν το τρέχουμε, τυπώνει:

```text
$ ./overflow
-294967296
```

Τι συνέβη; Πώς το διορθώνουμε;

## Υπόδειξη

Ποιος είναι ο τύπος των δύο σταθερών, άρα και του αθροίσματος, και ποια είναι η
μέγιστη τιμή του; Συγκρίνετε το σωστό άθροισμα με το $2^{32}$. Για τη διόρθωση,
σκεφτείτε έναν τύπο με μεγαλύτερο εύρος, το suffix των σταθερών και το προσδιοριστικό
της `printf` που του αντιστοιχεί.
