import login
def main():
    print('Ваше имя для входа в систему:')
    print(login.get_login( input ('Введите свое имя: '), input ('Введите свою фамилию: '), input('Введите свой номер студента: ')))

if __name__ == '__main__': main()