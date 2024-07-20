from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cc = Counter(a)
    
    alice = False
    
    for count in cc.values():
        if count % 2 != 0:
            alice = True
            break 

    if alice:
        print("YES")
    else:
        print("NO")
