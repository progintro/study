---
id: lab-lab05-ladder
kind: lab
title: "Σκαλί-σκαλί (Παλιό θέμα, Προαιρετικό)"
source:
  title: "Εργαστήριο 5, Άσκηση 3"
  url: https://progintro.github.io/lab-material/labs/lab05/
  years: [2025]
chapters: [16, 11, 2]
topics: [recursion, dynamic-programming, integer-representation]
difficulty: 3
type: programming
---

Ένα παιδί ανεβαίνει μια σκάλα και σε κάθε βήμα του ανεβαίνει 1, 2 ή 3 σκαλιά. Έστω ότι η
σκάλα έχει 5 σκαλιά. Ένας τρόπος να τα ανέβει είναι 1-1-1-1-1, δηλαδή ένα σκαλί την φορά.
Ένας άλλος είναι ο 2-2-1 (δύο σκαλιά στα πρώτα δύο βήματα και μετά ένα σκαλί). Άλλοι
πιθανοί τρόποι είναι οι 3-2, 2-3, 3-1-1, κ.ο.κ - σε κάθε περίπτωση ο συνολικός αριθμός
των σκαλιών που ανέβηκε πρέπει να ισούται με τον αριθμό των σκαλιών της σκάλας. Γράψτε
ένα πρόγραμμα `ladder.c` το οποίο διαβάζει τον συνολικό αριθμό των σκαλοπατιών και
επιστρέφει τον αριθμό των διαφορετικών τρόπων με τους οποίους το παιδί μπορεί να ανέβει
την σκάλα. Το πρόγραμμά σας θέλουμε να βγάζει σωστά αποτελέσματα για σκάλες μέχρι 50
σκαλιά. Λάβετε υπόψη σας ότι στην C δεν μπορούν να αναπαρασταθούν ακέραιοι μεγαλύτεροι
από το $2^{64} - 1$, δεδομένου ότι ο ευρύτερος τύπος ακεραίου που μπορούμε να έχουμε είναι
ο `unsigned long long` (των 8 bytes). Ακολουθούν ενδεικτικές εκτελέσεις:

```text
$ ./ladder
Please provide the number of steps: 4
There are 7 different ways to climb the ladder
$ ./ladder
Please provide the number of steps: 5
There are 13 different ways to climb the ladder
$ ./ladder
Please provide the number of steps: 6
There are 24 different ways to climb the ladder
$ ./ladder
Please provide the number of steps: 50
There are 10562230626642 different ways to climb the ladder
```

## Υπόδειξη

Σκεφτείτε το τελευταίο βήμα του παιδιού: ήταν 1, 2 ή 3 σκαλιά, οπότε οι τρόποι για $n$
σκαλιά προκύπτουν από τους τρόπους για λιγότερα σκαλιά (όπως στο Fibonacci, αλλά με τρεις
όρους). Προσέξτε τις βασικές περιπτώσεις για μικρά $n$. Η αφελής αναδρομή δεν θα
τελειώσει ποτέ για 50 σκαλιά, και το αποτέλεσμα δεν χωράει σε `int`.
