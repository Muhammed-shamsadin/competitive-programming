t = int(input())

for i in range(t):
    rating = int(input())

    if rating >= 1900:
        print("Division 1")
    elif rating >= 1600 and rating <= 1899:
        print("Division 2")
    elif rating >= 1400 and rating <= 1599:
        print("Division 3")
    elif rating <= 1399:
        print("Division 4")