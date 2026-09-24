---
id: kahoot-arrow-operator
kind: kahoot
title: "Ο τελεστής ->"
source:
  title: "Kahoot «Προχωρημένες Δομές» (διάλεξη 20), «Προχωρημένες Δομές #2»"
  years: [2025]
chapters: [19]
topics: [structs, pointers, precedence]
difficulty: 2
type: multiple-choice
answer: "(*robin).hood"
stats: {responses: 164, accuracy: 48}
---

Η έκφραση `robin->hood` στην C είναι ισοδύναμη με:

- `robin.(*hood)`
- `*robin.hood`
- `hood.robin`
- `(*robin).hood`

## Υπόδειξη

Το `robin` είναι δείκτης σε δομή· πρώτα πρέπει να φτάσετε στη δομή και μετά στο πεδίο, και θυμηθείτε ότι η `.` έχει μεγαλύτερη προτεραιότητα από το `*`.
