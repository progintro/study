---
id: slides-lec18-stderr-redirect
kind: slides
title: "Ανακατεύθυνση της stderr"
source:
  title: "Διάλεξη 18, διαφάνεια 56"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec18.pdf
  years: [2025]
chapters: [18, 1]
topics: [redirection, files]
difficulty: 1
type: tooling
---

Σύγκρινε το `find / -name foo` με το `find / -name foo 2> error.txt`.

## Υπόδειξη

Τρέξτε και τις δύο εντολές και δείτε τι εμφανίζεται στην οθόνη και τι στο
`error.txt`. Ποιον file descriptor έχει η `stderr`, και σε ποιο ρεύμα γράφει η
`find` τα μηνύματα «Permission denied»;
