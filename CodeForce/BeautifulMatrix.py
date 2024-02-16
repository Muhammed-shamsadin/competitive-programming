matrix = [input().split() for i in range(5)]
for i in range(5):
    for j in range(5):
        if matrix[i][j] == '1':
            distance = abs(i-2) + abs(j-2)
            print(distance)

