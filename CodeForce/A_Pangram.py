n = int(input())
s = input().lower()

k = set(s)

if n >= 26 and len(k) == 26:
    print("YES")
else:
    print("NO")