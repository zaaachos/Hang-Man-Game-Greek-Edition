import random

diary = ['χρησμοδοτούσατε','αλύπητες', 'αναδιπλασιασμένος', 'εξογκώνει', 'ζωτικότατε', 'λιθόσφαιρα', 'ασχήμιζες','δυστυχήσατε','χορταστικοί',
         'συνδικαλίστριας', 'ψιλορώταγα', 'τσούπρα', 'βαρυστόμαχου', 'ακαθαρσιών', 'χουφτώνουν','αυτονομαζόμαστε', 'πλουσιότερος', 'ομότοιχη',
         'αντεπαναστατών', 'δασκαλικούς','φυσιολατρικοί','δοξαστικέ','επιβλεπόσουν', 'τσιμινιέρα', 'ξεφλούδιστοι', 'μπολιάσουν', 'διπλοκλειδωνόμαστε',
         'διασαφήνισή', 'τροπικούς', 'λήσταρχος', 'σπουδαιολογείς', 'ταβερνογυριστής','καθοριστικότατο', 'αψεγάδιαστων', 'τσαρλατάνε',
         'πειθαρχήσετε', 'συδαυλιστούν', 'χειριστήριον', 'λιποειδών', 'στερεοχημικός','συστέλλονταν', 'επιρροές','τοποθέτηση',
         'επανιδρυόσασταν', 'βαλβιδοπάθειας', 'διαφράγματος', 'λαμπικαρισμένης', 'αρχαιόσυλων', 'φτιασιδώνετε', 'μεσολαβητικοί' ]



def wordchoice(diary,excluded):
    word = random.choice(diary)
    while word in excluded:
        word = random.choice(diary)
    return word

def crypto(word):
    encrypt = ''.join(['_' for x in word])
    return encrypt

def withspaces(word):
    listtool = [letter+' ' for letter in word]
    return ''.join(listtool)


def visual(mistakes,lives):
    a1 = '|---------|'
    a2 = '|'
    a3 = '|'
    a4 = '|'
    a5 = '|'
    a6 = '|'
    a7 = '|'
    
    b1= '|         Ο'
    b2= '|         |'
    b3= '|         |\ '
    b4= '|        /|\ '
    b5= '|          \_'
    b6= '|       _/ \_'
    b7= '|       ##  ## '
    b8= '|        fire '
    steps = [b1,b2,b3,b4,b5,b6,b7,b8]
    if mistakes >0:
        a2 = b1
    if (mistakes>=2 and lives==8)or(mistakes>=2 and lives==6)or(mistakes>=1 and lives==4):
        a3,a4 = b2,b2
    if mistakes ==3 and lives==8:
        a4 = b3
    if (mistakes>=4 and lives==8)or(mistakes>=3 and lives==6)or(mistakes>=2 and lives==4):
        a4 = b4
    if mistakes ==5 and lives ==8:
        a5 = b5
    if (mistakes>=6 and lives==8)or(mistakes>=4 and lives==6)or(mistakes>=2 and lives==4):
        a5 = b6
    if (mistakes>=7 and lives==8)or(mistakes>=5 and lives==6)or(mistakes>=3 and lives==4):
        a6 = b7
    if (mistakes>=8 and lives==8)or(mistakes>=6 and lives==6)or(mistakes>=4 and lives==4):
        a7 = b8

    lines = [a1,a2,a3,a4,a5,a6,a7]
    for line in lines:
        print(line)



def variations(letter):
    if letter=='α' or letter =='ά':
        var = ['α','ά']
    elif letter=='υ' or letter =='ύ' or letter=='ΰ' or letter=='ϋ' :
        var = ['υ','ύ','ΰ']
    elif letter=='ι' or letter =='ί' or letter=='ΐ' or letter=='ϊ':
        var = ['ι','ί','ΐ']
    elif letter=='η' or letter =='ή':
        var = ['η','ή']
    elif letter=='ο' or letter =='ό':
        var = ['ο','ό']
    elif letter=='ε' or letter =='έ':
        var = ['ε','έ']
    elif letter=='ω' or letter =='ώ':
        var = ['ω','ώ']
    elif letter=='σ' or letter =='ς':
        var = ['σ','ς']
    else:
        var = letter
    return var

def letterinput():
    letter = input('Δώσε γράμμα:')
    while not (len(letter)==1 and (ord(letter) in range(940,976))):
        letter = input('Λάθος είσοδος, ξαναδώσε γράμμα:')
    return letter






















          
    
    
