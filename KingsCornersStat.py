import random
import KingsCornersFunctions as kcf
import xlwt

#writing to spreadsheet
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Sheet_1')

wu = 1
while(wu < 49):
    trials = 10000
    startinghand = wu
    goesout = 0

    bdeck = []
    deck = []
    hand = []
    r1 = []
    r2 = []
    r3 = []
    r4 = []

    i = 1
    while(i < 53): #Makes a deck cause I'll lazy
        if(i< 14):
              z = 'H' + str(i)
        elif(i< 27):
              z = 'S' + str(i - 13)
        elif(i< 40):
              z = 'D' + str(i - 26)
        elif(i< 53):
              z = 'C' + str(i - 39)
        deck.append(z)
        i += 1
    bdeck = deck.copy()
    i = 0
    while(i < trials):
        deck = []
        hand = []
        r1 = []
        r2 = []
        r3 = []
        r4 = []
        deck = bdeck.copy()
        x = 0
        while(x < startinghand): #Generates starting hand
            num = random.randint(0,len(deck) - 1)
            hand.append(deck[num])
            del deck[num]
            x += 1
        x = 0

        #Creates Rows
        num = random.randint(0,len(deck) - 1)
        r1.append(deck[num])
        del deck[num]
        num = random.randint(0,len(deck) - 1)
        r2.append(deck[num])
        del deck[num]
        num = random.randint(0,len(deck) - 1)
        r3.append(deck[num])
        del deck[num]
        num = random.randint(0,len(deck) - 1)
        r4.append(deck[num])
        del deck[num]

        #actually playing game
        hand, r1, r2, r3, r4, KRH, KRS, KRD, KRC = kcf.CheckForKings(hand, r1, r2, r3, r4) #Checks for Kings in hand and rows
    ##    print(hand, r1, r2, r3, r4, KRH, KRS, KRD, KRC)

        b = 0
        tr = 5
        while(b < tr):
    ##        print("-------------------------Turn %s--------------------------" % str(b + 1))
            bhand = hand.copy()
            br1 = r1.copy()
            br2 = r2.copy()
            br3 = r3.copy()
            br4 = r4.copy()
            
            #Fills open slots
            hand, r1, r2, r3, r4 = kcf.FillSlots(hand, r1, r2, r3, r4)
    ##        print("")
    ##        print("")
    ##        print(hand, r1, r2, r3, r4)
            
            #Checks for moves from hand
            hand, r1 = kcf.Moves(hand, r1)
            hand, r2 = kcf.Moves(hand, r2)
            hand, r3 = kcf.Moves(hand, r3)
            hand, r4 = kcf.Moves(hand, r4)
            hand, KRH = kcf.Moves(hand, KRH)
            hand, KRS = kcf.Moves(hand, KRS)
            hand, KRD = kcf.Moves(hand, KRD)
            hand, KRC = kcf.Moves(hand, KRC)
    ##        print("")
    ##        print("")
    ##        print(hand, r1, r2, r3, r4, KRH, KRS, KRD, KRC)

            #Checks for colum moves
            r1, r2 = kcf.ColMoves(r1, r2)
            r2, r3 = kcf.ColMoves(r2, r3)
            r3, r4 = kcf.ColMoves(r3, r4)
            r1, r3 = kcf.ColMoves(r1, r3)
            r1, r4 = kcf.ColMoves(r1, r4)
            r2, r4 = kcf.ColMoves(r2, r4)
    ##        print("")
    ##        print("")
    ##        print(hand, r1, r2, r3, r4, KRH, KRS, KRD, KRC)

            if(hand == []):
                b = tr
                goesout += 1
            elif(not(bhand == hand and br1 == r1 and br2 == r2 and br3 == r3 and br4 == r4)):
                b = 0
            b+=1
                
        i += 1

##    print("Went out %s times out of %d trials" % (goesout,trials))
    suc = goesout/trials
##    print(suc)


    sheet.write(startinghand - 1, 0, suc)
    
    wu += 1
    
workbook.save('KingCornersData.xls')


