import random as rdn
def dct_country_capital():
    country_capital = {}
    while True:
        country = input('Введите название страны: ')
        capital = input("Введите название столицы: ")
        country_capital[country] = capital
        enter = input('Хотите продолжить? д/н: ')
        if enter != 'д':
            print("Словарь создан.")
            break
    return country_capital

def get_list_keys(par):
    list_keys = []
    for key in par:
        list_keys.append(key)
    return list_keys

def rand_keys(list_keys):
    number = rdn.randint(0, len(list_keys) - 1)
    return list_keys[number]
def Capitals_quiz():
    country_capital = dct_country_capital()
    list_keys = get_list_keys(country_capital)
    right = 0
    wrong = 0
    while True:
        country = rand_keys(list_keys)
        capital = country_capital[country]
        print(f'Страна {country}, назовите столицу страны.')
        enter = input(': ')
        if enter == capital:
            print('Правильно.')
            right += 1
        else:
            print("Не правильно.")
            wrong += 1
        if input('Хотите продолжить? д/н: ') != 'д':
            print(f'Викторина завершена.')
            break
    print(f'Количество правильных ответов {right}, количество неправильных ответов {wrong}')

Capitals_quiz()
