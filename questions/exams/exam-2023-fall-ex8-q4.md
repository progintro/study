---
id: exam-2023-fall-ex8-q4
kind: exam
title: "Ταξινόμηση Πακέτων"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #8, Θέμα 4"
  url: https://progintro.github.io/exams/2023/fall/ex8/
  years: [2023]
chapters: [17, 18, 14]
topics: [sorting, files, strings, dynamic-memory]
difficulty: 3
type: programming
---

> Σημαντικό: φροντίζουμε τα προγράμματά μας να είναι ευανάγνωστα, αποδοτικά (σε χώρο και χρόνο) και να έχουν έξοδο όμοια με τα παραδείγματα εκτέλεσης καθώς αυτό είναι μέρος της βαθμολόγησης. Για οποιαδήποτε είσοδο εκτός προδιαγραφών το πρόγραμμα πρέπει να τερματίζει με exit code 1 και αντίστοιχο μήνυμα σφάλματος.

Πρόγραμμα: `packet.c`

Γράψτε ένα πρόγραμμα το οποίο παίρνει ως όρισμα το όνομα ενός αρχείου που περιέχει πακέτα ακολουθούμενα από κόμμα `,` και στην συνέχεια έναν αύξοντα αριθμό (packet id) που δείχνει που έπρεπε να βρίσκονται κανονικά στην σειρά των πακέτων και τυπώνει τα πακέτα ταξινομημένα σε αύξουσα σειρά με βάση τους αύξοντες αριθμούς. Παράδειγμα επιτυχούς εκτέλεσης ακολουθεί:

```text
$ gcc -o packet packet.c
$ cat unordered.txt
Hello from five,5
This is the first packet,1
Continuing with seven,7
Almost there,9
Middle of the sequence,6
Starting to make sense,8
The very last packet,10
Second in line,2
Getting closer,4
Third packet coming through,3
$ ./packet unordered.txt
This is the first packet,1
Second in line,2
Third packet coming through,3
Getting closer,4
Hello from five,5
Middle of the sequence,6
Continuing with seven,7
Starting to make sense,8
Almost there,9
The very last packet,10
```

## Υπόδειξη

Αποθηκεύστε κάθε γραμμή μαζί με το packet id της (το κείμενο μετά το τελευταίο κόμμα) και ταξινομήστε με `qsort` και κατάλληλη συνάρτηση σύγκρισης. Δεν ξέρετε εκ των προτέρων πόσες γραμμές ή πόσο μεγάλη θα είναι η καθεμία, οπότε χρειάζεστε δυναμικούς πίνακες που μεγαλώνουν με `realloc`.
