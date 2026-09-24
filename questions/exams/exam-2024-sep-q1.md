---
id: exam-2024-sep-q1
kind: exam
title: "Η συνάρτηση about"
source:
  title: "Εξέταση Σεπτεμβρίου 2024, Θέμα 1"
  url: https://progintro.github.io/exams/2024/progintro-exam-sep-24.pdf
  years: [2024]
chapters: [0, 3]
topics: [input-output, functions, strings]
difficulty: 1
type: programming
---

**About [5 Μονάδες]**

Γράψτε μια συνάρτηση `about` η οποία τυπώνει 3 γραμμές στην πρότυπη έξοδο (stdout):
1) το όνομά σας με λατινικούς χαρακτήρες στην 1η, 2) το sdi σας στην 2η και 3)
`I'm 100% "ready"!` στην 3η. Παράδειγμα εξόδου από την εκτέλεση της συνάρτησης `about`:

```text
Michael Jordan
sdi2300999
I'm 100% "ready"!
```

## Υπόδειξη

Η παγίδα είναι η τρίτη γραμμή: σκεφτείτε ποιοι χαρακτήρες έχουν ειδική σημασία μέσα
σε ένα string literal της C και ποιοι μέσα στο format string της `printf`. Τα διπλά
εισαγωγικά και το `%` χρειάζονται ειδικό χειρισμό, το μονό εισαγωγικό όχι.
