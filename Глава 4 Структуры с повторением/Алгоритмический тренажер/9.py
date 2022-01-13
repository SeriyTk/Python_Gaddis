numer = int(input('Введите число от 1 до 100: '))
while numer <= 0 or numer > 100:
    print('Вы ввели некорректное число.')
    numer = int(input('Введите число от 1 до 100: '))
print(numer)
