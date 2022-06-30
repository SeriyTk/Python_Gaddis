import random


def main():
    numers = [random.randint(1, 100) for i in range(int(input('Количество чисел: ')))]
    print(numers)
    total_sum = 0
    for i in numers: total_sum += i
    average = total_sum / len(numers)
    print(f'''
Наименьшее число в списке: {min(numers)};
наибольшее число в списке: {max(numers)};
сумма чисел в списке: {total_sum};
среднее арифметическое значение чисел в списке: {average:.2f}.
''')


main()
