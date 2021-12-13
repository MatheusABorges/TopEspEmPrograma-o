from pilha import Pilha


def toInt(List):
    intList = []
    for i in List:
        intList.append(int(i))
    return intList

#input
stackInputLine = None
stacks = []
try:
    stackInputLine = input()
except EOFError:
    exit()
    

while(stackInputLine != ''):
    
    stack = Pilha()
    stack.pushListReverse(toInt(stackInputLine.split(' ')))
    stacks.append(stack)
    
    try:
        stackInputLine = input()
    except EOFError:
        break
        
#endInput

# stack = Pilha()
# stack.pushListReverse([20, 9, 3, 13, 5, 19, 1, 18, 12, 11, 15, 7, 10, 14, 8, 4, 17, 6, 2, 16])
# stacks = [stack]


for i in stacks:
    i.printSpaced()
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
            moves.append(size - n + 1)
            # print(size)
            # print(n)
            # print(pos)
            # print("")
            i.pushList(tempList)

            
        else:
            
            i.dumpIntoList(tempList, pos+1)
            moves.append(size - pos)
            # print(size)
            # print(pos)
            # print("")
            i.pushList(tempList)

            tempList.clear()
            i.dumpIntoList(tempList, n)
            # print(size)
            # print(pos)
            # print("")
            moves.append( size - n + 1 )
            i.pushList(tempList)
            
        n -= 1
        
        
    #i.print()
    moves.append(0)
    for m in range (len(moves)-1):
        print(moves[m], end=' ')
    print(moves[len(moves)-1])
    
    

    