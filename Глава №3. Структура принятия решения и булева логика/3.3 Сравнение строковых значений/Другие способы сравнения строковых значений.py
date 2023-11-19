def sort_names():
    name1 = input('Введите фамилию и имя: ')
    name2 = input('Введите еще одну фамилию и имя: ')

    print('Boт имена, ранжированные по алфавиту: ')

    if name1 < name2: print(name1); print(name2)
    else: print(name2); print(name1)

if __name__ == '__main__': sort_names = sort_names()
