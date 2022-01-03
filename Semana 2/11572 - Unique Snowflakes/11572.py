nTests = int(input().strip())

for i in range(nTests):
    nCases = int(input().strip())
    flakes = []
    m = {}
    maxSize = 0
    bot = 0
    cont = 0
    for i in range(nCases):
        newFlake = int( input().strip() )
        #pos = contains(flakes, bot, i, newFlake)
        flakes.append(newFlake)
        
        if(newFlake in m):
            if(cont > maxSize):
                maxSize = cont
                
            bot = m[newFlake]
            
            for j in range(i - cont, bot+1):
                del m[flakes[j]]
                cont-=1
        m[newFlake] = i
        cont += 1
        
        
    if(cont> maxSize):
        maxSize = cont
    print(maxSize)