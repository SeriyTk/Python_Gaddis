def main():
    total_sum = 0
    total = 0
    try:
        for number in open('numbers.txt'): total_sum += int(number); total += 1
    except IOError: print('Ошибка! Такого файла нет.')
    except TypeError: print('Ошибка!.')
    else: print(f'Среднее арифметическое: {total_sum / total}')


main()
