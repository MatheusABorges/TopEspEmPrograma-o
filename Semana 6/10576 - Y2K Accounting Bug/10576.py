while(True):
    try:
        s, d = input().split(" ")
        
        s = int(s)
        d = int(d)
        
        n = 1
        while(s*(5-n)-(n*d) > 0 and n<5):
            n+=1
        if(n >= 5):
            print("Deficit")
            continue
        res = []
        cont = 0
        #print(n)
        
        for i in range(12):
            if(cont >= 5-n):
                for j in range (n):
                    res.append(d*-1)
                cont = 0
            res.append(s)
            cont += 1
            
        
        value = sum(res[0:12])
        if(value > 0):
            print(value)
        else:
            print("Deficit")
        
        # print(res[0:12])
        # print(sum(res[0:12]))
    except:
        break