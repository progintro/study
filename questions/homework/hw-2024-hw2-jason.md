---
id: hw-2024-hw2-jason
kind: homework
title: "Το Δικό σου Chatbot (jason)"
source:
  title: "Εργασία 2 (2024-25), Άσκηση 3"
  url: https://github.com/progintro/progintro.github.io/releases/download/2024/hw2.pdf
  years: [2024]
chapters: [14, 11, 18]
topics: [strings, dynamic-memory, files, recursion, code-organization, input-output]
difficulty: 3
type: programming
---

**Το Δικό σου Chatbot - (jason - 50 Μονάδες)**

Η τεχνητή νοημοσύνη έχει μπει για τα καλά στην ζωή μας, και χρήστες και
προγραμματιστές/τριες βρίσκουν συνεχώς νέες εφαρμογές της. Πόσο δύσκολο είναι όμως να
φτιάξουμε ένα εργαλείο που να μπορεί να αξιοποιήσει τις υπηρεσίες τεχνητής νοημοσύνης
και να προσφέρει λύσεις σε χρήστες; Αυτή είναι η ερώτηση που θα μας απασχολήσει σε
αυτήν την άσκηση.

Προκειμένου να μιλήσουμε με απομακρυσμένες υπηρεσίες, πρέπει να μπορούμε να μιλήσουμε
την γλώσσα τους. Τυχαίνει σήμερα πάμπολλες εφαρμογές στο internet να μεταφέρουν
δεδομένα χρησιμοποιώντας μια μορφοποίηση (data format) που λέγεται JSON (JavaScript
Object Notation). Για να δούμε ένα παράδειγμα. Έστω ότι έχουμε ένα αρχείο
`person.json` με τα ακόλουθα περιεχόμενα:

```text
{
  "first_name": "John",
  "last_name": "Smith",
  "age": 27,
  "address": {
    "street_address": "21 2nd Street",
    "city": "New York",
    "state": "NY",
  },
  "phone_numbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [
    "Catherine",
    "Thomas",
    "Trevor"
  ],
  "spouse": null
}
```

Το παραπάνω παράδειγμα JSON παρουσιάζει ιεραρχικά τα δεδομένα για ένα άτομο.
Παρατηρούμε ότι όλα τα δεδομένα είναι μέσα σε ένα object (περικλείονται από αγκύλες {
και }) και μέσα σε αυτό έχει διάφορα πεδία που κλείνονται μέσα σε διπλά quotes ":
first_name, last_name, ..., children, spouse. Πέρα από αυτό παρατηρούμε ότι κάθε πεδίο
μπορεί να έχει ως τιμή (ότι ακολουθεί την άνω και κάτω τελεία ":") ένα από τα
ακόλουθα:

1. έναν αριθμό (π.χ., `"age": 27`)
2. ένα string (`"first_name": "John"`)
3. μια λίστα από δεδομένα (`"children": ["Catherine", "Thomas", "Trevor"]`)
4. ένα object με δικά του πεδία (`"address": { ... }`)

Παρατηρήστε ότι ο παραπάνω ορισμός είναι αυτο-αναφορικός (ένα JSON object μπορεί να
περιέχει ένα πεδίο τύπου JSON object, που μπορεί να περιέχει ένα JSON object κοκ).

Τι σχέση έχουν όλα αυτά με την τεχνητή νοημοσύνη; Προκειμένου να χρησιμοποιήσουμε τις
υπηρεσίες τεχνητής νοημοσύνης πρέπει να μπορούμε να εξάγουμε κάποια συγκεκριμένα
δεδομένα από ένα JSON. Για παράδειγμα, δείτε το παρακάτω παράδειγμα-απάντηση του
gpt-4o-mini μοντέλου τεχνητής νοημοσύνης στην ερώτηση "Tell me a joke":

```text
{
  "id": "chatcmpl-Ag5hb4g6PYiVpvBp3tuiJjqX9KjqN",
  "object": "chat.completion",
  "created": 1734595059,
  "model": "gpt-4o-mini-2024-07-18",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Why do programmers always mix up Halloween
                    and Christmas?\nBecause Oct 31 == Dec 25!\n",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 23,
    "total_tokens": 33,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "system_fingerprint": "fp_6fc10e10eb"
}
```

