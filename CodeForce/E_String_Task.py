s = input()
vowel = "aeiouyAEIOUY"
res = ""

for i in s:
    if i not in vowel:
        res += "." + i.lower()

print(res)
