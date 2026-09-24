---
id: hw-2023-hw2-fauxtoshop
kind: homework
title: "FauxtoShop: περιστροφή εικόνας BMP"
source:
  title: "Εργασία 2 (2023-24), Άσκηση 1"
  url: https://github.com/progintro/progintro.github.io/releases/download/2023/hw2.pdf
  years: [2023]
chapters: [12, 13, 18]
topics: [image-audio, multidim-arrays, dynamic-memory, redirection]
difficulty: 3
type: programming
---

Πολύ συχνά βγάζουμε φωτογραφίες που δεν έχουν τον σωστό προσανατολισμό και θέλουμε να
τις περιστρέψουμε, χωρίς τους περιορισμούς (κόστος, μέγεθος εικόνας) των προγραμμάτων
επεξεργασίας εικόνας.

Το ζητούμενο σε αυτήν την άσκηση είναι να υλοποιήσουμε το δικό μας `fauxtoshop` που μας
επιτρέπει να περιστρέψουμε εικόνες τύπου
[BMP (BitMaP)](https://en.wikipedia.org/wiki/BMP_file_format) δεξιόστροφα κατά 90° (με
την φορά του ρολογιού). Προκειμένου να το καταφέρουμε αυτό, θα χρειαστεί να μάθουμε λίγο
παραπάνω για την μορφή των αρχείων BMP. Σε αυτήν την άσκηση θα ασχοληθούμε με μια
κατηγορία αρχείων BMP τα οποία έχουν την μορφή κεφαλίδων (headers) ακολουθούμενη από
κάποια bytes και έναν δισδιάστατο πίνακα εικονοστοιχείων (pixels):

```text
Headers (H bytes) | Other Data (M bytes) | Pixel 2-D array (N bytes)
```

Τα Σχήματα 1 και 2 της εκφώνησης παρουσιάζουν την ανάλυση των περιεχομένων ενός
ενδεικτικού αρχείου `color6x6.bmp`. Για τις ανάγκες της άσκησης, μπορείτε να υποθέσετε
ότι H ≥ 54 και ότι τα δεδομένα ανάμεσα στις κεφαλίδες Other Data δεν χρειάζονται αλλαγή
αλλά πρέπει να αντιγραφούν όπως είναι.

**Σχήμα 1** (τα 54 πρώτα bytes της κεφαλίδας, με την εντολή `xxd`):

```text
$ xxd -l 54 -g 1 -c 14 < color6x6.bmp
00000000: 42 4d ae 00 00 00 00 00 00 00 36 00 00 00  BM........6...
0000000e: 28 00 00 00 06 00 00 00 06 00 00 00 01 00  (.............
0000001c: 18 00 00 00 00 00 78 00 00 00 c4 0e 00 00  ......x.......
0000002a: c4 0e 00 00 00 00 00 00 00 00 00 00        ............
```

Τα σχόλια του σχήματος εξηγούν τα καίρια πεδία (απαραίτητα για την άσκηση):

- Τα αρχεία bmp αρχίζουν με τους χαρακτήρες 'B' και 'M' (magic number 0x42 0x4d).
- Στο 2ο byte της κεφαλίδας περιέχεται το μέγεθος του αρχείου (εδώ 174 bytes).
- Στο 10ο byte της κεφαλίδας περιέχεται το offset του πίνακα των pixels σε μορφή little
  endian (εδώ 54).
- Στο 18ο byte της κεφαλίδας περιέχεται το πλάτος (width) της εικόνας σε pixels σε μορφή
  little endian.
- Στο 22ο byte της κεφαλίδας περιέχεται το ύψος (height) της εικόνας σε pixels σε μορφή
  little endian.
- Στο 34ο byte της κεφαλίδας περιέχεται το συνολικό μέγεθος της εικόνας σε bytes σε
  μορφή little endian.

**Σχήμα 2** (μόνο τα bytes των pixels, παραλείποντας τα 54 πρώτα):

```text
$ xxd -s 54 -c 20 -g 3 < color6x6.bmp
00000036: 00ffff 00ffff 00ffff ff0000 ff0000 ff0000 0000
0000004a: 00ffff 00ffff 00ffff ff0000 ff0000 ff0000 0000
0000005e: 00ffff 00ffff 00ffff ff0000 ff0000 ff0000 0000
00000072: 0000ff 0000ff 0000ff 00ff00 00ff00 00ff00 0000
00000086: 0000ff 0000ff 0000ff 00ff00 00ff00 00ff00 0000
0000009a: 0000ff 0000ff 0000ff 00ff00 00ff00 00ff00 0000
```

