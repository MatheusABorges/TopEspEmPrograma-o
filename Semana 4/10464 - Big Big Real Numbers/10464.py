def trimEndZeroes(d):
    cont = len(d)-1
    res = ""
    while(cont > 0):
        if(d[cont] != '0'):
            break
        cont-=1
    for i in range(cont+1):
        res = res+str(d[i])
    return res

def trimInitZeroes(i):
    cont = 0
    res = ""
    while(cont < len(i)):
        if(i[cont] != '0'):
            break
        cont+=1
    
    for n in range(cont, len(i)):
        res = res+str(i[n])
    return res

def trimZeroes(n):
    n = trimEndZeroes(n)
    n = trimInitZeroes(n)
    return n

def splitSpace(s):
    fs = ""
    ss = ""
    
    inFirst = True
    for i in s:
        if(i == " "):
            inFirst = False
            continue
        if(inFirst):
            fs = fs + i
        else:
            ss = ss + i
    return[fs, ss]

def splitDot(s):
    fs = ""
    ss = ""
    
    inFirst = True
    
    for i in s:
        if(i == "."):
            inFirst = False
            continue
        if(i == " "):
            continue
        if(inFirst):
            fs = fs + i
        else:
            ss = ss+i
    return[fs, ss]

def isFirstBigger(f, s):
    auxF = f if f[0] != '-' else trimZeroes(f)[1:len(f)]
    auxS = s if s[0] != '-' else trimZeroes(s)[1:len(s)]
    
    fi, fd = splitDot(auxF)
    si, sd = splitDot(auxS)
    
    
    for i in range( abs( len(fi) - len(si) ) ):
        if(len(fi) > len(si)):
            si = "0" + si
        elif(len(si) > len(fi)):
            fi = "0" + fi
            
    for i in range( abs( len(fd) - len(sd) ) ):
        if(len(fd) > len(sd)):
            sd = sd + "0"
        elif(len(sd) > len(fd)):
            fd = fd + "0"
    
    auxF = fi + "." + fd
    auxS = si + "." + sd
    
    for i in range(min(len(auxF), len(auxS))):
        if(auxF[i] > auxS[i]):
            return True
        elif(auxF[i] < auxS[i]):
            return False
    return None


def Soma(n1i, n1d, n2i, n2d, containsDot):
    carryOver = 0
    res = []
    Sum = 0
    # print("n1i: " + n1i + " n1d: " + n1d + "\nn2i: " + n2i + " n2d: " + n2d)
    for i in range( max( len(n1d), len(n2d) ) ):
        
        s1 = int(n1d[i]) if len(n1d) > i else 0
        s2 = int(n2d[i]) if len(n2d) > i else 0
        
        Sum = s1 + s2 + carryOver
        
        carryOver = 1 if Sum >= 10 else 0
        
        res.append(Sum if Sum < 10 else Sum - 10)  
    
    if(containsDot):
        res.append(".")
    
    for i in range( max( len(n1i), len(n2i) ) ):
        
        s1 = int(n1i[i]) if len(n1i) > i else 0
        s2 = int(n2i[i]) if len(n2i) > i else 0
    
        Sum = s1 + s2 + carryOver
        
        carryOver = 1 if Sum >= 10 else 0
        
        res.append(Sum if Sum < 10 else Sum - 10)
        
    if(carryOver > 0):
        res.append(carryOver)
    return res



def Sub(n1i, n1d, n2i, n2d, containsDot):

    carryOver = 0
    res = []
    sub = 0
    for i in range( max( len(n1d), len(n2d) ) ):
        s1 =  int(n1d[i]) if len(n1d) > i else 0
        s2 =  int(n2d[i]) if len(n2d) > i else 0
        
        sub = s1 - s2 - carryOver
        
        carryOver = 1 if sub < 0 else 0
        
        res.append(sub if sub >= 0 else sub+10)
    
    if(containsDot):
        res.append(".")
    
    for i in range( max( len(n1i), len(n2i) ) ):
        s1 = int(n1i[i]) if len(n1i) > i else 0
        s2 = int(n2i[i]) if len(n2i) > i else 0
        
        sub = s1 - s2 - carryOver
        
        carryOver = 1 if sub < 0 else 0
        
        res.append(sub if sub >= 0 else sub+10)
        
    return res


n = int(input())

for i in range(n):
    
    ent = input()
    n1, n2 = splitSpace(ent)
    
    n1i, n1d = splitDot(n1)
    
    n2i, n2d = splitDot(n2)
    
    n1d = n1d[::-1]
    n2d = n2d[::-1]
    
    #n1Bigger = abs(float(n1))>abs(float(n2))
    #equal = abs(float(n1)) == abs(float(n2))
    
    n1Bigger = isFirstBigger(n1, n2)
    equal = False
    
    #print(n1Bigger)
    
    if(n1Bigger == None):
        equal = True
        n1Bigger = False
    
    res = ""
    printMinus = False
    containsDot = True
    
    if("." not in ent):
        containsDot = False
    
    if(n1i == ""):
        n1i ="0"
    if(n1d == ""):
        n1d = "0"
    if(n2i == ""):
        n2i = "0"
    if(n2d == ""):
        n2d = "0"
    
    if(len(n1d) > len(n2d)):
        for i in range(len(n1d) - len(n2d)):
            n2d = "0" + n2d
        
    elif(len(n2d) > len(n1d)):
        for i in range(len(n2d) - len(n1d)):
            n1d = "0" + n1d
    
    if(n1i[0] == '-' and n2i[0] != '-'):
        n1i = n1i[1:len(n1i)]
        n1i = n1i[::-1]
        n2i = n2i[::-1]
        if n1Bigger:
            res = Sub(n1i, n1d, n2i, n2d, containsDot)
            printMinus = True
        else :
            res = Sub(n2i, n2d, n1i, n1d, containsDot)
        
    elif(n2i[0] == '-' and n1i[0] != '-'):
        n2i = n2i[1:len(n2i)]
        n1i = n1i[::-1]
        n2i = n2i[::-1]
        if n1Bigger:
            res = Sub(n1i, n1d, n2i, n2d, containsDot)  
        else: 
            res = Sub(n2i, n2d, n1i, n1d, containsDot)
            if(not equal):
                printMinus = True
            
        
        
    elif(n2i[0] == '-' and n1i[0] == '-'):

        n1i = n1i[1:len(n1i)]
        n2i = n2i[1:len(n2i)]
        
        
        n1i = n1i[::-1]
        n2i = n2i[::-1]
        
        res = Soma(n1i, n1d, n2i, n2d, containsDot)
        printMinus = True
        
        
    else:
        n1i = n1i[::-1]
        n2i = n2i[::-1]
        res = Soma(n1i, n1d, n2i, n2d, containsDot)
    
    res = res[::-1]
    res = trimZeroes(trimZeroes(res))
    
    if(res == "" or res == None):
        res = "."

    
    if(res[0] == "." and len(res)>1):
        if(printMinus):
            print("-", end="")
        print("0" + res)
    elif(res[len(res)-1] == "." and len(res)>1):
        if(printMinus):
            print("-", end="")
        print(res + "0")
    elif(len(res) == 1 and res[0] == "."):
        print("0" + res + "0")
    else:
        if(printMinus):
            print("-", end="")
        print(res)
