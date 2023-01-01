def Days_in_February():
    enter_year = int(input('Введите год: '))
    if enter_year % 100 == 0 and enter_year % 400 == 0: print(f'Год {enter_year} высокосный.')
    elif enter_year % 4 == 0: print(f'Год {enter_year} высокосный.')
    else: print(f'Год {enter_year} не высокосный.')


Days_in_February()