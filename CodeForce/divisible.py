t = int(input())
for i in range(t):
    l, r = [int(i) for i in input().split()]
    if l*2 <= r:
        x = l
        y = l*2
    else:
        x = l
        y = l + 1
    print(x, y)
