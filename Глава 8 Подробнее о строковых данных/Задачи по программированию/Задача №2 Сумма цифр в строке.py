def Sum_of_digits():
    total = 0
    for i in input('Введите цифры: '):
        total += int(i)
    return total


print(Sum_of_digits())
