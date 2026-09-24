# Γλωσσάριο

<!-- {% raw %} -->

Όλοι οι όροι του οδηγού, από τους πίνακες «Ορολογία» των κεφαλαίων, με τον αγγλικό
όρο, σύντομο ορισμό και τα κεφάλαια όπου εμφανίζονται.

| Ελληνικά | English | Ορισμός | Κεφάλαια |
| --- | --- | --- | --- |
| bitwise τελεστής | bitwise operator | `&`, `\|`, `^`, `~`, `<<`, `>>`, bit προς bit | [5](chapters/05-operators-statements/) |
| byte, οκτάδα | byte, octet | Ομάδα (συνήθως 8) bits σε ένα κελί μνήμης | [2](chapters/02-memory-variables/) |
| camelCase / snake_case | camelCase / snake_case | Στυλ ονομάτων: `piApprox` / `pi_approx`. | [9](chapters/09-input/) |
| include guard | include guard | `#ifndef`/`#define`/`#endif` γύρω από ένα `.h`. | [23](chapters/23-code-organization/) |
| lvalue / rvalue | lvalue / rvalue | Αριστερός (μεταβλητή) / δεξιός (τιμή) τελεστέος της ανάθεσης | [4](chapters/04-git-operators/) |
| null byte | null byte / null terminator | Ο χαρακτήρας `'\0'` (τιμή 0) που σημειώνει το τέλος ενός string. | [10](chapters/10-arrays/) |
| null byte | null byte | Ο χαρακτήρας `'\0'` που σημαδεύει το τέλος. | [14](chapters/14-scope-strings/) |
| variadic συνάρτηση | variadic function | συνάρτηση με μεταβλητό αριθμό ορισμάτων (`...`) | [24](chapters/24-advanced-topics/) |
| ακέραια διαίρεση | integer division | `/` μεταξύ ακεραίων, που κρατάει μόνο το πηλίκο | [5](chapters/05-operators-statements/) |
| ακολουθία διαφυγής | escape sequence | `\` και ένας χαρακτήρας, π.χ. `\n` | [2](chapters/02-memory-variables/), [3](chapters/03-functions/) |
| αλγόριθμος | algorithm | Σαφής διαδικασία από εκτελέσιμα βήματα που τερματίζει | [0](chapters/00-hello-world/) |
| αλλαγή γραμμής | newline | Ο χαρακτήρας `\n` | [0](chapters/00-hello-world/) |
| αλφαριθμητικό μορφοποίησης | format string | Η πρώτη παράμετρος της `printf` | [2](chapters/02-memory-variables/), [3](chapters/03-functions/), [9](chapters/09-input/), [10](chapters/10-arrays/) |
| αμφισημία | ambiguity | Όταν μια λέξη ή πρόταση έχει περισσότερες από μία σημασίες | [0](chapters/00-hello-world/) |
| αναδρομή | recursion | Μια συνάρτηση καλεί τον εαυτό της. | [11](chapters/11-pointers-recursion/) |
| αναδρομική περίπτωση | recursive case | Το σημείο όπου η συνάρτηση καλεί τον εαυτό της. | [11](chapters/11-pointers-recursion/) |
| αναδρομική σχέση | recurrence | Τύπος που εκφράζει τη λύση ενός προβλήματος μέσω λύσεων μικρότερων στιγμιοτύπων. | [25](chapters/25-problem-solving-3/) |
| αναζήτηση | search | Εύρεση ενός στοιχείου (και της θέσης του) σε μια συλλογή. | [17](chapters/17-binary-search-sorting/) |
| αναζήτηση κατά βάθος | depth-first search (DFS) | Εξερεύνηση όσο πιο βαθιά γίνεται, μετά οπισθοδρόμηση. | [21](chapters/21-lists-trees/), [22](chapters/22-trees/) |
| αναζήτηση κατά πλάτος | breadth-first search (BFS) | Εξερεύνηση επίπεδο-επίπεδο. | [21](chapters/21-lists-trees/), [22](chapters/22-trees/) |
| ανάθεση | assignment | Αποθήκευση τιμής σε μεταβλητή (`x = 42;`) | [2](chapters/02-memory-variables/), [3](chapters/03-functions/) |
| ανοχή σε σφάλματα | fault tolerance | Ικανότητα ενός συστήματος να λειτουργεί σωστά παρά την αποτυχία κάποιου μέρους του. | [7](chapters/07-problem-solving/) |
| αντικειμενικό αρχείο | object file (`.o`) | Αποτέλεσμα μεταγλώττισης ενός `.c` με `gcc -c`. | [23](chapters/23-code-organization/), [24](chapters/24-advanced-topics/), [26](chapters/26-make/) |
| αντιμετάθεση | swap | Ανταλλαγή των τιμών δύο θέσεων. | [17](chapters/17-binary-search-sorting/), [18](chapters/18-sorting-input-2/) |
| αντιστάθμισμα χρόνου–μνήμης | time–space tradeoff | Ταχύτερη λύση με περισσότερη μνήμη, ή το αντίστροφο. | [16](chapters/16-problem-solving-2/) |
| άνω όριο | upper bound, Big-O | $g = O(f)$: η $g$ δεν ξεπερνά τη $c \cdot f$ για μεγάλα $n$. | [15](chapters/15-complexity-preprocessor/) |
| ανώνυμη δομή | anonymous struct | Δομή χωρίς ετικέτα, συνήθως με `typedef`. | [19](chapters/19-structs/) |
| απαρίθμηση | enumeration (`enum`) | Τύπος με ονομασμένες ακέραιες σταθερές. | [20](chapters/20-advanced-structs/) |
| απλά συνδεδεμένη λίστα | singly linked list | Αλυσίδα κόμβων, ο καθένας δείχνει στον επόμενο, ο τελευταίος στο `NULL`. | [20](chapters/20-advanced-structs/) |
| απλά συνδεδεμένη λίστα | single linked list | Κόμβοι όπου ο καθένας δείχνει στον επόμενο και ο τελευταίος στο `NULL`. | [21](chapters/21-lists-trees/) |
| άπληστος αλγόριθμος | greedy algorithm | Αλγόριθμος που κάνει σε κάθε βήμα την τοπικά καλύτερη επιλογή χωρίς να την αναθεωρεί. | [25](chapters/25-problem-solving-3/) |
| αποαναφορά | dereference | Πρόσβαση με `*` στη μεταβλητή όπου δείχνει ο δείκτης. | [11](chapters/11-pointers-recursion/), [12](chapters/12-pointers-arrays/) |
| αποθετήριο | repository | Φάκελος αρχείων μαζί με το ιστορικό τους | [4](chapters/04-git-operators/), [7](chapters/07-problem-solving/) |
| αποθήκευση κατά γραμμές | row-major order | Οι γραμμές αποθηκεύονται η μία μετά την άλλη. | [12](chapters/12-pointers-arrays/) |
| αποκλειστικό Ή | XOR (`^`) | Bit 1 όταν τα δύο bits διαφέρουν· $x \oplus x = 0$. | [16](chapters/16-problem-solving-2/) |
| απομνημόνευση | memoization | Αποθήκευση αποτελεσμάτων ώστε να μην ξαναϋπολογίζονται. | [16](chapters/16-problem-solving-2/), [25](chapters/25-problem-solving-3/) |
| αποσφαλμάτωση | debugging | Εντοπισμός και διόρθωση λαθών σε πρόγραμμα | [0](chapters/00-hello-world/), [24](chapters/24-advanced-topics/) |
| απροσδιόριστη συμπεριφορά | undefined behavior | Περίπτωση όπου η C δεν ορίζει τι θα συμβεί | [8](chapters/08-control-flow-2/), [10](chapters/10-arrays/) |
| αριθμητική δεικτών | pointer arithmetic | Το `p + n` δείχνει `n` στοιχεία (όχι bytes) μετά. | [11](chapters/11-pointers-recursion/) |
| αρχείο | file | Πόρος για αποθήκευση δεδομένων, συνήθως στον δίσκο | [1](chapters/01-command-line/), [18](chapters/18-sorting-input-2/) |
| αρχείο επικεφαλίδας | header file | Αρχείο με δηλώσεις, π.χ. `stdio.h` | [0](chapters/00-hello-world/), [15](chapters/15-complexity-preprocessor/), [23](chapters/23-code-organization/), [24](chapters/24-advanced-topics/) |
| αρχείο υλοποίησης | implementation file (`.c`) | Περιέχει τον κώδικα των συναρτήσεων. | [23](chapters/23-code-organization/) |
| αρχικοποίηση | initialization | Ανάθεση κατά τον ορισμό (`int x = 42;`) | [2](chapters/02-memory-variables/) |
| αρχικοποίηση / βήμα | initialization / step | Το πρώτο και το τρίτο μέρος της `for` | [6](chapters/06-control-flow/) |
| αρχικοποίηση δομής | struct initialization | Τιμές σε `{ }` με τη σειρά των πεδίων. | [19](chapters/19-structs/) |
| ατέρμονας βρόχος | infinite loop | Βρόχος που δεν τερματίζει ποτέ | [6](chapters/06-control-flow/) |
| αυτοαναφορά | self-reference | Όταν κάτι αναφέρεται στον εαυτό του. | [20](chapters/20-advanced-structs/) |
| αυτοαναφορική δομή | self-referential struct | Δομή με μέλος-δείκτη σε δομή του ίδιου τύπου. | [20](chapters/20-advanced-structs/) |
| αυτόματη μεταβλητή | automatic variable | `$@`, `$^`, `$<`: αλλάζουν τιμή ανά rule | [26](chapters/26-make/) |
| αφαίρεση | abstraction | Περιγραφή του τι κάνει ένα κομμάτι, κρύβοντας το πώς. | [23](chapters/23-code-organization/), [24](chapters/24-advanced-topics/) |
| αφηρημένος τύπος δεδομένων | abstract data type (ADT) | Τύπος που ορίζεται από τις λειτουργίες του, όχι από την υλοποίηση. | [21](chapters/21-lists-trees/), [22](chapters/22-trees/) |
| βάθος | depth | Ο μέγιστος αριθμός συνδέσμων από τη ρίζα ως ένα φύλλο. | [20](chapters/20-advanced-structs/) |
| βάθος / ύψος | depth / height | Μέγιστος αριθμός συνδέσμων από τη ρίζα ως τα φύλλα / από τα φύλλα ως τη ρίζα. | [21](chapters/21-lists-trees/), [22](chapters/22-trees/) |
| βασική αιτία | root cause | Το αρχικό σφάλμα από το οποίο ξεκίνησε μια αποτυχία. | [7](chapters/07-problem-solving/) |
| βασική περίπτωση | base case | Η συνθήκη όπου η αναδρομή σταματά. | [11](chapters/11-pointers-recursion/) |
| βήμα | step | Η έκφραση που αλλάζει τη μεταβλητή του βρόχου στο τέλος κάθε επανάληψης της `for`. | [7](chapters/07-problem-solving/) |
| βρόχος | loop | Εντολή που επαναλαμβάνει ένα σώμα | [6](chapters/06-control-flow/), [7](chapters/07-problem-solving/) |
| γεμάτο δυαδικό δέντρο | full binary tree | Κάθε κόμβος έχει 0 ή 2 παιδιά. | [22](chapters/22-trees/) |
| γέμισμα | padding | Αχρησιμοποίητα bytes που προσθέτει ο μεταγλωττιστής. | [19](chapters/19-structs/) |
| γλώσσα προγραμματισμού | programming language | Γλώσσα χωρίς αμφισημίες για εντολές σε υπολογιστή | [0](chapters/00-hello-world/) |
| γονικός φάκελος | parent folder | Ο φάκελος που περιέχει έναν άλλο φάκελο. | [20](chapters/20-advanced-structs/) |
| γραμμές κώδικα | lines of code (LOC) | μετρική μεγέθους ενός προγράμματος | [24](chapters/24-advanced-topics/) |
| γραμμή κώδικα | line of code (LOC / SLOC) | Εντολές μέχρι την αλλαγή γραμμής· μετρική μεγέθους. | [23](chapters/23-code-organization/) |
| γραμμική / σειριακή αναζήτηση | linear / serial search | Έλεγχος των στοιχείων ένα προς ένα· $O(n)$. | [17](chapters/17-binary-search-sorting/) |
| γραμμικό πέρασμα | linear pass | Διάσχιση των δεδομένων μία φορά, σε χρόνο $O(n)$. | [25](chapters/25-problem-solving-3/) |
| γραφική διεπαφή χρήστη | GUI | Αλληλεπίδραση με παράθυρα και ποντίκι | [1](chapters/01-command-line/) |
| γράφος | graph | Κόμβοι συνδεδεμένοι με ακμές, π.χ. πόλεις και δρόμοι. | [20](chapters/20-advanced-structs/) |
| δεδομένα εισόδου / εξόδου | input / output data | Ό,τι δίνεται στο πρόγραμμα / ό,τι παράγει. | [9](chapters/09-input/) |
| δεδομένο εξόδου | output | Ό,τι παράγει ένα πρόγραμμα όταν τελειώσει | [1](chapters/01-command-line/) |
| δείκτης | pointer | Μεταβλητή που κρατά τη διεύθυνση ενός δεδομένου. | [11](chapters/11-pointers-recursion/) |
| δείκτης σε δείκτη | pointer to pointer | Δείκτης που κρατά διεύθυνση δείκτη, π.χ. `int **`. | [12](chapters/12-pointers-arrays/) |
| δείκτης σε κενό | `void *` | Pointer σε «κάτι»: σκέτη διεύθυνση. | [13](chapters/13-memory/) |
| δείκτης σε συνάρτηση | function pointer | μεταβλητή με τη διεύθυνση μιας συνάρτησης | [24](chapters/24-advanced-topics/) |
| δείχνει σε | points to | Ο δείκτης κρατά τη διεύθυνση της μεταβλητής. | [11](chapters/11-pointers-recursion/) |
| δεκαεξαδικό σύστημα | hexadecimal | Αρίθμηση με βάση το 16 (`0`–`9`, `A`–`F`) | [2](chapters/02-memory-variables/) |
| δεσμευμένη λέξη | reserved keyword | Λέξη της C που δεν γίνεται όνομα (`int`, `if`, …) | [2](chapters/02-memory-variables/), [3](chapters/03-functions/) |
| δευτερεύουσα μνήμη | secondary memory | Μόνιμη αποθήκευση: δίσκοι, flash, DVD | [2](chapters/02-memory-variables/) |
| δήλωση | declaration | Εισαγωγή μεταβλητής με τύπο και όνομα | [2](chapters/02-memory-variables/) |
| δήλωση / ορισμός | declaration / definition | Ενημερώνει για τον τύπο / δεσμεύει μνήμη ή δίνει κώδικα. | [23](chapters/23-code-organization/) |
| διάγραμμα ενεργοποίησης | activation record / stack frame | Ο χώρος στη στοίβα για μία κλήση συνάρτησης. | [13](chapters/13-memory/) |
| διάγραμμα ροής | flowchart | Σχήμα με ρόμβους (συνθήκες) και ορθογώνια (εντολές) | [6](chapters/06-control-flow/) |
| διαίρει και βασίλευε | divide and conquer | Διαίρεση σε υποπροβλήματα, αναδρομική λύση, συνδυασμός. | [17](chapters/17-binary-search-sorting/), [18](chapters/18-sorting-input-2/) |
| διαρροή μνήμης | memory leak | Μνήμη που δεσμεύτηκε και δεν αποδεσμεύτηκε ποτέ. | [13](chapters/13-memory/), [25](chapters/25-problem-solving-3/) |
| διάσχιση | traversal | Επίσκεψη όλων των κόμβων με μια συγκεκριμένη σειρά. | [21](chapters/21-lists-trees/), [22](chapters/22-trees/) |
| διαχειριστής | root | Χρήστης με πλήρη δικαιώματα στο σύστημα | [1](chapters/01-command-line/), [20](chapters/20-advanced-structs/), [22](chapters/22-trees/) |
| διεπαφή | interface | Τι προσφέρει ένα κομμάτι του προγράμματος στα άλλα. | [23](chapters/23-code-organization/), [24](chapters/24-advanced-topics/) |
| διεπαφή γραμμής εντολών | CLI, terminal, console | Αλληλεπίδραση με εντολές κειμένου | [1](chapters/01-command-line/) |
| διεύθυνση | address | Η θέση ενός κελιού (byte) στη μνήμη | [2](chapters/02-memory-variables/), [9](chapters/09-input/), [10](chapters/10-arrays/), [11](chapters/11-pointers-recursion/) |
| διπλή αποδέσμευση | double free | Δεύτερη `free` στον ίδιο pointer. | [13](chapters/13-memory/) |
| δισδιάστατος πίνακας | two-dimensional array | Πίνακας από πίνακες, `a[γραμμές][στήλες]`. | [12](chapters/12-pointers-arrays/) |
| δομή / εγγραφή | struct / record | Συλλογή πεδίων που περιγράφουν μια οντότητα· νέος τύπος. | [19](chapters/19-structs/) |
| δομή δεδομένων | data structure | Τρόπος οργάνωσης δεδομένων στη μνήμη για αποδοτική χρήση. | [10](chapters/10-arrays/) |
| δομημένος προγραμματισμός | structured programming | Προγράμματα μόνο από ακολουθία, επιλογή, επανάληψη | [8](chapters/08-control-flow-2/) |
| δυαδική αναζήτηση | binary search | Σύγκριση με το μέσο και συνέχεια στο μισό· $O(\log n)$. | [17](chapters/17-binary-search-sorting/) |
| δυαδικό δέντρο | binary tree | Δενδρική διάταξη κόμβων με 0 έως 2 παιδιά ο καθένας. | [20](chapters/20-advanced-structs/), [21](chapters/21-lists-trees/), [22](chapters/22-trees/) |
| δυαδικό δέντρο αναζήτησης | binary search tree (BST) | Δέντρο με μικρότερα αριστερά και μεγαλύτερα δεξιά σε κάθε κόμβο. | [21](chapters/21-lists-trees/), [22](chapters/22-trees/) |
| δυαδικό σύστημα | binary | Αρίθμηση με βάση το 2 | [2](chapters/02-memory-variables/) |
| δυαδικό ψηφίο | bit (binary digit) | Η μικρότερη μονάδα πληροφορίας: 0 ή 1 | [2](chapters/02-memory-variables/) |
| δυναμική βιβλιοθήκη | dynamic library (`.so`) | Βιβλιοθήκη που φορτώνεται στην εκτέλεση, π.χ. `libm.so` | [26](chapters/26-make/) |
| δυναμικός πίνακας | dynamic array | Πίνακας με μέγεθος που αποφασίζεται κατά την εκτέλεση. | [12](chapters/12-pointers-arrays/), [13](chapters/13-memory/) |
| δυναμικός προγραμματισμός | dynamic programming | Επίλυση υποπροβλημάτων από τα μικρότερα στα μεγαλύτερα, με αποθήκευση των λύσεων σε πίνακα. | [25](chapters/25-problem-solving-3/) |
| δύο δείκτες | two pointers | Δύο θέσεις που κινούνται στα δεδομένα για να αποφύγουν εμφωλευμένους βρόχους. | [25](chapters/25-problem-solving-3/) |
| εκτελέσιμο | executable | Αρχείο που μπορεί να τρέξει ο επεξεργαστής | [0](chapters/00-hello-world/) |
| εκτελέσιμο, δυαδικό | executable, binary | Το πρόγραμμα σε κώδικα μηχανής, π.χ. `a.out` | [1](chapters/01-command-line/) |
| έκφραση | expression | Συνδυασμός τελεστών και τελεστέων με τιμή | [5](chapters/05-operators-statements/) |
| εκφυλισμένο δυαδικό δέντρο | degenerate binary tree | Κάθε κόμβος έχει έως ένα παιδί. | [22](chapters/22-trees/) |
| έλεγχος εκδόσεων | version control | Σύστημα που κρατάει το ιστορικό όλων των αλλαγών | [4](chapters/04-git-operators/) |
| εμβέλεια | scope | Το μέρος του προγράμματος όπου ένα όνομα είναι ορατό. | [14](chapters/14-scope-strings/) |
| εμφωλευμένες if | nested if | `if` μέσα στο σώμα άλλης `if` ή `else` | [6](chapters/06-control-flow/) |
| ενδιάμεση μνήμη | buffer | Όπου περιμένουν οι χαρακτήρες πριν φτάσουν στο πρόγραμμα. | [9](chapters/09-input/) |
| ένθετη / εμφωλευμένη δομή | nested struct | Δομή που είναι πεδίο άλλης δομής. | [19](chapters/19-structs/) |
| ενσωματωμένος κανόνας | built-in rule | Rule που το Make ξέρει ήδη (π.χ. `.o` από `.c`) | [26](chapters/26-make/) |
| εντολή | statement | Συντακτική δομή που εκτελείται | [5](chapters/05-operators-statements/), [6](chapters/06-control-flow/) |
| εντολή break | break statement | Τερματίζει αμέσως τον βρόχο ή τη `switch` | [8](chapters/08-control-flow-2/) |
| εντολή continue | continue statement | Προχωρά στην επόμενη επανάληψη του βρόχου | [8](chapters/08-control-flow-2/) |
| εντολή goto | goto statement | Άλμα σε εντολή με ετικέτα στην ίδια συνάρτηση | [8](chapters/08-control-flow-2/) |
| εντολή switch | switch statement | Επιλογή περίπτωσης με βάση μια ακέραια τιμή | [8](chapters/08-control-flow-2/) |
| εντολή έκφρασης | expression statement | Μια έκφραση που τελειώνει με `;` | [6](chapters/06-control-flow/) |
| ένωση | union | Τύπος σαν τη δομή, όπου όλα τα μέλη μοιράζονται την ίδια μνήμη. | [20](chapters/20-advanced-structs/) |
| εξάρτηση | dependency | Ένα αρχείο χρειάζεται ένα άλλο για να χτιστεί. | [23](chapters/23-code-organization/), [24](chapters/24-advanced-topics/) |
| έξοδος σφάλματος | standard error | Το ρεύμα `stderr`, για μηνύματα λάθους. | [18](chapters/18-sorting-input-2/) |
| επανάληψη | iteration | Μία εκτέλεση του σώματος του βρόχου | [6](chapters/06-control-flow/) |
| επέκταση | extension | Το τέλος του ονόματος (`.txt`, `.c`) που δείχνει τον τύπο | [1](chapters/01-command-line/), [18](chapters/18-sorting-input-2/) |
| επεξεργαστής κειμένου | editor | Πρόγραμμα για τη σύνταξη του κώδικα (π.χ. `vim`, VS Code). | [7](chapters/07-problem-solving/) |
| επιθεματικός / προθεματικός | postfix / prefix | `a++` (παλιά τιμή) / `++a` (νέα τιμή) | [4](chapters/04-git-operators/) |
| επίπεδο κόμβου | node level | Πόσοι κόμβοι μεσολαβούν ως τη ρίζα· η ρίζα είναι στο 1. | [21](chapters/21-lists-trees/), [22](chapters/22-trees/) |
| επισκίαση | shadowing | Εσωτερική δήλωση με ίδιο όνομα κρύβει την εξωτερική. | [14](chapters/14-scope-strings/) |
| ετικέτα | label | Όνομα με `:` μπροστά από εντολή, στόχος της `goto` | [8](chapters/08-control-flow-2/) |
| ετικέτα δομής | struct tag | Το όνομα μετά το `struct`, π.χ. `student`. | [19](chapters/19-structs/) |
| ευθυγράμμιση μνήμης | memory alignment | Διευθύνσεις πεδίων πολλαπλάσιες του 4 ή του 8. | [19](chapters/19-structs/) |
| θέση | index | Ο αριθμός (από 0) που επιλέγει ένα στοιχείο του πίνακα. | [10](chapters/10-arrays/) |
| ισορροπημένο / εκφυλισμένο δέντρο | balanced / degenerate binary tree | Ύψη υποδέντρων που διαφέρουν ≤ 1 / κάθε κόμβος με ≤ 1 παιδί. | [21](chapters/21-lists-trees/) |
| ισορροπημένο δυαδικό δέντρο | balanced binary tree | Σε κάθε κόμβο τα ύψη των υποδέντρων διαφέρουν έως 1. | [22](chapters/22-trees/) |
| κανόνας | rule | `target: prerequisites` μαζί με το recipe | [26](chapters/26-make/) |
| κανόνας μοτίβου | wildcard / pattern rule | Rule με `%` που ορίζει οικογένεια rules | [26](chapters/26-make/) |
| κανονική λειτουργία | canonical mode | Το τερματικό στέλνει την είσοδο ανά γραμμή. | [9](chapters/09-input/) |
| κατάλογος, φάκελος | directory, folder | Περιέχει αρχεία και άλλους καταλόγους | [1](chapters/01-command-line/) |
| κατάσταση ροής | flow | Κατάσταση πλήρους απορρόφησης και συγκέντρωσης σε μια δραστηριότητα. | [7](chapters/07-problem-solving/) |
| καταχώρηση | commit | Αποθήκευση των αλλαγών στο τοπικό repository | [4](chapters/04-git-operators/) |
| καταχωρητής | register | ταχύτατη θέση αποθήκευσης μέσα στη CPU | [24](chapters/24-advanced-topics/) |
| κάτω όριο | lower bound, $\Omega$ | $g = \Omega(f)$: η $g$ είναι τουλάχιστον $c \cdot f$ για μεγάλα $n$. | [15](chapters/15-complexity-preprocessor/) |
| κέλυφος | shell | Πρόγραμμα που τρέχει τις εντολές που πληκτρολογούμε | [1](chapters/01-command-line/) |
| κενή εντολή | empty / null statement | Το σκέτο `;`, που δεν κάνει τίποτα (no-op) | [6](chapters/06-control-flow/) |
| κενοί χαρακτήρες | whitespace | Κενά, tabs και αλλαγές γραμμής. | [10](chapters/10-arrays/) |
| κενός δείκτης | null pointer (`NULL`) | Δείκτης με τιμή 0 που δεν δείχνει πουθενά. | [11](chapters/11-pointers-recursion/), [12](chapters/12-pointers-arrays/), [13](chapters/13-memory/) |
| κενός τύπος | `void` | Τύπος χωρίς τιμές· π.χ. συνάρτηση που δεν επιστρέφει τίποτα. | [13](chapters/13-memory/) |
| κεφαλή / ουρά | head / tail | Το πρώτο / (συνήθως) το τελευταίο στοιχείο της λίστας. | [21](chapters/21-lists-trees/) |
| κινητή υποδιαστολή | floating point | Αναπαράσταση πραγματικών (`float`, `double`), κατά προσέγγιση. | [9](chapters/09-input/) |
| κλήση κατά τιμή | call by value | Η συνάρτηση παίρνει αντίγραφα των ορισμάτων. | [16](chapters/16-problem-solving-2/) |
| κλήση συνάρτησης | function call | Εκτέλεση της συνάρτησης με συγκεκριμένα ορίσματα | [3](chapters/03-functions/) |
| κόμβος | node | Ένα στοιχείο λίστας ή δέντρου (μια δομή). | [20](chapters/20-advanced-structs/) |
| κόμβος / παιδί | node / child | Στοιχείο του δέντρου / κόμβος ακριβώς κάτω από έναν άλλο. | [22](chapters/22-trees/) |
| κρεμασμένο else | dangling else | Αμφισημία για το σε ποια `if` ανήκει ένα `else` | [6](chapters/06-control-flow/) |
| κύρια μνήμη | primary memory (RAM) | Προσωρινή μνήμη με άμεση πρόσβαση από τον επεξεργαστή | [2](chapters/02-memory-variables/) |
| κώδικας-μακαρονάδα | spaghetti code | Κώδικας με μπερδεμένη ροή, δύσκολος στην ανάγνωση | [8](chapters/08-control-flow-2/) |
| κωδικός εξόδου | exit code | Η τιμή που επιστρέφει η `main`· `0` = επιτυχία | [1](chapters/01-command-line/), [3](chapters/03-functions/) |
| λάθος κατά ένα | off-by-one error | Βρόχος που κάνει μία επανάληψη παραπάνω ή λιγότερο λόγω λάθους στο όριο. | [7](chapters/07-problem-solving/) |
| λειτουργικό σύστημα | operating system (OS) | Λογισμικό που διαχειρίζεται υλικό και πόρους και εξυπηρετεί τα προγράμματα | [1](chapters/01-command-line/) |
| λογικός τελεστής | logical operator | `&&`, `\|\|`, `!` | [5](chapters/05-operators-statements/) |
| λογισμικό / υλικό | software / hardware | Τα προγράμματα / η ίδια η συσκευή | [0](chapters/00-hello-world/) |
| μακροεντολή | macro | Όνομα (με ή χωρίς παραμέτρους) που αντικαθίσταται με κείμενο. | [15](chapters/15-complexity-preprocessor/), [26](chapters/26-make/) |
| μέγεθος | size | Πόσα στοιχεία έχει ο πίνακας· στατικό μετά τη δήλωση. | [10](chapters/10-arrays/) |
| μέση / χειρότερη περίπτωση | average / worst case | Κόστος κατά μέσο όρο / για τη χειρότερη είσοδο. | [18](chapters/18-sorting-input-2/) |
| μεταβλητή | variable | Τμήμα της μνήμης με όνομα και τύπο | [2](chapters/02-memory-variables/) |
| μεταβλητή-σημαία | flag | Μεταβλητή 0/1 που καταγράφει αν συνέβη κάτι | [8](chapters/08-control-flow-2/), [16](chapters/16-problem-solving-2/) |
| μεταγλώττιση υπό συνθήκη | conditional compilation | Κράτημα ή αφαίρεση κώδικα με `#if` / `#ifdef`. | [15](chapters/15-complexity-preprocessor/) |
| μεταγλωττιστής | compiler | Μετατρέπει πηγαίο κώδικα σε γλώσσα μηχανής (π.χ. `gcc`) | [0](chapters/00-hello-world/), [1](chapters/01-command-line/), [3](chapters/03-functions/), [15](chapters/15-complexity-preprocessor/) |
| μέτωπο | frontier / worklist | Οι κόμβοι που περιμένουν επεξεργασία στη BFS. | [21](chapters/21-lists-trees/), [22](chapters/22-trees/) |
| μη έγκυρος δείκτης | invalid pointer | Δείκτης που δεν κρατά έγκυρη διεύθυνση. | [11](chapters/11-pointers-recursion/) |
| μη προσημασμένος | unsigned | Ακέραιος τύπος χωρίς αρνητικές τιμές | [2](chapters/02-memory-variables/) |
| μήκος λίστας | list length | Ο αριθμός των στοιχείων της λίστας. | [20](chapters/20-advanced-structs/) |
| μονάδα μετάφρασης | translation unit | Ένα αρχείο `.c` μαζί με ό,τι φέρνουν τα `#include` του | [26](chapters/26-make/) |
| μοναδιαίος / δυαδικός / τριαδικός | unary / binary / ternary | Τελεστής με έναν / δύο / τρεις τελεστέους | [5](chapters/05-operators-statements/) |
| μονοπάτι | path | Η θέση ενός αρχείου στην ιεραρχία, π.χ. `/home/users` | [1](chapters/01-command-line/) |
| μονοπάτι | filepath | Η πλήρης θέση ενός αρχείου, π.χ. `/home/…/students.txt`. | [18](chapters/18-sorting-input-2/) |
| μορφοποιητής κώδικα | code formatter | Εργαλείο (π.χ. `clang-format`) που ξαναγράφει τον κώδικα σύμφωνα με ένα στυλ. | [7](chapters/07-problem-solving/) |
| Ν-αδικό δέντρο | N-ary tree | Δέντρο με περισσότερα από 2 παιδιά ανά κόμβο. | [22](chapters/22-trees/) |
| οδηγία | directive | Γραμμή που αρχίζει με `#`, π.χ. `#include` | [1](chapters/01-command-line/), [3](chapters/03-functions/) |
| οδηγία προεπεξεργαστή | preprocessor directive | Γραμμή που αρχίζει με `#`, π.χ. `#include`. | [15](chapters/15-complexity-preprocessor/) |
| οκταδικό σύστημα | octal | Αρίθμηση με βάση το 8 | [2](chapters/02-memory-variables/) |
| ολοκληρωμένο περιβάλλον ανάπτυξης | IDE | Editor με ενσωματωμένη μεταγλώττιση, τερματικό και debugger. | [7](chapters/07-problem-solving/) |
| οπισθοδρόμηση | backtracking | Επιστροφή σε προηγούμενο κόμβο για να δοκιμαστεί άλλος κλάδος. | [22](chapters/22-trees/) |
| όρισμα | argument | Τιμή που δίνουμε σε ένα πρόγραμμα όταν το τρέχουμε | [1](chapters/01-command-line/), [3](chapters/03-functions/) |
| ορίσματα γραμμής εντολών | command-line arguments | Οι λέξεις της κλήσης, στα `argc`/`argv`. | [12](chapters/12-pointers-arrays/) |
| ορισμός συνάρτησης | function definition | Τύπος, όνομα, ορίσματα και σώμα | [3](chapters/03-functions/) |
| παγκόσμια / στατική μνήμη | global / static memory | Μνήμη για μεταβλητές που ζουν όσο το πρόγραμμα. | [13](chapters/13-memory/), [14](chapters/14-scope-strings/) |
| παγκόσμια μεταβλητή | global variable | Δηλώνεται έξω από συναρτήσεις· ορατή ως το τέλος του αρχείου. | [14](chapters/14-scope-strings/) |
| παλινδρομικός | palindrome | Που διαβάζεται ίδια και από τις δύο μεριές. | [16](chapters/16-problem-solving-2/) |
| παραγοντικό | factorial | $n! = 1 \cdot 2 \cdots n$, με $0! = 1$. | [11](chapters/11-pointers-recursion/) |
| παράμετρος εξόδου | output parameter | Δείκτης μέσω του οποίου η συνάρτηση γράφει ένα αποτέλεσμα. | [16](chapters/16-problem-solving-2/) |
| παρωχημένο | out of date | Target που λείπει ή είναι παλαιότερο από prerequisite του | [26](chapters/26-make/) |
| πεδίο / μέλος | field / member | Μία από τις μεταβλητές μέσα σε μια δομή. | [19](chapters/19-structs/) |
| πεδίο bit | bit field | Μέλος δομής με δηλωμένο πλήθος bits (`int year : 3;`). | [20](chapters/20-advanced-structs/) |
| περιγραφέας αρχείου | file descriptor (FD) | Ο ακέραιος που ταυτίζει ένα ανοιχτό αρχείο (`fileno`). | [18](chapters/18-sorting-input-2/) |
| περίπτωση | case | Σημείο εισόδου της `switch` για μια σταθερά | [8](chapters/08-control-flow-2/) |
| πηγαίο αρχείο | source file | Αρχείο κειμένου με τον κώδικα, π.χ. `helloworld.c` | [0](chapters/00-hello-world/) |
| πηγαίος κώδικας | source code | Το πρόγραμμα όπως το γράφουμε, π.χ. `hello.c` | [1](chapters/01-command-line/) |
| πίνακας | array | Σύνολο στοιχείων ίδιου τύπου σε συνεχόμενες θέσεις μνήμης, με ένα όνομα. | [10](chapters/10-arrays/) |
| πίνακας / θέση | array / index | Στοιχεία ίδιου τύπου σε συνεχόμενη μνήμη / ο `i` στο `a[i]`. | [12](chapters/12-pointers-arrays/) |
| πίνακας ASCII | ASCII table | Αντιστοίχιση κωδικών 0–127 σε χαρακτήρες | [2](chapters/02-memory-variables/) |
| πίνακας από δείκτες | array of pointers | Πίνακας με στοιχεία τύπου δείκτη, π.χ. `char *s[5]`. | [12](chapters/12-pointers-arrays/) |
| πίνακας εκτέλεσης | trace table | Πίνακας με τις τιμές των μεταβλητών σε κάθε βήμα μιας εκτέλεσης με το χέρι. | [25](chapters/25-problem-solving-3/) |
| πλάτος πεδίου | field width | Ο αριθμός στο `%6s`: μέγιστοι χαρακτήρες που θα διαβαστούν. | [18](chapters/18-sorting-input-2/) |
| πλήθος τελεστέων | arity | Μοναδιαίος (1), δυαδικός (2), τριαδικός (3) | [4](chapters/04-git-operators/) |
| πλήρες δυαδικό δέντρο | complete binary tree | Γεμάτα επίπεδα εκτός ίσως του τελευταίου, που γεμίζει από αριστερά. | [22](chapters/22-trees/) |
| πολυπλοκότητα | complexity | Μέτρο απόδοσης ενός αλγορίθμου ως συνάρτηση του μεγέθους του προβλήματος. | [15](chapters/15-complexity-preprocessor/) |
| προαπαιτούμενο | prerequisite | Target από το οποίο εξαρτάται ένα άλλο target | [26](chapters/26-make/) |
| πρόγραμμα | program | Η καταγραφή της επίλυσης ενός προβλήματος, ως σύνολο εντολών | [0](chapters/00-hello-world/) |
| προγραμματισμός | programming | Σαφής καθορισμός διαδικασίας που λύνει πρόβλημα υπολογισμού | [0](chapters/00-hello-world/) |
| προγραμματισμός σε ζεύγη | pair programming | Driver γράφει, navigator ελέγχει, αλλάζουν ρόλους | [3](chapters/03-functions/), [4](chapters/04-git-operators/) |
| προεπεξεργαστής | preprocessor | Πρώτο στάδιο του μεταγλωττιστή· μετασχηματίζει το κείμενο του κώδικα. | [15](chapters/15-complexity-preprocessor/) |
| προεπιλογή | default | Η περίπτωση όταν δεν ταιριάζει κανένα `case` | [8](chapters/08-control-flow-2/) |
| προθεματικά αθροίσματα | prefix sums | Πίνακας με τα αθροίσματα των πρώτων $i$ στοιχείων, για αθροίσματα διαστημάτων σε $O(1)$. | [25](chapters/25-problem-solving-3/) |
| προθεματικός / επιθεματικός | prefix / postfix | Πριν / μετά τη μεταβλητή (`++a` / `a++`) | [5](chapters/05-operators-statements/) |
| προσδιοριστής const | const qualifier | Δηλώνει ότι μια θέση μνήμης δεν αλλάζει. | [23](chapters/23-code-organization/) |
| προσδιοριστικό μορφοποίησης | format specifier | `%` και χαρακτήρες, π.χ. `%d` | [2](chapters/02-memory-variables/), [3](chapters/03-functions/) |
| προσεταιριστικότητα | associativity | Σειρά υπολογισμού για ίση προτεραιότητα | [4](chapters/04-git-operators/), [5](chapters/05-operators-statements/) |
| προσωρινή λίστα | staging area | Οι αλλαγές που θα μπουν στο επόμενο commit | [4](chapters/04-git-operators/) |
| προτεραιότητα | precedence | Ποιος τελεστής εφαρμόζεται πρώτος | [4](chapters/04-git-operators/), [5](chapters/05-operators-statements/) |
| προτροπή | prompt | Το `user@host:dir$` πριν από κάθε εντολή | [1](chapters/01-command-line/) |
| πρότυπη είσοδος | standard input (`stdin`) | Η προεπιλεγμένη είσοδος, συνήθως το πληκτρολόγιο. | [9](chapters/09-input/) |
| πρότυπη είσοδος / έξοδος | standard input / output | Τα ρεύματα `stdin` / `stdout` του προγράμματος. | [18](chapters/18-sorting-input-2/) |
| πρωτότυπο συνάρτησης | function prototype | Όνομα, τύπος επιστροφής και ορίσματα, χωρίς σώμα. | [23](chapters/23-code-organization/), [24](chapters/24-advanced-topics/) |
| πτώση | fall-through | Συνέχιση στο επόμενο `case` όταν λείπει το `break` | [8](chapters/08-control-flow-2/) |
| πυρήνας | kernel | Το κεντρικό μέρος του OS, που μιλάει με το υλικό | [1](chapters/01-command-line/) |
| ρεύμα | stream | Ένα ανοιχτό αρχείο, ως `FILE *`. | [18](chapters/18-sorting-input-2/) |
| ρίζα | root directory | Ο κατάλογος `/`, κορυφή της ιεραρχίας | [1](chapters/01-command-line/) |
| ρίζα / φύλλο | root / leaf | Ο πρώτος κόμβος / κόμβος χωρίς παιδιά. | [21](chapters/21-lists-trees/) |
| ροή ελέγχου | control flow | Η σειρά εκτέλεσης των εντολών | [5](chapters/05-operators-statements/), [6](chapters/06-control-flow/) |
| σειρά bytes | endianness | Η σειρά αποθήκευσης των bytes ενός ακεραίου. | [12](chapters/12-pointers-arrays/), [13](chapters/13-memory/) |
| σειριακή αναζήτηση | linear search | Έλεγχος των στοιχείων ένα-ένα μέχρι να βρεθεί το ζητούμενο. | [10](chapters/10-arrays/) |
| σιωπηρή μετατροπή | implicit type conversion | Αυτόματη μετατροπή στον «μεγαλύτερο» τύπο | [4](chapters/04-git-operators/), [5](chapters/05-operators-statements/) |
| σταθερά απαρίθμησης | enumeration constant | Ένα από τα ονόματα μιας απαρίθμησης, π.χ. `Mon`. | [20](chapters/20-advanced-structs/) |
| σταθερή / λογαριθμική / γραμμική | constant / logarithmic / linear | $O(1)$ / $O(\log n)$ / $O(n)$. | [15](chapters/15-complexity-preprocessor/) |
| σταθερή συμβολοσειρά | string literal | Κείμενο σε εισαγωγικά μέσα στον κώδικα. | [14](chapters/14-scope-strings/) |
| στατική μεταβλητή | static variable | Κρατά την τιμή της ανάμεσα σε κλήσεις, ως το τέλος του προγράμματος. | [14](chapters/14-scope-strings/) |
| στοίβα | stack | Συνεχόμενη μνήμη LIFO για τοπικές μεταβλητές και ορίσματα. | [13](chapters/13-memory/) |
| στοιχείο διαμέρισης | pivot element | Το στοιχείο γύρω από το οποίο γίνεται η διαμέριση. | [17](chapters/17-binary-search-sorting/), [18](chapters/18-sorting-input-2/) |
| στοίχιση | indentation | Τα κενά στην αρχή κάθε γραμμής που δείχνουν το επίπεδο εμφώλευσης. | [7](chapters/07-problem-solving/) |
| στόχος | target | Ό,τι μπορεί να παραχθεί, συνήθως ένα αρχείο | [26](chapters/26-make/) |
| συγκριτικός τελεστής | comparison / relational operator | `==`, `!=`, `<`, `>`, `<=`, `>=` | [5](chapters/05-operators-statements/) |
| συγχώνευση | merge | Ένωση δύο ταξινομημένων ακολουθιών σε μία ταξινομημένη. | [17](chapters/17-binary-search-sorting/), [18](chapters/18-sorting-input-2/) |
| συμβόλαιο | contract | Εγγύηση που δίνει η δήλωση μιας συνάρτησης στους χρήστες της. | [23](chapters/23-code-organization/), [24](chapters/24-advanced-topics/) |
| σύμβολο | symbol | Όνομα συνάρτησης ή μεταβλητής σε αρχείο αντικειμένου. | [14](chapters/14-scope-strings/) |
| συμβολοσειρά | string | Κείμενο ανάμεσα σε διπλά εισαγωγικά, π.χ. `"Hello world\n"` | [0](chapters/00-hello-world/), [10](chapters/10-arrays/), [14](chapters/14-scope-strings/) |
| συμπλήρωμα ως προς 2 | two's complement | Αναπαράσταση αρνητικών: flip όλα τα bits και +1 | [2](chapters/02-memory-variables/) |
| συνάρτηση | function | Υπολογισμός από εισόδους σε έξοδο, με όνομα | [3](chapters/03-functions/) |
| σύνδεση | linking | Ένωση αντικειμενικών αρχείων σε εκτελέσιμο. | [23](chapters/23-code-organization/), [24](chapters/24-advanced-topics/) |
| συνδέτης | linker | Ενώνει αντικειμενικά αρχεία και βιβλιοθήκες σε εκτελέσιμο | [0](chapters/00-hello-world/), [3](chapters/03-functions/), [26](chapters/26-make/) |
| συνδυαστικός τελεστής ανάθεσης | compound assignment | `+=`, `-=`, … | [5](chapters/05-operators-statements/) |
| συνένωση | concatenation | Προσάρτηση ενός string στο τέλος άλλου. | [14](chapters/14-scope-strings/) |
| σύνθετη εντολή | compound statement / block | Εντολές μέσα σε `{ }`, που μετράνε ως μία | [6](chapters/06-control-flow/) |
| σύνολο ορισμού / τιμών | domain / co-domain | Τα σύνολα εισόδων και εξόδων | [3](chapters/03-functions/) |
| συνταγή | recipe | Οι εντολές shell που φτιάχνουν ένα target | [26](chapters/26-make/) |
| συνώνυμο τύπου | `typedef` | Νέο όνομα για υπάρχοντα τύπο. | [19](chapters/19-structs/) |
| συσσωρευτής | accumulator | Μεταβλητή που μαζεύει ένα αποτέλεσμα (άθροισμα, γινόμενο) κατά τη διάρκεια ενός βρόχου. | [7](chapters/07-problem-solving/) |
| σύστημα κατασκευής | build system | Εργαλείο που αυτοματοποιεί το χτίσιμο ενός project | [26](chapters/26-make/) |
| σφάλμα κατάτμησης | segmentation fault | Τερματισμός από πρόσβαση σε μη επιτρεπτή μνήμη. | [11](chapters/11-pointers-recursion/) |
| σφάλμα σύνδεσης | linking error | Ο linker δεν βρίσκει υλοποίηση συμβόλου (`undefined reference`) | [26](chapters/26-make/) |
| σχόλιο | comment | Κείμενο μέσα σε `/* */` που αγνοεί ο μεταγλωττιστής | [0](chapters/00-hello-world/), [1](chapters/01-command-line/), [7](chapters/07-problem-solving/) |
| σωρός | heap | Η περιοχή μνήμης από την οποία δεσμεύει η `malloc`. | [12](chapters/12-pointers-arrays/), [13](chapters/13-memory/) |
| τάξη μεγέθους | order of growth, $\Theta$ | Ισχύουν ταυτόχρονα $O$ και $\Omega$. | [15](chapters/15-complexity-preprocessor/) |
| ταξινομημένη ακολουθία | sorted sequence | $a_i \leq_\alpha a_j$ για κάθε $i \leq j$. | [17](chapters/17-binary-search-sorting/) |
| ταξινόμηση | sorting | Αναδιάταξη μιας ακολουθίας ώστε να γίνει ταξινομημένη. | [17](chapters/17-binary-search-sorting/), [18](chapters/18-sorting-input-2/) |
| ταξινόμηση εισαγωγής | insertion sort | Εισάγει κάθε στοιχείο σε ταξινομημένο πρόθεμα. | [17](chapters/17-binary-search-sorting/) |
| ταξινόμηση επιλογής | selection sort | Φέρνει κάθε φορά το ελάχιστο του υπολοίπου μπροστά. | [17](chapters/17-binary-search-sorting/) |
| ταξινόμηση συγχώνευσης | merge sort | Ταξινομεί τα δύο μισά και τα συγχωνεύει. | [17](chapters/17-binary-search-sorting/) |
| ταξινόμηση φυσαλίδας | bubblesort | Αντιμεταθέτει γειτονικά στοιχεία σε λάθος σειρά. | [17](chapters/17-binary-search-sorting/) |
| ταχυταξινόμηση | quicksort | Διαμερίζει γύρω από ένα pivot και ταξινομεί τα δύο μέρη. | [17](chapters/17-binary-search-sorting/) |
| τεκμηρίωση | documentation | Ονόματα, σχόλια και `README` που κάνουν ένα πρόγραμμα κατανοητό. | [7](chapters/07-problem-solving/) |
| τέλειο / γεμάτο / πλήρες δέντρο | perfect / full / complete binary tree | Βλ. «Τύποι δυαδικών δέντρων». | [21](chapters/21-lists-trees/) |
| τέλειο δυαδικό δέντρο | perfect binary tree | Όλοι οι εσωτερικοί κόμβοι με 2 παιδιά, όλα τα φύλλα στο ίδιο επίπεδο. | [22](chapters/22-trees/) |
| τελεστέος | operand | Μεταβλητή ή σταθερά πάνω στην οποία δουλεύει ο τελεστής | [4](chapters/04-git-operators/), [5](chapters/05-operators-statements/) |
| τελεστής | operator | Σύμβολο που κάνει υπολογισμό και επιστρέφει τιμή | [4](chapters/04-git-operators/), [5](chapters/05-operators-statements/) |
| τελεστής ανάθεσης | assignment operator | `=`· αναθέτει και επιστρέφει την τιμή | [4](chapters/04-git-operators/), [5](chapters/05-operators-statements/) |
| τελεστής αύξησης / μείωσης | increment / decrement operator | `++` / `--` | [5](chapters/05-operators-statements/) |
| τελεστής βέλους | arrow operator (`->`) | `ptr->f` ισοδυναμεί με `(*ptr).f`. | [19](chapters/19-structs/) |
| τελεστής μετατροπής | cast operator | `(τύπος)τελεστέος`, ρητή μετατροπή τύπου | [4](chapters/04-git-operators/), [5](chapters/05-operators-statements/) |
| τελεστής παράθεσης | comma operator | `a, b`: υπολογίζει το `a`, επιστρέφει το `b` | [4](chapters/04-git-operators/), [5](chapters/05-operators-statements/) |
| τελεστής συνθήκης | conditional operator | `σ ? α : β`, ο μόνος τριαδικός τελεστής | [5](chapters/05-operators-statements/) |
| τέλος αρχείου | End-Of-File (`EOF`) | Τιμή (`-1`) που δηλώνει ότι δεν υπάρχει άλλη είσοδος. | [9](chapters/09-input/), [10](chapters/10-arrays/) |
| τετραγωνική / εκθετική | quadratic / exponential | $O(n^2)$ / $O(2^n)$. | [15](chapters/15-complexity-preprocessor/) |
| τιμή επιστροφής | return value | Η τιμή που δίνει πίσω μια συνάρτηση. | [9](chapters/09-input/) |
| τοπική μεταβλητή | local variable | Δηλώνεται σε συνάρτηση· ορατή ως το τέλος του block. | [14](chapters/14-scope-strings/) |
| τρέχων / γονικός κατάλογος | current / parent directory | `.` και `..` | [1](chapters/01-command-line/) |
| τυπική έξοδος | standard output (stdout) | Το αρχείο όπου γράφει η `printf` | [2](chapters/02-memory-variables/), [9](chapters/09-input/) |
| τύπος | type | Πόση μνήμη πιάνει μια τιμή και πώς ερμηνεύεται | [2](chapters/02-memory-variables/), [3](chapters/03-functions/) |
| τύπος ορισμένος από τον χρήστη | user-defined type | Τύπος που ορίζει το πρόγραμμα, όπως μια δομή. | [19](chapters/19-structs/) |
| υλικό | hardware | Οι φυσικές συσκευές του υπολογιστή | [1](chapters/01-command-line/) |
| υπερχείλιση | overflow | Αποτέλεσμα που δεν χωράει στον τύπο της μεταβλητής | [8](chapters/08-control-flow-2/), [11](chapters/11-pointers-recursion/) |
| υπερχείλιση / υποχείλιση | overflow / underflow | Πρόσβαση μετά το τέλος / πριν την αρχή ενός πίνακα. | [10](chapters/10-arrays/) |
| υπερχείλιση buffer | buffer overflow | Εγγραφή πέρα από το τέλος ενός πίνακα. | [14](chapters/14-scope-strings/) |
| υπερχείλιση ακεραίων | integer overflow | Αποτέλεσμα που δεν χωράει στον τύπο του | [2](chapters/02-memory-variables/), [3](chapters/03-functions/) |
| υπερχείλιση στοίβας | stack overflow | Η στοίβα ξεπερνά το όριό της, π.χ. από ατέρμονη αναδρομή. | [13](chapters/13-memory/) |
| υποδέντρο | subtree | Ένα παιδί μαζί με όλους τους απογόνους του. | [22](chapters/22-trees/) |
| υποεντολή | subcommand | Λέξη στο `argv[1]` που επιλέγει τι θα κάνει το πρόγραμμα. | [16](chapters/16-problem-solving-2/) |
| υπολογιστής | computer | Κατασκευή που επεξεργάζεται δεδομένα και παράγει αποτελέσματα | [0](chapters/00-hello-world/) |
| φύλλο | leaf | Κόμβος χωρίς παιδιά. | [20](chapters/20-advanced-structs/), [22](chapters/22-trees/) |
| χειρότερη / μέση περίπτωση | worst / average case | Κόστος για τη δυσκολότερη / κατά μέσο όρο είσοδο. | [17](chapters/17-binary-search-sorting/) |
| χειρότερη περίπτωση | worst case | Η είσοδος που κάνει τον αλγόριθμο να δουλέψει περισσότερο. | [16](chapters/16-problem-solving-2/) |
| χρήση μετά την αποδέσμευση | use after free | Πρόσβαση σε μνήμη μετά την `free` της. | [13](chapters/13-memory/) |
| χρονική / χωρική πολυπλοκότητα | time / space complexity | Πώς αυξάνεται ο χρόνος / η μνήμη με το $n$. | [15](chapters/15-complexity-preprocessor/) |
| χρονική πολυπλοκότητα | time complexity | Πώς αυξάνονται τα βήματα με το μέγεθος της εισόδου. | [16](chapters/16-problem-solving-2/) |
| χρόνος ζωής | lifetime | Το διάστημα της εκτέλεσης όπου υπάρχει η μεταβλητή. | [14](chapters/14-scope-strings/) |
| χωρική πολυπλοκότητα | space complexity | Πόση επιπλέον μνήμη χρειάζεται σε σχέση με την είσοδο. | [16](chapters/16-problem-solving-2/) |

<!-- {% endraw %} -->
