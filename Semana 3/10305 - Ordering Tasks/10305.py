def init(n):
    aux = {}
    for i in range(1, n+1):
        aux[i] = []
    return aux

n, m = input().split(" ")
while(True):
    try:
        n = (int(n))
        m = (int(m))
        if(n == 0 and m ==0):
            break
    except:
        break
    
    dependencies = init(n)
    for d in range (m):
        i, j = input().split(" ")
        i = int(i)
        j = int(j)
        
        dependencies[j].append(i)
    
    
    cont = 0
    while(len(dependencies) > 0):
        task = 0
        #print(dependencies)
        for i in dependencies:
            if(len(dependencies[i]) == 0):
                task = i
                del dependencies[i]
                break
        for i in dependencies:
            dependencies[i].remove(task) if dependencies[i].count(task) >= 1 else ""
        print(task, end = " ")
        cont += 1
                
    print("")
    
    
    
    
    
    
    
    
    
    n, m = input().split(" ")