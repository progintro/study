---
id: exam-2023-fall-ex5-q4
kind: exam
title: "Μεταμορφώσιμες Προτάσεις"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #5 (HP Themed), Θέμα 4"
  url: https://progintro.github.io/exams/2023/fall/ex5/
  years: [2023]
chapters: [14, 12]
topics: [strings, command-line-args, arrays]
difficulty: 3
type: programming
---

> Σημαντικό: φροντίζουμε τα προγράμματά μας να είναι ευανάγνωστα, αποδοτικά (σε χώρο και χρόνο) και να έχουν έξοδο όμοια με τα παραδείγματα εκτέλεσης καθώς αυτό είναι μέρος της βαθμολόγησης. Για οποιαδήποτε είσοδο εκτός προδιαγραφών το πρόγραμμα πρέπει να τερματίζει με exit code 1 και αντίστοιχο μήνυμα σφάλματος.

Πρόγραμμα: `meta.c` (25 μονάδες)

Γράψτε ένα πρόγραμμα που παίρνει 2 προτάσεις ως ορίσματα από την γραμμή εντολών και τυπώνει αν η μία πρόταση μπορεί να μεταμορφωθεί στην άλλη κάνοντας αντικαταστάσεις λέξεων καθώς και ποιες αντικαταστάσεις απαιτούνται. Για να μπορεί να μεταμορφωθεί μια πρόταση σε μια δεύτερη πρέπει *όλες* οι λέξεις της πρώτης να ταιριάξουν με λέξεις της δεύτερης μία προς μία. Οι προτάσεις θα έχουν μόνο κενά και λατινικούς χαρακτήρες (A-Z, a-z). Παραδείγματα εκτέλεσης ακολουθούν:

```text
$ ./meta "I solemnly swear I am up to no good" "Magic glimmers brightly Magic creatures stand under the moonlight"
You can metamorphose the first sentence into the second sentence
I <-> Magic
solemnly <-> glimmers
swear <-> brightly
am <-> creatures
up <-> stand
to <-> under
no <-> the
good <-> moonlight
$ ./meta "I solemnly swear I am up to no good" "Magic glimmers brightly magic creatures stand under the moonlight"
You cannot metamorphose the first sentence into the second sentence
```

## Υπόδειξη

Χωρίστε κάθε πρόταση σε πίνακα λέξεων και απαιτήστε ίδιο πλήθος λέξεων. Η αντιστοίχιση πρέπει να είναι ένα-προς-ένα και προς τις δύο κατευθύνσεις: η ίδια λέξη της πρώτης πρότασης πρέπει πάντα να πηγαίνει στην ίδια λέξη της δεύτερης, και δύο διαφορετικές λέξεις δεν μπορούν να πάνε στην ίδια. Προσέξτε ότι η σύγκριση κάνει διάκριση πεζών-κεφαλαίων (δεύτερο παράδειγμα) και ότι κάθε ζεύγος τυπώνεται μία φορά, με τη σειρά πρώτης εμφάνισης.
