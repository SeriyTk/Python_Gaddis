def Sum_numbers():
    amount = int(input('Количество чисел: '))
    total = 0
    for i in range(amount):
        numb = int(input('Введите положительное число: '))
        if numb < 0: break
        else: total += numb

    print(total)

Sum_numbers()