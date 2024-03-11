t = int(input())

for i in range(t):
    n, m, k = [int(i) for i in input().split()]
    l = [int(i) for i in input().split()]
    r = [int(i) for i in input().split()]

    cnt = 0
    for i in range(n):
        for j in range(m):
            if l[i] + r[j] <= k:
                cnt += 1

    print(cnt)
