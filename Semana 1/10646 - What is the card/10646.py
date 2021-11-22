
class Node:
    value = None
    nextNode = None
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

class Pilha:
        
    def __init__(self):
        self.size = 0
        self.nodes = Node(None, None)
    def push(self, value):
        newNode = Node(value, self.nodes)
        self.nodes = newNode
        self.size = self.size + 1
    
    def pop(self):
        if(self.size<=0):
            raise Exception("Popping empty stack")
            return
        value = self.nodes.value
        self.nodes = self.nodes.nextNode
        self.size = self.size - 1
        return value
        
    def size(self):
        return self.size
   
    def print(self):
        node = self.nodes
        for i in range (self.size-1):
            print(node.value, end=", ")
            node = node.nextNode
        print(node.value)
def empilha(pilha, vetor):
    for i in range(len(vetor)):
        pilha.push(vetor[i])

def value(card):
    if( ord(card[0]) > 49 and ord(card[0]) <= 57 ):
        return int(card[0])
    return 10

#variáveis
nCards = 52
nCases = int(input())
casesInput = []

#input
for i in range (nCases):
    case = []
    case = input().split(" ")
    casesInput.append(case)


#algoritmo
for i in range(nCases):
    cards = Pilha()
    empilha(cards, casesInput[i])
    Y = 0
    # print("---")
    # cards.print()
    # print("---")
    aux = Pilha()
    
    for j in range(25):
        aux.push(cards.pop())
        
    # print("\nAux:\n---")
    # aux.print()
    # print("---")
    
    # print("\nCards:\n---")
    # cards.print()
    # print("---")
    
    for j in range(3):
        top = cards.pop()
        # print("\n---")
        X = value(top)
        # print(top, end=" " + str(X) + '\n')
        # print("---")
        Y += X
        for k in range(10 - X):
            cards.pop()
            
    # print("\nCards After pop:\n---")
    # cards.print()
    # print("---")
    
    for j in range(25):
        cards.push(aux.pop())
    
    # print("\nCards After Hand adding\n---")
    # cards.print()
    # print("---")
    
    aux2 = Pilha()
    
    for j in range(cards.size):
        aux2.push(cards.pop())
    
    
    saida = 0
    for j in range(Y):
        saida = aux2.pop()
    
    print("Case " + str(i+1) + ": " + saida)
