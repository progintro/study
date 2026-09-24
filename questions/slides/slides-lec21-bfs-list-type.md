---
id: slides-lec21-bfs-list-type
kind: slides
title: "Τι κρατά η λίστα της BFS;"
source:
  title: "Διάλεξη 21, διαφάνεια 55"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec21.pdf
  years: [2025]
chapters: [21]
topics: [linked-lists, trees, graphs, pointers]
difficulty: 2
type: short-answer
---

```c
void bfs(Tree t) {
  List worklist = NULL;
  Tree tmp;
  insert(&worklist, t);
  while(worklist) {
    tmp = pop_last(&worklist);
    printf("%d ", tmp->value);
    if (tmp->left) insert(&worklist, tmp->left);
    if (tmp->right) insert(&worklist, tmp->right);
  }
}
```

Σημείωση: Ο τύπος List παραπάνω δεν περιέχει πλέον ακεραίους. Τι περιέχει; Πως θα έπρεπε να αλλάξει προκειμένου να υποστηρίξει μια τέτοια υλοποίηση; Τι θα κάνατε ώστε οι λίστες σας να δουλεύουν με κάθε τύπου δεδομένα;

## Υπόδειξη

Δείτε τι περνά η `bfs` ως δεύτερο όρισμα στην `insert` και τι περιμένει πίσω από την `pop_last`. Για το τελευταίο ερώτημα, σκεφτείτε ποιος τύπος δείκτη στη C μπορεί να δείχνει σε δεδομένα οποιουδήποτε τύπου, και διαβάστε για τους αφηρημένους τύπους δεδομένων.
