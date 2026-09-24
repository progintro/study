---
id: slides-lec20-list-layout
kind: slides
title: "Η διάταξη των φακέλων"
source:
  title: "Διάλεξη 20, διαφάνεια 38"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec20.pdf
  years: [2025]
chapters: [20,21]
topics: [linked-lists, structs]
difficulty: 1
type: short-answer
---

Η πραγματική διάταξη (layout) των φακέλων `newton/`, `hw0/`, `thanos/`, `home/`, `/`
στη μνήμη μπορεί να είναι περίπλοκη. Σε αφηρημένη μορφή είναι κάπως έτσι:

```text
"newton" | &hw0  ->  "hw0" | &user  ->  "thanos" | &home
  ->  "home/" | &root  ->  "/" | NULL
```

Μας θυμίζει κάτι αυτή η διάταξη;

## Υπόδειξη

Κάθε στοιχείο κρατά μια τιμή και δείχνει στο επόμενο, και το τελευταίο δείχνει στο
`NULL`. Ποια δομή δεδομένων ορίζεται ακριβώς έτσι;
