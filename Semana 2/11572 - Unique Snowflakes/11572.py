def biggestUniqueStream(stream, i):
    u = []
    for i in range(i, len(stream)):
        if(stream[i] not in u):
            u.append(stream[i])
        else:
            break
    return len(u)

nTests = int(input())

for i in range(nTests):
    nCases = int(input())
    flakes = []
    
    for i in range(nCases):
        flakes.append(int(input()))
    
    size = 0
    for i in range(len(flakes)):
        u = []
        for j in range(i, len(flakes)):
            if(flakes[j] not in u):
                u.append(flakes[j])
            else:
                break
        big = len(u)
        if(size < big):
            size = big
    print(size)
    
    #print(flakes)
    #print(a)
