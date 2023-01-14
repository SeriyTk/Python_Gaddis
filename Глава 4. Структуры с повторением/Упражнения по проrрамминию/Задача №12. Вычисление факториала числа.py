def Calculating_factorial():
    factorial = 1
    while True:
        num = int(input('Введите неотрицательное целое число: '))
        if num < 0: print('Неверное число.')
        else:
            for i in range(2, num + 1): factorial *= i
            print(factorial)
        break

Calculating_factorial()