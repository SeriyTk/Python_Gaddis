def Personal_Information():
    name = input('Ваше имя: ')
    adress = input('Ваш адрес проживания: ')
    num_phone = input('Ваш номер телефона: ')
    specialization = input('Ваша специализация в учебном заведении: ')

    print(f'''
Ваше имя: {name}
Ваш ваш адрес проживания, с городом, областью и почтовым индексом: {adress}
Ваш номер телефона: {num_phone}
Ваша специализация в учебном заведении: {specialization}
''')

if __name__ == '__main__': Personal_Information = Personal_Information()
