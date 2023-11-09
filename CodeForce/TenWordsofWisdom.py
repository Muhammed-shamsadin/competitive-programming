'''
This was solved in: Wednesday 25 oct 2023
'''
def ans():
    n = int(input())
    w = 0
    p = 0

    for i in range(n):
        m, q = map(int, input().split())

        if m <= 10:
            if q > w:
                w = q
                p = i + 1

    print(p)

t = int(input())

for _ in range(t):
    ans()