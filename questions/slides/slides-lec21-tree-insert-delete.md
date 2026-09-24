---
id: slides-lec21-tree-insert-delete
kind: slides
title: "Εισαγωγή και αφαίρεση σε δυαδικό δέντρο"
source:
  title: "Διάλεξη 21, διαφάνεια 38"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec21.pdf
  years: [2025]
chapters: [21]
topics: [trees, recursion, dynamic-memory]
difficulty: 3
type: programming
---

Με τον τύπο

```c
typedef struct treenode {
  int value; struct treenode * left; struct treenode * right;
} * Tree;
```

υλοποιήστε μόνοι σας τις δύο βασικές λειτουργίες με δυαδικά δέντρα που η διάλεξη αφήνει ανοιχτές:

- `insert`: Προσθήκη στοιχείου στο δέντρο (μόνοι σας)
- `delete`: Αφαίρεση στοιχείου από δέντρο (μόνοι σας)

## Υπόδειξη

Αποφασίστε πρώτα πού πρέπει να μπαίνει ένα νέο στοιχείο: σε δυαδικό δέντρο αναζήτησης η θέση προκύπτει από τις συγκρίσεις, όπως στην `exists`, και ο νέος κόμβος μπαίνει εκεί όπου συναντάτε `NULL`. Όπως στη λίστα, η συνάρτηση πρέπει να μπορεί να αλλάξει τον δείκτη που δείχνει στο υποδέντρο (είτε με `Tree *` είτε επιστρέφοντας το νέο δέντρο). Για την αφαίρεση, εξετάστε χωριστά κόμβο χωρίς παιδιά, με ένα παιδί και με δύο παιδιά.
