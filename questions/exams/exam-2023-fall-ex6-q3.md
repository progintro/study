---
id: exam-2023-fall-ex6-q3
kind: exam
title: "Σπάσε το PIN"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #6 (Crypto Themed), Θέμα 3"
  url: https://progintro.github.io/exams/2023/fall/ex6/
  years: [2023]
chapters: [14, 8]
topics: [problem-solving, strings, loops]
difficulty: 2
type: programming
---

Πρόγραμμα: `pin.c` (25 μονάδες)

Το αρχείο pin.c προσομοιάζει τον έλεγχο ενός συστήματος που ελέγχει αν το pin σου είναι σωστό και αν επιτρέπεται η πρόσβαση. Βρείτε το pin και προσθέστε το στο πρόγραμμα προκειμένου να τυπώσει "Access granted". Δεν επιτρέπεται να αλλάξετε τις ρουτίνες υπολογισμού της ορθότητας του pin αλλά μπορείτε να κάνετε όποιες άλλες δοκιμές / αλλαγές θέλετε. Γνωρίζουμε ότι ο pin είναι τετραψήφιος. Βεβαιωθείτε ότι καταγράψατε στο αρχείο όλον τον κώδικα που γράψατε για να βρείτε το pin. Παράδειγμα επιτυχούς εκτέλεσης ακολουθεί:

```text
$ gcc -o pin pin.c
$ ./pin
Access granted
```

Το αρχείο [pin.c](https://progintro.github.io/exams/2023/fall/ex6/pin.c):

```c
// Program that checks whether a pin is correct.

#include <stdio.h>

// Password converter routine, cannot be changed
int converter(const char *str) {
    int num = 5381;
    int c;
    while ((c = *str++)) {
        num = ((num << 5) + num) + c;
    }
    return num;
}

int main() {

    // Γνωρίζουμε ότι το πρώτο ψηφίο του pin είναι το 7,
    // αλλά δεν γνωρίζουμε την συνέχεια. Αλλάξτε το pin προκειμένου
    // να μπορέσουμε να πάρουμε πρόσβαση. Γράψτε όσον κώδικα χρειαστήκατε
    // και όποιες μεθόδους χρησιμοποιήσατε για να το βρείτε σε αυτό το
    // αρχείο. Μπορείτε να βάλετε εδώ το σωστό pin όταν το βρείτε.
    char pin[] = "7...";



    // Cannot change the checks below
    if (converter(pin) == 2088511771) {
        printf("Access granted\n");
    } else {
        printf("Access denied\n");
    }

    return 0;
}
```

## Υπόδειξη

Η `converter` είναι μια συνάρτηση κατακερματισμού που δεν αντιστρέφεται εύκολα, αλλά οι υποψήφιοι τετραψήφιοι κωδικοί είναι ελάχιστοι: δοκιμάστε τους όλους (ωμή βία). Χρειάζεται να φτιάχνετε για κάθε υποψήφιο την αντίστοιχη συμβολοσειρά τεσσάρων ψηφίων (π.χ. με `sprintf` ή γεμίζοντας τις θέσεις του πίνακα με `'0' + ψηφίο`) και να κρατήσετε τον κώδικα αναζήτησης στο αρχείο, όπως ζητά η εκφώνηση.
