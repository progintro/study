---
id: kahoot-signed-char-ff
kind: kahoot
title: "Το 0xFF σε signed char"
source:
  title: "Kahoot «Μεταβλητές και Μνήμη», «Μεταβλητές και Συναρτήσεις» (διάλεξη 2)"
  years: [2024, 2025]
chapters: [2]
topics: [integer-representation, types]
difficulty: 3
type: multiple-choice
answer: "-1"
stats: {responses: 301, accuracy: 33}
---

Για ένα `signed char` που έχει τιμή `0xFF` (συμπλήρωμα του δύο), ποια είναι η δεκαδική τιμή του;

- 1
- -1
- 256
- 0

## Συχνή παρανόηση

Το 41% απάντησε 256, που δεν χωράει καν σε 8 bits (το `0xFF` ως unsigned είναι 255)· σε `signed char` με συμπλήρωμα ως προς 2 όλοι οι άσοι σημαίνουν αρνητικό αριθμό.

## Υπόδειξη

Στο συμπλήρωμα ως προς 2 το πιο σημαντικό bit δείχνει το πρόσημο. Για να βρείτε το μέτρο ενός αρνητικού, κάντε flip όλα τα bits και προσθέστε 1.
