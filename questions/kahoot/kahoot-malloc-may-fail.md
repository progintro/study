---
id: kahoot-malloc-may-fail
kind: kahoot
title: "Πάντα πετυχαίνει η malloc;"
source:
  title: "Kahoot «Δείκτες Παντού!» (διάλεξη 12) και «Μνήμη» (διάλεξη 13)"
  years: [2025]
chapters: [13]
topics: [dynamic-memory, memory-model]
difficulty: 1
type: multiple-choice
answer: "False"
stats: {responses: 215, accuracy: 70}
---

Έχω 16KB ελεύθερη μνήμη και τρέχω `malloc(8000)`: αυτή η κλήση σίγουρα θα πετύχει.

- True
- False

## Υπόδειξη

Η ελεύθερη μνήμη δεν είναι απαραίτητα ένα ενιαίο κομμάτι, και γι' αυτό ελέγχουμε πάντα την τιμή επιστροφής.
