---
id: kahoot-strcpy-literal-to-array
kind: kahoot
title: "strcpy από literal σε πίνακα"
source:
  title: "Kahoot «Εμβέλεια, Μνήμη και Συμβολοσειρές» (διάλεξη 14)"
  years: [2025]
chapters: [14]
topics: [strings, pointers]
difficulty: 3
type: multiple-choice
answer: "World"
stats: {responses: 97, accuracy: 32}
---

Τι θα τυπώσει ο παρακάτω κώδικας;

```c
char *s1 = "World", s2[] = "Hello";
strcpy(s2, s1);
printf("%s\n", s2);
```

- Hello
- World
- HelloWorld
- Θα κρασάρει

## Συχνή παρανόηση

Το 24% απάντησε ότι θα κρασάρει, μπερδεύοντας τους ρόλους: η `strcpy` γράφει στον πίνακα `s2`, που είναι εγγράψιμος και χωράει τα 6 bytes του `"World"`· το literal `s1` μόνο διαβάζεται.

## Υπόδειξη

Ποιος από τους δύο είναι πίνακας που μπορούμε να γράψουμε και ποιος δείχνει σε string literal; Σε ποιον γράφει η `strcpy`, και χωράει εκεί το αποτέλεσμα;
