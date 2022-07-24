import modules1 as m1



def main():
    cap_cit = m1.get_dct()
    right = 0
    wrong = 0
    while True:
        country, capital = m1.get_random_capital(cap_cit)
        print(f'Страна {country}')
        cap = input('Какая столица этой страны: ')
        if cap == capital: print(f'Столица страны {country} - {capital}'); right += 1
        else: print('Ответ не правильный.'); wrong += 1
        if input('Прододжить? ') != '': print('Викторина окончена.'); break

    print(f'Правильных ответов {right} , не правильных ответов {wrong}')

main()