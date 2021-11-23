
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