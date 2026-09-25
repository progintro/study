---
id: exam-2023-fall-ex6-q4
kind: exam
title: "Ταξινόμηση Αρχείων Καταγραφής"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #6 (Crypto Themed), Θέμα 4"
  url: https://progintro.github.io/exams/2023/fall/ex6/
  years: [2023]
chapters: [18, 13, 14]
topics: [sorting, files, strings]
difficulty: 2
type: programming
---

Πρόγραμμα: `sortlog.c` (25 μονάδες)

Γράψτε ένα πρόγραμμα το οποίο παίρνει ως όρισμα το όνομα ενός αρχείου που περιέχει δεδομένα από αρχεία καταγραφής (logs) και τυπώνει όλα τα μηνύματα ταξινομημένα με βαση την ημερομηνία καταγραφής σε αύξουσα σειρά (δηλαδή πρώτα οι ημερομηνίες που είναι νωρίτερα). Κάθε γραμμή καταγραφής έχει την μορφή ημερομηνίας με ακρίβεια λεπτού (μορφής "χρόνος-μήνας-ημέρα Τ ώρες:λεπτά") ακολουθούμενη από `:` και μετά το μήνυμα της καταγραφής. Παράδειγμα επιτυχούς εκτέλεσης ακολουθεί:

```text
$ gcc -o sortlog sortlog.c
$ cat logs.txt
2024-03-02T13:20: Info: New user 'developer' created successfully.
2000-07-18T07:00: System startup sequence completed successfully.
2024-12-12T11:25: 'admin' initiated system reboot after security patch application.
2024-11-07T08:15: Scheduled backup started for database 'TestDB'.
2024-12-01T09:00: System startup sequence initiated.
2024-03-15T05:45: System shutdown sequence initiated.
2024-03-02T10:30: User 'admin' logged in from IP address 192.168.1.105.
2024-02-05T16:30: Warning: Disk usage exceeds 85% on drive C:.
2004-03-09T21:00: Error: Network timeout while connecting to server 'backup.example.com'.
2025-03-04T14:45: Database connection established successfully.
$ ./sortlog logs.txt
2000-07-18T07:00: System startup sequence completed successfully.
2004-03-09T21:00: Error: Network timeout while connecting to server 'backup.example.com'.
2024-02-05T16:30: Warning: Disk usage exceeds 85% on drive C:.
2024-03-02T10:30: User 'admin' logged in from IP address 192.168.1.105.
2024-03-02T13:20: Info: New user 'developer' created successfully.
2024-03-15T05:45: System shutdown sequence initiated.
2024-11-07T08:15: Scheduled backup started for database 'TestDB'.
2024-12-01T09:00: System startup sequence initiated.
2024-12-12T11:25: 'admin' initiated system reboot after security patch application.
2025-03-04T14:45: Database connection established successfully.
```

## Υπόδειξη

Διαβάστε όλες τις γραμμές σε έναν πίνακα από δείκτες σε δυναμικά δεσμευμένες συμβολοσειρές (δεν ξέρετε ούτε πόσες είναι ούτε πόσο μεγάλες) και ταξινομήστε τον με `qsort`. Παρατηρήστε ότι στη μορφή `ΕΕΕΕ-ΜΜ-ΗΗTΩΩ:ΛΛ` η λεξικογραφική σύγκριση των πρώτων 16 χαρακτήρων συμπίπτει με τη χρονολογική. Ελέγξτε ότι κάθε γραμμή έχει πράγματι αυτή τη μορφή, και σκεφτείτε αν σας ενδιαφέρει η σειρά γραμμών με την ίδια ώρα.
