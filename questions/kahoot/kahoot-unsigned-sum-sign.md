---
id: kahoot-unsigned-sum-sign
kind: kahoot
title: "Άθροισμα θετικών unsigned int"
source:
  title: "Kahoot «Μεταβλητές και Μνήμη», «Μεταβλητές και Συναρτήσεις» (διάλεξη 2)"
  years: [2024, 2025]
chapters: [2]
topics: [integer-representation, types]
difficulty: 2
type: multiple-choice
answer: "Ναι"
stats: {responses: 301, accuracy: 63}
---

Αν προσθέσω δύο θετικούς αριθμούς τύπου `unsigned int`, το αποτέλεσμα είναι πάντα θετικό;

- Ναι
- Όχι

## Συχνή παρανόηση

Το 30% απάντησε «Όχι», μεταφέροντας τη συμπεριφορά του `int` (όπου η υπερχείλιση δίνει αρνητικό) στους unsigned· ένας `unsigned int` αναδιπλώνεται modulo $2^{32}$ και δεν γίνεται ποτέ αρνητικός (αυστηρά, μπορεί να βγει 0 ή μικρότερος από τους προσθετέους).

## Υπόδειξη

Ποιες τιμές μπορεί να αναπαραστήσει καθόλου ένας `unsigned int`; Υπάρχει στο εύρος του κάποιος αρνητικός;
