---
id: kahoot-getchar-257-values
kind: kahoot
title: "Πόσες τιμές επιστρέφει η getchar"
source:
  title: "Kahoot «Δεδομένα Εισόδου» (διάλεξη 9)"
  years: [2025]
chapters: [9]
topics: [input-output, types]
difficulty: 3
type: multiple-choice
answer: "257"
stats: {responses: 244, accuracy: 18}
---

Πόσες διαφορετικές τιμές μπορεί να πάρει η τιμή επιστροφής της `getchar()`;

- 0
- 128
- 256
- 257

## Συχνή παρανόηση

Το 64% επέλεξε 256, μετρώντας μόνο τις τιμές ενός byte και ξεχνώντας την επιπλέον τιμή `EOF`, που είναι και ο λόγος που η `getchar` επιστρέφει `int`.

## Υπόδειξη

Μετρήστε πόσοι διαφορετικοί χαρακτήρες (bytes) μπορούν να διαβαστούν και μην ξεχάσετε ότι υπάρχει και μία ακόμη ειδική τιμή.
