if __name__ == '__main__':
    n = int(input())
    student_mark = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))

        student_mark [name] = scores
    query_name = input()
    average = sum(student_mark[query_name])/len(student_mark[query_name])
    average = format(average, '.2f')

    print(average)