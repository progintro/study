---
id: exam-2023-fall-ex4-q2
kind: exam
title: "Τα Πάνω Κάτω"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #4 (Rick Astley Themed), Θέμα 2"
  url: https://progintro.github.io/exams/2023/fall/ex4/
  years: [2023]
chapters: [14, 9]
topics: [strings, input-output]
difficulty: 2
type: programming
---

> Σημαντικό: φροντίζουμε τα προγράμματά μας να είναι ευανάγνωστα, αποδοτικά (σε χώρο και χρόνο) και να έχουν έξοδο όμοια με τα παραδείγματα εκτέλεσης καθώς αυτό είναι μέρος της βαθμολόγησης. Για οποιαδήποτε είσοδο εκτός προδιαγραφών το πρόγραμμα πρέπει να τερματίζει με exit code 1 και αντίστοιχο μήνυμα σφάλματος.

Πρόγραμμα: `updown.c` (25 μονάδες)

Γράψτε ένα πρόγραμμα που διαβάζει το κείμενο που δίνεται από την πρότυπη είσοδο (stdin) και τυπώνει την κάθε λέξη χαρακτήρα στην πρότυπη έξοδο (stdout) έχοντας κάνει την εξής αντικατάσταση: κάθε λέξη "up" πρέπει να αντικατασταθεί με την λέξη "down" και κάθε "down" πρέπει να αντικατασταθεί με την λέξη "up". Οι λέξεις χωρίζονται με κενά (whitespace). Η αντικατάσταση πρέπει να γίνεται σε ολόκληρες λέξεις, όχι μέρος τους. Παράδειγμα εκτέλεσης:

```text
$ cat rick.txt
upload and download this �:
never gonna give you up ,
never gonna let you down ,
never gonna run around and desert you !
$ gcc -o updown updown.c
$ ./updown < rick.txt
upload and download this �:
never gonna give you down ,
never gonna let you up ,
never gonna run around and desert you !
```

## Υπόδειξη

Συγκεντρώστε κάθε λέξη (μέγιστη ακολουθία χαρακτήρων που δεν είναι whitespace) σε έναν buffer και, μόλις τελειώσει, συγκρίνετέ την με `strcmp` με τα `"up"` και `"down"` πριν την τυπώσετε· τα whitespace αντιγράφονται αυτούσια. Προσοχή στις πολύ μεγάλες λέξεις (δεν χωράνε σε σταθερό buffer, αλλά αρκεί να ξέρετε ότι δεν είναι ούτε `up` ούτε `down`) και στην τελευταία λέξη όταν το αρχείο δεν τελειώνει σε αλλαγή γραμμής.
