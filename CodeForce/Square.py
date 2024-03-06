t = int(input())

for _ in range(t):
    tot = []
    for _ in range(4):
        a = [int(i) for i in input().split()]
        tot.extend(a)

  
    min_x = min(tot[::2])
    max_x = max(tot[::2])
    min_y = min(tot[1::2])
    max_y = max(tot[1::2])

    side_length = max(max_x - min_x, max_y - min_y)
    print(side_length ** 2)
