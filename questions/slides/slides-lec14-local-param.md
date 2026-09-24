---
id: slides-lec14-local-param
kind: slides
title: "Αύξηση παραμέτρου μέσα σε συνάρτηση"
source:
  title: "Διάλεξη 14, διαφάνειες 11–12"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec14.pdf
  years: [2025]
chapters: [14, 3]
topics: [scope, functions]
difficulty: 1
type: trace
---

Τι θα επιστρέψει αυτό το πρόγραμμα;

```c
void foo(int i) {
  i++;
}
int main() {
  int i = 42;
  foo(i);
  return i;
}
```

```text
$ gcc -o local2 local2.c
$ ./local2
$ echo $?
```

## Υπόδειξη

Η παράμετρος μιας συνάρτησης είναι κι αυτή τοπική μεταβλητή, που αρχικοποιείται
κατά την κλήση με την τιμή του ορίσματος. Σκεφτείτε ποια μεταβλητή αυξάνει το `i++`
και ποια επιστρέφει η `main`.
