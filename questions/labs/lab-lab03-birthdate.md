---
id: lab-lab03-birthdate
kind: lab
title: "Υπολογισμός ημέρας μίας δεδομένης ημερομηνίας"
source:
  title: "Εργαστήριο 3, Άσκηση 3"
  url: https://progintro.github.io/lab-material/labs/lab03/
  years: [2025]
chapters: [5, 6]
topics: [operators, conditionals]
difficulty: 1
type: programming
---

Ο ακόλουθος αλγόριθμος υπολογίζει την ημέρα που αντιστοιχεί σε μία δεδομένη ημερομηνία:

Έστω η ημερομηνία $DD / MM / YYYY$ (δύο ψηφία για την μέρα DD - Day, δύο ψηφία για τον
μήνα MM - Month, 4 ψηφία για τον χρόνο YYYY - Year).

**Αν** $\text{MM} \leq 2$, **τότε**:

$$\begin{matrix} \text{NYYYY} = \text{YYYY} - 1 \\ \text{NMM} = 0 \\ \end{matrix}$$

**Αν** $\text{MM} > 2$, **τότε**:

$$\begin{matrix} \text{NYYYY} = \text{YYYY} \\ \text{NMM} = \left\lfloor \frac{4 \cdot \text{MM} + 23}{10} \right\rfloor \\ \end{matrix}$$

$$IDAY = 365 \cdot YYYY + DD + 31 \cdot (MM - 1) - NMM + \left\lfloor \frac{NYYYY}{4}\right\rfloor - \left\lfloor \frac{3}{4} \cdot \left(\left\lfloor \frac{NYYYY}{100} \right\rfloor + 1\right) \right\rfloor$$

Για τον υπολογισμό της ημέρας, αν:

- $IDAY \mod 7 = 0$, τότε DAY = **Saturday**
- $IDAY \mod 7 = 1$, τότε DAY = **Sunday**
- ...
- $IDAY \mod 7 = 6$, τότε DAY = **Friday**

Όπου, με $\lfloor x \rfloor$ συμβολίζουμε τον μέγιστο ακέραιο αριθμό που δεν είναι
μεγαλύτερος του αριθμού $x$ - γνωστή και ως συνάρτηση `floor`
([αντίστοιχα υπάρχει και η συνάρτηση ceil](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions)).
Δεν είμαστε σίγουροι πώς λειτουργεί - πώς θα το βρούμε;

**Εργασία**: Γράψτε ένα πρόγραμμα `birthdate.c` το οποίο να χρησιμοποιεί τον αλγόριθμο
παραπάνω και να υπολογίζει τι ημέρα γεννηθήκατε (ενσωματώστε την ημερομηνία γέννησής σας
μέσα στο πρόγραμμα).

Ο παραπάνω υπολογισμός φαίνεται περίπλοκος; Δεν έχετε δει τίποτε ακόμη! Πραγματικές
συναρτήσεις βιβλιοθήκης ημερομηνιών πρέπει να χειρίζονται ημερομηνίες και στο παρελθόν,
με ιδιαίτερα περίπλοκες αλλαγές - τι γίνεται για παράδειγμα αν ο χρήστης θέλει να βρει
την ημερομηνία 16 Φεβρουαρίου 1923 στην Ελλάδα
[[8]](https://en.wikipedia.org/wiki/Adoption_of_the_Gregorian_calendar);

## Υπόδειξη

Για θετικούς αριθμούς, η ακέραια διαίρεση της C κάνει ήδη το $\lfloor \cdot \rfloor$,
οπότε δεν χρειάζεστε `floor`. Προσέξτε τον όρο $\frac{3}{4} \cdot (\dots)$: αν τον γράψετε
αφελώς σε ακέραια αριθμητική, το `3/4` βγαίνει 0, άρα αλλάξτε τη σειρά των πράξεων
(πρώτα πολλαπλασιασμός, μετά διαίρεση). Για την ονομασία της ημέρας αρκεί μια αλυσίδα
`if`/`else if` ή ένα `switch` πάνω στο υπόλοιπο.
