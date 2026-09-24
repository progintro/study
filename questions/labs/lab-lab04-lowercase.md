---
id: lab-lab04-lowercase
kind: lab
title: "Τροποποίηση κειμένου"
source:
  title: "Εργαστήριο 4, Άσκηση 3"
  url: https://progintro.github.io/lab-material/labs/lab04/
  years: [2025]
chapters: [9]
topics: [input-output, redirection, conditionals]
difficulty: 1
type: programming
---

**3.1** Αντιγράψτε το αρχείο `capitalize.c` παρακάτω, μεταγλωττίστε το και εκτελέστε το
με είσοδο το ίδιο το πηγαίο αρχείο `capitalize.c`. Παρατηρήστε τη λειτουργία του.

```c
/* File: capitalize.c */

#include <stdio.h>

int main() {
  int ch; /* Be careful! Declare ch as int because of getchar() and EOF */
  ch = getchar(); /* Read first character */
  while (ch != EOF) { /* Go on if we didn't reach end of file */
    if (ch >= 'a' && ch <= 'z') { /* If lower case letter */
      ch = ch - ('a'-'A'); /* Move 'a'-'A' positions in the ASCII table */
    }
    putchar(ch); /* Print out character */
    ch = getchar(); /* Read next character */
  }
  return 0;
}
```

Η συνάρτηση `getchar()` διαβάζει έναν χαρακτήρα από την είσοδο και επιστρέφει τον ASCII
κωδικό του χαρακτήρα. Αν δεν υπάρχει άλλος χαρακτήρας για διάβασμα στην είσοδο,
επιστρέφει την ειδική ακέραια τιμή EOF που είναι ορισμένη στο stdio.h.

**3.2** Γράψτε ένα πρόγραμμα `lowercase.c`, ώστε να κάνει το αντίστροφο, δηλαδή να
μετατρέπει τους χαρακτήρες που εμφανίζονται με κεφαλαία γράμματα σε χαρακτήρες με μικρά
γράμματα.

**3.3** Τροποποιήστε το `lowercase.c`, ώστε να μετατρέπονται ταυτόχρονα και οι κεφαλαίοι
χαρακτήρες σε μικρούς και οι μικροί σε κεφαλαίους.

## Υπόδειξη

Κρατήστε τον ίδιο σκελετό ανάγνωσης μέχρι το `EOF` και αλλάξτε μόνο τον έλεγχο και τη
μετατόπιση στον πίνακα ASCII. Στο 3.3 προσέξτε να μη μετατρέψετε έναν χαρακτήρα δύο
φορές: οι δύο περιπτώσεις πρέπει να αποκλείουν η μία την άλλη.
