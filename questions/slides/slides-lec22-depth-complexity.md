---
id: slides-lec22-depth-complexity
kind: slides
title: "Πολυπλοκότητα της depth"
source:
  title: "Διαλέξεις 21–22: Δέντρα, διαφάνεια 20 (διάλεξη 21: διαφάνειες 41–42)"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec22.pdf
  years: [2025]
chapters: [22, 21]
topics: [trees, recursion, complexity]
difficulty: 2
type: short-answer
---

Δίνεται η συνάρτηση που υπολογίζει το βάθος ενός δυαδικού δέντρου:

```c
int depth(Tree t) {
  if (t == NULL) return -1;
  int left_depth = depth(t->left);
  int right_depth = depth(t->right);
  return 1 + ((left_depth > right_depth) ? left_depth : right_depth);
}
```

Ποια η πολυπλοκότητα για ένα τέλειο δυαδικό δέντρο; (χρόνος και χώρος)

## Υπόδειξη

Για τον χρόνο, μετρήστε πόσες φορές καλείται η `depth` για κάθε κόμβο. Για τον χώρο, σκεφτείτε πόσες κλήσεις μπορεί να βρίσκονται ταυτόχρονα στη στοίβα, και πώς σχετίζεται αυτό με το ύψος ενός τέλειου δέντρου με $n$ κόμβους.
