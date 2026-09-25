---
id: exam-2023-fall-ex10-q4
kind: exam
title: "Πλησιάζοντας στον Στόχο"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #10, Θέμα 4"
  url: https://progintro.github.io/exams/2023/fall/ex10/
  years: [2023]
chapters: [17, 19, 12]
topics: [sorting, structs, command-line-args, floating-point]
difficulty: 2
type: programming
---

Πρόγραμμα: `treasure.c`

Γράψτε ένα πρόγραμμα το οποίο παίρνει ως ορίσματα από την γραμμή εντολών μια συντεταγμένη στόχο (goal) και στην συνέχεια ένα σύνολο άλλων συντεταγμένων (starting points) και τυπώνει όλες τις συντεταγμένες ταξινομημένες σε αύξουσα σειρά με βάση την απόστασή τους από τον στόχο. Όλοι οι αριθμοί κινητής υποδιαστολής θέλουμε να τυπώνονται με ακρίβεια με δύο δεκαδικών ψηφίων. Όλες οι συντεταγμένες είναι της μορφής x,y όπου x,y είναι αριθμοί κινητής υποδιαστολής. Η απόσταση δύο σημείων x1,y1 και x2,y2 δίνεται από την έκφραση:

$$ \sqrt{(x2 - x1)^2 + (y2 - y1)^2} $$

Παράδειγμα εκτέλεσης ακολουθεί:

```text
$ gcc -o treasure treasure.c -lm
$ ./treasure 17,42 3.01,50.5 27.27,7 32,65.1 25,4 77,42.42 50,50 30.30,12
1. Point 3.01,50.50 is 16.37 steps away from the goal
2. Point 32.00,65.10 is 27.54 steps away from the goal
3. Point 30.30,12.00 is 32.82 steps away from the goal
4. Point 50.00,50.00 is 33.96 steps away from the goal
5. Point 27.27,7.00 is 36.48 steps away from the goal
6. Point 25.00,4.00 is 38.83 steps away from the goal
7. Point 77.00,42.42 is 60.00 steps away from the goal
```

## Υπόδειξη

Αναλύστε κάθε όρισμα `x,y` σε δύο `double` (π.χ. με `sscanf` ή `strtod`) και απορρίψτε όσα δεν έχουν αυτή τη μορφή. Κρατήστε κάθε σημείο σε ένα `struct` μαζί με την απόστασή του από τον στόχο και ταξινομήστε με `qsort`.
