---
id: exam-2023-fall-ex6-q2
kind: exam
title: "Μήνυμα από τον Καίσαρα"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #6 (Crypto Themed), Θέμα 2"
  url: https://progintro.github.io/exams/2023/fall/ex6/
  years: [2023]
chapters: [9, 5]
topics: [input-output, operators]
difficulty: 1
type: programming
---

Πρόγραμμα: `caesar.c` (25 μονάδες)

Υπάρχει ένας τρόπος κρυπτογράφησης που αποδίδεται στον Καίσαρα (Caesar Cipher) όπου κάθε γράμμα της αλφαβήτου αντιστοιχίζεται σε ένα άλλο. Για παράδειγμα με μετάθεση γραμμάτων κατά 3 παίρνουμε την ακόλουθη αντιστοίχιση:

![Αντιστοίχιση γραμμάτων](https://progintro.github.io/exams/2023/fall/ex6/images/caesar.png)

Όπου το A αντιστοιχεί στο Z, το D στο A, κοκ. Γράψτε ένα πρόγραμμα που διαβάζει το κείμενο που δίνεται από την πρότυπη είσοδο (stdin) και το τυπώνει στην πρότυπη έξοδο (stdout) αφού το περάσει από κρυπτογράφηση με την μέθοδο του Καίσαρα όπου η μετατόπιση είναι 13, δηλαδή το A αντιστοιχεί στο N, το B αντιστοιχεί στο O κοκ. Το πρόγραμμα πρέπει να αντικαθιστά μόνο λατινικούς χαρακτήρες (A-Z, a-z) και όλοι οι υπόλοιποι πρέπει να μένουν ίδιοι. Παράδειγμα εκτέλεσης:

```text
$ gcc -o caesar caesar.c
$ cat toto.txt
Vg'f tbaan gnxr n ybg gb qent zr njnl sebz lbh� ,
Gurer'f abguvat gung n uhaqerq zra be zber pbhyq rire qb ,
V oyrff gur envaf qbja va Nsevpn ,
Tbaan gnxr fbzr gvzr gb qb gur guvatf jr arire unq !
$ ./caesar < toto.txt
It's gonna take a lot to drag me away from you� ,
There's nothing that a hundred men or more could ever do ,
I bless the rains down in Africa ,
Gonna take some time to do the things we never had !
```

## Υπόδειξη

Διαβάστε χαρακτήρα προς χαρακτήρα· για κεφαλαία και πεζά ξεχωριστά, υπολογίστε τη θέση του γράμματος στο αλφάβητο (`c - 'A'`), προσθέστε τη μετατόπιση και κάντε αναδίπλωση με `%`. Όλοι οι άλλοι χαρακτήρες, ακόμη και bytes που δεν είναι έγκυρο κείμενο, περνάνε αυτούσιοι. Αφού το αλφάβητο έχει 26 γράμματα, τι παθαίνει ένα κείμενο αν του εφαρμόσετε ROT13 δύο φορές;
