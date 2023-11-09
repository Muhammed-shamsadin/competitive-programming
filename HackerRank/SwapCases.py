def swap_case(s):
    result = ""
    for i in s:
        if i.islower():
            result += i.upper()
        elif i.isupper():
            result += i.lower()
        else:
            result += i
    return result
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

'''
Other way to solve this :

    def swap_case(s):
        return s.swapcase()
    if __name__ == '__main__':
       s = input()
       result = swap_case(s)
       print(result)
       
'''