Το παραπάνω JSON φαίνεται χαοτικό στην αρχή, αλλά αν το κοιτάξετε καλύτερα θα βρείτε
το περιεχόμενο της απάντησης. Για να την ανιχνεύσουμε μαζί:

- Στο πάνω επίπεδο, έχουμε ένα JSON object με ένα πεδίο "choices".
  - Το πεδίο choices είναι τύπου λίστα (ξεκινά με ’\[’) και το πρώτο στοιχείο
    (index = 0) είναι επίσης JSON object.
    - Το JSON object της λίστας choices έχει μέσα ένα πεδίο που λέγεται "message" το
      οποίο είναι επίσης τύπου JSON object.
      - Τέλος, το message έχει μέσα ένα πεδίο το οποίο λέγεται "content", το οποίο
        περιέχει το string με την απάντησή μας μέσα σε double quotes: "Why do
        programmers always mix up Halloween and Christmas?\\n Because Oct 31 == Dec
        25!\\n" - παρατηρήστε ότι οι αλλαγές γραμμής είναι escaped όπως θα ήταν σε
        ένα string που θα γράφαμε σε πρόγραμμα σε γλώσσα C.

Ένας πιο γρήγορος τρόπος να συμβολίσουμε το παραπάνω πεδίο είναι ως εξής:
`json.choices[0].message.content` - μετάφραση: στο JSON αρχείο που μας δίνεται, θέλουμε
να βρούμε την λίστα choices, να πάρουμε το πρώτο στοιχείο της, από εκεί να πάρουμε το
message και στο τέλος να πάρουμε την τιμή του content. Αν είχαμε την δυνατότητα να
πάρουμε οποιοδήποτε αρχείο JSON και να εξάγουμε αυτήν την πληροφορία θα μπορούσαμε να
φτιάξουμε το δικό μας chatbot!

Αυτό θα είναι και ο στόχος αυτής της άσκησης, θα υλοποιήσουμε ένα πρόγραμμα το οποίο
θα εξάγει την παραπάνω πληροφορία από αρχεία JSON και θα την αξιοποιεί για να δώσει
απαντήσεις στον χρήστη.

### Τεχνικές Προδιαγραφές

- Repository Name: progintro/hw2-\<YourUsername\>
- C Filepath: jason/src/jason.c
- Το πρόγραμμά θα έχει δύο modes:
  - **Extraction mode**. Το πρόγραμμά σας μπαίνει σε extraction mode όταν ο χρήστης
    δώσει το option `--extract`. Το option `--extract` περιμένει στην συνέχεια το
    όνομα του αρχείου που περιέχει τα περιεχόμενα JSON και από τα οποία θα πρέπει να
    εξάγετε το `json.choices[0].message.content` και να το τυπώσετε στην πρότυπη
    έξοδο. Εάν δωθεί οποιοδήποτε αρχείο που δεν είναι valid JSON, το πρόγραμμά σας
    πρέπει να τυπώσει μήνυμα ίδιο με τα παραδείγματα παρακάτω στο stderr.
  - **Conversation mode**. Το πρόγραμμά σας μπαίνει σε διαδικασία συζήτησης με τον
    χρήστη όταν δωθεί το option `--bot` χωρίς άλλα ορίσματα. Στην διαδικασία
    συζήτησης, το πρόγραμμά σας ρωτάει επαναλαμβανόμενα τον χρήστη
    `> What would you like to know?` μέχρι να στείλει ο χρήστης End-of-File (EOF).
    Κάθε ερώτηση του χρήστη τελειώνει με καινούρια γραμμή και πρέπει να στέλνεται
    αυτούσια στην κατάλληλη συνάρτηση της βιβλιοθήκης neurolib (δες παρακάτω).
- Για τις διαδράσεις με το σύστημα τεχνητής νοημοσύνης (conversation mode) είναι
  υποχρεωτικό να χρησιμοποιήσετε την βιβλιοθήκη neurolib (neurolib.c και neurolib.h)
  που σας δίνεται στον φάκελο jason/src. Δυστυχώς κατεβάσαμε αυτήν την βιβλιοθήκη από
  ένα online project χωρίς καθόλου documentation / testing. Προκειμένου να την
  αξιοποιήσετε θα χρειαστεί να διαβάσετε τις διαθέσιμες συναρτήσεις στο header file
  της και να ανακαλύψετε την χρήση τους. Ο στόχος σας είναι να στείλετε queries στην
  υπηρεσία τεχνητής νοημοσύνης και να πάρετε JSON απαντήσεις.
- Το αρχείο C που θα υποβληθεί πρέπει να μεταγλωττίζεται χωρίς ειδοποιήσεις για λάθη
  και με κωδικό επιστροφής (exit code) που να είναι 0. Συγκεκριμένα, το αρχείο σας
  **πρέπει** να μπορεί να μεταγλωττιστεί επιτυχώς με τις ακόλουθες εντολές σε ένα από
  τα μηχανήματα του εργαστηρίου (linuxXY.di.uoa.gr) - για παράδειγμα το linux14:

  ```sh
  gcc -Wall -Wextra -Werror -pedantic -c neurolib.c
  gcc -Wall -Wextra -Werror -pedantic -c jason.c
  gcc -o jason neurolib.o jason.o -lssl -lcrypto
  ```
- README Filepath: jason/README.md
- Τα αρχεία JSON θα είναι μέχρι 1MB σε μέγεθος.
- Πρέπει να ολοκληρώνει την εκτέλεση μέσα σε: 1 δευτερόλεπτο.
- Το πρόγραμμά σας θα πρέπει να έχει τα λιγότερα δυνατά memory leaks.

Παραδείγματα εκτέλεσης ακολουθούν, πρώτα σε extraction mode:

```text
$ ./jason --extract json/1.json
Why do programmers always mix up Halloween and Christmas?
Because Oct 31 == Dec 25!
$ echo $?
0
$ ./jason --extract json/2.json 2> stderr
$ echo $?
1
$ cat stderr
Not an accepted JSON!
```

Και στην συνέχεια σε conversation mode:

```text
$ ./jason --bot
> What would you like to know? What is the last digit of pi?
I’d answer that, but I don’t want to ruin the surprise.
> What would you like to know? What is the age of the universe?
I could tell you, but then I’d have to awkwardly dance away without explaining why.
> What would you like to know? Terminating
```

Ή μπορείτε να αλληλεπιδράσετε με μια πραγματική υπηρεσία τεχνητής νοημοσύνης (αν
αγοράσετε tokens):

```text
$ export OPENAI_API_KEY=... # enter your key here
$ ./jason --bot
> What would you like to know? What is the last digit of pi?
Pi (pi) is an irrational number, which means it has an infinite
number of decimal places and does not terminate. Therefore, it
does not have a last digit. The decimal representation of pi begins
with 3.14159 and continues indefinitely without repeating.
> What would you like to know? What is the age of the universe?
As of my last knowledge update in October 2023, the age of the
universe is estimated to be about 13.8 billion years. This estimate
is based on measurements of the cosmic microwave background radiation,
the expansion rate of the universe (Hubble constant), and observations
of the oldest known star clusters. However, scientific understanding is
always evolving, so it's possible that new discoveries could refine
this estimate in the future.
> What would you like to know? Terminating
```

Αν φτάσατε μέχρι εδώ: (1) συγχαρητήρια, (2) μην ξεχάσετε το README.md και (3) όπως
πάντα ο κώδικας απαιτείται να είναι καλά τεκμηριωμένος με σχόλια καθώς αυτό θα είναι
μέρος της βαθμολόγησης.

## Υπόδειξη

Διαβάστε όλο το αρχείο σε ένα δυναμικό buffer και γράψτε έναν μικρό αναδρομικό
parser (recursive descent) με μία συνάρτηση ανά είδος τιμής (object, array, string,
αριθμός, literal), που προχωρά έναν δείκτη πάνω στο κείμενο και αποτυγχάνει μόλις
κάτι δεν ταιριάζει. Δεν χρειάζεται να χτίσετε όλο το δέντρο: αρκεί να ακολουθήσετε
τη διαδρομή `choices` → `[0]` → `message` → `content` και να μετατρέψετε τα escapes
(`\n`, `\"`, `\\`, …) κατά την εκτύπωση. Για το `--bot`, ξεκινήστε από το
`neurolib.h`, και ελέγξτε με valgrind ότι ελευθερώνετε κάθε απάντηση.
