---
id: slides-lec11-atoi
kind: slides
title: "Η δική μας atoi"
source:
  title: "Διάλεξη 11, διαφάνειες 41–42"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec11.pdf
  years: [2025]
chapters: [11, 10]
topics: [strings, arrays, functions]
difficulty: 2
type: programming
---

Θέλω μια συνάρτηση `atoi` που να παίρνει έναν πίνακα χαρακτήρων (μόνο ψηφία) και να
επιστρέφει έναν ακέραιο. Πώς;

## Υπόδειξη

Διατρέξτε τους χαρακτήρες μέχρι το `'\0'`. Η τιμή ενός χαρακτήρα-ψηφίου προκύπτει
αφαιρώντας του το `'0'`· σκεφτείτε πώς αλλάζει το μέχρι τώρα αποτέλεσμα όταν
«προσθέτετε» ένα ψηφίο στα δεξιά του (π.χ. από 12 σε 123).
