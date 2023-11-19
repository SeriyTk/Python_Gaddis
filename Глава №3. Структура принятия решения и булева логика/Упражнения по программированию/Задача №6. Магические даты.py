def Magic_dates():
    day = int(input('Число: '))
    month = int(input('Месяц: '))
    year = int(input("Год: "))
    sum = day * month
    if sum == year: print('Дата магическая.')
    else: print("Дата не магическая.")


if __name__ == '__main__': Magic_dates = Magic_dates()
