---
id: slides-lec14-palindrome
kind: slides
title: "Παλινδρομικό string"
source:
  title: "Διάλεξη 14, διαφάνειες 43–44"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec14.pdf
  years: [2025]
chapters: [14]
topics: [strings, arrays]
difficulty: 1
type: programming
---

Θέλω να ελέγξω αν ένα string είναι παλινδρομικό. Πώς;

Γράψτε μια συνάρτηση `int isPalindrome(char *str)` που επιστρέφει 1 αν το `str`
διαβάζεται ίδιο από την αρχή και από το τέλος, και 0 αλλιώς.

## Υπόδειξη

Χρησιμοποιήστε δύο δείκτες θέσης που ξεκινούν από τις δύο άκρες του string και
κινούνται ο ένας προς τον άλλο. Προσέξτε πού είναι ο τελευταίος χαρακτήρας: το
`strlen` δεν μετρά το null byte.
