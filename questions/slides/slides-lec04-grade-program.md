---
id: slides-lec04-grade-program
kind: slides
title: "Υπολογισμός βαθμολογίας πρωτοετών"
source:
  title: "Διάλεξη 4: Git και Τελεστές, διαφάνεια 8"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec04.pdf
  years: [2025]
chapters: [4, 3]
topics: [operators, functions, command-line-args]
difficulty: 1
type: programming
---

Ο βαθμός των πρωτοετών υπολογίζεται ως:

50% * Τελική Εξέταση + 30% * Ασκήσεις + 20% * Εργαστήριο

Έστω ότι χρησιμοποιούμε 3 ακεραίους για να αναπαραστήσουμε τα αποτελέσματα [0 - 100]:
`int final_exam`, `int homework`, `int lab`.

Στα μαθηματικά:

grade(final_exam, homework, lab) = final_exam x 50% + homework x 30% + lab x 20%

Έλεγχος ορθότητας: `grade(70, 80, 100) == 79`?

Σε C; Γράψτε μια συνάρτηση `grade` και ένα πρόγραμμα που παίρνει τους τρεις βαθμούς
ως ορίσματα της γραμμής εντολών και τυπώνει τον τελικό βαθμό:

```text
$ ./grade 70 80 100
My grade is: 79
```

## Υπόδειξη

Τα ορίσματα φτάνουν στη `main` ως κείμενο μέσω των `argc`/`argv`· ελέγξτε πρώτα ότι
είναι τρία και μετατρέψτε τα σε ακεραίους με μια συνάρτηση του `stdlib.h`. Με
ακεραίους, προσέξτε με ποια σειρά γίνονται ο πολλαπλασιασμός και η διαίρεση με το 100.
