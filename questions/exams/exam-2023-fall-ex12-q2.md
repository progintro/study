---
id: exam-2023-fall-ex12-q2
kind: exam
title: "Προσεγγίζοντας την Λέξη"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #12, Θέμα 2"
  url: https://progintro.github.io/exams/2023/fall/ex12/
  years: [2023]
chapters: [14, 10]
topics: [strings, command-line-args, arrays]
difficulty: 2
type: programming
---

> Σημαντικό: φροντίζουμε τα προγράμματά μας να είναι ευανάγνωστα, αποδοτικά (σε χώρο και χρόνο) και να έχουν έξοδο όμοια με τα παραδείγματα εκτέλεσης καθώς αυτό είναι μέρος της βαθμολόγησης. Για οποιαδήποτε είσοδο εκτός προδιαγραφών το πρόγραμμα πρέπει να τερματίζει με exit code 1 και αντίστοιχο μήνυμα σφάλματος.

Πρόγραμμα: `check.c`

Γράψτε ένα πρόγραμμα που να δέχεται ως πρώτο όρισμα μια λέξη στόχο (goal) ακολουθούμενο από μια σειρά από προσπάθειες του χρήστη να μαντέψει την λέξη στόχο και να τυπώνει στην πρότυπη έξοδο την εγγύτητα της κάθε προσπάθειας στην λέξη στόχο. Η εγγύτητα της κάθε λέξης εξαρτάται από δύο μετρικές: (1) πόσα σωστά γράμματα μάντεψε ο χρήστης και είναι σε λάθος θέση και (2) πόσα σωστά γράμματα μάντεψε ο χρήστης και είναι στην σωστή θέση. Όλες οι λέξεις θα αποτελούνται από λατινικούς χαρακτήρες και θα έχουν το ίδιο μήκος. Παραδείγματα εκτέλεσης ακολουθούν:

```text
$ gcc -o check check.c
$ ./check unlit legal vinyl sling inlet unlit
legal has 0 correct letters in correct position and 1 correct letters in an incorrect position
vinyl has 0 correct letters in correct position and 3 correct letters in an incorrect position
sling has 0 correct letters in correct position and 3 correct letters in an incorrect position
inlet has 3 correct letters in correct position and 1 correct letters in an incorrect position
unlit has 5 correct letters in correct position and 0 correct letters in an incorrect position
$ ./check hello world worll wrllo
world has 1 correct letters in correct position and 1 correct letters in an incorrect position
worll has 1 correct letters in correct position and 2 correct letters in an incorrect position
wrllo has 3 correct letters in correct position and 0 correct letters in an incorrect position
```

## Υπόδειξη

Μετρήστε πρώτα τις ακριβείς θέσεις. Για τα γράμματα σε λάθος θέση, προσέξτε τα διπλά γράμματα: φτιάξτε πίνακες συχνοτήτων (26 θέσεις) μόνο για τα γράμματα που δεν ταίριαξαν ακριβώς, σε στόχο και προσπάθεια, και αθροίστε το ελάχιστο ανά γράμμα. Λέξεις με διαφορετικό μήκος είναι σφάλμα.
