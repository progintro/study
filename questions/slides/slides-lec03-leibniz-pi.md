---
id: slides-lec03-leibniz-pi
kind: slides
title: "Προσέγγιση του π με τη σειρά Leibniz"
source:
  title: "Διάλεξη 3: Συναρτήσεις, διαφάνεια 43"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec03.pdf
  years: [2025]
chapters: [3, 6]
topics: [floating-point, loops, math-algorithms]
difficulty: 2
type: programming
---

Challenge #2: Ο Leibniz έδειξε ότι μπορούμε να προσεγγίσουμε την τιμή του π με την
ακόλουθη φόρμουλα:

$$\frac{\pi}{4} = \sum_{i=0}^{\infty} \frac{(-1)^i}{2i+1} = \frac{1}{1} - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots$$

Θέλουμε να γράψουμε ένα πρόγραμμα που να προσεγγίζει το π. Μπορούμε;

## Υπόδειξη

Αθροίστε ένα μεγάλο αλλά πεπερασμένο πλήθος όρων (π.χ. 100000) σε μεταβλητή `double`.
Δεν χρειάζεται να υψώνετε το $-1$ σε δύναμη: κρατήστε τον αριθμητή και τον παρονομαστή
του τρέχοντος όρου σε μεταβλητές και ενημερώνετε τις σε κάθε επανάληψη. Μην ξεχάσετε
τον πολλαπλασιασμό με 4 στο τέλος.
