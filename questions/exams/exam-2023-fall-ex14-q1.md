---
id: exam-2023-fall-ex14-q1
kind: exam
title: "Ορεκτικό"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #14, Θέμα 1"
  url: https://progintro.github.io/exams/2023/fall/ex14/
  years: [2023]
chapters: [9]
topics: [input-output]
difficulty: 1
type: programming
---

Πρόγραμμα: `steak.c`

Γράψτε ένα πρόγραμμα που διαβάζει από την πρότυπη είσοδο (stdin) ένα κείμενο και το τυπώνει στην πρότυπη έξοδο (stdout) αφού πρώτα προσθέσει μια μπριζόλα (χαρακτήρας unicode U+1F969)  στην αρχή και στο τέλος κάθε γραμμής. Το υπόλοιπο της πρότασης δεν πρέπει να αλλάζει. Το πρόγραμμά σας πρέπει να χειρίζεται γραμμές οποιουδήποτε μήκους. Παράδειγμα εκτέλεσης ακολουθεί:

```text
$ cat message.txt
Come savor the pleasure, of treasures beyond measure,
In our cozy abode, where gourmet is the code�
We await your presence, for an experience quintessence,
At our steakhouse divine, where dining is fine!
$ gcc -o steak steak.c
$ ./steak  < message.txt
🥩Come savor the pleasure, of treasures beyond measure,🥩
🥩In our cozy abode, where gourmet is the code�🥩
🥩We await your presence, for an experience quintessence,🥩
🥩At our steakhouse divine, where dining is fine!🥩
```

> Σημείωση: στο πρωτότυπο το παράδειγμα δίνεται ως στιγμιότυπο τερματικού ([steak.png](https://progintro.github.io/exams/2023/fall/ex14/images/steak.png)) και εδώ μεταγράφεται ως κείμενο· ο χαρακτήρας � είναι ένα byte του αρχείου που δεν είναι έγκυρο UTF-8.

## Υπόδειξη

Δεν χρειάζεται να αποθηκεύσετε γραμμές: με `getchar` τυπώστε τη μπριζόλα στην αρχή κάθε γραμμής και πριν από κάθε `'\n'`. Ο χαρακτήρας U+1F969 στο UTF-8 είναι μια ακολουθία 4 bytes που μπορείτε να γράψετε ως string. Σκεφτείτε την τελευταία γραμμή χωρίς `'\n'` και την κενή είσοδο.
