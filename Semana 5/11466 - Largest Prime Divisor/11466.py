from math import sqrt
MAX = 10000010
p = []
def sieve(n):
    primes = [True for i in range(n+1)]

    global p
    
    for i in range(2, n):
        if(not primes[i]):
            continue
        mult = i
        p.append(i)
        while(mult<n):
            mult += i
            if(mult >= len(primes)):
                break
            primes[mult] = False
            
            

    return primes


s = sieve(MAX)

while(True):
    n = int(input())
    larg = []
    if(n == 0):
        break
    if(n < len(s) and s[n]):
        print("-1")
        continue
    for i in range(len(p)):
        if(n%p[i]==0):
            larg.append(p[i])
    
    print(larg[len(larg)-1] if len(larg) > 1 else "-1")