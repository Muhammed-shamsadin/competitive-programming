n = int(input())

prev = 0
count = 0
for i in range(n):
    a = int(input())
    if prev != a:
        prev = a
        count += 1
print(count)