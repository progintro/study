---
id: kahoot-ptr-offset-equals-index
kind: kahoot
title: "*(ptr + 4) και ptr[4]"
source:
  title: "Kahoot «Δείκτες και Αναδρομή» (διάλεξη 11)"
  years: [2025]
chapters: [11]
topics: [pointer-arithmetic, arrays]
difficulty: 2
type: multiple-choice
answer: "True"
stats: {responses: 152, accuracy: 67}
---

Η έκφραση `*(ptr + 4)` είναι ισοδύναμη με την έκφραση `ptr[4]`.

- True
- False

## Συχνή παρανόηση

Το 26% απάντησε False, θεωρώντας ότι οι αγκύλες είναι κάτι διαφορετικό από την αριθμητική δεικτών. Στην C το `ptr[n]` ορίζεται ακριβώς ως `*(ptr + n)`.

## Υπόδειξη

Θυμηθείτε πώς ορίζει η C τον τελεστή `[]` με βάση την αριθμητική δεικτών.
