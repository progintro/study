---
id: exam-2023-fall-ex8-q1
kind: exam
title: "Άρτια Bits"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #8, Θέμα 1"
  url: https://progintro.github.io/exams/2023/fall/ex8/
  years: [2023]
chapters: [4, 12]
topics: [bitwise, command-line-args]
difficulty: 1
type: programming
---

Πρόγραμμα: `parity.c`

Γράψτε ένα πρόγραμμα που παίρνει δεκαδικούς ακεραίους ως ορίσματα από την γραμμή εντολών και τυπώνει για κάθε έναν από αυτούς εάν έχει έναν άρτιο αριθμό από bits που είναι 1 (even parity). Για παράδειγμα ο αριθμός 5 είναι ο 101 στο δυαδικό και επομένως έχει άρτιο αριθμό από bits που είναι 1. Αντίθετα ο αριθμός 7 (111 στο δυαδικό) έχει περιττό αριθμό από bits που έχουν τεθεί στο 1. Παράδειγμα εκτέλεσης ακολουθεί:

```text
$ ./parity 5 7 64 65 987234 97823462
Number 5 has even parity
Number 7 does not have even parity
Number 64 does not have even parity
Number 65 has even parity
Number 987234 has even parity
Number 97823462 does not have even parity
$ ./parity 92873847981279843
Number 92873847981279843 has even parity
$ ./parity 92873847981279844
Number 92873847981279844 does not have even parity
```

## Υπόδειξη

Μετρήστε τα bits που είναι 1 με μάσκα και ολίσθηση (`&`, `>>`) μέχρι ο αριθμός να γίνει 0. Προσέξτε ότι τα παραδείγματα έχουν αριθμούς πάνω από 2^31, άρα χρειάζεστε 64-bit τύπο (`long long` / `strtoll`) και έλεγχο ότι κάθε όρισμα είναι έγκυρος ακέραιος.
