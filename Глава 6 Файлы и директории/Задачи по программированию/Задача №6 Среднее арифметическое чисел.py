def Arithmetic_mean_of_numbers():
    with open(r'G:\number_list.txt') as file_number:
        total_sum = 0
        num_num = 0
        for i in file_number:
            total_sum += int(i)
            num_num += 1
        return total_sum / num_num


print(Arithmetic_mean_of_numbers())
