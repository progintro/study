---
id: exam-2023-fall-ex3-q1
kind: exam
title: "Προσθήκη Νιφάδων"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #3 (Frozen Themed), Θέμα 1"
  url: https://progintro.github.io/exams/2023/fall/ex3/
  years: [2023]
chapters: [9]
topics: [input-output]
difficulty: 2
type: programming
---

Πρόγραμμα: `snow.c` (25 μονάδες)

Γράψτε ένα πρόγραμμα που διαβάζει το κείμενο που δίνεται από την πρότυπη είσοδο (stdin) και τυπώνει την κάθε λέξη χαρακτήρα στην πρότυπη έξοδο (stdout) εμπλουτισμένη με νιφάδες, δηλαδή με τον χαρακτήρα `*`. Νιφάδες μπαίνουν μόνο ανάμεσα στα γράμματα της κάθε λέξης. Λέξεις με μόνο ένα γράμμα δεν χρειάζονται κάποια προσθήκη. Οι λέξεις αποτελούνται από τα γράμματα A-Z και a-z. Αριθμοί ή σημεία στίξης *δεν* θεωρούνται λέξεις. Παράδειγμα εκτέλεσης:

```text
$ cat elsa.txt
	Let it go, let it go�,
	Turn away and slam the door ,
	I don't care what they're going to say ,
	Let the storm rage on ,
	The cold never bothered me anyway !
$ gcc -o snow snow.c
$ ./snow < elsa.txt
	L*e*t i*t g*o, l*e*t i*t g*o�,
	T*u*r*n a*w*a*y a*n*d s*l*a*m t*h*e d*o*o*r ,
	I d*o*n't c*a*r*e w*h*a*t t*h*e*y'r*e g*o*i*n*g t*o s*a*y ,
	L*e*t t*h*e s*t*o*r*m r*a*g*e o*n ,
	T*h*e c*o*l*d n*e*v*e*r b*o*t*h*e*r*e*d m*e a*n*y*w*a*y !
```

## Υπόδειξη

Διαβάστε χαρακτήρα προς χαρακτήρα και θυμηθείτε μόνο αν ο προηγούμενος χαρακτήρας ήταν γράμμα: η νιφάδα μπαίνει ακριβώς όταν δύο γράμματα είναι διαδοχικά. Κοιτάξτε στο παράδειγμα τι συμβαίνει στο `don't` και στο `they're`. Προσέξτε ότι η `isalpha` εξαρτάται από το locale, ενώ η εκφώνηση ορίζει ρητά A-Z και a-z.
