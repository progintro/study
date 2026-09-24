---
id: lab-lab07-my_prog
kind: lab
title: "Εντοπισμός σφάλματος μνήμης με τον gdb"
source:
  title: "Εργαστήριο 7, Άσκηση 6"
  url: https://progintro.github.io/lab-material/labs/lab07/
  years: [2025]
chapters: [10, 24]
topics: [debugging, arrays, undefined-behavior]
difficulty: 1
type: debug
---

Το παρακάτω πρόγραμμα `my_prog.c` προσπαθεί να μετρήσει πόσοι αριθμοί στον πίνακα `p`
είναι θετικοί και να υπολογίσει το άθροισμά τους (παρατηρήστε ότι το μέγεθος του πίνακα
δεν είναι καθορισμένο με άμεσο τρόπο).

```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    int p[] = {10, -1, 8, 6, 9, 13, 0, -9, 6};
    int count = 0, sum = 0, i = 0;
    do {
        if (p[i] > 0) {
            count++;
            sum += p[count];
        }
        i++;
    } while (1);
    printf("There are %d positive numbers with sum %d\n", count, sum);
    return 0;
}
```

Τρέχοντας αυτό το πρόγραμμα, αργά ή γρήγορα θα μας δώσει segmentation fault.
Μεταγλωττίζοντας με `gcc -g3 -o my_prog my_prog.c` και τρέχοντάς το μέσα στον `gdb`
(`gdb ./my_prog` και μετά `r`), παίρνουμε κάτι σαν:

```text
Program received signal SIGSEGV, Segmentation fault.
0x080483ac in main () at my_prog.c:7
7   if (p[i] > 0) {
```

```text
(gdb) p p[i]
Cannot access memory at address 0xbf8de000
(gdb) p i
$3 = 1279
```

Δεδομένου ότι το μέγεθος του πίνακα p δεν δηλώνεται ρητά, πώς θα αντιμετωπίζατε αυτό το
πρόβλημα; Ήταν αυτό αρκετό για να λειτουργήσει σωστά το πρόγραμμα; Αν φταίει και κάτι
άλλο, προσπαθήστε να το βρείτε με τη χρήση του gdb.

Με βάση όσα είδατε παραπάνω, διορθώστε το `my_prog.c` ώστε να μην ξεπερνά τα όρια του
πίνακα και να τερματίζει σωστά.

## Υπόδειξη

Το πλήθος των στοιχείων ενός πίνακα που δηλώθηκε με αρχικοποίηση βγαίνει από το
`sizeof` όλου του πίνακα διά το `sizeof` ενός στοιχείου, και αυτό πρέπει να μπει στη
συνθήκη του βρόχου. Μετά τη διόρθωση των ορίων, ελέγξτε με `p` στον `gdb` ποιο στοιχείο
προστίθεται στο `sum` σε κάθε βήμα: είναι αυτό που μόλις ελέγξατε;
