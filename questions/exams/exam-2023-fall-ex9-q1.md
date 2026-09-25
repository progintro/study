---
id: exam-2023-fall-ex9-q1
kind: exam
title: "Έλεγχος Εκτελέσιμου"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #9, Θέμα 1"
  url: https://progintro.github.io/exams/2023/fall/ex9/
  years: [2023]
chapters: [18]
topics: [files]
difficulty: 1
type: programming
---

Πρόγραμμα: `elf.c`

Γράψτε ένα πρόγραμμα που παίρνει ως όρισμα το όνομα ενός αρχείου και αποφαίνεται για το αν το αρχείο είναι ένα Linux εκτελέσιμο ELF (Executable and Linking Format) ή όχι. Ένα αρχείο θεωρείται ELF όταν ξεκινάει με τους χαρακτήρες 0x7f, E, L, F. Οποιοδήποτε άλλο αρχείο δεν θεωρείται ELF. Παραδείγματα εκτέλεσης ακολουθούν:

```text
$ gcc -o elf elf.c
$ ./elf foo
Error: Unable to read file
$ ./elf message.txt
message.txt is NOT an ELF file.
$ ./elf ./elf.c
./elf.c is NOT an ELF file.
$ ./elf ./elf
./elf is an ELF file.
$ ./elf /bin/ls
/bin/ls is an ELF file.
$ ./elf /lib/x86_64-linux-gnu/libc.so.6
/lib/x86_64-linux-gnu/libc.so.6 is an ELF file.
```

## Υπόδειξη

Ανοίξτε το αρχείο σε δυαδική μορφή (`"rb"`) και διαβάστε μόνο τα πρώτα 4 bytes. Σκεφτείτε τις ακραίες περιπτώσεις: αρχείο που δεν ανοίγει, αρχείο με λιγότερα από 4 bytes, λάθος πλήθος ορισμάτων.
