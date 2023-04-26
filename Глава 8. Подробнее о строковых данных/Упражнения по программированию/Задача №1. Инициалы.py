def main():
    str  = input('Введите фамилию, имя, отчество: ')
    for item in  str.split(' '): print(f'{item[0]}', end='.')

if __name__ == '__main__': main()