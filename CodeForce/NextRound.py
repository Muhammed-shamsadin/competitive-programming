'''
This was solved in: Friday 20 oct 2023
'''
# n = no of participant
# k = minimum score fro participant to pass
# input contains first line of 2 int and Second line of n participant
#output contains the number of participants who passed the round

n, k = map(int, input().split())
inputs = list(map(int, input().split()[:n]))
kth_value = inputs[k-1]
count = 0
for i in inputs:
    if i >= kth_value and i > 0:
        count += 1

print(count)