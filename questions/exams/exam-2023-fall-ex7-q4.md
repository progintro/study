---
id: exam-2023-fall-ex7-q4
kind: exam
title: "Κόψιμο Αρχείων"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #7 (Star Wars Themed), Θέμα 4"
  url: https://progintro.github.io/exams/2023/fall/ex7/
  years: [2023]
chapters: [18, 12]
topics: [files, command-line-args]
difficulty: 1
type: programming
---

Πρόγραμμα: `cut.c` (25 μονάδες)

Γράψτε ένα πρόγραμμα το οποίο παίρνει ως όρισμα το όνομα ενός αρχείου που περιέχει δεδομένα και έναν ακέραιο αριθμό από bytes τα οποία θέλουμε να κόψουμε από το τέλος του αρχείου και τυπώνει το νέο αρχείο - έχοντας "κόψει" αυτά τα bytes - στην πρότυπη έξοδο. Τα αρχεία θα είναι μέχρι 100MB. Παράδειγμα επιτυχούς εκτέλεσης ακολουθεί:

```text
$ gcc -o cut cut.c
$ echo hello world > msg.txt
$ hexdump -C msg.txt
00000000  68 65 6c 6c 6f 20 77 6f  72 6c 64 0a              |hello world.|
0000000c
$ ./cut msg.txt 6 > msg-cut.txt
$ hexdump -C msg-cut.txt
00000000  68 65 6c 6c 6f 20                                 |hello |
00000006
$ wc -c imperial.mp3
2846267 imperial.mp3
$ ./cut imperial.mp3 2256267 > imperial-cut.mp3
$ wc -c imperial-cut.mp3
590000 imperial-cut.mp3
```

## Υπόδειξη

Βρείτε πρώτα το μέγεθος του αρχείου (π.χ. `fseek` στο τέλος και `ftell`, σε αρχείο ανοιγμένο με `"rb"`), υπολογίστε πόσα bytes πρέπει να κρατήσετε και αντιγράψτε ακριβώς τόσα στην έξοδο, κατά προτίμηση σε μπλοκ με `fread`/`fwrite`. Τι κάνετε αν ζητηθεί να κοπούν περισσότερα bytes από όσα έχει το αρχείο, ή αν ο αριθμός είναι αρνητικός ή δεν είναι αριθμός;
