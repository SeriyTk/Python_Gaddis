def main():
    value = 99
    print(f'Значение равно {value}')
    change_me(value)

def change_me(par):
    print('Я изменяю значение.')
    par = 0
    print(f'{par}')


main()
