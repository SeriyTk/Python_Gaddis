import login

def main():
    print('Ваш логин:')
    print(login.get_login_name(input('Имя: '), input('Фамилия: '), input('ИД: ')))



main()
