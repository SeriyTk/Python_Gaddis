def Personal_data():
    name = input('Введите Ваше имя: ')
    adress = input('Ваш адрес проживания: ')
    num_phone = int(input('Номер телефона: '))
    specialty = input('Ваша специальность: ')
    print(f'''
    Меня зовут {name},
    адрес проживания {adress},
    номер телефона {num_phone},
    специальность {specialty}.
''')


Personal_data()
