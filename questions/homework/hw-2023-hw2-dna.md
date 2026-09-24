---
id: hw-2023-hw2-dna
kind: homework
title: "DNA Matching"
source:
  title: "Εργασία 2 (2023-24), Άσκηση 2"
  url: https://github.com/progintro/progintro.github.io/releases/download/2023/hw2.pdf
  years: [2023]
chapters: [25, 18, 14]
topics: [dynamic-programming, strings, files, dynamic-memory]
difficulty: 3
type: programming
---

Ένα εργαστήριο βιοπληροφορικής ψάχνει λύσεις για να βρίσκει *αποδοτικά* κοινές
αλληλουχίες DNA ανάμεσα σε διαφορετικά άτομα ή ακόμα και οργανισμούς, γνωστό και ως
[DNA matching](https://www.ancestry.com/cs/dna-help/matches/dna-matching).

Το [DNA](https://en.wikipedia.org/wiki/DNA) συνήθως το αναπαριστούμε με την μορφή μιας
αλυσίδας (συμβολοσειράς) από τέσσερα διαφορετικά στοιχεία που λέγονται *βάσεις*: A
(Αδενίνη), G (Γουανίνη), T (Θυμίνη) και C (Κυτοσίνη) τα οποία μπορούν να συνδυαστούν με
οποιαδήποτε σειρά. Προκειμένου να κάνουμε DNA matching θέλουμε να δούμε αν υπάρχουν
κοινά τμήματα σε αυτές τις αλυσίδες DNA και να δούμε πόσο μεγάλες είναι. Το Σχήμα 4 της
εκφώνησης δείχνει ένα παράδειγμα δύο αλυσίδων με κοινό τμήμα: οι αλυσίδες
`CATTAGATATAGACG` και `CTATAGATATAGGGC` έχουν κοινό το τμήμα `TAGATATAG`.

Για το ζητούμενο αυτής της άσκησης, καλείστε να γράψετε ένα πρόγραμμα που διαβάζει δύο
αλυσίδες DNA, βρίσκει την μέγιστη κοινή αλυσίδα ανάμεσα στις δύο και την τυπώνει.

**Τεχνικές Προδιαγραφές**

- Repository Name: `progintro/hw2-<YourUsername>`
- C Filepath: `dna/src/dna.c`
- Το πρόγραμμά σας θα πρέπει να παίρνει δύο ορίσματα από την γραμμή εντολών. Και τα δύο
  θα είναι ονόματα αρχείων που περιέχουν τις εισόδους για το πρόγραμμα, δηλαδή τις δύο
  αλυσίδες DNA - στην μορφή `./dna filename1 filename2`. Για το περιεχόμενο των αρχείων
  δείτε παρακάτω. Αν δεν περαστούν δύο ορίσματα στην γραμμή εντολών ή οποιοδήποτε από
  τα αρχεία δεν μπορεί να ανοιχτεί το πρόγραμμα πρέπει να επιστρέφει με κωδικό εξόδου
  (exit code) 1.
- Η βασική είσοδος για το πρόγραμμα θα είναι μέσω των περιεχομένων των αρχείων. Τα
  αρχεία θα περιέχουν τις αλυσίδες DNA οι οποίες αποτελούνται από τους κεφαλαίους
  χαρακτήρες A, G, T και C. Όλοι οι χαρακτήρες θα είναι σε μορφή ASCII, και το αρχείο θα
  διαβάζεται και ως κείμενο. Οποιοσδήποτε χαρακτήρας εκτός από τους A, G, T, C πρέπει να
  αγνοηθεί καθώς θεωρείται σφάλμα που δημιουργήθηκε κατά το
  [sequencing](https://en.wikipedia.org/wiki/DNA_sequencing) της αλυσίδας.
- Η έξοδος του προγράμματος θα πρέπει να είναι η μέγιστη κοινή αλυσίδα των δύο αλυσίδων
  που δώσαμε ως είσοδο, ακολουθούμενη από μια καινούρια γραμμή. Όλα τα στοιχεία της
  αλυσίδας εξόδου θα πρέπει να είναι βάσεις DNA - δεν επιτρέπονται άλλοι χαρακτήρες.
  Εάν υπάρχουν πάνω από μία μέγιστη κοινή αλυσίδα, αρκεί να επιστραφεί μία από αυτές.
- Το αρχείο C που θα υποβληθεί πρέπει να μεταγλωττίζεται χωρίς ειδοποιήσεις για λάθη
  και με κωδικό επιστροφής (exit code) που να είναι 0. Συγκεκριμένα, το αρχείο σας
  **πρέπει** να μπορεί να μεταγλωττιστεί επιτυχώς με την ακόλουθη εντολή σε ένα από τα
  μηχανήματα του εργαστηρίου (linuxXY.di.uoa.gr):
  `gcc -Ofast -m32 -Wall -Wextra -Werror -pedantic -o dna dna.c -lm`
- README Filepath: `dna/README.md`
- **Ένα αρχείο που να περιέχει στοιχεία εισόδου και ένα εξόδου διαφορετικά από αυτά
  της άσκησης. Συγκεκριμένα προτείνουμε να βάλετε έναν συνδυασμό που θεωρείται ότι
  είναι δύσκολος να γίνει σωστός.**
  - input1 Filepath: `dna/test/input1.dna`
  - input2 Filepath: `dna/test/input2.dna`
  - output Filepath: `dna/test/output.dna`
- Πρέπει να ολοκληρώνει την εκτέλεση μέσα σε: 90 δευτερόλεπτα.
- Το μέγιστο μέγεθος επιτρεπτής αλυσίδας: 100.000 βάσεις.

Παρακάτω παραθέτουμε την αλληλεπίδραση με μια ενδεικτική λύση με μερικά δείγματα DNA
που κατεβάσαμε:

```text
$ gcc -Ofast -Wall -Wextra -Werror -pedantic -o dna dna.c -lm
$ wc -c *.dna
 62487 alien.dna
  8193 carsonella-ruddii.dna
 47811 claviceps-purpurea.dna
 21992 escherichia-coli.dna
    16 sample1.dna
    16 sample2.dna
 99492 theobroma-cacao.dna
240007 total
$ $./dna
Error: arguments missing. Usage: ./dna dnafile1 dnafile2
$ echo $?
1
$ ./dna3 foo.bar bar.zonk
Error: cannot open file foo.bar
$ echo $?
1
$ cat sample1.dna
CATTAGATATAGACG
$ cat sample2.dna
CTATAGATATAGGGC
$ ./dna sample1.dna sample2.dna
TAGATATAG
$ echo -e "CTATAGAT\nHello WORLDATAGGG" > split.dna
$ ./dna split.dna split.dna
CTATAGATATAGGG
$ ./dna carsonella-ruddii.dna sample1.dna
ATATAGACG
$ ./dna escherichia-coli.dna carsonella-ruddii.dna
AATTAAAATTTTATT
$ ./dna claviceps-purpurea.dna carsonella-ruddii.dna
GTTTTTTTTTTCT
$ time ./dna theobroma-cacao.dna escherichia-coli.dna
GGTTTGCTTTTATG

real 0m4.550s
user 0m4.549s
sys 0m0.001s
$ time ./dna theobroma-cacao.dna alien.dna
AAAAAAAAAAAAAAAAACC

real 0m2.828s
user 0m2.827s
sys 0m0.001s
$ time ./dna theobroma-cacao.dna theobroma-cacao.dna > shared.dna

real 0m21.817s
user 0m21.815s
sys 0m0.001s
$ wc -c shared.dna
98165 shared.dna
$ md5sum shared.dna
5ca8c9e6fd76d46221d3beadd610b165  shared.dna
$ time ./dna alien.dna alien.dna > shared.dna

real 0m1.917s
user 0m1.915s
sys 0m0.001s
$ wc -c shared.dna
62488 shared.dna
$ md5sum shared.dna
d4544ab6971c6a54bb375159adc5852b  shared.dna
```

Τα παραπάνω dna αρχεία είναι στο: <https://github.com/progintro/data/tree/main/dna>
άλλα μπορείτε να δοκιμάσετε και άλλα παραδείγματα δικά σας. Στο αρχείο `README.md`
πρέπει να προσθέσετε οποιεσδήποτε παρατηρήσεις σας κατά την διεκπεραίωση της άσκησης. Ο
κώδικας απαιτείται να είναι καλά τεκμηριωμένος με σχόλια καθώς αυτό θα είναι μέρος της
βαθμολόγησης.

## Υπόδειξη

Πρόκειται για το πρόβλημα της μέγιστης κοινής *υποσυμβολοσειράς* (διαδοχικοί
χαρακτήρες, όχι υποακολουθία). Φιλτράρετε πρώτα κάθε αρχείο σε μια καθαρή συμβολοσειρά
μόνο με A, G, T, C, σε δυναμικά δεσμευμένη μνήμη. Μια σχέση του τύπου «μήκος κοινού
τμήματος που τελειώνει στη θέση i της πρώτης και j της δεύτερης» δίνει λύση
δυναμικού προγραμματισμού· ένας πλήρης πίνακας 100.000 × 100.000 όμως δεν χωράει στη
μνήμη, οπότε σκεφτείτε ποιες γραμμές του χρειάζεστε πραγματικά κάθε στιγμή.

## Δείτε επίσης

- [Υποδειγματική υποβολή φοιτητή](https://progintro.github.io/samples/code/dna1/) (περιέχει λύση: δείτε την αφού λύσετε την άσκηση)
