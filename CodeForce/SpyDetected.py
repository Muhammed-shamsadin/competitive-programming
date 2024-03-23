'''
4
4
11 13 11 11
5
1 4 4 4 4
10
3 3 3 3 10 3 3 3 3 3
3
20 20 10

Approach:
this is what i will do
i will check if the current number and the next are not equal but then i would not kw
which number should be chosen coz i should check the next element but if are just started iterating the array at a[0]
that a[0] will be the one
but when we come to the last part of the array and then a[i] != a[i] we will choose the last one since
i is n - 1 but this will not be iffective for elements in the middle of the array:
the should be checked by looking through the next plus 2 elements
like: 11, 13, 11, 11
11 -> 13.okay they are different then we check if our element a [i - 1] == a[0]
if not okay ..elif is it a[i] == a[n - 1] if yes so it is the last element
but if neither both
11 -> 13 -> 11 -> 11

'''
t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]

    for i in range(n):
        if i == 0:
            if a[i] != a[i + 1] and a[i] != a[i + 2]:
                print(i + 1)
                break
        elif i == n - 1:
            if a[i] != a[i - 1] and a[i] != a[i - 2]:
                print(i + 1)
                break
        else:
            if a[i] != a[i + 1] and a[i] != a[i -1]:
                print(i + 1)
                break









