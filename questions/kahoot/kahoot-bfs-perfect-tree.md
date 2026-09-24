---
id: kahoot-bfs-perfect-tree
kind: kahoot
title: "BFS σε τέλειο δυαδικό δέντρο"
source:
  title: "Kahoot «Λίστες, Δέντρα and Beyond»"
  years: [2025]
chapters: [22, 21]
topics: [trees, graphs, complexity, searching]
difficulty: 3
type: multiple-choice
answer: "False"
stats: {responses: 93, accuracy: 37}
---

MIT (3-ετείς): έστω T ένα τέλειο δυαδικό δέντρο με n κόμβους. Μπορώ να βρω ένα στοιχείο με BFS σε O(log n);

- True
- False

## Συχνή παρανόηση

Το 61% απάντησε True, μπερδεύοντας το ύψος του δέντρου (log n) με το κόστος της αναζήτησης· η BFS σε δέντρο που δεν είναι BST μπορεί να χρειαστεί να επισκεφθεί όλους τους κόμβους.

## Υπόδειξη

Η BFS δεν ξέρει προς ποιο παιδί να πάει· σκεφτείτε πόσους κόμβους επισκέπτεται στη χειρότερη περίπτωση, αν το στοιχείο είναι στο τελευταίο επίπεδο.
