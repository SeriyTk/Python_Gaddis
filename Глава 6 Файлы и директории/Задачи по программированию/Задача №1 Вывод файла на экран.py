def Screen_file():
    with open(r'G:\number_list.txt') as file_numbers:
        return file_numbers.read()


print(Screen_file())