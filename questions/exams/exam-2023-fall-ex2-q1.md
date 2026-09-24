---
id: exam-2023-fall-ex2-q1
kind: exam
title: "Pikaκίστικα"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #2 (Pokémon Themed), Θέμα 1"
  url: https://progintro.github.io/exams/2023/fall/ex2/
  years: [2023]
chapters: [9]
topics: [input-output]
difficulty: 2
type: programming
---

> Σημαντικό: φροντίζουμε τα προγράμματά μας αν είναι ευανάγνωστα, αποδοτικά (σε χώρο και χρόνο) και να έχουν έξοδο όμοια με τα παραδείγματα εκτέλεσης καθώς αυτό είναι μέρος της βαθμολόγησης. Για οποιαδήποτε είσοδο εκτός προδιαγραφών το πρόγραμμα πρέπει να τερματίζει με exit code 1 και αντίστοιχο μήνυμα σφάλματος.

Πρόγραμμα: `pika.c` (25 μονάδες)

Γράψτε ένα πρόγραμμα που διαβάζει το κείμενο που δίνεται από την πρότυπη είσοδο (stdin) και τυπώνει την κάθε λέξη χαρακτήρα στην πρότυπη έξοδο (stdout) με το πρόθεμα "pika". Οι λέξεις χωρίζονται με κενούς (whitespace) χαρακτήρες. Αριθμοί ή σημεία στίξης *δεν* θεωρούνται λέξεις. Παράδειγμα εκτέλεσης:

```text
$ cat ash.txt
	I wanna be the very best�,
	Like no one ever was ,
	To catch them is my real-test ,
	To train them is my cause !
$ ./pika  < ash.txt
	pikaI pikawanna pikabe pikathe pikavery pikabest�,
	pikaLike pikano pikaone pikaever pikawas ,
	pikaTo pikacatch pikathem pikais pikamy pikareal-test ,
	pikaTo pikatrain pikathem pikais pikamy pikacause !
```

## Υπόδειξη

Δεν χρειάζεται να αποθηκεύσετε ολόκληρες λέξεις: διαβάστε χαρακτήρα προς χαρακτήρα και κρατήστε μια μεταβλητή κατάστασης «είμαι μέσα σε λέξη ή όχι». Το πρόθεμα μπαίνει τη στιγμή που ξεκινά μια λέξη, και τα κενά (μαζί με τα tabs) αντιγράφονται όπως είναι. Κοιτάξτε προσεκτικά στο παράδειγμα ποιος χαρακτήρας κάνει ένα token «λέξη» (π.χ. `real-test` και `best�,` αλλά όχι `,` ή `!`).
