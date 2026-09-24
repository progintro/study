---
id: slides-lec10-addnums
kind: slides
title: "Πρόσθεση δύο αριθμών από την είσοδο"
source:
  title: "Διάλεξη 10, διαφάνεια 5"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec10.pdf
  years: [2025]
chapters: [10, 9]
topics: [input-output]
difficulty: 1
type: programming
---

Θέλω να διαβάσω δύο αριθμούς από την πρότυπη είσοδο και να τους προσθέσω. Πώς;

```text
$ ./addnums
Give me a number: 40
Give me another number: 2
Total: 42
```

Ένας τρόπος είναι να χρησιμοποιήσουμε την `getchar` και να φτιάξουμε μια συνάρτηση
`getinteger` που διαβάζει τους χαρακτήρες έναν-έναν και τους μετατρέπει σε αριθμό.
Υπάρχει άλλος τρόπος να επιτύχουμε το ίδιο αποτέλεσμα; Γράψτε το πρόγραμμα
`addnums.c`.

## Υπόδειξη

Η πρότυπη βιβλιοθήκη έχει μια «αδελφή» της `printf` για διάβασμα. Θυμηθείτε ότι
πρέπει να της δώσετε πού να αποθηκεύσει κάθε τιμή, και ελέγξτε τι επιστρέφει.
