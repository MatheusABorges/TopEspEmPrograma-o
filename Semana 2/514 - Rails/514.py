from pilha import Pilha
size = input()
if(size == "0"):
    exit
coaches = input().split(" ")
cont = 0
while(True):
    if(len(coaches) > 1 and cont>0):
        print("")
    while(len(coaches) > 1):
        isPossible = True
        stack = Pilha()
        i = len(coaches)-1
        n = i+1
        result = []
        while(i>=0):
            if(stack.top() == str(n)):
                result.append(stack.pop())
                n-=1
            else:
                stack.push(coaches[i])
                i-=1   
        #stack.print()        
        while(stack.size>0):
            if(stack.top() != str(n)):
                isPossible = False
                break
            result.append(stack.pop())
            n-=1  
        print("Yes") if isPossible else print("No")
        coaches = input().split(" ")
    
    size = input().split(" ")
    if(len(size) == 1):
        if(size[0] == '0'):
            break
    coaches = size
    cont+=1

print("")