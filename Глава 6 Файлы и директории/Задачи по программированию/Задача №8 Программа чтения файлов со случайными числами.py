import random as ran


def read_random_numbers():
    total_sum = 0
    num_num = 0
    with open(r'G:\number_file.txt') as f:
        for i in f:
            num_num += 1
            total_sum += int(i)
    return total_sum, num_num


print(read_random_numbers())
