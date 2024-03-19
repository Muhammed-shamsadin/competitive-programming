t = int(input())

for i in range(t):
    n = input()
    l = sum(map(int, n[:3]))
    r = sum(map(int, n[3:]))
    if l == r:
        print("YES")
    else:
        print("NO")
