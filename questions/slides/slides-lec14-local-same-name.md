---
id: slides-lec14-local-same-name
kind: slides
title: "Τοπική μεταβλητή με το ίδιο όνομα σε δύο συναρτήσεις"
source:
  title: "Διάλεξη 14, διαφάνειες 9–10"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec14.pdf
  years: [2025]
chapters: [14]
topics: [scope, functions]
difficulty: 1
type: trace
---

Η τοπική μεταβλητή μιας συνάρτησης δεν είναι ορατή σε κάποια άλλη συνάρτηση και
επομένως μπορούμε να δηλώσουμε μεταβλητές με το ίδιο όνομα σε άλλες συναρτήσεις και
να αναφέρονται σε άλλες θέσεις μνήμης.

Τι θα επιστρέψει αυτό το πρόγραμμα;

```c
void foo() {
  int i = 43;
}
int main() {
  int i = 42;
  foo();
  return i;
}
```

```text
$ gcc -o local local.c
$ ./local
$ echo $?
```

## Υπόδειξη

Αναρωτηθείτε αν το `i` της `foo` και το `i` της `main` είναι η ίδια μεταβλητή:
πού είναι η εμβέλεια του καθενός και σε ποιο frame της στοίβας ζει; Θυμηθείτε ότι το
`echo $?` τυπώνει την τιμή που επέστρεψε η `main`.