Κάθε pixel είναι 3 bytes με σειρά B, G, R. Κάθε γραμμή έχει στο τέλος 2 bytes padding
ώστε κάθε γραμμή να είναι πολλαπλάσιο του 4. Η πρώτη γραμμή του αρχείου είναι η κάτω
γραμμή της εικόνας: το `pixels[0][0]` είναι το κάτω αριστερά pixel (κίτρινο) και το
`pixels[4][1]` ένα κόκκινο pixel της πάνω αριστερά περιοχής. Η εικόνα έχει κίτρινο
τεταρτημόριο κάτω αριστερά, μπλε κάτω δεξιά, κόκκινο πάνω αριστερά και πράσινο πάνω
δεξιά. Δίνουμε **προσοχή στο padding** που μπορεί να έχει το κάθε αρχείο bmp το οποίο
δεν έχει απεικόνιση για τους χρήστες.

**Τεχνικές Προδιαγραφές**

- Repository Name: `progintro/hw2-<YourUsername>`
- C Filepath: `fauxtoshop/src/fauxtoshop.c`
- Ένα αρχείο εισόδου/εξόδου BMP είναι δεκτό μόνο εάν:
  - Ξεκινάει την μαγική κεφαλίδα με τα bytes: 'B' 'M'.
  - Χρησιμοποιεί 24-bit για την αναπαράσταση χρώματος (μονοχρωματικά BMP δεν είναι
    δεκτά).
  - Χρησιμοποιεί τουλάχιστον 54 (14 + 40) bytes για την αναπαράσταση των κεφαλίδων
    ακολουθώντας το Windows 3.x format (Bitmap file header + DIB header). Για
    παράδειγμα, αρχεία που είναι συμβατά με την μορφή κεφαλίδας που δείχνουμε στο
    Σχήμα 1 είναι δεκτά.
  - Έχει σωστό μέγεθος αρχείου (τα μεγέθη στις κεφαλίδες συμφωνούν με τα περιεχόμενα
    του αρχείου).
  - Έχει σωστό μήκος, πλάτος και padding.
- Το πρόγραμμά θα πρέπει να παίρνει είσοδο από το standard input. Για οποιαδήποτε
  είσοδο δεν είναι μέσα στις προδιαγραφές το πρόγραμμα πρέπει να επιστρέφει με κωδικό
  εξόδου (exit code) 1.
- Ένα αρχείο `image.bmp` μπορεί να περαστεί στο πρόγραμμά μας με ανακατεύθυνση
  (redirection) στο stdin και αντίστοιχα η έξοδος μπορεί να γραφτεί σε ένα αρχείο
  `rotated.bmp` και πάλι με ανακατεύθυνση του stdout:
  `$ ./fauxtoshop < image.bmp > rotated.bmp`
- Το αρχείο C που θα υποβληθεί πρέπει να μεταγλωττίζεται χωρίς ειδοποιήσεις για λάθη
  και με κωδικό επιστροφής (exit code) που να είναι 0. Συγκεκριμένα, το αρχείο σας
  **πρέπει** να μπορεί να μεταγλωττιστεί επιτυχώς με την ακόλουθη εντολή σε ένα από τα
  μηχανήματα του εργαστηρίου (linuxXY.di.uoa.gr):
  `gcc -O3 -Wall -Wextra -Werror -pedantic -o fauxtoshop fauxtoshop.c`
- README Filepath: `fauxtoshop/README.md`
- **Ένα αρχείο που να περιέχει στοιχεία εισόδου και ένα εξόδου διαφορετικά από αυτά
  της άσκησης. Συγκεκριμένα προτείνουμε να βάλετε έναν συνδυασμό που θεωρείται ότι
  είναι δύσκολος να γίνει σωστός.**
  - input Filepath: `fauxtoshop/test/input.bmp`
  - output Filepath: `fauxtoshop/test/output.bmp`
- Πρέπει να ολοκληρώνει την εκτέλεση μέσα σε: 10 δευτερόλεπτα.
- **Δεν επιτρέπεται** η χρήση δομών/εγγραφών (`struct`).

Παρακάτω παραθέτουμε την αλληλεπίδραση με μια ενδεικτική λύση (το Σχήμα 3 της
εκφώνησης δείχνει την εικόνα `Apparition_of_Face_and_Fruit.bmp` πριν και μετά την
περιστροφή):

