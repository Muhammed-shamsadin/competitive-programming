t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    l = -1
    r = -1

    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            l = i
            r = i + 1
            break
    print(l, r)