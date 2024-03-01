'''
Approach: 1st we take the input as a string then we break it down
         to make it a list.
         After that we create an empty list for later to append our results
         Then USE WHILE LOOP this is where the magic happens,
         the while loop will help us to prevent index out of range.
         then put conditions, and for every one condition it increments by 1
         but when there are 2 conditions like "-" & "-" it will be i += 2.

'''

b = input()
a = list(b)

c = []
i = 0
while i < len(a):
    if a[i] == ".":
        c.append("0")
        i += 1
    elif a[i] == "-" and i + 1 < len(a) and a[i + 1] == ".":
        c.append("1")
        i += 2
    elif a[i] == "-" and i + 1 < len(a) and a[i + 1] == "-":
        c.append("2")
        i += 2

print("".join(c))
