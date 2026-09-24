---
id: kahoot-or-combine
kind: kahoot
title: "0xbeef | 0xcafe0000"
source:
  title: "Kahoot «Git και Τελεστές» (διάλεξη 4)"
  years: [2025]
chapters: [4, 5]
topics: [bitwise]
difficulty: 3
type: multiple-choice
answer: "0xcafebeef"
stats: {responses: 318, accuracy: 29}
---

Ποια η τιμή της παράστασης `0xbeef | 0xcafe0000`;

- `0xffffffff`
- `0xcafebeef`
- `0xbeefcafe`
- `0x00000000`

## Συχνή παρανόηση

Το 29% απάντησε `0xbeefcafe`, διαβάζοντας το OR σαν «παράθεση με τη σειρά που γράφονται»· όμως το OR δεν μετακινεί bits, το καθένα μένει στη θέση του, και το `0xcafe` βρίσκεται στα πάνω 16 bits.

## Υπόδειξη

Κάθε δεκαεξαδικό ψηφίο είναι 4 bits. Τα δύο νούμερα έχουν μη μηδενικά ψηφία σε διαφορετικές θέσεις· τι κάνει το OR όταν σε κάθε θέση ο ένας από τους δύο είναι 0;
