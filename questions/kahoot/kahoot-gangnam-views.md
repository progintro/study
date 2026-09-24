---
id: kahoot-gangnam-views
kind: kahoot
title: "Ο μετρητής του Gangnam Style"
source:
  title: "Kahoot «Μεταβλητές και Μνήμη», «Μεταβλητές και Συναρτήσεις» (διάλεξη 2)"
  years: [2024, 2025]
chapters: [2]
topics: [types, integer-representation]
difficulty: 2
type: multiple-choice
answer: "int"
stats: {responses: 301, accuracy: 41}
---

Όταν το Gangnam Style στο YouTube κόντευε τα 2 δις views, η Google άλλαξε τον τύπο των views. Τι τύπου ήταν αρχικά;

- `char`
- `double`
- `int64_t`
- `int`

## Συχνή παρανόηση

Το 26% διάλεξε `int64_t`, που είναι ο τύπος στον οποίο μετέβη η Google *μετά*· ένας 64-bit ακέραιος δεν θα κόντευε ποτέ να υπερχειλίσει στα 2 δις.

## Υπόδειξη

Ποιος από τους τύπους έχει μέγιστη τιμή κοντά στα 2 δισεκατομμύρια; Υπολογίστε το $2^{31}$.
