def mutate_string(s,pos,char):
    s = s[:pos] + char + s[pos + 1:]
    return s
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
