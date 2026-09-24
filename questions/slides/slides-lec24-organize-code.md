---
id: slides-lec24-organize-code
kind: slides
title: "Ο καλύτερος τρόπος οργάνωσης του κώδικα"
source:
  title: "Διάλεξη 24: Προχωρημένα Θέματα, διαφάνεια 15"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec24.pdf
  years: [2025]
chapters: [24, 23]
topics: [code-organization]
difficulty: 1
type: short-answer
---

Σε ένα μεγάλο έργο, όπως το [openssl](https://github.com/openssl/openssl/tree/master),
κάθε αρχείο περιέχει μεταβλητές και συναρτήσεις που σχετίζονται θεματικά, λειτουργικά
ή σύμφωνα με άλλα κριτήρια:

```text
├── README.md
├── ssl
│   ├── ssl_init.c
│   ├── event_queue.c
│   ├── ssl_err.c
│   ├── sslerr.h
...
├── test
│   ├── aborttest.c
│   ├── acvp_test.c
...
```

Ποιος είναι ο καλύτερος τρόπος να οργανώσουμε τον κώδικά μας;

## Υπόδειξη

Διακρίνετε τα αρχεία υλοποίησης (`.c`) από τα αρχεία κεφαλίδας (`.h`) και
σκεφτείτε τι πρέπει να βλέπει ένα αρχείο από ένα άλλο για να το χρησιμοποιήσει.
Αναρωτηθείτε επίσης με ποιο κριτήριο ομαδοποιούνται τα αρχεία στους καταλόγους (π.χ.
γιατί τα tests είναι χωριστά).
