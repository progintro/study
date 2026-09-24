---
id: lab-lab08-legolas
kind: lab
title: "Πετυχαίνοντας τον στόχο (Παλιό θέμα)"
source:
  title: "Εργαστήριο 8, Άσκηση 3"
  url: https://progintro.github.io/lab-material/labs/lab08/
  years: [2025]
chapters: [12, 16]
topics: [command-line-args, problem-solving, integer-representation]
difficulty: 2
type: programming
---

Γράψτε ένα πρόγραμμα το οποίο παίρνει ως ορίσματα από την γραμμή εντολών έναν
ακέραιο-στόχο (goal το `argv[1]`) και στην συνέχεια ένα σύνολο υποψηφίων ακεραίων
(candidates) και τυπώνει όλους τους συνδυασμούς 3 υποψηφίων των οποίων το άθροισμα
ισούται με τον στόχο. Η σειρά με την οποία εκτυπώνονται τα αποτελέσματα δεν έχει σημασία
για την ορθότητα του προγράμματος. Παραδείγματα εκτέλεσης ακολουθούν:

```text
$ gcc -o legolas legolas.c
$ ./legolas 42 19 21 3 5 12
No combination of candidates leads to 42
$ ./legolas 42 19 21 3 5 12 11
Candidates combination found: 19 + 12 + 11 = 42
$ ./legolas 42 27 25 12 31 5 26 40 34 3 18
Candidates combination found: 27 + 12 + 3 = 42
Candidates combination found: 25 + 12 + 5 = 42
Candidates combination found: 5 + 34 + 3 = 42
$ ./legolas 37372082074 9238742398 82934723 27893492387 127863435 239847289
Candidates combination found: 9238742398 + 27893492387 + 239847289 = 37372082074
```

## Υπόδειξη

Διαλέξτε τριάδες διαφορετικών θέσεων με τρεις εμφωλευμένους βρόχους όπου κάθε δείκτης
ξεκινά μετά τον προηγούμενο, ώστε κάθε συνδυασμός να εμφανίζεται μία φορά. Το τελευταίο
παράδειγμα έχει αριθμούς που δεν χωρούν σε `int`, οπότε η μετατροπή από συμβολοσειρά
πρέπει να γίνει σε `long long`. Μην ξεχάσετε το μήνυμα όταν δεν βρεθεί κανένας
συνδυασμός.
