CATEGORY_A = 20
CATEGORY_B = 15
CATEGORY_C = 10


def main():
    total_sum = 0

    menu()
    while True:
        enter = int(input('Категория: '))
        if enter == 4: break
        elif enter != 1 and enter !=2 and enter != 3:
            print('Такой категории нет.')
        else:
            if enter == 1: tik1= int(input('Места класса A: ')); total_sum += (tik1 * CATEGORY_A)
            elif enter == 2: tik2 = int(input('Места класса B: ')); total_sum += (tik2 * CATEGORY_B)
            elif enter == 3: tik3 = int(input('Места класса C: ')); total_sum += (tik3 * CATEGORY_C)

    print(F'''
Продано билетов класса А: {tik1},
продано билетов класса В:  {tik2},
продано билетов класса В:  {tik3},
сумма дохода: {total_sum}''')



def menu():
    print(f'''
Меню:
1. Класс А
2. Класс В
3. Класс С
4. Выход
''')


main()
