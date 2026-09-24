---
id: slides-lec04-git-cycle
kind: slides
title: "Ο κύκλος clone, add, commit, push, pull"
source:
  title: "Διάλεξη 4: Git και Τελεστές, διαφάνειες 15-18"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec04.pdf
  years: [2025]
chapters: [4]
topics: [git]
difficulty: 1
type: tooling
---

Στο repository μιας εργασίας σας (π.χ. `git@github.com:progintro/hw0-barbouni-2005.git`):

1. Κάντε `git clone` το repository. Ελέγξτε τον φάκελο: τι αρχείο έχει; Τρέξτε
   `git status` μέσα στον φάκελο: υπάρχουν αλλαγές;
2. Δημιουργήστε ένα καινούργιο αρχείο, π.χ. `touch command/solution.txt`. Τρέξτε
   `git status`: πώς καταγράφεται το νέο αρχείο;
3. Προσθέστε το με `git add command/solution.txt` και τρέξτε ξανά `git status`.
4. Τρέξτε `git commit` και δώστε ένα μήνυμα που περιγράφει την αλλαγή σας. Τρέξτε
   `git status` και πάλι.
5. Τρέξτε `git push` και ελέγξτε ότι οι αλλαγές σας εμφανίζονται στο GitHub!
6. Κάντε κάποιες αλλαγές στο repository από το GitHub UI και μετά τρέξτε `git pull`.

Τα βήματα προϋποθέτουν ότι έχετε φτιάξει ένα κλειδί για τον GitHub λογαριασμό σας και
έχετε τελειώσει το configuration όπως περιγράφεται στο Φυλλάδιο 1 του εργαστηρίου.

## Υπόδειξη

Μετά από κάθε βήμα, διαβάστε προσεκτικά τι λέει το `git status`: untracked, έτοιμο για
commit, ή «ahead» του server. Αν το `clone` ή το `push` αποτυγχάνει με
`Permission denied (publickey)`, ελέγξτε το κλειδί SSH (Εργαστήριο 1, Βήμα 6).
