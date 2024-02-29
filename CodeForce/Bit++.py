n= int(input())
ops = 0
for i in range(n):
    a = input()
    if "++" in a:
        ops += 1
    elif "--" in a:
        ops -= 1
print(ops)