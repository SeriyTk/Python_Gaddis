def number():
    with open('G:\\number_list.txt', 'w') as file_number:
        for num in range(1, 101):
            print(int(num), file=file_number)

    print('Цифры в файл занесены.')


number()