---
id: slides-lec22-expression-evaluator
kind: slides
title: "Διάσχιση για αποτιμητή εκφράσεων"
source:
  title: "Διάλεξη 22: Δέντρα, διαφάνεια 29"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec22.pdf
  years: [2025]
chapters: [22]
topics: [trees, recursion]
difficulty: 2
type: short-answer
---

Θέλω να γράψω έναν αποτιμητή εκφράσεων (calculator / evaluator / interpreter). Ποια
διάσχιση θα χρησιμοποιήσω;

Το δέντρο της διαφάνειας έχει ρίζα `+`· το αριστερό παιδί του είναι `*` (με παιδιά `2`
και `9`) και το δεξί είναι `1`.

```mermaid
flowchart TD
  P(("+")) --> M(("*"))
  P --> O(("1"))
  M --> T(("2"))
  M --> N(("9"))
```

## Υπόδειξη

Για να υπολογίσετε τον τελεστή ενός κόμβου χρειάζεστε ήδη τις τιμές των δύο υποδέντρων του. Ποια από τις τρεις διασχίσεις (pre-order, in-order, post-order) επεξεργάζεται τον κόμβο αφού έχει τελειώσει με τα παιδιά του;
