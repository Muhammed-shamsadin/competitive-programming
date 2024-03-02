'''
input is string
output the rearranged sum in non decreasing order
stp 1: accept them as strings
stp 2:
'''
summand = [i for i in input().split("+")]
summand.sort()

rearranged_sum = "+".join(summand)
print(rearranged_sum)