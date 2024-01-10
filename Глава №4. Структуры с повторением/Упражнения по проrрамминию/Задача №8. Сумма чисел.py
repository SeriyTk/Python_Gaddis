def Sum_numbers():
    total = 0
    while True:
        number = int(input('Введите положительное число: '))
        if number < 0: print(total); break
        elif number == 0: continue
        elif number > 0: total += number


if __name__ == '__main__': Sum_numbers = Sum_numbers()
