---
id: kahoot-scanf-return-partial
kind: kahoot
title: "Τιμή επιστροφής της scanf με λάθος είσοδο"
source:
  title: "Kahoot «Δεδομένα Εισόδου» (διάλεξη 9)"
  years: [2025]
chapters: [9]
topics: [input-output, input-validation]
difficulty: 3
type: multiple-choice
answer: "1"
stats: {responses: 244, accuracy: 11}
---

Έδωσα την ακολουθία `42 hello 43` στο πρόγραμμά μου:

```c
scanf("%d%d", &n1, &n2);
```

Ποια η τιμή επιστροφής της `scanf`;

- 42 42
- 42 43
- 1
- EOF

## Συχνή παρανόηση

Το 42% επέλεξε `42 43`, μπερδεύοντας την τιμή επιστροφής της `scanf` με τις τιμές που αποθηκεύει στις μεταβλητές, και ξεχνώντας ότι σταματά στο `hello`.

## Υπόδειξη

Η `scanf` δεν επιστρέφει τις τιμές που διάβασε αλλά πόσες μετατροπές πέτυχαν. Σκεφτείτε πού σταματά όταν συναντήσει κάτι που δεν είναι ακέραιος.
