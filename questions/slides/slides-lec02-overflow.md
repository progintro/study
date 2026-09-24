---
id: slides-lec02-overflow
kind: slides
title: "Υπερχείλιση ακεραίων"
source:
  title: "Διάλεξη 2: Μνήμη και Μεταβλητές, διαφάνεια 26"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec02.pdf
  years: [2025]
chapters: [2]
topics: [integer-representation, types, input-output]
difficulty: 2
type: debug
---

Τι θα τυπώσει το παρακάτω πρόγραμμα;

```c
#include <stdio.h>

int main() {
  printf("%d\n", 2000000000 + 2000000000);
  return 0;
}
```

```text
$ ./overflow
-294967296
```

Τι συνέβη; Πώς το διορθώνουμε;

## Υπόδειξη

Ποιος είναι ο τύπος των δύο σταθερών, και ποια η μεγαλύτερη τιμή που χωράει σε αυτόν; Συγκρίνετε το $4.000.000.000$ με το $2^{32}$. Για τη διόρθωση, χρειάζεστε έναν τύπο με περισσότερα bits, τόσο για τις σταθερές όσο και στο προσδιοριστικό της `printf`.
