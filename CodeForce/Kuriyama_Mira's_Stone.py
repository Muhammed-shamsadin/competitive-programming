n = int(input())

y = [0] * (n + 1)
z = [0] * (n + 1)

arr = [int(i) for i in input().split()]

for a in range(1, n + 1):
    y[a] = arr[a - 1]
    z[a] = arr[a - 1]

y.sort()
for a in range(1, n + 1):
    z[a] += z[a - 1]
    y[a] += y[a - 1]

m = int(input())
for i in range(m):
    opt, l, r = [int(i) for i in input().split()]

    if opt == 1:
        print(z[r] - z[l - 1])
    else:
        print(y[r] - y[l - 1])


