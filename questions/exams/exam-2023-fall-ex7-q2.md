---
id: exam-2023-fall-ex7-q2
kind: exam
title: "Κρυφό Μήνυμα"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #7 (Star Wars Themed), Θέμα 2"
  url: https://progintro.github.io/exams/2023/fall/ex7/
  years: [2023]
chapters: [18, 5]
topics: [files, bitwise, command-line-args]
difficulty: 1
type: programming
---

> Σημαντικό: φροντίζουμε τα προγράμματά μας να είναι ευανάγνωστα, αποδοτικά (σε χώρο και χρόνο) και να έχουν έξοδο όμοια με τα παραδείγματα εκτέλεσης καθώς αυτό είναι μέρος της βαθμολόγησης. Για οποιαδήποτε είσοδο εκτός προδιαγραφών το πρόγραμμα πρέπει να τερματίζει με exit code 1 και αντίστοιχο μήνυμα σφάλματος.

Πρόγραμμα: `r2d2.c` (25 μονάδες)

Γράψτε ένα πρόγραμμα που παίρνει ως ορίσματα δύο ονόματα αρχείων και στην συνέχεια τυπώνει το xor των bytes των δύο αρχείων. Για κάθε byte του πρώτου αρχείου a0, a1, a2 και κάθε byte του δεύτερου αρχείου b0, b1, b2 το πρόγραμμά σας θα πρέπει να τυπώνει τα bytes `a0 xor b0`, `a1 xor b1`, `a2 xor b2`. Παράδειγμα εκτέλεσης ακολουθεί:

```text
$ gcc -o r2d2 r2d2.c
$ hexdump -C message.txt
00000000  3b 04 9f da fe db 32 10  28 6a b7 2c c0 a8 bb ee  |;.....2.(j.,....|
00000010  12 fa 32 1a 3e c7 a8 ec  dd 56 a7 11 c7 e0 07 95  |..2.>....V......|
...
00000140  2d cd fe 38 24                                    |-..8$|
00000145
$ hexdump -C key.txt
00000000  68 70 ed b3 95 b2 5c 77  08 0c c5 43 ad 88 da ce  |hp....\w...C....|
00000010  74 95 40 6e 4c a2 db 9f  fd 3e ce 75 a3 85 69 b5  |t.@nL....>.u..i.|
...
00000140  48 bb 9b 4a 0a                                    |H..J.|
00000145
$ ./r2d2 message.txt key.txt
Striking from a fortress hidden among the billion stars of the galaxy, rebel spaceships have won their first victory in a battle with the powerful Imperial Starfleet. The EMPIRE fears that another defeat could bring a thousand more solar systems into the rebellion, and Imperial control over the galaxy would be lost forever.
```

Παρατηρήστε ότι το a0 είναι 0x3b και το b0 είναι 0x68 και το 0x3b xor 0x68 κάνει 0x53 ('S'). Το υπόλοιπο μήνυμα προκύπτει με αντίστοιχο τρόπο.

> Σημείωση: τα δύο hexdump (0x145 = 325 bytes το καθένα) συντομεύτηκαν εδώ· τα αρχεία είναι τα [message.txt](https://progintro.github.io/exams/2023/fall/ex7/message.txt) και [key.txt](https://progintro.github.io/exams/2023/fall/ex7/key.txt).

## Υπόδειξη

Ανοίξτε και τα δύο αρχεία σε δυαδική λειτουργία (`"rb"`), διαβάστε ένα byte από το καθένα σε κάθε βήμα με `fgetc` και γράψτε το αποτέλεσμα του τελεστή `^` με `putchar`. Ελέγξτε το `EOF` πριν το χρησιμοποιήσετε ως byte, και αποφασίστε τι σημαίνει το να έχουν τα δύο αρχεία διαφορετικό μήκος.
