import random as rd
def main():
    country_capitals = {'Украина' : 'Киев', 'США' : 'Вашингтон', 'Канада' : 'Оттава'}
    country = rd.choice(list(country_capitals))
    capital = input(f'Какая столица у {country}: ')
    if country_capitals[country] == capital: print('Правильно.')
    else: print("Неправильно.")


if __name__ == '__main__': main()