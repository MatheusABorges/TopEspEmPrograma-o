import sys


def show(word):
    for i in word:
        print(i, end="")
    print("")

def insert(vec, element, n):
    for i in range (n):
        vec.append(element)
        
prev = ""

for line in sys.stdin:
    if(prev == ""):
        prev = line
        continue
    commonLetters = []
    
    cont1 = {}
    cont2 = {}

    for i in prev:
        if(i != "\n"):
            if(i not in cont1):
                cont1[i] = 1
            else:
                cont1[i] += 1
    
    for i in line:
        if(i != "\n"):
            if(i not in cont2):
                cont2[i] = 1
            else:
                cont2[i] += 1
                
    for i in cont1:
        if(i in cont2):
            insert(commonLetters, i, min(cont1[i], cont2[i]))
    
    commonLetters = "".join(sorted(commonLetters))
    
    print(commonLetters)

    prev = ""
    
