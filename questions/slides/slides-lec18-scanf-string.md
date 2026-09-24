---
id: slides-lec18-scanf-string
kind: slides
title: "Μια λέξη σε char[7] με scanf"
source:
  title: "Διάλεξη 18, διαφάνειες 31–35"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec18.pdf
  years: [2025]
chapters: [18, 12]
topics: [strings, input-output, undefined-behavior]
difficulty: 2
type: debug
---

Τι κάνει το παρακάτω πρόγραμμα;

```c
#include <stdio.h>
int main() {
  char message[7];
  printf("Say something: ");
  scanf("%s", message);
  printf("%s\n", message);
  return 0;
}
```

```text
$ ./message
Say something: hello!
hello!
```

1. Δεν βάλαμε `&` πριν τη μεταβλητή `message`. Πώς και λειτουργεί;
2. Μπορεί να πάει κάτι στραβά εδώ; Τι θα συμβεί αν ο χρήστης γράψει
   `Houston, we've had a problem here.`; Πώς το διορθώνουμε;

## Υπόδειξη

Θυμηθείτε σε τι μετατρέπεται το όνομα ενός πίνακα όταν το περνάμε σε συνάρτηση. Για
το δεύτερο σκέλος, μετρήστε πόσους χαρακτήρες (μαζί με το `'\0'`) διαβάζει το `%s`
από την πρώτη λέξη και πόσοι χωρούν στον πίνακα· η `scanf` δέχεται και πλάτος πεδίου.
