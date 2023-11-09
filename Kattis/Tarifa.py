x = int(input())
n = int(input())
sum = 0
for i in range(n):
    p = int(input())
    a = x - p
    sum += a
print(sum + x)