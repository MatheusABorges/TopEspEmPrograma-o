while(True):
    try:
        line = input().strip()
        while line == "":
            line = input().strip()
        
        line = line.split()
        if len(line) == 2:
            size = int(line[0])
            string = line[1]
        else:
            size = int(line[0])
            string = input().strip()
            while string == "":
                string = input().strip()
            
        passwords = {}
        for i in range(len(string)-size+1):
            subString = string[i:i+size]
            if(subString not in passwords):
                passwords[subString] = 1
            else:
                passwords[subString] += 1
        Max = -1
        out = None
        for i in passwords:
            if(passwords[i] > Max):
                 Max = passwords[i]
                 out = i
    
        print(out)
    
    except(EOFError):
        break