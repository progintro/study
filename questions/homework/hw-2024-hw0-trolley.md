---
id: hw-2024-hw0-trolley
kind: homework
title: "Το Πρόβλημα του Τρόλεϊ (trolley)"
source:
  title: "Εργασία 0 (2024-25), Άσκηση 3"
  url: https://github.com/progintro/progintro.github.io/releases/download/2024/hw0.pdf
  years: [2024]
chapters: [9, 10, 6]
topics: [input-output, input-validation, loops, integer-representation]
difficulty: 2
type: programming
---

**Το Πρόβλημα του Τρόλεϊ (trolley - 50 Μονάδες)**

Τα αυτοκινούμενα οχήματα (self-driving cars) πρέπει κάποια στιγμή να λύσουν μια
εκδοχή του *Προβλήματος του Τρόλεϊ*, του ηθικού διλήμματος που πρότεινε η Philippa
Foot το 1967: το όχημα φτάνει σε μια διασταύρωση, τα φρένα δεν λειτουργούν, και πρέπει
να στρίψει αριστερά ή δεξιά, με κάθε επιλογή να έχει κάποιο κόστος.

Για τις ανάγκες αυτής της άσκησης, θα γράψετε ένα πρόγραμμα το οποίο λύνει
επαναλαμβανόμενες εκδοχές του προβλήματος του τρόλεϊ όπως θα χρειαζόταν να τις λύσει
και ένας αυτόματος πιλότος σε ένα αυτοκινούμενο όχημα. Επειδή η άσκηση μας είναι
κυρίως προγραμματιστική, δεν θα αποπειραθούμε να λύσουμε τα ηθικά διλήμματα και θα
ζητάμε από τον χρήστη να μας ενημερώσει για το κόστος της κάθε επιλογής μας αν πάμε
αριστερά ή δεξιά.

### Τεχνικές Προδιαγραφές

- Repository Name: progintro/hw0-\<YourUsername\>
- Αρχείο C (Filepath): trolley/src/trolley.c
- Το αρχείο C που θα υποβληθεί πρέπει να μεταγλωττίζεται χωρίς ειδοποιήσεις για λάθη
  και με κωδικό επιστροφής (exit code) που να είναι 0. Συγκεκριμένα, το αρχείο σας
  **πρέπει** να μπορεί να μεταγλωττιστεί επιτυχώς με την ακόλουθη εντολή σε ένα από τα
  μηχανήματα του εργαστηρίου (linuxXY.di.uoa.gr):
  `gcc -O0 -m32 -Wall -Wextra -Werror -pedantic -o trolley trolley.c`
- README Filepath: trolley/README.md
- Το πρόγραμμά σας πρέπει να διαβάζει όλα τα κόστη που έδωσε ο χρήστης μέχρι το τέλος
  αρχείου (End Of File - EOF).
- Όλα τα κόστη που θα δοθούν στο πρόγραμμά σας θα είναι δεκαδικοί ακέραιοι στο εύρος:
  $-10^{18}$ έως $10^{18}$.
- Σε κάθε επανάληψη του προβλήματος το πρόγραμμά σας θα πρέπει να ζητάει από τον
  χρήστη να δώσει τα κόστη για δύο επιλογές: αν πάει αριστερά (left) ή αν πάει δεξιά
  (right). Το πρόγραμμά σας πρέπει να ζητάει το κόστος για την αριστερή επιλογή πρώτα
  και στην συνέχεια για την δεξιά.
- Τα κόστη που θα δώσει ο χρήστης μπορούν να διαχωρίζονται με κενό (space), tab ή νέα
  γραμμή (new line).
- Για κάθε δύο κόστη που δίνονται, το πρόγραμμά σας πρέπει να τυπώνει στην πρότυπη
  έξοδο (stdout) είτε `Go left` είτε `Go right` - διαλέγοντας πάντα την επιλογή με το
  μικρότερο κόστος. Αν οι δύο επιλογές έχουν το ίδιο κόστος, το πρόγραμμά σας πρέπει
  να τυπώνει `Go left`.
- Αν ο χρήστης δώσει EOF αντί για το πρώτο κόστος το πρόγραμμά σας πρέπει να
  τερματίζει με κωδικό εξόδου (exit code) 0.
- Αν δοθεί οποιαδήποτε είσοδος εκτός προδιαγραφών (για παράδειγμα ο χρήστης δίνει
  μόνο το κόστος της αριστερής επιλογής) το πρόγραμμά σας πρέπει να τερματίζει με
  κωδικό εξόδου (exit code) 1.
- Για 10.000 επαναλήψεις του πειράματος, το πρόγραμμά σας πρέπει να ολοκληρώνει την
  εκτέλεση μέσα σε: 1 δευτερόλεπτο.

Παρακάτω παραθέτουμε αλληλεπιδράσεις με μια ενδεικτική λύση:

```text
thanassis@linux14:~$ hostname
linux14
thanassis@linux14:~$ gcc -O0 -m32 -Wall -Wextra -Werror -pedantic -o trolley trolley.c
thanassis@linux14:~$ ./trolley
Please enter the cost of going left: 10
Please enter the cost of going right: 100
Go left.
Please enter the cost of going left: 41
Please enter the cost of going right: 42
Go left.
Please enter the cost of going left: 42
Please enter the cost of going right: 41
Go right.
Please enter the cost of going left: 1000000
Please enter the cost of going right: 1000000
Go left.
Please enter the cost of going left: Terminating.
thanassis@linux14:~$ echo $?
0
thanassis@linux14:~$ ./trolley
Please enter the cost of going left: 42
Please enter the cost of going right: No right cost provided.
thanassis@linux14:~$ echo $?
1
thanassis@linux14:~$ ./trolley
Please enter the cost of going left: 10000000000000
Please enter the cost of going right: 4
Go right.
Please enter the cost of going left: -4
Please enter the cost of going right: -4
Go left.
Please enter the cost of going left: 10000000000000
Please enter the cost of going right: 4000000000000
Go right.
Please enter the cost of going left: Terminating.
thanassis@linux14:~$ echo $?
0
```

Στο αρχείο README.md πρέπει να προσθέσετε οποιεσδήποτε παρατηρήσεις σας κατά την
διεκπεραίωση της άσκησης. Ο κώδικας απαιτείται να είναι καλά τεκμηριωμένος με σχόλια
καθώς αυτό θα είναι μέρος της βαθμολόγησης.

## Υπόδειξη

Με `-m32` ο `long` έχει 32 bits, άρα για κόστη έως $10^{18}$ χρειάζεστε τύπο 64 bits
και τον αντίστοιχο προσδιοριστή μορφής στη `scanf`. Η τιμή επιστροφής της `scanf`
ξεχωρίζει τις τρεις περιπτώσεις που σας ενδιαφέρουν: διαβάστηκε αριθμός, ήρθε EOF, ή
ήρθε κάτι που δεν είναι αριθμός. Προσέξτε ότι το EOF πριν από το αριστερό κόστος είναι
κανονικός τερματισμός, ενώ πριν από το δεξί είναι σφάλμα.

## Δείτε επίσης

- [Υποδειγματική υποβολή φοιτητή](https://progintro.github.io/samples/code/trolley1/) (περιέχει λύση: δείτε την αφού λύσετε την άσκηση)
- [Υποδειγματική υποβολή φοιτητή (2)](https://progintro.github.io/samples/code/trolley2/) (περιέχει λύση: δείτε την αφού λύσετε την άσκηση)
