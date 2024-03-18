t = int(input())

for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    incr = False
    ans = True

    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            incr = True

        if incr and a[i] < a[i - 1]:
            ans = False
            break

    if ans:
        print("YES")
    else:
        print("NO")