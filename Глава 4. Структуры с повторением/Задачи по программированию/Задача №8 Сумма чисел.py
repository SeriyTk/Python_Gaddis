def Sum_of_numbers():
    total = 0
    while True:
        number = int(input('Введите положительное число: '))
        if number < 0: break
        else:
            total += number
    print(total)


Sum_of_numbers()
