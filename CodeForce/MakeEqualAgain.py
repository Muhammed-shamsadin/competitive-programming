t = int(input())

for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    l = 0
    r = 0

    while l < n and a[0] == a[l]:
        l += 1
    while r < n and a[n - r - 1] == a[n - 1]:
        r += 1

    res = n
    if a[0] == a[n-1]:
        res -= l
        res -= r
    else:
        res -= max(l, r)

    print(max(0, res))