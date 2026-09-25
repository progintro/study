---
id: exam-2023-fall-ex4-q1
kind: exam
title: "Αναγράμματα"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #4 (Rick Astley Themed), Θέμα 1"
  url: https://progintro.github.io/exams/2023/fall/ex4/
  years: [2023]
chapters: [10, 14]
topics: [arrays, strings, command-line-args]
difficulty: 2
type: programming
---

Πρόγραμμα: `anagram.c` (25 μονάδες)

Γράψτε ένα πρόγραμμα που δέχεται δύο ορίσματα και ελέγχει αν το ένα είναι ένα ανάγραμμα του άλλου. Δύο φράσεις λέγονται αναγράμματα όταν περιέχουν τους ίδιους χαρακτήρες αλλά πιθανώς με διαφορετική σειρά π.χ., οι φράσεις "desert you" και "you rested" είναι αναγράμματα η μία της άλλης. Παράδειγμα εκτέλεσης:

```text
$ gcc -o anagram anagram.c
$ ./anagram "desert you!" "you rested!"
"desert you!" is an anagram of "you rested!".
$ ./anagram "never gonna give" "never gonna give"
"never gonna give" is an anagram of "never gonna give".
$ ./anagram "never gonna give" "gonna run around"
"never gonna give" is NOT an anagram of "gonna run around".
```

## Υπόδειξη

Μετρήστε πόσες φορές εμφανίζεται κάθε χαρακτήρας σε κάθε φράση, με έναν πίνακα 256 μετρητών που δεικτοδοτείται από την τιμή του byte (ως `unsigned char`), και συγκρίνετε τα δύο ιστογράμματα. Αυτό είναι O(n), σε αντίθεση με την ταξινόμηση ή τη σύγκριση όλων με όλους. Ελέγξτε ότι δόθηκαν ακριβώς δύο ορίσματα.
