---
id: exam-2023-fall-ex1-q4
kind: exam
title: "Debugging"
source:
  title: "Online τελική εξέταση Δεκεμβρίου 2023, Εξέταση #1 (Coreutils Themed), Θέμα 4"
  url: https://progintro.github.io/exams/2023/fall/ex1/
  years: [2023]
chapters: [21, 13]
topics: [linked-lists, dynamic-memory, debugging]
difficulty: 2
type: debug
---

> Σημαντικό: φροντίζουμε τα προγράμματά μας αν είναι ευανάγνωστα, αποδοτικά (σε χώρο και χρόνο) και να έχουν έξοδο όμοια με τα παραδείγματα εκτέλεσης καθώς αυτό είναι μέρος της βαθμολόγησης. Για οποιαδήποτε είσοδο εκτός προδιαγραφών το πρόγραμμα πρέπει να τερματίζει με exit code 1 και αντίστοιχο μήνυμα σφάλματος.

Πρόγραμμα: `broken.c` (25 μονάδες)

Το πρόγραμμα [broken.c](https://progintro.github.io/exams/2023/fall/ex1/broken.c) δεν λειτουργεί για κάποιον λόγο - όταν το τρέχουμε κρασάρει. Βρείτε όποιο σφάλμα υπάρχει και διορθώστε το χωρίς να εισάγετε καινούρια σφάλματα στο πρόγραμμα. Παράδειγμα επιτυχούς εκτέλεσης ακολουθεί:

```text
$ gcc -o broken broken.c
$ ./broken
yesss! -> yee -> bruh -> NULL
listdelete: 1
yesss! -> yee -> NULL
```

Το πρόγραμμα:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
    char value[128];
    struct node * next;
} Elem;

int listdelete(char value[], Elem ** head) {
    Elem * tmp;

    while (*head && strcmp((*head)->value, value)) {
        head = &((*head)->next);
    }

    if (*head) {
        tmp=*head;
        *head = tmp->next;
        free(tmp);
        return 1;
    }
    return -1;
}

int listadd(char value[], Elem ** head) {
    Elem * new = malloc(sizeof(Elem));
    if (new == NULL) {
        return 0;
    }
    Elem * tmp;
    tmp=*head;
    *head=new;
    new->next=tmp;
    strncpy(new->value, value, 127);
    return 1;
}

void listprint(Elem * list) {
  while(list) {
    printf("%s -> ", list->value);
    list = list->next;
  }
  printf("NULL\n");
}

int main() {

    Elem elem1 = {"bruh", NULL};
    Elem * head = &elem1;

    listadd("yee", &head);
    listadd("yesss!", &head);
    listprint(head);
    printf("listdelete: %d\n", listdelete("bruh", &head));
    listprint(head);
    return 0;
}
```

## Υπόδειξη

Εκτελέστε το με `valgrind` ή `gcc -fsanitize=address` και δείτε σε ποια γραμμή σκάει. Αναρωτηθείτε για κάθε κόμβο της λίστας πού ζει στη μνήμη (στοίβα ή σωρός) και ποιοι κόμβοι επιτρέπεται να δοθούν στην `free`. Η διόρθωση πρέπει να κρατήσει τη λίστα συνεπή και να μην αφήνει διαρροές.
