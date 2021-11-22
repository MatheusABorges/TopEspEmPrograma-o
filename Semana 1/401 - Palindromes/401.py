from pilha import Pilha

def mirrowedCharacter(c):
    if(c == 'A'):
        return 'A'
    elif(c == 'E'):
        return '3'
    elif(c == 'H'):
        return 'H'
    elif(c == 'I'):
        return 'I'
    elif(c == 'J'):
        return 'L'
    elif(c == 'L'):
        return 'J'
    elif(c == 'M'):
        return 'M'
    elif(c == 'O'):
        return 'O'
    elif(c == 'S'):
        return '2'
    elif(c == 'T'):
        return 'T'
    elif(c == 'U'):
        return 'U'
    elif(c == 'V'):
        return 'V'
    elif(c == 'W'):
        return 'W'
    elif(c == 'X'):
        return 'X'
    elif(c == 'Y'):
        return 'Y'
    elif(c == 'Z'):
        return '5'
    elif(c == '1'):
        return '1'
    elif(c == '2'):
        return 'S'
    elif(c == '3'):
        return 'E'
    elif(c == '5'):
        return 'Z'
    elif(c == '8'):
        return '8'
    else:
        return '#'

def isSringMirrowed(word):
    rWord = Pilha()
    for i in word:
        rWord.push(mirrowedCharacter(i))
    for i in word:
        if(i != rWord.pop()):
            return False
    return True
    
def isStringPalindrome(word):
    rWord = Pilha()
    for i in word:
        rWord.push(i)
    for i in word:
        if(i != rWord.pop()):
            return False
    return True
    
loops = 3
try:
    word = input()
except EOFError:
    exit()

while(word != ''):
    
    isMirrowed = isSringMirrowed(word)
    isPalindrome = isStringPalindrome(word)
    
    if(isMirrowed and isPalindrome):
        print(word + " -- is a mirrored palindrome.\n")
    elif(isMirrowed and (not isPalindrome)):
        print(word + " -- is a mirrored string.\n")
    elif((not isMirrowed) and isPalindrome):
        print(word + " -- is a regular palindrome.\n")
    else:
        print(word + " -- is not a palindrome.\n")
    try:
        word = input()
    except EOFError:
        break