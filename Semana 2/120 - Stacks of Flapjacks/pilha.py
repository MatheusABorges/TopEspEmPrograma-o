
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
    
    #dumps another stack into the object that calls this method
    def dump(self, stack, n):
        for i in range(n):
            self.push(stack.pop)
            
    def dumpIntoList(self, List, n):
        for i in range(n):
            List.append(self.pop())
            
    def pushList(self, List):
        for i in List:
            self.push(i)
        
    def pushListReverse(self, List):
        i = len(List)-1
        while(i >= 0):
            self.push(List[i])
            i-=1
            
    def getMaxElementAndIndex(self, n):
        node = self.nodes
        Max = node.value
        index = 0
        cont = 0
        while(node.value != None and cont<n):
            if(node.value != None and node.value > Max):
                Max = node.value
                index = cont
            node = node.nextNode
            cont+=1
        return Max, index
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            