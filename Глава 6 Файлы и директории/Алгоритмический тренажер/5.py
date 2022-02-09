def sum_number():
    with open('G:\\number_list.txt') as file_number:
        total_sum = 0
        for num in file_number:
            total_sum += int(num)
        print(total_sum)


sum_number()



