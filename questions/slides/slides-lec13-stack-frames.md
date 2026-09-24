---
id: slides-lec13-stack-frames
kind: slides
title: "Τα stack frames της equalIgnoreCase"
source:
  title: "Διάλεξη 13, διαφάνειες 20–26"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec13.pdf
  years: [2025]
chapters: [13]
topics: [memory-model, functions]
difficulty: 1
type: short-answer
---

```c
char tolower(char c) {
    if (c >= 'A' && c <= 'Z')
        return c + ('a' - 'A');
    return c;
}
int equalIgnoreCase(char char1, char char2) {
    char lowerChar1 = tolower(char1);
    char lowerChar2 = tolower(char2);
    return lowerChar1 == lowerChar2;
}
```

Η εκτέλεση βρίσκεται μέσα στην `equalIgnoreCase`, και η στοίβα περιέχει το stack
frame της (`char1`, `char2`, `lowerChar1`, `lowerChar2` και προσωρινά δεδομένα του
μεταγλωττιστή).

1. Τι θα συμβεί όταν κληθεί η συνάρτηση `tolower` την πρώτη φορά;
2. Τι θα συμβεί όταν εκτελεστεί η εντολή `return` (της `tolower`);
3. Τι θα συμβεί όταν εκτελεστεί η δεύτερη κλήση `tolower`;
4. Τι θα συμβεί όταν εκτελεστεί η `return` της `equalIgnoreCase`;

## Υπόδειξη

Θυμηθείτε ότι η στοίβα λειτουργεί με σειρά LIFO και ότι κάθε κλήση συνάρτησης
παίρνει το δικό της activation record με τα ορίσματα, τις τοπικές μεταβλητές και
προσωρινά δεδομένα. Σχεδιάστε τη στοίβα ως κουτάκια μετά από κάθε βήμα.
