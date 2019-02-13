from functions import *


excludedprv = []
excludedcur = []
rounds = int(input('Δώσε τον αριθμό των γύρων:'))
players = int(input('Δώσε τον αριθμό των παικτών:'))
lives = int(input('Ζωές καθε παίκτη(4 ή 6 ή 8):'))
losers = []
playernames = []
for i in range(players):
    message = 'Δώσε το όνομα του παίκτη '+str(i+1)+':'
    insert = input(message)
    playernames.append(insert)

for i in range(rounds):
    for player in playernames :
        if player not in losers:
            excluded = excludedprv + excludedcur
            print('Παίκτης:',player)
            print('Έχεις περιθώριο να επιλέξεις μέχρι '+ str(lives-1)+ ' λάθος γράμματα και ,το '+ str(lives) +'ο λάθος γράμμα σε βγάζει εκτός παιχνιδιού.')
            word = wordchoice(diary,excluded)
            excludedcur.append(word)
            hiddenword = crypto(word)
            playerlives = lives

            while hiddenword!=word and player not in losers:
                
                print('Η λέξη που πρέπει να μαντέψεις είναι:',withspaces(hiddenword),' help:',word)
                givenletter = letterinput()
                varieties = variations(givenletter)
                changed = False
                for i in range(len(word)):
                    if word[i] in varieties:
                        hiddenlist = list(hiddenword)
                        hiddenlist[i] = word[i]
                        hiddenword = ''.join(hiddenlist)                        
                        changed = True
                if hiddenword == word:
                    print('Βρήκες τη λέξη:',word)
                if not changed :
                    playerlives += -1
                    visual(lives-playerlives,lives)
                print('Έχεις ακόμα '+str(playerlives)+' ζωές')
                if playerlives==0:
                    losers.append(player)


    excludedprv = excludedcur
    excludedcur = []
    if len(losers)==players:
        print('Χωρίς νικητή')
        break
    if len(losers)+1==players:
        for item in playernames:
            if item not in losers:
                winner = item
        
        print('Νικητής ο:',winner)
        break
                    

                
                
                
                
