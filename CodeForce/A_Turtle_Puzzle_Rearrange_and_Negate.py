# ID: Ugr/26320/14
# Lab-03

t = int(input())

for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    
    
    sum = 0
    
    for i in range(n):
        if a[i] > 0:
            sum += a[i]
        if a[i] < 0:
            a[i] = abs(a[i])
            sum += a[i]
    print(sum)
        
