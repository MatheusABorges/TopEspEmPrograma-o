def allEqual(array):
    a = array[0]
    isEqual = True
    for i in array:
        isEqual = isEqual and (i == a)
    if(a == 'X'):
        return isEqual, 'X'
    elif(a == 'O'):
        return isEqual, 'O'
    else:
        return isEqual, '.'
        
def nObjects(table):
    circles = 0
    crosses = 0
    for i in table:
        for j in i:
            if(j == 'O'):
                circles += 1
            elif(j == 'X'):
                crosses += 1
    return circles, crosses

def whoWon(table, circles, crosses):
    xWon = False
    oWon = False
    
    #check rows
    for i in range(3):
        won, who = allEqual(table[i])
        if(won):
            if(who == 'O'):
                oWon = True
            if(who == 'X'):
                xWon = True
    if(xWon and crosses != circles+1):
        #print("false 2")
        return False
    if(oWon and crosses != circles):
        #print("false 3")
        return False
    if(oWon and xWon):
        #print("false 4")
        return False
    
    #check columns
    for i in range(3):
        won, who = allEqual([table[0][i], table[1][i], table[2][i]])
        if(won):
            if(who == 'O'):
                oWon = True
            if(who == 'X'):
                xWon = True
    if(xWon and crosses != circles+1):
        #print("false 5")
        return False
    if(oWon and crosses != circles):
        #print("false 6")
        return False
    if(oWon and xWon):
        #print("false 7")
        return False
    
    #check diagonals
    won, who = allEqual( [ table[0][0], table[1][1], table[2][2] ] )
    if(won):
        if(who == 'O'):
            oWon = True
        if(who == 'X'):
            xWon = True
    if(xWon and crosses != circles+1):
        #print("false 8")
        return False
    if(oWon and crosses != circles):
        #print("false 9")
        return False
    if(oWon and xWon):
        #print("false 10")
        return False
    
    won, who = allEqual( [ table[0][2], table[1][1], table[2][0] ] )
    if(won):
        if(who == 'O'):
            oWon = True
        if(who == 'X'):
            xWon = True
    if(xWon and crosses != circles+1):
        #print("false 11")
        return False
    if(oWon and crosses != circles):
        #print("false 12")
        return False
    if(oWon and xWon):
        #print("false 13")
        return False
    
    return True

def rules(table):
   
    circles, crosses = nObjects(table)
    if(circles != crosses and circles != crosses-1):
        #print("false 1 - " + str(circles) +  " " + str(crosses))
        return False
    return whoWon(table, circles, crosses)
    
  

n = int(input())
for i in range(n):
    table = []
    table.append(input())
    table.append(input())
    table.append(input())
    
    if(rules(table)):
        print('yes')
    else:
        print('no')
    try:
        lBreak = input()
    except:
        break


