x = 0
y = 0
d = 0

def euclidesExtendido(a, b):
    global x
    global y
    global d
    if (b == 0):
        x = 1
        y = 0
        d = a
        return
    euclidesExtendido(b, a % b)
    x1 = y;
    y1 = x - (a // b) * y;
    x = x1;
    y = y1;


while(True):
    try:
        a,b = input().split(" ")
        a = int(a)
        b = int(b)
        euclidesExtendido(a, b)
        print(x, end=' ')
        print(y, end=' ')
        print(d)
    
    except:
        break