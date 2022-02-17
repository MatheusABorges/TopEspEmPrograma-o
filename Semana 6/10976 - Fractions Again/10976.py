
while(True):
    try:
        k = int(input())
        result = []
        for y in range(k,2*k+1):
            if( (y-k) != 0 and (k*y) % (y-k) == 0 ):
                x = (k*y)//(y-k)
            else:
                x=0
            if(x != 0):
                result.append("1/" + str(k) + " = 1/" + str(x) + " + 1/" + str(y))
            
            
        print(len(result))
        for i in result:
            print(i)
            
    except:
        break