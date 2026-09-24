---
id: kahoot-expression-tree-eval
kind: kahoot
title: "Αποτίμηση δέντρου εκφράσεων"
source:
  title: "Kahoot «Λίστες, Δέντρα and Beyond»"
  years: [2025]
chapters: [22]
topics: [trees, recursion]
difficulty: 3
type: multiple-choice
answer: "postorder"
stats: {responses: 93, accuracy: 35}
---

Θέλω να γράψω έναν αποτιμητή εκφράσεων που αναπαρίστανται με δέντρα. Προτιμώ διάσχιση:

- preorder
- inorder
- postorder
- Δεν χρειάζομαι διάσχιση, το κάνω σε O(1)

## Συχνή παρανόηση

Το 28% επέλεξε preorder, όμως για να εφαρμόσουμε τον τελεστή της ρίζας χρειαζόμαστε πρώτα τις τιμές και των δύο υποδέντρων.

## Υπόδειξη

Σε έναν κόμβο `+` με παιδιά τις υποεκφράσεις, τι πρέπει να έχετε υπολογίσει πριν κάνετε την πρόσθεση;
