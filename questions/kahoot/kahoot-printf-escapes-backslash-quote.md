---
id: kahoot-printf-escapes-backslash-quote
kind: kahoot
title: 'Ακολουθίες διαφυγής για `\\` και `"`'
source:
  title: "Kahoot «Τύπωμα και Συναρτήσεις» (διάλεξη 3)"
  years: [2025]
chapters: [3]
topics: [input-output, strings]
difficulty: 2
type: multiple-choice
answer: "printf(\"I'm \\\\\\\\ \\\"back\\\"\");"
stats: {responses: 190, accuracy: 43}
---

Πώς τυπώνουμε την ακολουθία: `I'm \\ "back"`

- `printf("I'm \\\\ \"back\"");`
- `printf("I\'m \\ \"back\"");`
- `printf("I'm \\ "back"");`
- `printf("I am \n %dback%d");`

## Υπόδειξη

Μέσα σε ένα αλφαριθμητικό, κάθε `\` που θέλουμε να τυπωθεί και κάθε `"` πρέπει να γραφτεί με ακολουθία διαφυγής. Μετρήστε πόσα `\` θέλουμε στην έξοδο.
