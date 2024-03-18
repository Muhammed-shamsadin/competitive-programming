t = int(input())

for i in range(t):
    s = input()
    x = set()
    i = 0
    while i < len(s):
        if i == len(s) - 1 or s[i] != s[i + 1]:
            x.add(s[i])
            i += 1
        else:
            i += 2

    res = ''.join(sorted(x))
    print(res)