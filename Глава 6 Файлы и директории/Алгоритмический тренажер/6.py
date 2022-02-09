def write_number():
    with open('G:\\number_list.txt', 'a') as file_number:
        for num in range(101, 201):
            print(num, file=file_number)
    print('Файл дописан.')


write_number()