def password():
    password = input('Введите пароль: ')
    if password == 'prospero': print('Пароль принят.')
    else: print('Извините, этот пароль неверньм.')


if __name__ == '__main__': password = password()
