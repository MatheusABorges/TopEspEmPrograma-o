import sys
from pilha import Pilha
def toInt(vec):
    aux = []
    for i in vec:
        if(i != "" and i != " " and i != "\n"):
            aux.append(int(i))
    return aux

#toys = input().split(" ")

for toy in sys.stdin:
    #print("TESTE")
    toys = toInt(toy.split(" "))
    toyStack = Pilha()
    sizeStack = Pilha()
    isMatrioshka = True
    
    
    for i in toys:
    
        if(i < 0):
            toyStack.push(i)
            if(sizeStack.size > 0):
                sizeStack.push( sizeStack.pop() - (i*-1) )
                #0 if it doesn't fit inside
                if(sizeStack.top() < 0):
                    isMatrioshka = False
                    break
                
            sizeStack.push((i*-1) - 1)
            
        if(i > 0):
            try:
                if(i != (toyStack.pop()*-1)):
                    isMatrioshka = False
                    break
                sizeStack.pop()
            except:
                isMatrioshka = False
                break
    
    if(toyStack.size>0):
        isMatrioshka = False
    
    print(":-) Matrioshka!") if isMatrioshka else print(":-( Try again.")