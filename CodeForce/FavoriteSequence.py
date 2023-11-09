'''
This was solved in: Wednesday 25 oct 2023
'''
t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    for i in range(n):
        if i % 2 == 0:
            a.append(b[i // 2])
        else:
            a.append(b[-(i // 2 + 1)])
    output_str = ' '.join(map(str, a))
    print(output_str)
