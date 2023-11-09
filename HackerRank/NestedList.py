if __name__ == '__main__':
    n = int(input())
    nestedList = []
    for i in range(n):
        sublist = []
        for j in range(1):
            name = input()
            score = float(input())
            sublist.append(name)
            sublist.append(score)
        nestedList.append(sublist)
    scores = set(sublist[1] for sublist in nestedList)
    second_lowest_score = sorted(scores)[1]
    second_lowest_students =[sublist[0] for sublist in nestedList if sublist[1] == second_lowest_score]
    second_lowest_students.sort()

    for student in second_lowest_students:
        print(student)
