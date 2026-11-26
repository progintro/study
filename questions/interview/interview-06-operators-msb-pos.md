---
id: interview-06-operators-msb-pos
kind: interview
title: "Θέση του υψηλότερου bit"
source:
  title: "Τράπεζα θεμάτων τεχνικής συνέντευξης 2026"
  years: [2026]
chapters: [6]
topics: [bitwise, loops]
difficulty: 1
type: programming
---

Για να ξέρετε σε πόσα bits χωρά ένας αριθμός (ή, ισοδύναμα, το ⌊log₂ n⌋ χωρίς `double`),
χρειάζεστε τη θέση του υψηλότερου bit που είναι 1. Γράψτε τη `int msb_pos(unsigned int n)`
που την επιστρέφει, μετρώντας από το `0` για το λιγότερο σημαντικό. Για παράδειγμα,
`msb_pos(1)` → `0`, `msb_pos(12)` (`1100`) → `3` και `msb_pos(0x80000000)` → `31`.
