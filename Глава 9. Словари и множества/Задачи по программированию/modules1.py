'''
Функции для задачи №1
'''

def get_audience_number():
    audience = {}
    while True:
        enter = input('Занести номера аудиторий список (д\н): ')
        if enter.lower() == 'н': print('Данные в список занесены.'); break
        elif enter.lower() == 'д': audience[input('Номер курса: ')] = input('Номер аудитории: ')
    return audience

def get_teacher():
    teacher = {}
    while True:
        enter = input('Занести преподавателй в список (д\н): ')
        if enter.lower() == 'н': print('Данные в список занесены.'); break
        elif enter.lower() == 'д': teacher[input('Номер курса: ')] = input('Преподователь: ')
    return teacher

def get_times():
    times = {}
    while True:
        enter = input('Занести время в список (д\н): ')
        if enter.lower() == 'н': print('Данные в список занесены.'); break
        elif enter.lower() == 'д': times[input('Номер курса: ')] = input('Время: ')
    return times

'''
Функции для задачи №2
'''
import random as rand
def get_dct():
    country_capital = {}
    while True:
        country = input('Страна: ')
        capital = input("Столица: ")
        country_capital[country] = capital
        enter = input('Еще? ')
        if enter != '': print('Список составлен.'); break
    return country_capital

def get_random_capital(country_capital):
    country, capital = rand.choice(list(country_capital.items()))
    return country, capital

'''
Функции для задачи №3
'''
import pickle
def encryptyon_file():
    with open('codes.dat', 'wb') as output_file:
        codes = {}
        while True:
            letter = input("Буква: ")
            symbol = input("Символ: ")
            codes[letter] = symbol
            again = input('Желаете ввести еще данные? ')
            if again != '': print('Данные сохранены.'); pickle.dump(codes, output_file); break


def decryption():
    with open('codes.dat', 'rb') as input_file: print(pickle.load(input_file))





