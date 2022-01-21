def Sum_of_numbers():
    total_sum = 0
    while True:
        print('Введите положительное число.')
        print('Если хотите завершить программу введите отрицательное число.')
        number = int(input(': '))
        if number >= 0:
            total_sum += number
        else:
            print('Программа завершена.')
            break

    print(f'Сумма всех чисел будет {total_sum}.')


Sum_of_numbers()
