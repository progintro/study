---
id: kahoot-strcat-self-overflow
kind: kahoot
title: "Η strcat με τον εαυτό της"
source:
  title: "Kahoot «Δυαδική Αναζήτηση, Ταξινόμηση, Πολυπλοκότητα και άλλα» και «Εμβέλεια, Μνήμη και Συμβολοσειρές» (διάλεξη 14)"
  years: [2024, 2025]
chapters: [14]
topics: [strings, undefined-behavior, arrays]
difficulty: 3
type: multiple-choice
answer: "Πιθανόν να κρασάρει"
stats: {responses: 127, accuracy: 24}
---

Τι θα τυπώσει ο παρακάτω κώδικας;

```c
char fruit[10];
strcpy(fruit, "banana");
strcat(fruit, fruit);
strcat(fruit, fruit);
printf("%s", fruit);
```

- banana
- bananabanana
- bananabananabananabanana
- Πιθανόν να κρασάρει

## Συχνή παρανόηση

Το 34% επέλεξε `bananabananabananabanana` και το 24% `bananabanana`, κοιτάζοντας μόνο τη λογική της συνένωσης: ο πίνακας έχει 10 bytes, οπότε ήδη η πρώτη `strcat` γράφει εκτός ορίων, και η επικάλυψη πηγής και προορισμού είναι από μόνη της απροσδιόριστη συμπεριφορά.

## Υπόδειξη

Μετρήστε πόσα bytes χρειάζεται το αποτέλεσμα, μαζί με το `'\0'`, και συγκρίνετε με το μέγεθος του `fruit`. Σκεφτείτε επίσης τι σημαίνει για την `strcat` να διαβάζει από τον ίδιο πίνακα στον οποίο γράφει.
