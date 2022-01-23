from math import log10
from math import floor

def logSum(init, end):
    auxI = init
    auxE = end
    res = 1
    while(auxI > auxE):
        res += log10(auxI)
        auxI-=1
    return res

while(True):
    try:
        n, r = input().split(" ")
        n = int(n)
        r = int(r)
        
        Range = n-r if (n-r)>r else r
        
        num = logSum(n, Range)
        den = logSum(n-r if Range==r else r, 1)
        
        print(floor(num-den)+1)
        
    except:
        break
    
    