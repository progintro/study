---
id: slides-lec19-struct-compare
kind: slides
title: "Σύγκριση με δομές"
source:
  title: "Διάλεξη 19, διαφάνεια 32"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec19.pdf
  years: [2025]
chapters: [19]
topics: [structs, operators]
difficulty: 1
type: short-answer
---

Μπορώ να συγκρίνω δομές με τελεστές σύγκρισης;

```c
struct point pt1 = { 3, 4 };
struct point pt2;
pt2 = pt1;
if (pt1 == pt2) printf("impossible\n");
```

## Υπόδειξη

Δοκιμάστε να το μεταγλωττίσετε και διαβάστε το μήνυμα του `gcc`. Αν η ανάθεση
επιτρέπεται, ισχύει το ίδιο για το `==`; Πώς αλλιώς μπορείτε να ελέγξετε αν δύο
σημεία είναι ίδια;
