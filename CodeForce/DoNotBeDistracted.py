'''
This was solved in: Saturday 21 oct 2023
'''
t = int(input()) #test cases
# 1st n number of days and 2nd line of String with length n
sus = False
for i in range(t):
    n = int(input())      #number of days
    tasks = input()[:n]   #takes a String input with length n
    for j in range(n):
        if tasks[j] in tasks[j + 1:]:
            sus = True
            print("no")
            break
        else:
            print("yes")





