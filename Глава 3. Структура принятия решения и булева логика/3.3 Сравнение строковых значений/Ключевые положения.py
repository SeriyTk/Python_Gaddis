name1 = 'Mark'
name2 = 'Mary'
if name1 == name2:
    print('Имена одинаковые.')
else:
    print("Имена разные")

def password():
    password = input('Введите пароль: ')
    if password == 'prospero':
        print('Пароль принят')
    else:
        print("Пароль не верный")

password()