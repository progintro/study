---
id: slides-lec15-preprocess-if-else
kind: slides
title: "Σε τι προεπεξεργάζεται το #if 0"
source:
  title: "Διάλεξη 15, διαφάνεια 53"
  url: https://progintro.github.io/assets/pdf/lec15.pdf
  years: [2025, 2026]
chapters: [15]
topics: [preprocessor]
difficulty: 1
type: trace
---

Οι εντολές `#if #else #endif` έχουν μορφή παρόμοια με την δομή ελέγχου if στην C αλλά
δρουν στο επίπεδο του κώδικα. Σε τι θα προεπεξεργαστεί το ακόλουθο πρόγραμμα;

```c
int main() {
#if 0
  return 42;
#else
  return 1;
#endif
}
```

## Υπόδειξη

Η συνθήκη του `#if` είναι σταθερά: είναι αληθής ή ψευδής; Κρατήστε μόνο τις γραμμές
του κλάδου που επιλέγεται και σβήστε όλες τις γραμμές που αρχίζουν με `#`. Επιβεβαιώστε
με `gcc -E`.
