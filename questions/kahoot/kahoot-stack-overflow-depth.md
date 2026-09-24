---
id: kahoot-stack-overflow-depth
kind: kahoot
title: "Βάθος αναδρομής μέχρι να γεμίσει η στοίβα"
source:
  title: "Kahoot «Μνήμη» (διάλεξη 13)"
  years: [2025]
chapters: [13]
topics: [recursion, memory-model, shell]
difficulty: 3
type: multiple-choice
answer: "~8000"
stats: {responses: 135, accuracy: 20}
---

Έστω ότι `ulimit -s` δίνει 8192 και το activation record της `foo` είναι 1024 bytes. Πόσες αναδρομικές κλήσεις μέχρι να «σκάσει» το πρόγραμμα;

- ~8
- 42
- ~400
- ~8000

## Συχνή παρανόηση

Το 48% επέλεξε `~8`, θεωρώντας ότι το 8192 είναι bytes. Το `ulimit -s` μετράει σε KB, άρα η στοίβα είναι 8 MB.

## Υπόδειξη

Ελέγξτε σε ποια μονάδα μετράει το `ulimit -s` το μέγεθος της στοίβας.
