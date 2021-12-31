def populate(n):
    aux = []
    for i in range(n):
        aux.append(str(i+1))
    return aux

def replace(vector, i, s):
    aux = []
    for e in range(len(vector)):
        if(e == i):
            aux.append(s)
        else:
            aux.append(vector[e])
    return aux

def increase(i, n):
    return (i+1)%n

def decrease(i, n):
    return (i-1)%n

def getLastSurvivor(vec, n):
    for i in range( len( vec ) ):
        if(vec[i] != '-'):
            return (n - int(vec[i]) + 2) if int(vec[i]) != 1 else 1

n, k = input().split(" ")
n = int(n)
k = int(k)
size = n
while(n!=0 or k!=0):
    
    people = populate(n)
    i = 0
    cont = 0
    while(n > 1):
        
        #print(i)
        while(cont<k):
            if(people[i] != '-'):
                cont += 1
            i = increase(i, size)
        #morreu
        #print("primeiro i:  " + str(i))
        
        died = decrease(i,size)
        people = replace(people, died, '-')
        #print(people)
        cont = 0
        n -= 1
        
        while(cont<k):
            if(people[i] != '-'):
                cont += 1
            i = increase(i, size)

        #print("segundo i:  " + str(i))
            
        buries  = decrease(i,size)
        people = replace(people, died, people[buries])
        people = replace(people, buries, '-')
        
        i = increase(died, size)
        cont = 0
        #print(people)
       # print("")
    
        
    print(getLastSurvivor(people, size))
    

    
    n, k = input().split(" ")
    n = int(n)
    k = int(k)
    size = n
