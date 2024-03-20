t = int(input())


for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    ans = a[0]
    for i in range(1, n):
        if a[i] > ans:
            ans = a[i]
        else:
            ans = ((ans // a[i]) + 1) * a[i]

    print(ans)