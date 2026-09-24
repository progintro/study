---
id: slides-lec22-tree-insert
kind: slides
title: "Προσθήκη στοιχείου σε δυαδικό δέντρο"
source:
  title: "Διαλέξεις 21–22: Δέντρα, διαφάνεια 16 (διάλεξη 21: διαφάνεια 38)"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec22.pdf
  years: [2025]
chapters: [22, 21]
topics: [trees, dynamic-memory, recursion]
difficulty: 2
type: programming
---

Στις βασικές λειτουργίες με δυαδικά δέντρα, η διάλεξη αφήνει ως άσκηση:

- insert: Προσθήκη στοιχείου στο δέντρο (μόνοι σας)

Υλοποιήστε την προσθήκη ενός ακεραίου σε δυαδικό δέντρο αναζήτησης (BST) με κόμβους

```c
typedef struct treenode {
  int value;
  struct treenode *left;
  struct treenode *right;
} *Tree;
```

ώστε το δέντρο να παραμένει ταξινομημένο. Ελέγξτε το αποτέλεσμα τυπώνοντας το δέντρο
με in-order διάσχιση.

## Υπόδειξη

Ακολουθήστε την ίδια διαδρομή με την αναζήτηση στο BST· όταν φτάσετε σε `NULL`, εκεί ανήκει ο νέος κόμβος, που δεσμεύεται με `malloc`. Για να αλλάξει ο δείκτης του γονιού (ή η ρίζα, αν το δέντρο είναι άδειο), είτε επιστρέψτε το νέο δέντρο είτε περάστε δείκτη σε `Tree`, όπως στην `insert` των λιστών.
