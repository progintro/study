---
id: slides-lec19-field-assignment
kind: slides
title: "Ανάθεση και χρήση πεδίων δομής"
source:
  title: "Διάλεξη 19, διαφάνειες 12–13"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec19.pdf
  years: [2025]
chapters: [19]
topics: [structs, strings]
difficulty: 1
type: trace
---

Με τη δομή

```c
struct student {
  char first_name[128];
  char last_name[128];
  unsigned int year;
  double grade;
};
```

τι τυπώνει αυτό το πρόγραμμα;

```c
int main() {
  struct student st1;
  st1.year = 1;
  st1.grade = 7.54;
  strncpy(st1.first_name, "Thanos", sizeof(st1.first_name) - 1);
  st1.first_name[sizeof(st1.first_name) - 1] = '\0';
  strncpy(st1.last_name, "Barbounis", sizeof(st1.last_name) - 1);
  st1.last_name[sizeof(st1.last_name) - 1] = '\0';
  printf("%s %s: %f [%u year]\n", st1.first_name, st1.last_name, st1.grade, st1.year);
  return 0;
}
```

## Υπόδειξη

Κάθε πεδίο συμπεριφέρεται όπως μια μεταβλητή του τύπου του. Προσέξτε πόσα δεκαδικά
τυπώνει το `%f` χωρίς ακρίβεια.
