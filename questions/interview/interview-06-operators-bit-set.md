---
id: interview-06-operators-bit-set
kind: interview
title: "Πλήθος bits που είναι 1"
source:
  title: "Τράπεζα θεμάτων τεχνικής συνέντευξης 2026"
  years: [2026]
chapters: [6]
topics: [bitwise, loops]
difficulty: 1
type: programming
---

Σε ένα σύστημα δικαιωμάτων κάθε bit ενός `unsigned int` είναι ένα δικαίωμα, και θέλετε να
ξέρετε πόσα δικαιώματα έχει ένας χρήστης. Γράψτε μια συνάρτηση `bit_set` που παίρνει ένα
`unsigned int n` και επιστρέφει πόσα bits του είναι 1. Για παράδειγμα, το `5` (`101` στο
δυαδικό) έχει `2`, το `0` έχει `0`, και το `0xFFFFFFFF` έχει `32`. Μη χρησιμοποιήσετε
έτοιμες συναρτήσεις όπως η `__builtin_popcount`.
