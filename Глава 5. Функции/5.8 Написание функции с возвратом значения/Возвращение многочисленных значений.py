def main():
    first_name, last_name = get_name()
    print(first_name, last_name)

def get_name(): return input('Введите имя: '), input('Введите фамилию: ')


main()