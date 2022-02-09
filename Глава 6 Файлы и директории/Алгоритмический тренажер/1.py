def name():
    with open('G:\\my_name.txt', 'w') as file_name:
        print(input('Ваше имя: '), file=file_name)
    print('Имя в файла занесено.')

name()