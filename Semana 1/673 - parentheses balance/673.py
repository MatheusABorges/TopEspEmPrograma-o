from pilha import Pilha

def toStack(string):
    stack = Pilha()
    for i in string:
        stack.push(i)
    return stack
        

n = int(input())

for i in range(n):
    
    string = input()
    
    stack = Pilha()
    
    isCorrect = True
    
    for i in string:
        try:
            if(i == '[' or i == '('):
                stack.push(i)
            elif(i == ']'):
                if(stack.pop() != '['):
                    isCorrect = False
                    break
            elif(i == ')'):
                if(stack.pop() != '('):
                    isCorrect = False
                    break
        except Exception:
            isCorrect=False
            break
    
    try:
        a = stack.pop()
        isCorrect = False
    except:
        if(isCorrect!=False):
            isCorrect = True
    
    if(isCorrect):
        print('Yes')
    else:
        print('No')