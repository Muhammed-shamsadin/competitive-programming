t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    i, j = 0, n - 1

    while i < j:
        if a[i] == 1 and a[j] == 0:
            cnt += 1
        elif a[i] == 1 and a[j] == 1:
            i -= 1
        elif a[i] == 0 and a[j] == 0:
            j += 1

        i += 1
        j -= 1
    print(cnt)
