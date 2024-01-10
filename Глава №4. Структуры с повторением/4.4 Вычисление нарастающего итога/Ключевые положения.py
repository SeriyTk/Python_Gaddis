MAX = 5
def sum_numbers():
    total = 0
    print(f'Эта программа вычисляет сумму из {MAX} чисел, которые вы введете.')
    for count in range(MAX): number = int(input('Введите число: ')); total += number
    print(f'Cyммa составляет {total}.')


if __name__ == '__main__': sum_numbers = sum_numbers()
