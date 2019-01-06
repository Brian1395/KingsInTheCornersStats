





def Fits(l,h):
    if((l == [])or(h == [])):
        return(False)
    hn = h.replace(h[0], "")
    ln = l.replace(l[0], "")
    cend = str(int(hn) - 1)
    if(cend == ln):
        if(((h[0] == 'H') or (h[0] == 'D')) and ((l[0] == 'S') or (l[0] == 'C'))):
            return(True)
        elif(((l[0] == 'H') or (l[0] == 'D')) and ((h[0] == 'S') or (h[0] == 'C'))):
            return(True)
    return(False)

def RFits(rl,rh):
    if((rl == [])or(rh == [])):
        return(False)
    if((len(rl[0]) == 0)or(len(rh[0]) == 0)):
        return(False)
    l = rl[len(rl) - 1]
    h = rh[0]
    if((l == '')or(h == '')):
        return(False)
    hn = h.replace(h[0], '')
    ln = l.replace(l[0], '')
    rln = int(ln)
    rln = rln + 1
    cend = str(rln)
    if(cend == hn):
        if((h[0] == 'H' or 'D') and (l[0] == 'S' or 'C')):
            return(True)
        elif((l[0] == 'H' or 'D') and (h[0] == 'S' or 'C')):
            return(True)
    return(False)


def FillSlots(hand, r1, r2, r3, r4):
    emptySlots = []
    if(r1 == []): 
        emptySlots.append('1')
    elif(r2 == []):
            emptySlots.append('2')
    elif(r3 == []):
            emptySlots.append('3')
    elif(r4 == []):
            emptySlots.append('4')
    if(emptySlots == []):
        return(hand, r1, r2, r3, r4)  #Exits if no slots are open
    
    i = 0
    while(i < len(hand)):
        if(emptySlots == []):
            return(hand, r1, r2, r3, r4)  #Exits if no slots are open
        w = hand[i]
        rw = [w]
        if(RFits(r1,rw) or RFits(r2,rw) or RFits(r3,rw) or RFits(r4,rw)):
            x = emptySlots[0]
            if(x == '1'):
                r1.append(w)
            elif(x == '2'):
                r2.append(w)
            elif(x == '3'):
                r3.append(w)
            elif(x == '4'):
                r4.append(w)
            hand.remove(w)
            emptySlots.remove(x)
        i += 1
            
    if(not (emptySlots == [] or hand == [])): #Just puts in the largest card if no good matches can be found
        i = 0
        handnum = []
        while(i < len(hand)):
            y = hand[i].replace(hand[i][0], "")
            handnum.append(int(y))
            i += 1
        w = max(handnum)
        w = handnum.index(w)
        w = hand[w]
        x = emptySlots[0]
        if(x == '1'):
            r1.append(w)
        elif(x == '2'):
            r2.append(w)
        elif(x == '3'):
            r3.append(w)
        elif(x == '4'):
            r4.append(w)
        hand.remove(w)
        emptySlots.remove(x)   
    return(hand, r1, r2, r3, r4)


def ColMoves(c1, c2):
    if((c1 == [])or(c2 == [])):
        return (c1, c2)
    
    #checks if c1 will fit on the end of c2
    en = c1[len(c1) - 1]
    st = c2[0]
    if(Fits(en,st)):
        c2 = c1 + c2
        c1 = []
        return(c1, c2) 
    #checks if c2 will fit on the end of c1
    en = c2[len(c2) - 1]
    st = c1[0]
    if(Fits(en,st)):
        c1 = c2 + c1
        c2 = []
        return(c1, c2)
    
    return(c1, c2)
    
        
    


def Moves(fro, w):
    if((fro == [])or(w == [])):
        return (fro, w)
    i = 0
    romv = []
    while(i < len(fro)):
        f = fro[i]
        if(Fits(f,w[0])):
           w.insert(0, f)
           romv.append(f)

        i += 1
    i = 0
    while(i < len(romv)):
        fro.remove(romv[i])
        i += 1
    return (fro, w)
            
        

