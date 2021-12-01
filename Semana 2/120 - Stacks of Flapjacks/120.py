from pilha import Pilha



#input
stackInputLine = None
stacks = []
try:
    stackInputLine = input()
except EOFError:
    exit()
    
    
while(stackInputLine != ''):
    
    stack = Pilha()
    stack.pushListReverse(stackInputLine.split(' '))
    stacks.append(stack)
    
    try:
        stackInputLine = input()
    except EOFError:
        break
        
#endInput

# stack = Pilha()
# stack.pushListReverse([4, 21, 8, 11, 23, 5, 3, 20, 26, 7, 12, 1, 25, 10, 2, 24, 19, 17, 13, 22, 27, 14, 9, 15, 6, 16, 18])
# stacks = [stack]


for i in stacks:
    i.print()
    n = i.size
    size = i.size
    moves = []    

    while(n>0):
        Max, pos = i.getMaxElementAndIndex(n)
        tempList = []

        if(pos == n-1):
            n -= 1
            continue
        
        if(pos == 0):
            i.dumpIntoList(tempList, n - pos)
            moves.append(size - (n-pos) + 1)
            i.pushList(tempList)

            
        else:
            
            i.dumpIntoList(tempList, pos+1)
            moves.append(size - pos)
            i.pushList(tempList)

            tempList.clear()
            i.dumpIntoList(tempList, n)
            moves.append(size - (n-pos))
            i.pushList(tempList)
            
        n -= 1
        
        
    i.print()
    moves.append(0)
    for m in moves:
        print(m, end=' ')
    print("")
    print("")
    
    

    