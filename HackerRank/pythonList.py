if __name__ == '__main__':
    N = int(input())
    my_List = []
    for i in range(N):
        commands = input().split()
        cmd = commands[0]

        if cmd == 'insert':
            index = int(commands[1])
            element= int(commands[2])
            my_List.insert(index,element) # Can insert an item in an specified index
        elif cmd == 'print':
            print(my_List)
        elif cmd == 'remove':
            element= int(commands[1])
            my_List.remove(element) # remove the last item of an element
        elif cmd == 'append':
            element= int(commands[1])
            my_List.append(element) # adds an item to the list
        elif cmd == 'sort':
            my_List.sort()  # sorts in a non decreasing order
        elif cmd == 'pop':
            my_List.pop()  # pops out the last item of the list
        elif cmd == 'reverse':
            my_List.reverse() # reverses the list