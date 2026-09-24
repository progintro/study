---
id: slides-lec11-factorial-overflow
kind: slides
title: "Αρνητικό παραγοντικό"
source:
  title: "Διάλεξη 11, διαφάνεια 46"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec11.pdf
  years: [2025]
chapters: [11]
topics: [integer-representation, recursion]
difficulty: 1
type: short-answer
---

Για κάποιους αριθμούς το αποτέλεσμα του αναδρομικού προγράμματος παραγοντικού (με
`int`) είναι αρνητικό. Τι συμβαίνει;

```text
$ ./fact 20
20! = -2102132736
```

## Υπόδειξη

Ποια είναι η μεγαλύτερη τιμή που χωρά σε έναν `int` των 32 bit; Υπολογίστε πρόχειρα
πόσο γρήγορα μεγαλώνει το $n!$ και βρείτε το πρώτο $n$ για το οποίο το ξεπερνά.
