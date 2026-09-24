---
id: slides-lec11-factorial-negative
kind: slides
title: "Αρνητικό όρισμα στο αναδρομικό παραγοντικό"
source:
  title: "Διάλεξη 11, διαφάνεια 46"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec11.pdf
  years: [2025]
chapters: [11]
topics: [recursion, undefined-behavior]
difficulty: 2
type: short-answer
---

Τι θα συμβεί αν δώσουμε έναν αρνητικό αριθμό στη συνάρτησή μας;

```c
int factorial(int number) {
  if (number == 0) return 1;
  else return number * factorial(number - 1);
}
```

## Υπόδειξη

Ακολουθήστε τις τιμές του `number` στις διαδοχικές κλήσεις ξεκινώντας από `-1`. Φτάνει
ποτέ στη βάση τερματισμού; Τι κοστίζει στη μνήμη κάθε κλήση που δεν έχει ακόμα
επιστρέψει; Πώς θα άλλαζε η συνθήκη της βάσης για να προστατεύεται η συνάρτηση;
