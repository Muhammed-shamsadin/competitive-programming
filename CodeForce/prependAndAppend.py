'''
This was solved in: Friday 20 oct 2023
'''
'''
n, k = int(input())  I cannot use this syntax to accept two integers with spaces)
to fix the code above use this way
'''
n, k = map(int, input().split())
arr = [int(x) for x in input().split()[:n]]

sum = 0
for x in arr:
    sum += x
print(sum)