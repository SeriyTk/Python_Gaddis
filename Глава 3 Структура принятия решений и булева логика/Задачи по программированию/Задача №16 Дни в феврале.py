def Days_in_February():
    year = int(input('Введите год: '))
    if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print(f'В {year} году в феврале 29 дней.')
    else:
        print(f'В {year} году в феврале 28 дней.')


Days_in_February()
