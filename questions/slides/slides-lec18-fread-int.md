---
id: slides-lec18-fread-int
kind: slides
title: "Ακέραιοι από αρχείο κειμένου με fread"
source:
  title: "Διάλεξη 18, διαφάνειες 50–51"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec18.pdf
  years: [2025]
chapters: [18, 12]
topics: [files, integer-representation]
difficulty: 2
type: trace
---

Το αρχείο `input.txt` δημιουργήθηκε με `echo hello > input.txt`. Εξηγήστε την
έξοδο του προγράμματος («What?!»).

```c
#include <stdio.h>
int main() {
  FILE *fileToRead, *fileToWrite;
  fileToRead = fopen("input.txt", "r");
  if (!fileToRead) return 1;
  int buffer[1024];
  size_t integersRead = fread(buffer, sizeof(int), 1023, fileToRead);
  printf("# of integers read: %d\n", integersRead);
  printf("Integer read: %d %08x\n", buffer[0], buffer[0]);
  fclose(fileToRead);
  return 0;
}
```

```text
$ ./freadint
# of integers read: 1
Integer read: 1819043176 6c6c6568
$ hexdump -C input.txt
00000000  68 65 6c 6c 6f 0a  |hello.|
```

## Υπόδειξη

Η `fread` αντιγράφει bytes χωρίς καμία μετατροπή και μετρά μόνο ολόκληρα δεδομένα
μεγέθους `sizeof(int)`. Συγκρίνετε τα bytes του `hexdump` με το δεκαεξαδικό που
τυπώθηκε και θυμηθείτε το endianness.