##    rednums, redcards, blacknums, blackcards = SepByColor(fro)
##    to = w[0]
##    n = 0
##    if(to[0] == 'D' or 'H'):
##        if(to[0] == 'H'):
##            n = to.replace("H", "")
##        elif(to[0] == 'D'):
##            n = to.replace("D", "")
##        n = str(int(n) - 1)
##        k = 0
##        while(k < len(blacknums)):
##            if(n == blacknums[k]):
##                w.insert(0, blackcards[k])
##                del blacknums[k]
##                del blackcards[k]
##                k = len(blacknums)
##            k += 1
##    elif(to[0] == 'S' or 'C'):
##        if(to[0] == 'S'):
##            n = to.replace("S", "")
##        elif(to[0] == 'C'):
##            n = to.replace("C", "")
##        n = str(int(n) - 1)
##        k = 0
##        while(k < len(rednums)):
##            if(n == rednums[k]):
##                w.insert(0, redcards[k])
##                del rednums[k]
##                del redcards[k]
##                k = len(rednums)
##            k += 1
##    fro = redcards + blackcards
##    return(fro, w)


def SepByColor(hand):
    rednums = []
    redcards = []
    blacknums = []
    blackcards = []
    u = 0
    while(u < len(hand)):
        w = hand[u]
        if(w[0] == 'H'):
            redcards.append(w)
            w = w.replace("H", "")
            rednums.append(w)
        elif(w[0] == 'D'):
            redcards.append(w)
            w = w.replace("D", "")
            rednums.append(w)
        elif(w[0] == 'S'):
            blackcards.append(w)
            w = w.replace("S", "")
            blacknums.append(w)
        elif(w[0] == 'C'):
            blackcards.append(w)
            w = w.replace("C", "")
            blacknums.append(w)
        u += 1
    return(rednums, redcards, blacknums, blackcards)

def CheckForKings(hand, r1, r2, r3, r4):
    KRH = []
    KRS = []
    KRD = []
    KRC = []
    while(('H13' in hand)or('S13' in hand)or('D13' in hand)or('C13' in hand)):
        if('H13' in hand):
            KRH = ['H13']
            hand.remove('H13')
        elif('S13' in hand):
            KRS = ['S13']
            hand.remove('S13')
        elif('D13' in hand):
            KRD = ['D13']
            hand.remove('D13')
        elif('C13' in hand):
            KRC = ['C13']
            hand.remove('C13')
    while(('H13' in r1)or('S13' in r1)or('D13' in r1)or('C13' in r1)): 
        if('H13' in r1):
            KRH = ['H13']
            r1.remove('H13')
        elif('S13' in r1):
            KRS = ['S13']
            r1.remove('S13')
        elif('D13' in r1):
            KRD = ['D13']
            r1.remove('D13')
        elif('C13' in r1):
            KRC = ['C13']
            r1.remove('C13')
    while(('H13' in r2)or('S13' in r2)or('D13' in r2)or('C13' in r2)): 
        if('H13' in r2):
            KRH = ['H13']
            r2.remove('H13')
        elif('S13' in r2):
            KRS = ['S13']
            r2.remove('S13')
        elif('D13' in r2):
            KRD = ['D13']
            r2.remove('D13')
        elif('C13' in r2):
            KRC = ['C13']
            r2.remove('C13')
    while(('H13' in r3)or('S13' in r3)or('D13' in r3)or('C13' in r3)): 
        if('H13' in r3):
            KRH = ['H13']
            r3.remove('H13')
        elif('S13' in r3):
            KRS = ['S13']
            r3.remove('S13')
        elif('D13' in r3):
            KRD = ['D13']
            r3.remove('D13')
        elif('C13' in r3):
            KRC = ['C13']
            r3.remove('C13')
    while(('H13' in r4)or('S13' in r4)or('D13' in r4)or('C13' in r4)): 
        if('H13' in r4):
            KRH = ['H13']
            r4.remove('H13')
        elif('S13' in r4):
            KRS = ['S13']
            r4.remove('S13')
        elif('D13' in r4):
            KRD = ['D13']
            r4.remove('D13')
        elif('C13' in r4):
            KRC = ['C13']
            r4.remove('C13')
    return(hand, r1, r2, r3, r4, KRH, KRS, KRD, KRC)
