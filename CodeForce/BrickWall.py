t = int(input())

for i in range(t):
    n, m = [int(i) for i in input().split()]
    k = m // 2
    print(k*n)