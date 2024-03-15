t = int(input())

for i in range(t):
    s = [i for i in input()]

    aa = s.count("A")
    bb = s.count("B")

    if aa > bb:
        print("A")
    else:
        print("B")

