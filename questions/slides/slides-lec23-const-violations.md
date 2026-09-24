---
id: slides-lec23-const-violations
kind: slides
title: "Αλλάζοντας κάτι const"
source:
  title: "Διάλεξη 23, διαφάνειες 23-24"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec23.pdf
  years: [2025]
chapters: [23]
topics: [variables, pointers, undefined-behavior]
difficulty: 2
type: trace
---

Τι θα συμβεί όταν μεταγλωττίσουμε και τρέξουμε καθένα από τα δύο προγράμματα; Σε
ποιο στάδιο (μεταγλώττιση ή εκτέλεση) εμφανίζεται το πρόβλημα, και γιατί;

`const1.c`:

```c
const char message[] = "Hello";
int main() {
  const int x = 42;
  const char const * msg_ptr = message;
  x++;
  return 0;
}
```

`const2.c`:

```c
const char message[] = "Hello";
int main() {
  const int x = 42;
  char * bad = (char*)message;
  bad[1] = 'o';
  return 0;
}
```

## Υπόδειξη

Στο πρώτο πρόγραμμα, ο μεταγλωττιστής ξέρει ότι το `x` είναι `const`: τι θα κάνει
με το `x++`; Στο δεύτερο, το cast κρύβει το `const` από τον μεταγλωττιστή, όμως ο
πίνακας `message` εξακολουθεί να βρίσκεται σε μνήμη που προορίζεται μόνο για ανάγνωση.
