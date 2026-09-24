---
id: hw-2025-hw0-aliquot
kind: homework
title: "Οι Ακολουθίες Aliquot"
source:
  title: "Εργασία 0 (2025-26), Άσκηση 3"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/hw0.pdf
  years: [2025]
chapters: [7, 9, 2]
topics: [math-algorithms, loops, integer-representation, input-validation]
difficulty: 2
type: programming
---

Στα μαθηματικά, η [ακολουθία aliquot](https://en.wikipedia.org/wiki/Aliquot_sequence) είναι
μια ακολουθία θετικών ακεραίων στην οποία ο κάθε όρος είναι το άθροισμα των γνησίων
διαιρετών του προηγουμένου όρου (γνήσιοι διαιρέτες ενός αριθμού $n$ λέγονται όλοι οι
ακέραιοι διαιρέτες του $n$ πλην του εαυτού του). Αν η ακολουθία φτάσει στον αριθμό 1,
τερματίζει, εφόσον το άθροισμα των γνησίων διαιρετών του 1 είναι 0. Συμβολίζοντας με
$s(n)$ το άθροισμα των γνήσιων διαιρετών του $n$, για $n = 12$ έχουμε:

$$s(12) = 1 + 2 + 3 + 4 + 6 = 16$$

και συνεχίζοντας με τον ίδιο τρόπο $s(16) = 15$, $s(15) = 9$, $s(9) = 4$, $s(4) = 3$,
$s(3) = 1$, $s(1) = 0$. Η ακολουθία τελικά φτάνει στο 0 μετά από 7 βήματα
($12 \to 16 \to 15 \to 9 \to 4 \to 3 \to 1 \to 0$). Ο αριθμός των βημάτων (ουσιαστικά ο
αριθμός των μεταβάσεων $\to$) που απαιτούνται για να μεταβεί ένας ακέραιος $n$ στο 0
λέγεται **μήκος aliquot** για το δοθέν $n$. Με τον συμβολισμό $s^m(n) = s(s(\cdots s(n)\cdots))$
($m$ φορές) γράφουμε $s^2(12) = 15$ ή $s^7(12) = 0$· ισοδύναμα, το μήκος aliquot $l$ είναι ο
μικρότερος ακέραιος $l$ για τον οποίο $s^l(n) = 0$.

Δεν είναι όλες οι ακολουθίες aliquot φθίνουσες. Για τους τέλειους αριθμούς όπως το 6
($s(6) = 1 + 2 + 3 = 6$) η ακολουθία δεν τερματίζει ποτέ, καθώς $s^m(6) = 6$ για κάθε $m$.
Υπάρχουν και οι φίλιοι αριθμοί όπως οι 220 και 284 ($220 \to 284 \to 220 \to \cdots$) και
οι κοινωνικοί αριθμοί με κύκλους μεγαλύτερης περιοδικότητας. Η εικασία Catalan-Dickson
(1888) λέει ότι κάθε ακολουθία είτε φτάνει στο 0 είτε πέφτει σε κύκλο, και ακόμα δεν έχει
αποδειχθεί. Για κάποιους σχετικά μικρούς αριθμούς, όπως ο 276, δεν έχουμε καταφέρει ακόμα
να υπολογίσουμε την πλήρη ακολουθία!

Θα χρειαστεί να υλοποιήσετε ένα πρόγραμμα το οποίο να μπορεί να υπολογίζει τους όρους και
τα μήκη της ακολουθίας aliquot για τους αριθμούς που επιλέγει ο χρήστης, με τους
περιορισμούς των τεχνικών προδιαγραφών που ακολουθούν.

### Τεχνικές Προδιαγραφές

- Repository Name: `progintro/hw0-<YourUsername>`
- Αρχείο C (Filepath): `aliquot/src/aliquot.c`
- Το αρχείο C που θα υποβληθεί πρέπει να μεταγλωττίζεται χωρίς ειδοποιήσεις για λάθη και
  με κωδικό επιστροφής (exit code) που να είναι 0. Συγκεκριμένα, το αρχείο σας **πρέπει**
  να μπορεί να μεταγλωττιστεί επιτυχώς με την ακόλουθη εντολή σε ένα από τα μηχανήματα
  του εργαστηρίου (linuxXY.di.uoa.gr):
  `gcc -O0 -m32 -Wall -Wextra -Werror -pedantic -o aliquot aliquot.c`
- README Filepath: `aliquot/README.md`
- Το πρόγραμμά σας πρέπει να διαβάζει από την πρότυπη είσοδο (stdin) 3 διαφορετικές
  τιμές:
  1. Τον θετικό ακέραιο από τον οποίο θέλετε να ξεκινήσετε την ακολουθία.
  2. Το μέγιστο μήκος της ακολουθίας (το 0 θα συμβολίζει ότι επιτρέπεται ακολουθίες
     "άπειρου" μήκους) που θέλουμε να υπολογιστεί.
  3. Έναν χαρακτήρα που να δηλώνει αν θέλετε το πρόγραμμά σας να τυπώσει την πλήρη
     ακολουθία `'f'` (full) ή να τυπώσει μόνο το μήκος της `'l'` (length).
- Δείτε παραδείγματα από τις πρότυπες εκτελέσεις παρακάτω για να δείτε την αναμενόμενη
  έξοδο.
- Όλοι οι ακέραιοι που θα δοθούν στο πρόγραμμά σας θα είναι ακέραιοι μικρότεροι από
  $10^{15}$. Αν κατά την διαδικασία του υπολογισμού της ακολουθίας το πρόγραμμά σας φτάσει
  σε ακέραιο μεγαλύτερο του $10^{15}$, το πρόγραμμά σας πρέπει να τερματίσει με μήνυμα
  λάθους και κωδικό εξόδου (exit code) 1.
- Αν δοθεί οποιαδήποτε είσοδος εκτός προδιαγραφών (για παράδειγμα ο χρήστης δεν δώσει
  κάποιον ακέραιο για να υπολογιστεί η ακολουθία) το πρόγραμμά σας πρέπει να τερματίζει
  με κωδικό εξόδου (exit code) 1.
- Για μια ακολουθία μήκους $n$, οι χρήστες αναμένουν πως το πρόγραμμά σας πρέπει να
  ολοκληρώνει την εκτέλεσή του μέσα σε λιγότερο από $n$ δευτερόλεπτα.

Παρακάτω παραθέτουμε αλληλεπιδράσεις με μια ενδεικτική λύση:

```text
$ hostname
linux14
$ gcc -O0 -m32 -Wall -Wextra -Werror -pedantic -o aliquot aliquot.c
$ ./aliquot
Please give the number to start the aliquot sequence from: 12
Provide the max aliquot length to look for (0 for unlimited): 0
Do you want to print the full sequence ('f') or just the length ('l')? f
12
16
15
9
4
3
1
0
$ ./aliquot
Please give the number to start the aliquot sequence from: 12
Provide the max aliquot length to look for (0 for unlimited): 0
Do you want to print the full sequence ('f') or just the length ('l')? l
Length of aliquot sequence: 7
$ echo $?
0
$ ./aliquot
Please give the number to start the aliquot sequence from: 138
Provide the max aliquot length to look for (0 for unlimited): 200
Do you want to print the full sequence ('f') or just the length ('l')? l
Length of aliquot sequence: 178
$ ./aliquot
Please give the number to start the aliquot sequence from: 6
Provide the max aliquot length to look for (0 for unlimited): 6
Do you want to print the full sequence ('f') or just the length ('l')? f
6
6
6
6
6
6
6
$ ./aliquot
Please give the number to start the aliquot sequence from: 276
Provide the max aliquot length to look for (0 for unlimited): 0
Do you want to print the full sequence ('f') or just the length ('l')? f
276
396
...
749365894850244
1414070378301756
Number exceeds maximum supported integer (1000000000000000). Stopping.
$ echo $?
1
```

Στο αρχείο `README.md` πρέπει να προσθέσετε οποιεσδήποτε παρατηρήσεις σας κατά την
διεκπεραίωση της άσκησης. Ο κώδικας απαιτείται να είναι καλά τεκμηριωμένος με σχόλια
καθώς αυτό θα είναι μέρος της βαθμολόγησης.

## Υπόδειξη

Με `-m32` ο `long` έχει 32 bits, οπότε τιμές μέχρι $10^{15}$ θέλουν `long long` (και
`%lld` στο `scanf`/`printf`). Για το $s(n)$ μη δοκιμάσεις όλους τους διαιρέτες μέχρι το
$n$: οι διαιρέτες έρχονται σε ζεύγη $d$ και $n/d$, άρα αρκεί να φτάσεις ως το $\sqrt{n}$,
προσέχοντας τα τέλεια τετράγωνα και ότι ο ίδιος ο $n$ δεν μετράει. Έλεγξε την τιμή
επιστροφής κάθε `scanf` και σκέψου τις ακραίες περιπτώσεις: $n = 1$, μέγιστο μήκος 0,
χαρακτήρας διαφορετικός από `f`/`l`.
