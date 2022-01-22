
a, b = input().split(" ")




while(int(a) != 0 or int(b) != 0):
    a = a[::-1]
    b = b[::-1]
    
    n = max(len(a), len(b))
    carryOver = 0
    cont = 0

    for i in range(n):
        Sum = (int(a[i]) if len(a) > i else 0) + (int(b[i]) if len(b)>i else 0) +  carryOver
        carryOver = (1 if Sum>=10 else 0)
        cont += (1 if carryOver == 1 else 0)
    
    if (cont == 0):
        print("No carry operation.")
    elif(cont == 1):
        print("1 carry operation.")
    else:
        print(str(cont) + " carry operations.")
    
    a, b = input().split(" ")
    