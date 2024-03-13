'''
 put the number of problems that are surely solved or not in a list
 then check whether the count of "1" in the list is greater than 2 or not
 then if it is greater than 2 use the intialized counter and add one on it.
 continues....
'''

n = int(input())
cnt = 0
for i in range(n):
    prob = list(map(int, input().split()))
    if prob.count(1) >= 2:
        cnt += 1
print(cnt)



