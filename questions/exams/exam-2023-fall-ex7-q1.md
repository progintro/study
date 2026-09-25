---
id: exam-2023-fall-ex7-q1
kind: exam
title: "Ανάβεις Φωτιές"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #7 (Star Wars Themed), Θέμα 1"
  url: https://progintro.github.io/exams/2023/fall/ex7/
  years: [2023]
chapters: [9]
topics: [input-output]
difficulty: 1
type: programming
---

Πρόγραμμα: `fire.c` (25 μονάδες)

Γράψτε ένα πρόγραμμα που διαβάζει από την πρότυπη είσοδο (stdin) ένα κείμενο και το τυπώνει στην πρότυπη έξοδο (stdout) αφού πρώτα προσθέσει μια φωτιά 🔥 (χαρακτήρας unicode U+1F525) ακολουθούμενη από κενό στην αρχή κάθε γραμμής. Το υπόλοιπο της πρότασης δεν πρέπει να αλλάζει. Το πρόγραμμά σας πρέπει να χειρίζεται γραμμές οποιουδήποτε μήκους. Παράδειγμα εκτέλεσης ακολουθεί:

```text
$ gcc -o fire fire.c
$ cat quotes.txt
May the force be with you!
Do... or do not. There is no try.
It's a trap�
I find your lack of faith disturbing.
I have a very bad feeling about this.
$ ./fire < quotes.txt
🔥 May the force be with you!
🔥 Do... or do not. There is no try.
🔥 It's a trap�
🔥 I find your lack of faith disturbing.
🔥 I have a very bad feeling about this.
```

> Σημείωση: στο πρωτότυπο το παράδειγμα είναι στιγμιότυπο τερματικού ([εικόνα](https://progintro.github.io/exams/2023/fall/ex7/images/fire.png)).

## Υπόδειξη

Αφού οι γραμμές μπορεί να έχουν οποιοδήποτε μήκος, μην τις αποθηκεύετε: διαβάστε χαρακτήρα προς χαρακτήρα με `getchar` και θυμηθείτε μόνο αν βρίσκεστε στην αρχή γραμμής. Η φωτιά τυπώνεται πριν από τον πρώτο χαρακτήρα κάθε γραμμής, όχι μετά το τελευταίο `'\n'`. Ο χαρακτήρας U+1F525 σε UTF-8 είναι τέσσερα bytes, που μπορείτε να τα γράψετε μέσα σε ένα string literal.
