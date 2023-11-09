'''
This was solved in: Wednesday 25 oct 2023
'''
n = int(input())
a = list(map(int, input().split()))
shft = 0

for i in range(n - 1):
    if a[i] > a[i + 1]:
        s = i
        shft += 1

if a[n - 1] > a[0]:
    s = n - 1
    shft += 1

if shft == 0:
    print(0)
elif shft > 1:
    print(-1)
else:
    print(n - 1 - s)