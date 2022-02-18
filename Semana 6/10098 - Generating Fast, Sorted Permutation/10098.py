import itertools


n = int(input())

for i in range(n):
    
    word = input()
    word = sorted(str(word))
    res = set(itertools.permutations(word))
    for j in sorted(res):
        for k in j:
            print(k, end="")
        print("")
    print("")