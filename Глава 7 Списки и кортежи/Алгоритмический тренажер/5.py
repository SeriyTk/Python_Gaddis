def numbers1_list():
    numbers1 = []
    for i in range(1, 101):
        numbers1.append(i)
    return numbers1


def total_sum(par):
    total = 0
    for i in par:
        total += i
    return total


print(total_sum(numbers1_list()))
