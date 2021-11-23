words = []

i = input().split(" ")

    
while(i[0] != '#'):
    for j in i:
        if(j != ''):
            words.append(j)
    i = input().split(" ")
    

wordsSorted = []

for j in words:
    wordsSorted.append(sorted(j.lower()))
    
    
a=0
result = []
for word in wordsSorted:
    if (wordsSorted.count(word) == 1):
        result.append(words[a])
    a+=1
    
result = sorted(result)
for word in result:
    print(word)