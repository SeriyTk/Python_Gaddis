def read_number():
    with open('G:\\number_list.txt') as file_number:
        for num in file_number:
            print(int(num), end=' ')


read_number()