```text
$ gcc -O3 -Wall -Wextra -Werror -pedantic -o fauxtoshop fauxtoshop.c
$ ./fauxtoshop < ./fauxtoshop
Error: not a BMP file
$ echo $?
1
$ ./fauxtoshop < color6x6.bmp > color6x6.90.bmp
$ ./fauxtoshop < color6x6.90.bmp > color6x6.180.bmp
$ ./fauxtoshop < color6x6.180.bmp > color6x6.270.bmp
$ ./fauxtoshop < color6x6.270.bmp > color6x6.360.bmp
$ md5sum color6x6*.bmp
755c07991c51c0b3af855ba7f668c7d0  color6x6.180.bmp
5f19168fa9511a6520ec5dba2db4b478  color6x6.270.bmp
33855d8642cf110f74464f8ff78449aa  color6x6.360.bmp
6d62a0c4264dbfa962b372b6e5c8b9be  color6x6.90.bmp
33855d8642cf110f74464f8ff78449aa  color6x6.bmp
$ wc -c color6x6*.bmp
174 color6x6.180.bmp
174 color6x6.270.bmp
174 color6x6.360.bmp
174 color6x6.90.bmp
174 color6x6.bmp
$ ./fauxtoshop < Apparition_of_Face_and_Fruit.bmp > app90.bmp
$ md5sum Apparition_of_Face_and_Fruit.bmp app90.bmp
841d3634ba8c6af641d86b63ac1b6dfc  Apparition_of_Face_and_Fruit.bmp
96e8c33582f8a922a6665d4891e62a77  app90.bmp
$ wc -c Apparition_of_Face_and_Fruit.bmp app90.bmp
1440054 Apparition_of_Face_and_Fruit.bmp
1440054 app90.bmp
2880108 total
$ ./fauxtoshop < school_of_athens.bmp > school_of_athens90.bmp
$ md5sum school_of_athens*.bmp
282d01bbd23044a7e6ca91f0dda2238f  school_of_athens90.bmp
112ce7f3a60265992dc939949232257d  school_of_athens.bmp
$ wc -c school_of_athens*.bmp
15252534 school_of_athens.bmp
15257654 school_of_athens90.bmp
30510188 total
$ file school_of_athens.bmp school_of_athens90.bmp
school_of_athens.bmp:   PC bitmap, Windows 3.x format, 2560 x 1986 x 24,
                        image size 15252480, cbSize 15252534, bits offset 54
school_of_athens90.bmp: PC bitmap, Windows 3.x format, 1986 x 2560 x 24,
                        image size 15257600, cbSize 15257654, bits offset 54
$ ./fauxtoshop < school_of_athens.bmp |./fauxtoshop | ./fauxtoshop |
          ./fauxtoshop > school_of_athens360.bmp
$ md5sum school_of_athens*.bmp
112ce7f3a60265992dc939949232257d  school_of_athens360.bmp
282d01bbd23044a7e6ca91f0dda2238f  school_of_athens90.bmp
112ce7f3a60265992dc939949232257d  school_of_athens.bmp
```

Τα παραπάνω bmp αρχεία είναι στο: <https://github.com/progintro/data/tree/main/bmp>
άλλα μπορείτε να δοκιμάσετε και άλλα παραδείγματα εικόνων που βρίσκετε online. Εκτός από
`scp` για να τα αντιγράψετε στο Linux lab, μπορείτε να τα κατεβάσετε και μέσω κονσόλας
χρησιμοποιώντας `curl`, για παράδειγμα:

```text
$ curl -O https://raw.githubusercontent.com/progintro/data/main/bmp/color6x6.bmp
```

Ως συνήθως, στο αρχείο `README.md` πρέπει να προσθέσετε οποιεσδήποτε παρατηρήσεις σας
κατά την διεκπεραίωση της άσκησης. Ο κώδικας απαιτείται να είναι καλά τεκμηριωμένος με
σχόλια καθώς αυτό θα είναι μέρος της βαθμολόγησης.

## Υπόδειξη

Διαβάστε ολόκληρο το stdin σε έναν δυναμικά δεσμευμένο πίνακα από `unsigned char` και
γράψτε μια βοηθητική συνάρτηση που διαβάζει ακέραιο 4 bytes σε little endian από
δοσμένο offset. Υπολογίστε το μέγεθος κάθε γραμμής με το padding (στρογγυλοποίηση του
3·width στο επόμενο πολλαπλάσιο του 4) για την είσοδο *και* για την έξοδο, όπου πλάτος
και ύψος αλλάζουν θέση· ενημερώστε στην κεφαλίδα της εξόδου πλάτος, ύψος, μέγεθος
εικόνας και αρχείου. Δουλέψτε πρώτα την αντιστοίχιση θέσεων (γραμμή, στήλη) στο χαρτί με
τη μικρή `color6x6.bmp`, θυμηθείτε ότι οι γραμμές αποθηκεύονται από κάτω προς τα πάνω,
και δοκιμάστε με μια εικόνα μη τετράγωνη με πλάτος που δεν είναι πολλαπλάσιο του 4.

## Δείτε επίσης

- [Υποδειγματική υποβολή φοιτητή](https://progintro.github.io/samples/code/fauxtoshop1/) (περιέχει λύση: δείτε την αφού λύσετε την άσκηση)
