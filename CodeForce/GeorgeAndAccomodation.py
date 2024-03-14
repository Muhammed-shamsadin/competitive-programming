n = int(input())

cnt = 0
for i in range(n):
    p, q = [int(i) for i in input().split()]

    s = q - p

    if p < q and s >= 2:
        cnt += 1

print(cnt)