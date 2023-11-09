'''
s = list(input())
t = list(input())
lowerc_s = [i.lower() for i in s]
lowerc_t = [i.lower() for i in t]
x = len(s)
y = len(t)
if x != y:
    added = next((elt for elt in t if elt not in s))
    print(added)
'''

def findTheDifference(s: str, t: str) -> str:
    s = list(s)
    t = list(t)
    for elt in t:
        if t.count(elt) != s.count(elt):
            return elt





