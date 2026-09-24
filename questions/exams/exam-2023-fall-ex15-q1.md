---
id: exam-2023-fall-ex15-q1
kind: exam
title: "Πλαγιαστά Γράμματα"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #15, Θέμα 1"
  url: https://progintro.github.io/exams/2023/fall/ex15/
  years: [2023]
chapters: [9]
topics: [input-output]
difficulty: 1
type: programming
---

> Σημαντικό: φροντίζουμε τα προγράμματά μας να είναι ευανάγνωστα, αποδοτικά (σε χώρο και χρόνο) και να έχουν έξοδο όμοια με τα παραδείγματα εκτέλεσης καθώς αυτό είναι μέρος της βαθμολόγησης. Για οποιαδήποτε είσοδο εκτός προδιαγραφών το πρόγραμμα πρέπει να τερματίζει με exit code 1 και αντίστοιχο μήνυμα σφάλματος.

Πρόγραμμα: `italics.c`

Γράψτε ένα πρόγραμμα που διαβάζει από την πρότυπη είσοδο (stdin) ένα κείμενο και το τυπώνει στην πρότυπη έξοδο (stdout) αφού πρώτα μετατρέψει τα γράμματα εντός των αστερίσκων (*) σε πλαγιαστά γράμματα (italics). Τα γράμματα που βρίσκονται εκτός αστερίσκων δεν χρειάζεται να αλλαχθούν. Οι αστερίσκοι θα παραλείπονται στην έξοδο του προγράμματος. Παράδειγμα εκτέλεσης ακολουθεί:

```text
$ cat ithaca.txt
As you set out for Ithaka
hope your road is a *long one*,
full of adventure, *full of discovery*.
Laistrygonians, Cyclops,
angry Poseidon *do not be afraid of them*.
$ gcc -o italics italics.c
$ ./italics < ithaca.txt
As you set out for Ithaka
hope your road is a long one,
full of adventure, full of discovery.
Laistrygonians, Cyclops,
angry Poseidon do not be afraid of them.
```

> Σημείωση: στο πρωτότυπο το παράδειγμα δίνεται ως στιγμιότυπο τερματικού ([italics.png](https://progintro.github.io/exams/2023/fall/ex15/images/italics.png)) και εδώ μεταγράφεται ως κείμενο: στην έξοδο τα κείμενα «long one», «full of discovery» και «do not be afraid of them» εμφανίζονται πλάγια.

## Υπόδειξη

Κρατήστε μια σημαία «είμαι μέσα σε αστερίσκους» που αλλάζει σε κάθε `*`, και τυπώστε τους υπόλοιπους χαρακτήρες όπως είναι. Το «έντονο» (και αντίστοιχα το πλάγιο ή το αναβόσβημα) στο τερματικό γίνεται με ακολουθίες διαφυγής ANSI (ANSI escape codes) που τυπώνετε πριν και μετά το κείμενο, π.χ. `\033[...m`· ψάξτε ποιος κωδικός αντιστοιχεί στο εφέ που θέλετε και ποιος τα επαναφέρει.
