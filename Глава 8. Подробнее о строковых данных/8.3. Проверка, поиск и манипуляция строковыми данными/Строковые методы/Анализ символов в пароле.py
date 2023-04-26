import login
def main():
    password = input('Введите свой пароль: ')
    while not login.valid_pass(password):
        print('Этот пароль недопустим.')
        password = input('Введите свой пароль: ')
    print('Это допустимый пароль. ')


if __name__ == '__main__': main()