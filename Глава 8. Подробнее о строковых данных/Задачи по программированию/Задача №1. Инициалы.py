def main():
    string = input('Имя, Отчество, Фамилия: ')
    for i in string:
        if i.isupper(): print(i, end='.')


main()
