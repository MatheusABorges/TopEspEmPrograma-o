
while(True):
    try:
        string = input().strip()
        if(string == '.'):
            break
        result = 1
        
        for i in range (2, len(string)+1 ):
            if(len(string)%i != 0):
                continue
            
            size = int(len(string)/i)
            base = string[0:size]
            isDivisible = True
            for j in range(0, len(string), size):
                if(string[j:size+j] != base):
                    #print(string[j:size+j])
                    # print(base)
                    # print("")
                    isDivisible = False
                    break
            if(isDivisible):
                result = int(i)
        
        print(result)
    except:
        break