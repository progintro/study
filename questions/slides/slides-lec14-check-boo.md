---
id: slides-lec14-check-boo
kind: slides
title: "Είναι το πρώτο όρισμα \"--boo\";"
source:
  title: "Διάλεξη 14, διαφάνεια 42"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec14.pdf
  years: [2025]
chapters: [14, 12]
topics: [strings, command-line-args]
difficulty: 1
type: programming
---

Θέλω να ελέγξω αν το πρώτο όρισμα του προγράμματός μου είναι `"--boo"`. Πώς;

## Υπόδειξη

Το πρώτο όρισμα είναι το `argv[1]`, αλλά υπάρχει μόνο αν το `argc` είναι αρκετά
μεγάλο. Ο τελεστής `==` σε δύο string συγκρίνει διευθύνσεις, όχι περιεχόμενα·
χρειάζεστε μια συνάρτηση της `string.h` και να θυμάστε τι επιστρέφει όταν τα string
είναι ίσα.
