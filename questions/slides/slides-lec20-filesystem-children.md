---
id: slides-lec20-filesystem-children
kind: slides
title: "Σύστημα αρχείων με υποφακέλους"
source:
  title: "Διάλεξη 20, διαφάνεια 47"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec20.pdf
  years: [2025]
chapters: [20]
topics: [structs, trees, pointers]
difficulty: 2
type: short-answer
---

Θέλω να αναπαραστήσω ένα σύστημα αρχείων (filesystem) ώστε να βρίσκω άμεσα τους
υποφακέλους και τον parent φάκελο. Πώς;

## Υπόδειξη

Ξεκινήστε από τη `struct folder` με όνομα και δείκτη `parent`. Τι πρέπει να
προσθέσετε ώστε να φτάνετε και προς τα κάτω; Ένας φάκελος μπορεί να έχει οσουσδήποτε
υποφακέλους, οπότε σκεφτείτε μια δομή που μεγαλώνει (π.χ. δυναμικός πίνακας δεικτών
ή λίστα).
