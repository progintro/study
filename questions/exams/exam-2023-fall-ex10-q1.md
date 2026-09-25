---
id: exam-2023-fall-ex10-q1
kind: exam
title: "Αφαίρεση Μη Λατινικών Χαρακτήρων"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #10, Θέμα 1"
  url: https://progintro.github.io/exams/2023/fall/ex10/
  years: [2023]
chapters: [9]
topics: [input-output]
difficulty: 2
type: programming
---

Πρόγραμμα: `bold.c`

Γράψτε ένα πρόγραμμα το οποίο διαβάζει κείμενο από την πρότυπη είσοδο (stdin) και το τυπώνει στην πρότυπη έξοδο (stdout) με τους εξής περιορισμούς:
1. Οι αλλαγές γραμμής πρέπει να διατηρούνται.
1. Πρέπει να μετατρέψει κάθε μη λατινικό χαρακτήρα (A-Za-z) σε κενό (space) χαρακτήρα ' '.
1. Η πρώτη λέξη σε κάθε γραμμή θέλουμε να φαίνεται **bold**.

Παράδειγμα εκτέλεσης ακολουθεί:

```text
$ gcc -o bold bold.c
$ cat island.txt
Fifteen men on the Dead Man's Chest Yo-ho-ho,
and a bottle of rum!
Drink and the devil had done for the rest Yo-ho-ho,
and a bottle of rum!
$ ./bold < island.txt
Fifteen men on the Dead Man s Chest Yo ho ho
and a bottle of rum
Drink and the devil had done for the rest Yo ho ho
and a bottle of rum
```

> Σημείωση: στο πρωτότυπο το παράδειγμα δίνεται ως στιγμιότυπο τερματικού ([bold.png](https://progintro.github.io/exams/2023/fall/ex10/images/bold.png)) και εδώ μεταγράφεται ως κείμενο: στην έξοδο οι λέξεις Fifteen, and, Drink, and (η πρώτη κάθε γραμμής) εμφανίζονται με έντονα γράμματα.

## Υπόδειξη

Διαβάστε με `getchar` και κρατήστε μια κατάσταση: αν βρίσκεστε ακόμη στην πρώτη λέξη της γραμμής. Μη λατινικοί χαρακτήρες (εκτός από το `'\n'`) γίνονται κενά και η αλλαγή γραμμής μηδενίζει την κατάσταση. Το «έντονο» (και αντίστοιχα το πλάγιο ή το αναβόσβημα) στο τερματικό γίνεται με ακολουθίες διαφυγής ANSI (ANSI escape codes) που τυπώνετε πριν και μετά το κείμενο, π.χ. `\033[...m`· ψάξτε ποιος κωδικός αντιστοιχεί στο εφέ που θέλετε και ποιος τα επαναφέρει.
