---
id: lab-lab09-grades-tree
kind: lab
title: "Καθαρή διαχείριση μνήμης"
source:
  title: "Εργαστήριο 9, Άσκηση 5"
  url: https://progintro.github.io/lab-material/labs/lab09/
  years: [2025]
chapters: [25, 21, 22]
topics: [debugging, dynamic-memory, linked-lists, trees]
difficulty: 2
type: programming
---

Η άσκηση βασίζεται στο παράρτημα «Αποσφαλμάτωση προγραμμάτων (Πράξη 5η)» του
[εργαστηρίου](https://progintro.github.io/lab-material/labs/lab09/), που δείχνει πώς
τρέχουμε ένα πρόγραμμα κάτω από το valgrind:

```text
gcc -g3 -o grades grades.c
valgrind --leak-check=full ./grades
```

και πώς διαβάζουμε τις κατηγορίες διαρροών (`definitely lost`, `indirectly lost`,
`possibly lost`, `still reachable`). Η μόνη έξοδος που θεωρούμε καθαρή είναι:

```text
==2578== HEAP SUMMARY:
==2578==     in use at exit: 0 bytes in 0 blocks
==2578==   total heap usage: 5 allocs, 5 frees, 4,160 bytes allocated
==2578==
==2578== All heap blocks were freed -- no leaks are possible
==2578==
==2578== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

**5.1** Καθαρίστε τις δομές σας.

Επιστρέψτε στις Ασκήσεις 3 και 4 αυτού του εργαστηρίου. Καμία από τις δύο δεν αποδεσμεύει
τη μνήμη που δεσμεύει.

**5.1.1** Γράψτε τη συνάρτηση `void free_list(Listptr ptr)` και καλέστε την από τη `main`
του `grades.c`. Επιβεβαιώστε με valgrind ότι βλέπετε το μήνυμα `All heap blocks were
freed`.

**5.1.2** Γράψτε την **αναδρομική** συνάρτηση `void free_tree(Treeptr p)` για το
`tree.c`. Προσοχή στη σειρά: πρέπει να αποδεσμεύσετε πρώτα τα υποδένδρα και μετά τον
κόμβο. Τι θα δείξει το valgrind αν το κάνετε ανάποδα;

**5.2** Ξαναδείτε ένα παλιό σφάλμα.

Στο εργαστήριο 8 αποσφαλματώσαμε το `wages.c` με τη βοήθεια ενός debugger. Τρέξτε τώρα
την **αρχική, λανθασμένη** έκδοση του με valgrind. Ποιο ακριβώς μήνυμα σας δίνει, και σε
ποια γραμμή; Σας οδηγεί πιο γρήγορα στο πρόβλημα από ό,τι ο `gdb`;

## Υπόδειξη

Στη λίστα, κρατήστε τον δείκτη στον επόμενο κόμβο πριν αποδεσμεύσετε τον τρέχοντα,
αλλιώς διαβάζετε μνήμη που μόλις ελευθερώσατε. Στο δένδρο, η σειρά είναι μια post-order
διάσχιση: αν ελευθερώσετε πρώτα τον κόμβο, τα `left` και `right` του διαβάζονται από
αποδεσμευμένη μνήμη.
