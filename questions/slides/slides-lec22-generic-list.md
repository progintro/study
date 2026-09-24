---
id: slides-lec22-generic-list
kind: slides
title: "Λίστα για το BFS και λίστες κάθε τύπου"
source:
  title: "Διαλέξεις 21–22: Δέντρα, διαφάνεια 33 (διάλεξη 21: διαφάνεια 55)"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec22.pdf
  years: [2025]
chapters: [22, 21]
topics: [linked-lists, trees, pointers]
difficulty: 2
type: short-answer
---

Δίνεται η συνάρτηση που τυπώνει ένα δέντρο με διάσχιση κατά πλάτος (BFS):

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

Σημείωση: Ο τύπος List παραπάνω δεν περιέχει πλέον ακεραίους. Τι περιέχει; Πως θα
έπρεπε να αλλάξει προκειμένου να υποστηρίξει μια τέτοια υλοποίηση; Τι θα κάνατε ώστε
οι λίστες σας να δουλεύουν με κάθε τύπου δεδομένα;

## Υπόδειξη

Κοιτάξτε τον τύπο του δεύτερου ορίσματος της `insert` και της τιμής που επιστρέφει η `pop_last`. Για το τελευταίο ερώτημα, σκεφτείτε έναν τύπο δείκτη της C που μπορεί να δείχνει σε δεδομένα οποιουδήποτε τύπου, και διαβάστε για τους αφηρημένους τύπους δεδομένων (ΑΤΔ).
