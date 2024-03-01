Gunner = [int(i) for i in input().split()]
Emma = [ int(i) for i in input().split()]
a = sum(Gunner)
b = sum(Emma)
if a > b:
    print("Gunnar")
elif b > a:
    print("Emma")
else:
    print("Tie")