---
id: interview-14-arrays-mystrlen
kind: interview
title: "Η δική σας strlen"
source:
  title: "Τράπεζα θεμάτων τεχνικής συνέντευξης 2026"
  years: [2026]
chapters: [14]
topics: [strings, loops]
difficulty: 1
type: programming
---

Σε ένα profile βλέπουμε ότι το πρόγραμμά μας περνά τον μισό του χρόνο μέσα στη `strlen`.
Για να καταλάβουμε γιατί, ξεκινάμε από το τι κάνει. Γράψτε τη δική σας `mystrlen`, που
υπολογίζει το μήκος ενός string (`const char *`) χωρίς να καλέσει την `strlen`, και
επιστρέφει ό,τι και εκείνη: το πλήθος των χαρακτήρων **πριν** από το `'\0'`. Για
παράδειγμα, `mystrlen("hello")` → `5` και `mystrlen("")` → `0`.
