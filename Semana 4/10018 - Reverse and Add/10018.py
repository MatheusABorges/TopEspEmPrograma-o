def isPalindrome(number):
    digits = str(number)
    reverse = digits[::-1]
    for i in range(len(digits)):
        if(digits[i] != reverse[i]):
            return False
    return True


n = int(input())

for i in range(n):
    
    
    digits = input()
    number = int(digits)
    reverse = int(digits[::-1])
    number = number + reverse
    digits = str(number)
    cont=0
    while( not isPalindrome(digits) ):
        reverse = int(digits[::-1])
        # print("number: " + str(number))
        # print("reverse: " + str(reverse))
        # print("digits: " + str(digits))
        # print("")
        number = number + reverse
        digits = str(number)
        cont+=1

    print(str(cont+1), end=" ")
    print(digits)