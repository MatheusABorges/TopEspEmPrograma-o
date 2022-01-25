def pascalTriangle(n):
    triangle = []
    for i in range (n):
        triangle.append([])
        triangle[i].append(1)
        
        for j in range (1, i):
            triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
        
        if(i != 0):
            triangle[i].append(1)
        
    return triangle



n = int(input())
pascal = pascalTriangle(52)

for i in range (n):
    base, k = input().split("^")
    
    k = int(k)
    res = []
    
    baseA, baseB = base.split("+")
    baseA = baseA[1:len(baseA)]
    baseB = baseB[0:len(baseB)-1]
    
    if(k==1):
        print("Case " + str(i+1) + ":" + " " + baseA + "+" + baseB)
        continue
    
    for j in range(k+1):
        if(k-j>0):
            if(pascal[k][j] != 1):
                res.append(str(pascal[k][j])) 
                res.append("*")
            res.append("a")
            if(k-j > 1):
                res.append("^")
                res.append(str(k-j))
        
        if(j > 0):
            if(k-j>0):
                res.append("*")
            res.append("b")
            if(j>1):
                res.append("^")
                res.append(str(j))
            
        res.append("+")
    res.pop()
    

    
    out = ""
    for j in (res):
        if(j == "a"):
            out = out + baseA
            continue
        elif(j == "b"):
            out = out + baseB
            continue
        out = out + j
    print("Case " + str(i+1) + ":" + " " + out)
        