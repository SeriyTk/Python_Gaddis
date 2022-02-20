from  Modules import Login


def val_password():
    password = input('Введите пароль: ')
    while not Login.valid_password(password):
        print('Этот пароль недопустим.')
        password = input('Введите другой пароль: ')
    print('Пароль принят.')
val_password()