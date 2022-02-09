def Sum_of_numbers():
    with open(r'G:\number_list.txt') as file_number:
        total_sum = 0
        for i in file_number:
            total_sum += int(i)
        return total_sum


print(Sum_of_numbers())
