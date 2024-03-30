s, n = [int(i) for i in input().split()]

a = []
for i in range(n):
    x, y = [int(i) for i in input().split()]
    a.append((x, y))

a.sort() 

for i in a:
    if s > i[0]:
        s += i[1] 
    else:
        print("NO")
        break
else:
    print("YES")
