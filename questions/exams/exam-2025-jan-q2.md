---
id: exam-2025-jan-q2
kind: exam
title: "Η συνάρτηση dog"
source:
  title: "Εξέταση Ιανουαρίου 2025, Θέμα 2"
  url: https://progintro.github.io/exams/2025/progintro-exam-jan-25.pdf
  years: [2025]
chapters: [14, 13, 2]
topics: [strings, pointer-arithmetic, dynamic-memory]
difficulty: 1
type: trace
---

**Η συνάρτηση dog (10 Μονάδες)**

```c
char *dog(const char *str1, const char *str2) {
    size_t len1 = strlen(str1);
    size_t len2 = strlen(str2);
    char *result = malloc(len1 + len2 + 1);
    if (!result) return NULL;
    char *ptr = result;
    while (*str1) *ptr++ = *str1++;
    while (*str2) *ptr++ = *str2++;
    *ptr = '\0';
    return result;
}
```

Τι κάνει η συνάρτηση dog (μέχρι 15 λέξεις εξήγηση); Τι θα τυπώσουν οι παρακάτω εντολές;

```c
char arg1[] = {71, 111, 111, 100, 32, 0};
char arg2[5] = {'j', 111, 98, '!', 0};
printf("%s\n", dog(arg1, arg2));
```

## Υπόδειξη

Παρακολουθήστε πού δείχνει ο `ptr` μετά από κάθε βρόχο και γιατί η `malloc` ζητά
`len1 + len2 + 1` bytes. Για την έξοδο, μετατρέψτε τους αριθμούς σε χαρακτήρες με τον
πίνακα ASCII (το 0 είναι ο τερματικός χαρακτήρας και το 32 το κενό). Σκεφτείτε επίσης
τι γίνεται με τη μνήμη που επιστρέφει η `dog` σε αυτή την κλήση.
