---
id: hw-2025-hw0-pages
kind: homework
title: "Νέο URL στο GitHub (pages)"
source:
  title: "Εργασία 0 (2025-26), Άσκηση 1"
  url: https://github.com/progintro/progintro.github.io/releases/download/2025/hw0.pdf
  years: [2023, 2024, 2025]
chapters: [4, 1]
topics: [git, shell]
difficulty: 1
type: tooling
---

Έχεις λογαριασμό στο GitHub; Έχεις ξαναφτιάξει repository; Έχεις φτιάξει URL στο
διαδίκτυο; Μετά από αυτήν την άσκηση θα μπορείς να απαντήσεις "ναι" σε όλα.

Η ιστοσελίδα του μαθήματος βασίζεται σε ένα public GitHub repository. Σκοπός αυτής της
άσκησης είναι να δημιουργήσεις ένα καινούριο repository στον προσωπικό σου λογαριασμό
GitHub και να το συνδέσεις με GitHub Pages προκειμένου να είναι διαθέσιμο στο διαδίκτυο.
Αυτό το [tutorial](https://docs.github.com/en/pages/quickstart) μπορεί να σε βοηθήσει.

### Τεχνικές Προδιαγραφές

Η υποβολή σου πρέπει να έχει τα ακόλουθα χαρακτηριστικά:

- Repository Name: `progintro/hw0-<YourUsername>`
- Αρχείο Λύσης Filepath: `pages/solution.txt`
- README Filepath (optional): `pages/README.md`

Έστω ότι το GitHub username σου είναι `YourUsername`. Το αρχείο `solution.txt` πρέπει να
περιέχει το URL με το domain `YourUsername.github.io` που δημιουργήσατε. Αν
χρησιμοποιήσετε κάποιο `*.github.io` URL που δεν δημιουργήσατε η άσκηση μηδενίζεται.
Ενδεικτική συμπεριφορά για μια επιτυχημένη υποβολή (**προσοχή: η γραμμή με την εντολή
curl εκτείνεται σε δύο γραμμές, πρέπει να αντιγράψετε και τις δύο προκειμένου να τρέξετε
αυτήν την εντολή**, το backslash `\` δείχνει ότι η εντολή είναι μία αλλά εκτείνεται σε δύο
γραμμές):

```text
# Check out solution URL
$ cat solution.txt
YourUsername.github.io
# Ensure the URL exists
$ curl --output /dev/null --silent --head --fail YourUsername.github.io && \
  echo "URL exists" || echo "URL does not exist"
URL exists
```

Το αρχείο `README.md` είναι προαιρετικό αν θέλετε να προσθέσετε κάτι στην υποβολή σας.

## Εμφανίσεις

- [Εργασία 0 (2023-24), Άσκηση 1](https://github.com/progintro/progintro.github.io/releases/download/2023/hw0.pdf): ίδια εκφώνηση, χωρίς τον σύνδεσμο προς το tutorial του GitHub Pages.
- [Εργασία 0 (2024-25), Άσκηση 1](https://github.com/progintro/progintro.github.io/releases/download/2024/hw0.pdf): ίδια εκφώνηση (20 μονάδες).
- [Εργασία 0 (2025-26), Άσκηση 1](https://github.com/progintro/progintro.github.io/releases/download/2025/hw0.pdf): η εκφώνηση που δίνεται εδώ.

## Υπόδειξη

Το GitHub Pages σερβίρει αυτόματα ένα repository με όνομα ακριβώς `<username>.github.io`
στον λογαριασμό σου, αρκεί να περιέχει ένα αρχείο όπως το `index.html`. Δοκίμασε το URL
με την εντολή `curl` της εκφώνησης πριν το γράψεις στο `solution.txt`, και θυμήσου ότι το
`solution.txt` ζει σε άλλο repository (το `hw0-<YourUsername>`), οπότε χρειάζεσαι
`git add`, `commit` και `push` και εκεί.
