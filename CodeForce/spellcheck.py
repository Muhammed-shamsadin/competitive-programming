t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    timur = {"T", "i", "m", "u", "r"}
    x = set()

    cnt = 0

    for i in s:
        x.add(i)

    for i in x:
        if i in timur:
            cnt += 1

    if cnt == 5 and len(s) == 5:
        print("YES")
    else:
        print("No")

