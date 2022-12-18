def Personal_data():
    name = input('Ваше имя: ')
    resident_address = input('Ваш адрес проживания, с городом, областью и почтовым индексом: ')
    phone = int(input('Ваш номер телефона: '))
    specialization = input('Вашу специализацию в учебном заведении: ')
    print(f'''
 Ваше имя: {name} 
 Ваш адрес: {resident_address}
 Ваш телефон: {phone}
 Специальность: {specialization}
''')
Personal_data()