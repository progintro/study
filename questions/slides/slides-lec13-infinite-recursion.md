---
id: slides-lec13-infinite-recursion
kind: slides
title: "Γιατί η αναδρομή πρέπει να τελειώνει;"
source:
  title: "Διάλεξη 13, διαφάνεια 27"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/lec13.pdf
  years: [2025]
chapters: [13, 11]
topics: [recursion, memory-model]
difficulty: 1
type: short-answer
---

Είχαμε πει «η αναδρομή πρέπει να τελειώνει». Γιατί;

```c
void recurse() {
  recurse();
}

int main() {
  recurse();
  return 0;
}
```

```text
$ gcc -o rec rec.c
$ ./rec
Segmentation fault
```

## Υπόδειξη

Σκεφτείτε τι μπαίνει στη στοίβα σε κάθε κλήση της `recurse` και πότε αφαιρείται.
Η στοίβα έχει πεπερασμένο μέγεθος (δείτε `ulimit -s`).
