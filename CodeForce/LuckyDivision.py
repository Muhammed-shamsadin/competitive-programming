'''
Approach:

'''

n = int(input())

a = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

if n in a:
    print("YES")
else:
    for i in range(len(a)):
        if n % a[i] == 0:
            print("YES")
            break
    else:
        print("NO")