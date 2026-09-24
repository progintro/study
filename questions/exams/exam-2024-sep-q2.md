---
id: exam-2024-sep-q2
kind: exam
title: "Η συνάρτηση what"
source:
  title: "Εξέταση Σεπτεμβρίου 2024, Θέμα 2"
  url: https://progintro.github.io/exams/2024/progintro-exam-sep-24.pdf
  years: [2024]
chapters: [17]
topics: [searching, arrays]
difficulty: 1
type: trace
---

**Η συνάρτηση what (10 Μονάδες)**

```c
int what(int *array, int x, int y) {
  int mid, low = 0, high = y - 1;
  while (low <= high) {
    mid = low + (high - low) / 2;
    printf("%d\n", mid);
    if (array[mid] == x) return 1;
    else if (array[mid] < x) low = mid + 1;
    else high = mid - 1;
  }
  return 0;
}
```

Τι κάνει η συνάρτηση `what` (μέχρι 10 λέξεις εξήγηση); Τι θα τυπώσει αν κληθεί με
ορίσματα `{57, 98, 105, 241}, 36, 4`;

## Υπόδειξη

Αναγνωρίστε το μοτίβο: δύο όρια `low`/`high` που πλησιάζουν μεταξύ τους και ένα
μεσαίο στοιχείο που συγκρίνεται με το `x`. Για την έξοδο, κρατήστε έναν πίνακα με
τις τιμές `low`, `high`, `mid` σε κάθε επανάληψη και προσέξτε ότι το 36 είναι
μικρότερο από όλα τα στοιχεία του πίνακα.
