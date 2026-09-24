---
id: exam-2023-fall-ex5-q1
kind: exam
title: "Αναποδογύρισμα"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #5 (HP Themed), Θέμα 1"
  url: https://progintro.github.io/exams/2023/fall/ex5/
  years: [2023]
chapters: [10, 9]
topics: [arrays, input-output]
difficulty: 1
type: programming
---

> Σημαντικό: φροντίζουμε τα προγράμματά μας να είναι ευανάγνωστα, αποδοτικά (σε χώρο και χρόνο) και να έχουν έξοδο όμοια με τα παραδείγματα εκτέλεσης καθώς αυτό είναι μέρος της βαθμολόγησης. Για οποιαδήποτε είσοδο εκτός προδιαγραφών το πρόγραμμα πρέπει να τερματίζει με exit code 1 και αντίστοιχο μήνυμα σφάλματος.

Πρόγραμμα: `flip.c` (25 μονάδες)

Γράψτε ένα πρόγραμμα που διαβάζει το κείμενο που δίνεται από την πρότυπη είσοδο (stdin) και τυπώνει την κάθε γραμμή στην πρότυπη έξοδο (stdout) αντίστροφα, δηλαδή τυπώνοντας τους χαρακτήρες όπως θα διαβάζονταν από τα δεξιά προς τα αριστερά. Παράδειγμα εκτέλεσης:

```text
$ gcc -o flip flip.c
$ cat riddle.txt
, esiugsid ni sevil ohw nosrep eht fo kniht tsriF
. seil tub thguan sllet dna sterces ni slaed ohW
, dnem ot gniht tsal eht syawla s'tahw em llet ,txeN
? dne eht fo dne dna elddim fo elddim ehT
 draeh netfo dnuos eht em evig yllanif dnA
� drow dnif-ot-drah a rof hcraes eht gniruD
, siht em rewsna dna ,rehtegot meht gnirts woN
? ssik ot gnilliwnu eb uoy dluow erutaerc hcihW
$ ./flip < riddle.txt
First think of the person who lives in disguise ,
Who deals in secrets and tells naught but lies .
Next, tell me what's always the last thing to mend ,
The middle of middle and end of the end ?
And finally give me the sound often heard
During the search for a hard-to-find word �
Now string them together, and answer me this ,
Which creature would you be unwilling to kiss ?
```

## Υπόδειξη

Μαζέψτε τους χαρακτήρες κάθε γραμμής σε έναν πίνακα μέχρι το `'\n'` και τυπώστε τους από το τέλος προς την αρχή, αφήνοντας την αλλαγή γραμμής στη θέση της. Αν οι γραμμές μπορεί να είναι οσοδήποτε μεγάλες, ο πίνακας πρέπει να μεγαλώνει δυναμικά (`realloc`). Μην ξεχάσετε την τελευταία γραμμή χωρίς `'\n'`.
