def average_list():
    scores = [2.5, 7.3, 6.5, 4.0, 5.2]
    total = 0
    for i in scores:
        total += i
    print(total / len(scores))


average_list()
