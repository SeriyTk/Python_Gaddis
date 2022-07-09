import login

def main():
    while not login.valid_password(input('Введите свой пароль: ')): print('Этот пароль недопустим.')
    print('Это допустимый пароль.')




main()