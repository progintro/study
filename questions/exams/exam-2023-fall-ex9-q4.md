---
id: exam-2023-fall-ex9-q4
kind: exam
title: "Κάδρο"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #9, Θέμα 4"
  url: https://progintro.github.io/exams/2023/fall/ex9/
  years: [2023]
chapters: [13, 9, 14]
topics: [dynamic-memory, input-output, strings]
difficulty: 3
type: programming
---

Πρόγραμμα: `frame.c`

Γράψτε ένα πρόγραμμα που διαβάζει από την πρότυπη είσοδο (stdin) ένα κείμενο λατινικών χαρακτήρων και το τυπώνει στην πρότυπη έξοδο (stdout) εντός ενός τετράγωνου κάδρου. Το κάδρο αποτελείται από τον χαρακτήρα '*' (42 στο δεκαδικό). Το πρόγραμμά σας πρέπει να μπορεί να χειριστεί οποιονδήποτε αριθμό γραμμών κάθε μία από τις οποίες μπορεί να είναι οποιουδήποτε μεγέθους. Παράδειγμα εκτέλεσης ακολουθεί:

```text
$ cat message.txt
    One Ring to
   Rule them all
    One Ring to
     find them
    One Ring to
   Bring them all
and in the darkness
    Bind them
$ gcc -o frame frame.c
$ ./frame < message.txt
*********************
*    One Ring to    *
*   Rule them all   *
*    One Ring to    *
*     find them     *
*    One Ring to    *
*   Bring them all  *
*and in the darkness*
*    Bind them      *
*********************
```

## Υπόδειξη

Το πλάτος του κάδρου εξαρτάται από τη μεγαλύτερη γραμμή, άρα πρέπει να διαβάσετε όλη την είσοδο πριν τυπώσετε οτιδήποτε. Δεν ξέρετε εκ των προτέρων πόσες γραμμές ή πόσο μεγάλη θα είναι η καθεμία, οπότε χρειάζεστε δυναμικούς πίνακες που μεγαλώνουν με `realloc`. Κάθε γραμμή συμπληρώνεται με κενά ως το μέγιστο μήκος.
