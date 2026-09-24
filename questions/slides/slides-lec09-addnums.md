---
id: slides-lec09-addnums
kind: slides
title: "Άθροισμα δύο αριθμών από την πρότυπη είσοδο"
source:
  title: "Διάλεξη 9: Δεδομένα Εισόδου, διαφάνεια 25–26"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec09.pdf
  years: [2025]
chapters: [9]
topics: [input-output, input-validation, functions]
difficulty: 2
type: programming
---

Θέλω να διαβάσω δύο αριθμούς από την πρότυπη είσοδο και να τους προσθέσω. Πώς;

```text
$ ./addnums
Give me a number: 40
Give me another number: 2
Total: 42
```

Η διάλεξη δείχνει έναν τρόπο με τη `getchar`, φτιάχνοντας μια συνάρτηση `getinteger` που διαβάζει τους χαρακτήρες έναν-έναν και τους μετατρέπει σε αριθμό. Υπάρχει άλλος τρόπος να επιτύχουμε το ίδιο αποτέλεσμα;

## Υπόδειξη

Με τη `getchar`, κάθε νέο ψηφίο `ch` αλλάζει την τιμή σε `10 * val + (ch - '0')`, μέχρι να διαβαστεί το `'\n'`. Ο άλλος τρόπος είναι μια συνάρτηση της `stdio.h` που είναι η «συμμετρική» της `printf`· μην ξεχάσετε να ελέγξετε τι επιστρέφει.
