from math import ceil
n, m, a = [int(i) for i in input().split()]

ans = ceil(m/a) * ceil(n/a)

print(ans)
