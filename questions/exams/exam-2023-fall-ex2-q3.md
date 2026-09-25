---
id: exam-2023-fall-ex2-q3
kind: exam
title: "Μίνι Βάση Δεδομένων"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #2 (Pokémon Themed), Θέμα 3"
  url: https://progintro.github.io/exams/2023/fall/ex2/
  years: [2023]
chapters: [18, 19, 13]
topics: [files, structs, sorting]
difficulty: 3
type: programming
---

Πρόγραμμα: `pokedex.c` (25 μονάδες)

Γράψτε ένα πρόγραμμα που παίρνει δύο ορίσματα: (1) το όνομα του αρχείο που περιέχει όλα τα pokémon που έχουμε πιάσει με όλα τα δεδομένα τους και (2) την ημερομηνία που αναζητούμε και επιστρέφει αναλυτικές πληροφορίες για όλα τα pokémon που πιάστηκαν *μετά* από εκείνη την ημερομηνία ταξινομημένα. Παράδειγμα εκτέλεσης ακολουθεί:

```text
$ cat pokedex.db
name, date_caught, level
geodude, 15-02-2024, 15
slowpoke, 16-01-2024, 20
pidgeotto, 19-02-2024, 5
bulbasaur, 01-01-2005, 37
onix, 31-07-2021, 21
gyarados, 20-12-2018, 19
$ gcc -o pokedex pokedex.c
$ ./pokedex pokedex.db 19-02-2024
pidgeotto was caught on 19-02-2024 and is level 5
$ ./pokedex pokedex.db 01-01-2024
slowpoke was caught on 16-01-2024 and is level 20
geodude was caught on 15-02-2024 and is level 15
pidgeotto was caught on 19-02-2024 and is level 5
```

## Υπόδειξη

Παραλείψτε τη γραμμή-επικεφαλίδα, διαβάστε κάθε εγγραφή σε ένα `struct` με `fgets` και `sscanf`, και μετατρέψτε την ημερομηνία `ΗΗ-ΜΜ-ΕΕΕΕ` σε έναν ακέραιο που συγκρίνεται σωστά (π.χ. έτος, μετά μήνας, μετά μέρα). Φιλτράρετε, ταξινομήστε κατά ημερομηνία με `qsort` και προσέξτε από το πρώτο παράδειγμα αν η ημερομηνία αναζήτησης περιλαμβάνεται. Επικυρώστε την ημερομηνία του ορίσματος (μορφή και εύρος μήνα/ημέρας).
