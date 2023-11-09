if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    newlist = set(arr)
    newlist.remove(max(newlist))

    print(max(newlist))