def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    sum_val = 0
    ct = 0
    for x in arr:
        if x == 1:
            ct += 1
        sum_val += x
    if sum_val >= ct + n and n > 1:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()