---
id: exam-2023-fall-ex11-q1
kind: exam
title: "Αναζητώντας τον Blinky"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #11, Θέμα 1"
  url: https://progintro.github.io/exams/2023/fall/ex11/
  years: [2023]
chapters: [9, 14]
topics: [input-output, strings]
difficulty: 2
type: programming
---

> Σημαντικό: φροντίζουμε τα προγράμματά μας να είναι ευανάγνωστα, αποδοτικά (σε χώρο και χρόνο) και να έχουν έξοδο όμοια με τα παραδείγματα εκτέλεσης καθώς αυτό είναι μέρος της βαθμολόγησης. Για οποιαδήποτε είσοδο εκτός προδιαγραφών το πρόγραμμα πρέπει να τερματίζει με exit code 1 και αντίστοιχο μήνυμα σφάλματος.

Πρόγραμμα: `blinky.c`

Γράψτε ένα πρόγραμμα το οποίο διαβάζει κείμενο από την πρότυπη είσοδο (stdin) και το τυπώνει στην πρότυπη έξοδο (stdout) με τους εξής περιορισμούς:
1. Κάθε φορά που βρίσκει την λέξη Blinky - να την τοποθετεί ανάμεσα σε αστεράκια '*' και να την κάνει να αναβοσβήνει (blink).
1. Αν το string Blinky είναι μέρος άλλης λέξης δεν χρειάζεται κάποια αλλαγή.
1. Οι λέξεις αποτελούνται μόνο από λατινικούς χαρακτήρες (A-Za-z) οποιοσδήποτε άλλος χαρακτήρας θεωρείται διαχωριστικό λέξεων.

Παράδειγμα εκτέλεσης ακολουθεί:

[![asciicast](https://asciinema.org/a/js20ZyFDDS0t8ocszkBBo6b4J.svg)](https://asciinema.org/a/js20ZyFDDS0t8ocszkBBo6b4J)

Αν για κάποιο λόγο δεν παίζει το παραπάνω link:

```text
$ gcc -o blinky blinky.c
$ cat description.txt
In the Pac-Man universe, Blinky is the red ghost who
persistently chases the game's hero, earning the
nickname "Shadow" for his relentless pursuit.
Blinky's strategy intensifies as Pac-Man consumes
more dots, making Blinky a formidable challenge and
a central figure in game strategy. His vivid red hue
not only marks Blinky as the primary antagonist but
also signals the immediate threat he poses.
$ ./blinky < description.txt
In the Pac-Man universe, *Blinky* is the red ghost who
persistently chases the game's hero, earning the
nickname "Shadow" for his relentless pursuit.
*Blinky*'s strategy intensifies as Pac-Man consumes
more dots, making *Blinky* a formidable challenge and
a central figure in game strategy. His vivid red hue
not only marks *Blinky* as the primary antagonist but
also signals the immediate threat he poses.
```

## Υπόδειξη

Μαζέψτε κάθε λέξη (μέγιστη ακολουθία λατινικών χαρακτήρων) σε έναν buffer και, όταν τελειώσει, συγκρίνετέ τη ολόκληρη με το `Blinky`· έτσι το `Blinky` μέσα σε μεγαλύτερη λέξη δεν αλλάζει. Οι διαχωριστικοί χαρακτήρες τυπώνονται αυτούσιοι. Το «έντονο» (και αντίστοιχα το πλάγιο ή το αναβόσβημα) στο τερματικό γίνεται με ακολουθίες διαφυγής ANSI (ANSI escape codes) που τυπώνετε πριν και μετά το κείμενο, π.χ. `\033[...m`· ψάξτε ποιος κωδικός αντιστοιχεί στο εφέ που θέλετε και ποιος τα επαναφέρει.
