
def toSet(string):
    aux = set()
    for i in string:
        aux.add(i)
    return aux

def addCoins(coins, newCoins):
    for i in newCoins:
        coins.add(i)

def removeCoins(coins, rCoins):
    for i in rCoins:
        if(i in coins):
            coins.remove(i)

n = int(input())

total  = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'}


for i in range (n):
    
    normalCoins = set()
    heavySuspects = set()
    lightSuspects = set()

    #1 row
    array = input().split(" ")
    left = array[0]
    right = array[1]
    balance = array[2]
    
    if(balance == 'even'):
        addCoins(normalCoins,left)
        addCoins(normalCoins,right)

    
    elif(balance == 'up'):
        addCoins(heavySuspects, left)
        addCoins(lightSuspects, right)
        addCoins(normalCoins, total - toSet(left + right))
        
    elif(balance == 'down'):
        addCoins(heavySuspects, right)
        addCoins(lightSuspects, left)
        addCoins(normalCoins, total - toSet(left + right))
        
    #2 row        
    array = input().split(" ")
    left = array[0]
    right = array[1]
    balance = array[2]
    
    if(balance == 'even'):
        addCoins(normalCoins,left)
        addCoins(normalCoins,right)
        removeCoins(heavySuspects, left)
        removeCoins(lightSuspects, right)
        removeCoins(heavySuspects, right)
        removeCoins(lightSuspects, left)
    
    elif(balance == 'up'):
        addCoins(heavySuspects, left)
        addCoins(lightSuspects, right)
        addCoins(normalCoins, total - toSet(left + right))
        
    elif(balance == 'down'):
        addCoins(heavySuspects, right)
        addCoins(lightSuspects, left)
        addCoins(normalCoins, total - toSet(left + right))
        
    coinsInCommon = lightSuspects.intersection(heavySuspects)
    if( len(coinsInCommon) > 0 ):
        removeCoins(lightSuspects, coinsInCommon)
        removeCoins(heavySuspects, coinsInCommon)
        addCoins(normalCoins, coinsInCommon)
    
    coinsInCommon = normalCoins.intersection(heavySuspects)
    if( len(coinsInCommon) > 0 ):
        removeCoins(heavySuspects, coinsInCommon)
        
    coinsInCommon = normalCoins.intersection(lightSuspects)
    if( len(coinsInCommon) > 0 ):
        removeCoins(lightSuspects, coinsInCommon)
        
        
    #3 row        
    array = input().split(" ")
    left = array[0]
    right = array[1]
    balance = array[2]
    
    if(balance == 'even'):
        addCoins(normalCoins,left)
        addCoins(normalCoins,right)
        removeCoins(heavySuspects, left)
        removeCoins(lightSuspects, right)
        removeCoins(heavySuspects, right)
        removeCoins(lightSuspects, left)
    
    elif(balance == 'up'):
        addCoins(heavySuspects, left)
        addCoins(lightSuspects, right)
        addCoins(normalCoins, total - toSet(left + right))
        
    elif(balance == 'down'):
        addCoins(heavySuspects, right)
        addCoins(lightSuspects, left)
        addCoins(normalCoins, total - toSet(left + right))
        
    coinsInCommon = lightSuspects.intersection(heavySuspects)
    if( len(coinsInCommon) > 0 ):
        removeCoins(lightSuspects, coinsInCommon)
        removeCoins(heavySuspects, coinsInCommon)
        addCoins(normalCoins, coinsInCommon)
    
    coinsInCommon = normalCoins.intersection(heavySuspects)
    if( len(coinsInCommon) > 0 ):
        removeCoins(heavySuspects, coinsInCommon)
        
    coinsInCommon = normalCoins.intersection(lightSuspects)
    if( len(coinsInCommon) > 0 ):
        removeCoins(lightSuspects, coinsInCommon)
        
    if(len(heavySuspects) > 0):
        iterator = iter(heavySuspects)
        if(len(heavySuspects) > 0):
            print(next(iterator, None) + " is the counterfeit coin and it is heavy.")
    elif(len(lightSuspects) > 0):
        iterator = iter(lightSuspects)
        if(len(lightSuspects) > 0):
            print(next(iterator, None) + " is the counterfeit coin and it is light.")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
