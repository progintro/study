---
id: exam-2023-fall-ex15-q4
kind: exam
title: "Δυνατότητες"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #15, Θέμα 4"
  url: https://progintro.github.io/exams/2023/fall/ex15/
  years: [2023]
chapters: [14, 18]
topics: [strings, files, command-line-args]
difficulty: 2
type: programming
---

Πρόγραμμα: `phone.c`

Σε κάποια τηλέφωνα, ίσως έχετε παρατηρήσει πως ο κάθε αριθμός αντιστοιχεί σε συγκεκριμένα γράμματα:

```text
1       2 ABC   3 DEF
4 GHI   5 JKL   6 MNO
7 PQRS  8 TUV   9 WXYZ
*       0       #
```

> Σημείωση: στο πρωτότυπο το πληκτρολόγιο δίνεται ως εικόνα ([phone.jpeg](https://progintro.github.io/exams/2023/fall/ex15/images/phone.jpeg)).

(2 -> ABC, 3 -> DEF, ... κοκ). Λέγοντας έναν αριθμό, μπορείς να περιγράψεις ένα σύνολο από λέξεις και το αντίστροφο: μια λέξη προσδιορίζει έναν συγκεκριμένο αριθμό. Για παράδειγμα, η λέξη CAT προσδιορίζει το 228 (C -> 2, A -> 2, T -> 8). Γράψτε ένα πρόγραμμα, το οποίο παίρνει ως πρώτο όρισμα ένα αρχείο με λέξεις (μία ανά γραμμή) και έναν αριθμό ως το δεύτερο όρισμα και τυπώνει όλες τις λέξεις που μπορούν να εκφραστούν με αυτόν τον αριθμό. Οποιοδήποτε ψηφίο δεν ταιριάζει σε κάποιο γράμμα (0, 1) θεωρείται "μπαλαντέρ", δηλαδή ταιριάζει με οποιοδήποτε γράμμα. Παραδείγματα εκτέλεσης ακολουθούν:

```text
$ gcc -o phone phone.c
$ ./phone words.txt
Usage: ./phone dictionary phone
$ cat words.txt
cat
dog
deep
purple
smoke
water
rain
spain
plain
$ ./phone words.txt 228
cat
$ ./phone words.txt 70000
smoke
spain
plain
$ ./phone words.txt 71246
spain
plain
$ ./phone /usr/share/dict/words 71246
Rabin
Robin
Rubin
Sabin
Spahn
Spain
plain
robin
slain
stain
swain
```

## Υπόδειξη

Φτιάξτε έναν πίνακα 26 θέσεων που αντιστοιχίζει κάθε γράμμα σε ψηφίο. Για κάθε λέξη του λεξικού ίδιου μήκους με τον αριθμό, συγκρίνετε θέση-θέση χωρίς διάκριση πεζών-κεφαλαίων, με τα 0 και 1 να ταιριάζουν με οτιδήποτε. Προσέξτε λέξεις με μη λατινικούς χαρακτήρες και το `'\n'` στο τέλος κάθε γραμμής.
