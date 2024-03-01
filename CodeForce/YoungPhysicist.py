# a = [0, 0, 1]
# b = [1, 2, 3]
# i = 0
# c = [a[i] + b[i], a[i+1] + b[i+1], a[i+2] + b[i+2]]
# print(c)

n = int(input())

b = [0, 0, 0]
c = []
for i in range(n):
    a = [int(i) for i in input().split()]
    b = [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
if b[0] != 0:
    print("NO")
else:
    print("YES")
