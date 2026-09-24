---
id: kahoot-list-use-after-free
kind: kahoot
title: "Ανάγνωση διαγραμμένου στοιχείου"
source:
  title: "Kahoot «Λίστες, Δέντρα and Beyond»"
  years: [2025]
chapters: [21, 13]
topics: [linked-lists, dynamic-memory, undefined-behavior]
difficulty: 1
type: multiple-choice
answer: "Το πρόγραμμά μου θα σκάσει (Segmentation Fault)"
stats: {responses: 93, accuracy: 92}
---

Μόλις διέγραψα ένα στοιχείο από μια λίστα. Τι θα συμβεί αν προσπαθήσω να το διαβάσω;

- Το πρόγραμμά μου θα σκάσει (Segmentation Fault)
- Όλα θα πάνε καλά και θα διαβάσω κανονικά το στοιχείο

## Υπόδειξη

Μετά το `free` η μνήμη του κόμβου δεν ανήκει πια στο πρόγραμμά σας· σκεφτείτε αν είναι ασφαλές να τη διαβάσετε.
