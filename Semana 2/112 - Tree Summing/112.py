from pilha import Pilha


def removeBlankChars(string):
    token = ""
    for c in string:
        if(c == " " or c == '\n' or c == '\t'):
            continue
        token += c
    return token

def getTargetValue(rawExpressions, i):    
    token = ""
    while(rawExpressions[i] != '(' and i<len(rawExpressions)):
        token += rawExpressions[i]
        i+=1
        
    return int(token), i

#input
rawExpressions = None

try:
    rawExpressions = input()
except EOFError:
    exit()

while(rawExpressions != ''):
    

    try:
        rawExpressions = rawExpressions + input()
    except EOFError:
        break
#end input

rawExpressions = removeBlankChars(rawExpressions)

stack = Pilha()

expressions = []
targets = []

expression = ""
for i in range(len(rawExpressions)):
    expression += rawExpressions[i]
    if( rawExpressions[i] == '(' ):
        stack.push(rawExpressions[i])
    elif( rawExpressions[i] == ')' ):
        stack.pop()
    
    if(stack.size == 0  ):
        expressions.append((expression))
        expression = ""
        
    
token = ""
newExpressions = []
for i in expressions:
    if(len(i) == 1):
        token += i
    else:
        print(token)
        newExpressions += str(token)
        newExpressions += str(i)
        token = ""
        
for i in newExpressions:
    print(i)
    
    
