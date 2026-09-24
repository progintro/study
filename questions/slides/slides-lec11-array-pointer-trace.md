---
id: slides-lec11-array-pointer-trace
kind: slides
title: "Αναφορά σε στοιχεία πίνακα μέσω δείκτη"
source:
  title: "Διάλεξη 11, διαφάνειες 29–30"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec11.pdf
  years: [2025]
chapters: [11]
topics: [pointer-arithmetic, pointers, arrays]
difficulty: 1
type: trace
---

Αναφορά σε στοιχεία πίνακα: τι θα τυπώσει;

```c
#include <stdio.h>
int main() {
  int *ptr, arr[] = {10, 20, 30};
  ptr = &arr[0];
  printf("mem[%p], %d\n", ptr, *ptr);
  ptr += 2;
  printf("mem[%p], %d\n", ptr, *ptr);
  return 0;
}
```

## Υπόδειξη

Τις ακριβείς διευθύνσεις δεν μπορείτε να τις ξέρετε, αλλά μπορείτε να πείτε πόσο
διαφέρουν οι δύο. Κατά πόσα bytes μετακινεί το `ptr += 2` έναν `int *`, και σε ποιο
στοιχείο του πίνακα δείχνει μετά;
