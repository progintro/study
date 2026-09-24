---
id: exam-2023-fall-ex4-q4
kind: exam
title: "Αλλαγή Μεγέθους"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #4 (Rick Astley Themed), Θέμα 4"
  url: https://progintro.github.io/exams/2023/fall/ex4/
  years: [2023]
chapters: [18, 12]
topics: [files, bitwise, command-line-args]
difficulty: 2
type: programming
---

> Σημαντικό: φροντίζουμε τα προγράμματά μας να είναι ευανάγνωστα, αποδοτικά (σε χώρο και χρόνο) και να έχουν έξοδο όμοια με τα παραδείγματα εκτέλεσης καθώς αυτό είναι μέρος της βαθμολόγησης. Για οποιαδήποτε είσοδο εκτός προδιαγραφών το πρόγραμμα πρέπει να τερματίζει με exit code 1 και αντίστοιχο μήνυμα σφάλματος.

Πρόγραμμα: `crop.c` (25 μονάδες)

Γράψτε ένα πρόγραμμα το οποίο παίρνει 3 ορίσματα: (1) το όνομα ενός αρχείου, (2) την τοποθεσία (offset) σε αριθμό bytes μέσα στο αρχείο και (3) έναν αριθμό των δύο bytes (short) και τυπώνει στην πρότυπη έξοδο (stdout) το περιεχόμενο του αρχείου με τα δύο bytes στην τοποθεσία που αναφέρθηκε να έχουν αντικατασταθεί από τα bytes του αριθμού που δόθηκε από την γραμμή εντολών (όρισμα 3). Το υπόλοιπο αρχείο δεν πρέπει να αλλαχθεί. Τα αρχεία που θα δοθούν θα είναι μέχρι 100ΜΒ. Η εκτέλεση `./crop file 2 13362` σημαίνει διάβασε το αρχείο `file` και στο byte στην θέση `2` τοποθέτησε τα δύο bytes του αριθμού `13362`. Παραδείγματα εκτέλεσης ακολουθούν:

```text
$ gcc -o crop crop.c
$ echo example > file
$ hexdump -C file
00000000  65 78 61 6d 70 6c 65 0a                           |example.|
00000008
$ ./crop file 2 13362 > file2
$ hexdump -C file2
00000000  65 78 34 32 70 6c 65 0a                           |ex42ple.|
00000008
$ file rick.jpg
rick.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 96x96, segment length 16, comment: "CREATOR: gd-jpeg v1.0 (using IJG JPEG v62), quality = 80", baseline, precision 8, 640x436, components 3
$ ./crop rick.jpg 224 218 > rick2.jpg
$ file rick2.jpg
rick2.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 96x96, segment length 16, comment: "CREATOR: gd-jpeg v1.0 (using IJG JPEG v62), quality = 80", baseline, precision 8, 640x218, components 3
```

Παρακάτω δείχνουμε το αποτέλεσμα της εκτέλεσης στην εικόνα [rick.jpg](https://progintro.github.io/exams/2023/fall/ex4/rick.jpg) (πριν):

![rick before](https://progintro.github.io/exams/2023/fall/ex4/rick.jpg)

Και μετά:

![rick after](https://progintro.github.io/exams/2023/fall/ex4/images/rick2.jpg)

## Υπόδειξη

Ανοίξτε το αρχείο σε δυαδική λειτουργία (`"rb"`) και αντιγράψτε το στην έξοδο byte προς byte ή σε μπλοκ, αντικαθιστώντας μόνο τα bytes στις θέσεις `offset` και `offset + 1`. Γράψτε το 13362 στο δεκαεξαδικό και συγκρίνετε με το hexdump για να δείτε με ποια σειρά μπαίνουν τα δύο bytes (endianness)· τα βγάζετε με ολισθήσεις και μάσκες, όχι με `memcpy` από ένα `short`. Ελέγξτε ότι ο αριθμός χωράει σε δύο bytes και ότι το offset δεν ξεπερνά το μέγεθος του αρχείου.
