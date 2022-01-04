trash = input()
while(True):
    try:
        trash = input()
        numbers = input().strip().split(" ")
        string = input()
        
        dic = {}
                
        # dic[numbers[0]] = string[0]
        # dic[numbers[1]] = string[1]
        cont = 0
        Max = 0
        #print(string)
        for i in string:
            if(cont>= len(numbers)):
                break
            if(ord(i) >= 65 and ord(i)<= 90):
                dic[numbers[cont]] = i
                if(int(numbers[cont]) > Max):
                    Max = int(numbers[cont])
                cont+=1
        #print(string)
        output = []
        a0 = 1
        a1 = 2
        while(a0 <= Max):
            if(str(a0) in dic):
                output.append(dic[str(a0)])
            else:
                output.append(" ")
            aux = a0
            a0 = a1
            a1 += aux
        
        # print(numbers)
        # print(dic)
        print("".join(output))
    except(EOFError):
        break
        
       