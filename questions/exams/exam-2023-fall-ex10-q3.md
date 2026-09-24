---
id: exam-2023-fall-ex10-q3
kind: exam
title: "Κρυμμένο Μήνυμα"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #10, Θέμα 3"
  url: https://progintro.github.io/exams/2023/fall/ex10/
  years: [2023]
chapters: [18, 14, 13]
topics: [files, strings, dynamic-memory, command-line-args]
difficulty: 2
type: programming
---

> Σημαντικό: φροντίζουμε τα προγράμματά μας να είναι ευανάγνωστα, αποδοτικά (σε χώρο και χρόνο) και να έχουν έξοδο όμοια με τα παραδείγματα εκτέλεσης καθώς αυτό είναι μέρος της βαθμολόγησης. Για οποιαδήποτε είσοδο εκτός προδιαγραφών το πρόγραμμα πρέπει να τερματίζει με exit code 1 και αντίστοιχο μήνυμα σφάλματος.

Πρόγραμμα: `hidden.c`

Γράψτε ένα πρόγραμμα που παίρνει ως όρισμα το όνομα ενός αρχείου που περιέχει ένα κείμενο με λέξεις που αποτελούνται από λατινικούς χαρακτήρες (a-zA-Z) και θετικούς ακεραίους που αντιστοιχούν στην θέση της κάθε λέξης μέσα στο κείμενο και τυπώνει αυτές τις λέξεις με την σειρά που δίνονται ως ορίσματα στο πρόγραμμα. Παραδείγματα εκτέλεσης ακολουθούν:

```text
$ gcc -o hidden hidden.c
$ cat message.txt
In the quiet glade, where whispers of the past weave,
Beneath the vault of heaven, a secret to conceive.
The oak, ancient and large, guards a mystery so deep,
Within its shadowed roots, a treasure lies asleep.
Hidden by time's embrace, under earth's tender keep,
Near the tree, love's promise, forever to reap
$ ./hidden message.txt 19 34 35 42 1 23 20 49
The treasure lies under the large oak tree
$ ./hidden message.txt 19 34 35 29
The treasure lies Within
```

Παρατηρούμε ότι η λέξη "The" τυπώνεται πρώτη καθώς είναι η 20η λέξη στο κείμενο, δηλαδή βρίσκεται στην θέση 19 και αυτός είναι ο πρώτος ακέραιος που δόθηκε ως όρισμα στην γραμμή εντολών μετά το αρχείο. Αντίστοιχα τυπώνονται και οι υπόλοιπες λέξεις.

## Υπόδειξη

Χωρίστε το κείμενο σε λέξεις από λατινικούς χαρακτήρες (οτιδήποτε άλλο είναι διαχωριστικό, άρα το `time's` δίνει δύο λέξεις) και αποθηκεύστε τες σε δυναμικό πίνακα, ώστε να έχετε άμεση πρόσβαση με τη θέση. Οι θέσεις μετράνε από το 0· ελέγξτε θέσεις εκτός ορίων.
